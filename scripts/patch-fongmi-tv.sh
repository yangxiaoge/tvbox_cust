#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "用法: $0 <fongmi-tv-source-dir>" >&2
  exit 2
fi

source_dir="$1"

python3 - "$source_dir" <<'PYEOF'
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
factory = root / "app/src/main/java/com/fongmi/android/tv/player/engine/PlayerEngineFactory.java"

content = factory.read_text(encoding="utf-8")
replacements = {
    "import com.fongmi.android.tv.player.mpv.MpvPlayerEngine;\n": "",
    "            case MPV -> new MpvPlayerEngine(decode, listener);":
        "            // 公开源码不包含 MPV Media3 封装，兼容构建统一回退到 ExoPlayer。\n"
        "            case MPV -> new ExoPlayerEngine(decode, listener);",
    "        return PlayerSetting.isMpv() && MpvPlayerEngine.isAvailable();":
        "        return false;",
}

for old, new in replacements.items():
    if old not in content:
        print(f"提示: PlayerEngineFactory.java 中未找到 {old.strip()}，尝试跳过或兼容匹配")
    else:
        content = content.replace(old, new)

factory.write_text(content, encoding="utf-8", newline="\n")

playback = root / "app/src/main/java/com/fongmi/android/tv/ui/activity/PlaybackActivity.java"
if playback.is_file():
    content = playback.read_text(encoding="utf-8")
    debug_methods = {
        """    public boolean isDebugViewVisible() {
        return getPlayerView().isDebugViewVisible();
    }""":
        """    public boolean isDebugViewVisible() {
        // 公开版 Media3 PlayerView 不包含 FongMi 的调试面板。
        return false;
    }""",
        """    public void toggleDebugView() {
        getPlayerView().toggleDebugView();
    }""":
        """    public void toggleDebugView() {
        // 公开源码兼容构建：无调试面板可切换。
    }""",
        """    public void hideDebugView() {
        getPlayerView().hideDebugView();
    }""":
        """    public void hideDebugView() {
        // 公开源码兼容构建：无调试面板可隐藏。
    }""",
    }
    for old, new in debug_methods.items():
        if old in content:
            content = content.replace(old, new)
    playback.write_text(content, encoding="utf-8", newline="\n")
    print("已处理 PlayerView 调试面板兼容")

exo_util = root / "app/src/main/java/com/fongmi/android/tv/player/exo/ExoUtil.java"
if exo_util.is_file():
    content = exo_util.read_text(encoding="utf-8")
    private_renderer_chain = (
        "        return factory.setFfmpegAudioPrefer(audioPrefer)"
        ".setFfmpegVideoPrefer(videoPrefer)"
        ".setEnableDecoderFallback(true)"
        ".setEnableDv7HevcFallback(PlayerSetting.isDv7HevcFallback())"
        ".setExtensionRendererMode(renderMode);"
    )
    public_renderer_chain = (
        "        // FongMi 私有的 FFmpeg 偏好和 DV7 fallback API 未包含在公开 Media3 中。\n"
        "        return factory.setEnableDecoderFallback(true)"
        ".setExtensionRendererMode(renderMode);"
    )
    if private_renderer_chain in content:
        content = content.replace(private_renderer_chain, public_renderer_chain)
        exo_util.write_text(content, encoding="utf-8", newline="\n")
        print("已移除公开 Media3 不支持的 FFmpeg/DV7 renderer 配置")

for relative in (
    "app/src/main/java/com/fongmi/android/tv/player/mpv/MpvPlayerEngine.java",
    "app/src/main/java/com/fongmi/android/tv/player/mpv/MpvUtil.java",
):
    path = root / relative
    if path.is_file():
        path.unlink()
        print(f"已移除不可公开构建的 MPV 源文件: {relative}")

print("MPV 引擎兼容处理完成")
PYEOF
