# 提示

> [!WARNING]
> **自用项目，请勿宣传！⚠️⚠️⚠️**
> 
> 本项目内所有数据均搜集于网络，不保证可用性。
> 感谢各位大佬的无私奉献。如果有收录您的配置，且您不希望被收录，请提交 [Issues](https://github.com/yangxiaoge/tvbox_cust/issues)，我们将在第一时间移除相关内容。
> 
> *因 GitHub 访问问题，项目配置中的部分 GitHub 地址已替换为 jsDelivr 等加速镜像源。*
> 
> 如果感兴趣，请复制/Fork项目后自行研究使用。

---

# TV 应用及相关配置

| 应用类型 | 客户端下载 | 辅助配置 / 相关链接 |
| :--- | :--- | :--- |
| **TV 默认桌面** | • [EmotnUI](/apk/EmotnUI_com.oversea.aslauncher_1.0.9.0_5094.apk) (默认桌面)<br>• [当贝桌面](/apk/当贝桌面_4.1.7精简去广告版.apk) (精简去广告版) | |
| **影视客户端** | • [自编影视](https://github.com/yangxiaoge/tvbox_cust/releases) (自用编译版)<br>• [FongMi影视](https://github.com/FongMi/Release/tree/fongmi/apk/release) (原版) | 接口订阅源: [点此跳转到下方TVBox源](#tvbox-源) |
| **IPTV 直播** | • [TiviMate 2.1.5](/apk/TiviMate-2.1.5推荐-Premium付费破解版.apk) (推荐/付费破解版) | • [配置恢复备份文件](https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/apk/TiviMate2.1.5_backup_20240409_104306.tmb)<br>• 订阅源官网: [fanmingming](https://github.com/fanmingming/live)<br>• [IPv6 直播源地址](https://live.fanmingming.com/tv/m3u/ipv6.m3u) |
| **开机自启** | • [开机自启 3.0](/apk/开机自启_3.0_2024-03-11.apk) (开机自动运行指定 App) | • 源码: [autoclick](https://gitee.com/sheepyang_study/auto-click-slide) (自用闭源) |

---

# 影视使用教程

> [!TIP]
> 📚 **新手指南**：[FongMi 影视图文教程](https://yangxiaoge.github.io/yingshi) 包含软件配置与详细使用步骤。

---

# TVBox 源

> [!NOTE]
> **如何配置？** 复制下方的接口链接，在 TVBox 客户端的 `设置 -> 点播 -> 配置地址` 处粘贴并保存。

### 1. 自用多仓 (推荐)
* **自用多仓链接**: `https://github.com/yangxiaoge/tvbox_cust/raw/refs/heads/master/tvbox/多仓.json`

### 2. 优秀大佬仓
* **饭太硬**: `http://www.饭太硬.net/tv`
* **王二小**: `http://new.王二小放牛娃.top/`
* **嗷呜**: `http://itv666.cc/aowu/config.webp`

### 3. 官方及大佬交流群 (Telegram)
* [FongMi 官方频道](https://web.telegram.org/k/#@fongmi_official) | [饭太硬](https://web.telegram.org/k/#@TVBoxxoo) | [王二小放牛娃](https://web.telegram.org/k/#@wangerxiaofangniuwa) | [嗷呜交流频道](https://web.telegram.org/a/#-1003462278777) 

### 4. 源解析服务
* [FongMi UA 解析服务](https://ua.fongmi.eu.org/) (`https://ua.fongmi.eu.org/`)

---

# Clash 代理规则

> [!NOTE]
> 供 Clash 或 OpenClash 客户端导入使用的订阅及规则配置。

* **Clash 订阅配置 (配置三)**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/Clash3.yml`
* **Clash 订阅配置 (配置二)**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/Clash2.yml`
* **OpenClash 自定义规则 (MihomoPro)**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/clash/custRule/MihomoPro-2025-09-10.yaml`

---

# GKD & 李跳跳 (广告自动跳过)

### 1. GKD (基于无障碍的跳广告工具)
> [!NOTE]
> GKD 是一款基于无障碍服务的跳广告工具。你可以复制下方的订阅链接导入到 GKD App 中。
>
> * **GKD 第三方订阅规则**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/gkd/GKD_subscription.json5`

### 2. 李跳跳
> [!TIP]
> 经典的自动跳广告工具。
>
> * **客户端下载**: [李跳跳 派大星 2.2](/litiaotiao/李跳跳_派大星2.2.apk)
> * **李跳跳规则文件**: [/litiaotiao/AllRules.json](/litiaotiao/AllRules.json)
> * **使用指南**: [李跳跳进阶指南.pdf](/litiaotiao/李跳跳进阶指南-掘金.pdf)

---

# 实用接口

### 法定节假日/工作日查询 API
* **接口地址**: `https://raw.githubusercontent.com/yangxiaoge/tvbox_cust/refs/heads/master/holiday/isHoliday.json`
* **说明**: 供相关自动化脚本或智能家居判定今日是否为节假日使用。

---

# 进阶玩法

## 1. 三方 TVBox 云编译
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

### 编译依赖项目及同步状态

| 项目名称 (Repository) | 编译分支 | 最新 Commit Hash | 同步时间 (Build Time) |
| :--- | :--- | :--- | :--- |
| [FongMi/TV (内置源版)](https://github.com/FongMi/TV) | release | 171a41b... | 2026-01-13 04:34:53 |
| [q215613905/TVBoxOS](https://github.com/q215613905/TVBoxOS) | main | 02f05c8... | 2026-06-22 05:22:35 |
| [takagen99/Box](https://github.com/takagen99/Box) | main | 258a5fe... | 2026-02-28 04:47:47 |
| [mlabalabala/box](https://github.com/mlabalabala/box) | main | c5dc2b9... | 2026-03-18 04:44:50 |

*同步数据更新于: 2026-06-22 05:22:35*

## 2. 自定义爬虫源 (Spiders)
提供给 TVBox / FongMi 等客户端解析视频使用的爬虫规则库：
* [CatVodSpider - 自用修改版](https://github.com/yangxiaoge/CatVodSpider)
* [CatVodSpider - FongMi 官方版](https://github.com/FongMi/CatVodSpider)
* [CatVodSpider - bizhangjie 版](https://github.com/bizhangjie/CatVodSpider)

---

# 免责声明

本项目（tvbox_cust）的源代码是按“原样”提供，不带任何明示或暗示的保证。使用者有责任确保其使用符合当地法律法规。

所有以任何方式查看本仓库内容的人、或直接或间接使用本仓库内容的使用者都应仔细阅读此声明。本仓库管理者保留随时更改或补充此免责声明的权利。一旦使用、复制、修改了本仓库内容，则视为您已接受此免责声明。

本仓库管理者不能保证本仓库内容的合法性、准确性、完整性和有效性，请根据情况自行判断。本仓库内容，仅用于测试和学习研究，禁止用于商业用途，不得将其用于违反国家、地区、组织等的法律法规或相关规定的其他用途，禁止任何公众号、自媒体进行任何形式的转载、发布，请不要在中华人民共和国境内使用本仓库内容，否则后果自负。

本仓库内容中涉及的第三方硬件、软件等，与本仓库内容没有任何直接或间接的关系。本仓库内容仅对部署和使用过程进行客观描述，不代表支持使用任何第三方硬件、软件。使用任何第三方硬件、软件，所造成的一切后果由使用的个人或组织承担，与本仓库内容无关。

所有直接或间接使用本仓库内容的个人和组织，应 24 小时内完成学习和研究，并及时删除本仓库内容。如对本仓库内容的功能有需求，应自行开发相关功能。所有基于本仓库内容的源代码，进行的任何修改，为其他个人或组织的自发行为，与本仓库内容没有任何直接或间接的关系，所造成的一切后果亦与本仓库内容和本仓库管理者无关。

---

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yangxiaoge/tvbox_cust&type=Date)](https://star-history.com/#yangxiaoge/tvbox_cust&Date)
