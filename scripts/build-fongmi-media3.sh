#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "用法: $0 <github-workspace>" >&2
  exit 2
fi

workspace="$1"
media3_repo="${workspace}/media3-local-repo"
source_dir="${workspace}/fongmi-media"
init_script="${RUNNER_TEMP:-/tmp}/media3-init.gradle"

mkdir -p "$media3_repo"

git clone --depth=1 --branch=release-1.10.1-fongmi \
  https://github.com/FongMi/media "$source_dir"
cd "$source_dir"
chmod +x gradlew

# FongMi/TV 引用了尚未公开到 FongMi/media 的两个兼容类。
# PlayerSeekView 用公开的 PlayerControlView 实现；DiskPreloadManager 保留 API，
# 但不执行预加载，确保公开源码构建不会改变正常播放路径。
python3 - <<'PYEOF'
from pathlib import Path

files = {
    Path("libraries/ui/src/main/java/androidx/media3/ui/PlayerSeekView.java"): r'''package androidx.media3.ui;

import android.content.Context;
import android.util.AttributeSet;

import androidx.annotation.Nullable;
import androidx.media3.common.util.UnstableApi;

/** Compatibility seek controller used by FongMi/TV. */
@UnstableApi
public final class PlayerSeekView extends PlayerControlView {

    public PlayerSeekView(Context context) {
        this(context, null);
    }

    public PlayerSeekView(Context context, @Nullable AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public PlayerSeekView(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    public TimeBar getTimeBar() {
        return (TimeBar) findViewById(R.id.exo_progress);
    }
}
''',
    Path("libraries/exoplayer/src/main/java/androidx/media3/exoplayer/source/preload/DiskPreloadManager.java"): r'''package androidx.media3.exoplayer.source.preload;

import androidx.media3.common.MediaItem;
import androidx.media3.common.PriorityTaskManager;
import androidx.media3.common.util.UnstableApi;
import androidx.media3.datasource.DataSource;
import androidx.media3.datasource.cache.Cache;
import androidx.media3.exoplayer.ExoPlayer;
import androidx.media3.exoplayer.RenderersFactory;

/**
 * Compatibility API for FongMi/TV.
 *
 * <p>The original disk preloader is not present in the public repository. This
 * implementation deliberately performs no background preload while preserving
 * the public API expected by the app.
 */
@UnstableApi
public final class DiskPreloadManager {

    private DiskPreloadManager() {}

    public void start(ExoPlayer player, MediaItem mediaItem, Options options) {}

    public void release() {}

    public static final class Builder {

        public Builder(
                Cache cache,
                DataSource.Factory upstreamDataSourceFactory,
                RenderersFactory renderersFactory) {}

        public Builder setPriorityTaskManager(PriorityTaskManager priorityTaskManager) {
            return this;
        }

        public DiskPreloadManager build() {
            return new DiskPreloadManager();
        }
    }

    public static final class Options {

        private Options() {}

        public static Builder builder() {
            return new Builder();
        }

        public static final class Builder {

            public Builder setDurationMs(long durationMs) {
                return this;
            }

            public Builder setMaxThreads(int maxThreads) {
                return this;
            }

            public Options build() {
                return new Options();
            }
        }
    }
}
''',
}

for path, content in files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"已注入公开源码兼容类: {path}")
PYEOF

# FongMi fork 引入了上游白名单中没有的依赖（如 smbj、brotli）。
# 将未知依赖按 JAR 处理，避免 missing_aar_type_workaround.gradle 直接报错。
python3 - <<'PYEOF'
import sys

path = "missing_aar_type_workaround.gradle"
with open(path, "r", encoding="utf-8") as file:
    content = file.read()

old = '''                        throw new IllegalStateException(
                            dependencyName + " is not on the JAR or AAR list in missing_aar_type_workaround.gradle")'''
new = '''                        // 未知依赖默认视为 JAR（FongMi fork 可能引入上游没有的依赖）
                        hasJar = true'''

if old not in content:
    print("未找到待修补的异常代码，源码可能已经变化：", file=sys.stderr)
    for number, line in enumerate(content.splitlines(), 1):
        if "is not on the JAR or AAR list" in line:
            print(f"  行 {number}: {line}", file=sys.stderr)
    sys.exit(1)

with open(path, "w", encoding="utf-8") as file:
    file.write(content.replace(old, new))

print("已修补 missing_aar_type_workaround.gradle：未知依赖默认按 JAR 处理")
PYEOF

echo "=== 验证修补结果 ==="
grep -n "hasJar = true\|is not on the JAR" missing_aar_type_workaround.gradle

# publish.gradle 通过该扩展属性判断是否启用。
printf '%s\n' 'gradle.ext.rootProjectIsAndroidXMedia3 = true' > "$init_script"

echo "可用的 publish 任务:"
./gradlew tasks --all 2>/dev/null |
  grep -i "publishReleasePublicationToMavenRepository" || true

./gradlew \
  :lib-common:publishReleasePublicationToMavenRepository \
  :lib-container:publishReleasePublicationToMavenRepository \
  :lib-database:publishReleasePublicationToMavenRepository \
  :lib-datasource:publishReleasePublicationToMavenRepository \
  :lib-datasource-okhttp:publishReleasePublicationToMavenRepository \
  :lib-decoder:publishReleasePublicationToMavenRepository \
  :lib-extractor:publishReleasePublicationToMavenRepository \
  :lib-exoplayer:publishReleasePublicationToMavenRepository \
  :lib-session:publishReleasePublicationToMavenRepository \
  :lib-ui:publishReleasePublicationToMavenRepository \
  :lib-ui-danmaku:publishReleasePublicationToMavenRepository \
  --init-script "$init_script" \
  -PmavenRepo="$media3_repo" \
  -PreleaseVersion=1.10.1 \
  --no-daemon --parallel

echo "FongMi Media3 构建完成，发布到: $media3_repo"
echo "=== 发布的产物 ==="
ls -la "$media3_repo/androidx/media3/" ||
  {
    echo "错误: 发布目录为空" >&2
    exit 1
  }

artifacts=(
  media3-common
  media3-container
  media3-database
  media3-datasource
  media3-datasource-okhttp
  media3-decoder
  media3-extractor
  media3-exoplayer
  media3-session
  media3-ui
  media3-ui-danmaku
)

for artifact in "${artifacts[@]}"; do
  if ! find "$media3_repo/androidx/media3/$artifact" -name '*.aar' -print -quit |
    grep -q .; then
    echo "错误: 缺少 $artifact 产物" >&2
    exit 1
  fi
done
echo "所有必需产物验证通过"

if [[ -n "${GITHUB_ENV:-}" ]]; then
  echo "media3Repo=$media3_repo" >> "$GITHUB_ENV"
fi
