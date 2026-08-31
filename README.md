# ⚠️ 提示与免责声明

> [!WARNING]
> **自用项目，请勿宣传！⚠️⚠️⚠️**
> 
> 1. **免责声明**：本项目（tvbox_cust）内所有数据与配置均搜集于网络，按“原样”提供，不保证可用性，不带任何明示或暗示的保证。使用者有责任确保其使用符合当地法律法规。
> 2. **学习用途**：本项目仅用于个人学习与技术研究，禁止用于商业用途或违反国家法律法规的其他用途。所有直接或间接使用本仓库内容的使用者，请在 24 小时内完成研究并自行删除相关内容。
> 3. **第三方内容**：本仓库中涉及的第三方硬件、软件等与本项目无直接或间接关系，所造成的一切后果由使用者自行承担。
> 4. **版权与移除**：感谢各位开源大佬的无私奉献。如果有收录您的配置且您不希望被收录，请提交 [Issues](https://github.com/yangxiaoge/tvbox_cust/issues)，我们将在第一时间移除相关内容。
> 
> 如果感兴趣，请复制/Fork 项目后自行研究使用。

---

# 📑 目录导航

- [📺 TVBox 影视接口源](#tvbox-影视接口源)
  - [1. 优秀大佬仓](#1-优秀大佬仓)
  - [2. 源解析服务](#2-源解析服务)
  - [3. 官方及交流群](#3-官方及大佬交流群-telegram)
- [📱 TV 客户端与配置](#tv-客户端与配置)
  - [客户端应用矩阵](#tv-客户端与配置)
  - [影视使用教程](#影视使用教程)
- [🚀 云编译与进阶开发](#云编译与进阶开发)
  - [1. 三方 TVBox 云编译](#1-三方-tvbox-云编译)
  - [2. 自定义爬虫源 (Spiders)](#2-自定义爬虫源-spiders)
- [🛠️ 实用工具与扩展](#实用工具与扩展)
  - [1. Clash 代理规则](#1-clash-代理规则)
  - [2. 跳广告工具 (推荐 GKD)](#2-跳广告工具-推荐-gkd--李跳跳存档)
  - [3. 洛雪音乐 (LX Music)](#3--音乐应用-lx-music)
  - [4. 节假日查询接口](#4--节假日查询接口)
- [🌟 Star History](#star-history)

---

# 📺 TVBox 影视接口源

> [!NOTE]
> **如何配置？** 复制下方的接口链接，在 TVBox 客户端的 `设置 -> 点播 -> 配置地址` 处粘贴并保存。

### 1. 优秀大佬仓
* **饭太硬**: `http://www.饭太硬.cc/tv`
* **王二小**: `http://new.王二小放牛娃.top`
* **嗷呜**: `http://www.英格里希嗷呜.top/tv`

### 2. 源解析服务
* [FongMi UA 解析服务](https://ua.fongmi.eu.org/) (`https://ua.fongmi.eu.org/`)

### 3. 官方及大佬交流群 (Telegram)
* [FongMi 官方频道](https://web.telegram.org/k/#@fongmi_official) | [饭太硬](https://web.telegram.org/k/#@TVBoxxoo) | [王二小放牛娃](https://web.telegram.org/k/#@wangerxiaofangniuwa) | [嗷呜交流频道](https://web.telegram.org/a/#-1003462278777) | [鱼壳交流群](https://web.telegram.org/k/#@webhtv)

---

# 📱 TV 客户端与配置

| 应用类型 | 客户端下载 | 辅助配置 / 相关链接 |
| :--- | :--- | :--- |
| **影视客户端** | • [FongMi影视](https://github.com/FongMi/Release)（官方原版发布）<br>• [鱼壳 (二开 / fish2018)](https://github.com/fish2018/webhtv)<br>• [默影视 (三开 / Silent1566)](https://github.com/Silent1566/webhtv) | 接口订阅源：[跳转至上方 TVBox 源](#tvbox-影视接口源) |
| **TV 默认桌面** | • [EmotnUI](/apk/EmotnUI_com.oversea.aslauncher_1.0.9.0_5094.apk)（默认桌面）<br>• [当贝桌面](/apk/当贝桌面_4.1.7精简去广告版.apk)（精简去广告版） | - |
| **IPTV / 央视直播** | • [TiviMate 2.1.5](/apk/TiviMate-2.1.5推荐-Premium付费破解版.apk)（通用直播，推荐）<br>• [WebViewTvLive](https://github.com/hxh19950701/WebViewTvLive)（WebView方式播放央视）<br>• [CCTV_Viewer](https://github.com/Eanya-Tonic/CCTV_Viewer) | • [TiviMate配置备份](https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/apk/TiviMate2.1.5_backup_20240409_104306.tmb)<br>• 订阅源仓库：[fanmingming](https://github.com/fanmingming/live)<br>• IPv6直播源：https://live.fanmingming.com/tv/m3u/ipv6.m3u |
| **开机自启** | • [开机自启 3.0](/apk/开机自启_3.0_2024-03-11.apk)（开机自动启动指定应用） | • 自用源码：[autoclick](https://gitee.com/sheepyang_study/auto-click-slide)（闭源） |

### 📚 影视使用教程
> [!TIP]
> [FongMi 影视图文教程](https://yangxiaoge.github.io/yingshi) 包含客户端软件配置与详细使用步骤。

---

# 🚀 云编译与进阶开发

### 1. 三方 TVBox 云编译
*基于开源项目 [o0HalfLife0o/TVBoxOSC](https://github.com/o0HalfLife0o/TVBoxOSC) & [zyqfork/TVBoxOSC](https://github.com/zyqfork/TVBoxOSC) 的在线构建脚本*

![Build](https://shields.io/github/actions/workflow/status/yangxiaoge/tvbox_cust/tvbox_app_action.yml?branch=master&logo=github&label=Build)
[![Download](https://img.shields.io/github/v/release/yangxiaoge/tvbox_cust?color=orange&logoColor=orange&label=Download&logo=DocuSign)](https://github.com/yangxiaoge/tvbox_cust/releases/latest) 
[![Total](https://shields.io/github/downloads/yangxiaoge/tvbox_cust/total?logo=Bookmeter&label=Counts&logoColor=yellow&color=yellow)](https://github.com/yangxiaoge/tvbox_cust/releases)

> [!TIP]
> **如何利用 GitHub Actions 自动编译你自己的 TVBox APP？**
> 1. 点击仓库右上角的 **Fork**，复制一份本项目到你的账号。
> 2. 在你 Fork 的项目页面中，点击顶部的 **Actions** 选项卡。
> 3. 点击 `TVBox App Build` 工作流，在右侧下拉菜单中点击 **Run workflow** 即可启动在线编译。
> 4. 编译完成后，可以在 **Releases** 或 Action 产物中下载 APK 安装包。

#### 编译依赖项目及同步状态

> [!NOTE]
> **说明**：由于 FongMi 影视近期构建流程及依赖较为复杂，暂已从自动云编译工作流中移除。需要 FongMi 影视 APK 请直接前往官方发布页下载：[FongMi/Release](https://github.com/FongMi/Release)。

| 项目名称 (Repository) | 编译分支 | 最新 Commit Hash | 同步时间 (Build Time) |
| :--- | :--- | :--- | :--- |
| [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS) | main | 301b28b... | 2026-08-28 17:35:31 |
| [takagen99/Box](https://github.com/takagen99/Box) | main | 258a5fe... | 2026-08-28 17:48:38 |
| [mlabalabala/box](https://github.com/mlabalabala/box) | main | c5dc2b9... | 2026-08-28 17:34:59 |

*同步数据更新于: 2026-08-28 17:48:38*

### 2. 自定义爬虫源 (Spiders)
提供给 TVBox / FongMi 等客户端解析视频使用的爬虫规则库：
* [CatVodSpider - 自用修改版](https://github.com/yangxiaoge/CatVodSpider)
* [CatVodSpider - FongMi 官方版](https://github.com/FongMi/CatVodSpider)
* [CatVodSpider - bizhangjie 版](https://github.com/bizhangjie/CatVodSpider)

---

# 🛠️ 实用工具与扩展

### 1. Clash 代理规则
> [!NOTE]
> 供 Clash 或 OpenClash 客户端导入使用的订阅及规则配置。

* **Clash 订阅配置 (配置三)**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/Clash3.yml`
* **Clash 订阅配置 (配置二)**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/Clash2.yml`
* **OpenClash 自定义规则 (MihomoPro)**:
  - `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/custRule/MihomoPro-2025-09-10.yaml`
  - 参考：`https://github.com/666OS/YYDS/tree/main/mihomo/config/legacy`

### 2. 跳广告工具 (推荐 GKD / 李跳跳存档)

#### GKD (基于无障碍的跳广告工具，推荐 ⭐)
> [!NOTE]
> GKD 是一款功能强大、持续活跃维护的基于无障碍跳广告工具。你可以复制下方的订阅链接导入到 GKD App 中。
>
> * **项目源码**: [gkd-kit/gkd](https://github.com/gkd-kit/gkd)
> * **GKD 第三方订阅规则**:
>   - **活跃维护 (推荐)**: `https://raw.githubusercontent.com/Lin-arm/GKD_subscription/main/dist/gkd.json5`
>   - **自用脚本自动拉取**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/gkd/GKD_subscription.json5`

#### 李跳跳 (已停止维护，仅存档)
> [!TIP]
> 经典的自动跳广告工具（已停止维护，仅作历史备份归档）。
>
> * **客户端下载**: [李跳跳 派大星 2.2](/litiaotiao/李跳跳_派大星2.2.apk)
> * **李跳跳规则文件**: [/litiaotiao/AllRules.json](/litiaotiao/AllRules.json)
> * **使用指南**: [李跳跳进阶指南.pdf](/litiaotiao/李跳跳进阶指南-掘金.pdf)

### 3. 🎵 音乐应用 (LX Music)
开源多端高颜值音乐播放器，支持导入自定义源接口。

- **客户端源码与下载**：
  - 🖥️ **桌面端**（Win / Mac / Linux）：[lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop)
  - 📱 **移动端**（Android）：[lyswhut/lx-music-mobile](https://github.com/lyswhut/lx-music-mobile)
- **音源与订阅配置**：
  - 🔗 **三方订阅源仓库**：[guoyue2010/lxmusic-](https://github.com/guoyue2010/lxmusic-)
  - 🌐 **纯净直达配置页**：https://77f77.48364836.xyz/lx

### 4. 📅 节假日查询接口
* **接口地址**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/holiday/isHoliday.json`
* **说明**: 供相关自动化脚本或智能家居判定今日是否为节假日使用。

---

# 🌟 Star History

[![Star History Chart](https://starhistory.link/yangxiaoge/tvbox_cust.svg?theme=rose&style=glass)](https://starhistory.link/yangxiaoge/tvbox_cust)
