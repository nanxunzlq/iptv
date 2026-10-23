# IPTV 聚合仓库

[![仓库自检](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml/badge.svg)](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

个人维护的 IPTV 直播源仓库：以**河南移动、河南电信 IPTV** 为核心，提供可直接订阅的频道列表（m3u / DIYP txt 双格式），并配套链接探活、源自动生成与仓库自检工具链。

- **直播源** — 河南移动 283 条 / 14 分组（含 EPG 与备用线路）+ 河南电信 57 条 / 3 分组；两套源各自 m3u 与 txt 的频道名、URL、分组一致
- **工具链** — `iptv-checker` 批量探活、`iptv-api` 采集生成（git submodule）
- **质量保障** — GitHub Actions 每周校验结构、分组数量、双格式等价性与订阅地址可达性
- **跨运营商对照** — 河南移动 132 个频道逐一匹配河南电信源，输出对照表与双向缺口清单

> **网络要求**：两套源都是运营商内网地址——河南移动源为 `iptv.cdn.ha.chinamobile.com`（仅河南移动宽带可播），河南电信源为 `219.150.217.47:6610`（仅河南电信宽带可播），跨网、跨省均不可用。

## 目录

- [核心功能](#核心功能)
- [主要特性](#主要特性)
- [适用场景](#适用场景)
- [快速开始](#快速开始)
- [直播源与频道构成](#直播源与频道构成)
- [技术栈](#技术栈)
- [目录说明](#目录说明)
- [配套工具](#配套工具)
- [自动化与维护](#自动化与维护)
- [许可证](#许可证)
- [相关链接](#相关链接)
- [说明](#说明)

---

## 核心功能

| 能力 | 说明 |
|---|---|
| 直播源分发 | 维护一份河南移动 IPTV 频道列表，以 m3u 与 DIYP txt 两种格式对外订阅 |
| 链接探活 | 用 `tools/iptv-checker` 批量检测播放列表中的链接，输出可用 / 失效两份清单 |
| 源自动生成 | 用 `tools/iptv-api` 完成采集 → 聚合 → 测速 → 生成播放列表 |
| 一致性校验 | 用 GitHub Actions 校验频道数、分组质量、双格式等价性与订阅地址可达性 |
| 跨运营商对照 | 将河南移动频道逐一映射到河南电信源，输出对照表与双向缺口清单（见 `docs/`） |

## 主要特性

**直播源**

- 283 条频道、14 个分组，覆盖央视频道、卫视、河南本地、4K、数字付费等类别（详见下文「频道构成」）
- 129 条主线路 + 154 条备用线路，主线路异常时可切换
- m3u 内置 EPG 地址（`epg.51zmt.top`），标准播放器会自动拉取节目单
- m3u 与 txt 的频道名、URL、分组完全一致，仅排列顺序不同，由脚本强制校验
- 含 4K 频道与 CHC 系列数字付费频道

**工具链**

- `iptv-checker`：基于 `ffprobe` 的 Node.js CLI，批量探活并输出 `online.m3u` / `failed.m3u`
- `iptv-api`：Python 实现的源自动生成工具，支持 CLI、桌面 GUI、Docker 与 GitHub Actions

**维护**

- 推送核心文件与每周定时触发自检，失败自动创建 `[自动巡检]` Issue
- Dependabot 跟踪 npm 依赖、子模块指针与 Actions 版本
- 多许可证边界清晰：自有内容与 `iptv-checker` 为 MIT，`iptv-api` 以子模块隔离 AGPL-3.0

## 适用场景

**适合**

- 河南移动宽带用户，希望在电视、机顶盒或手机上直接观看直播
- 使用 DIYP / 影视类安卓应用，需要 `频道名,URL` 格式的 txt 源
- 想自建或持续更新直播源的用户，复用本仓库的探活与生成工具

**不适合**

- 非河南移动网络环境 —— 源为运营商内网地址，换网络无法播放
- 需要全球公开频道 —— 请使用 [iptv-org/iptv](https://github.com/iptv-org/iptv)
- 需要商业授权或稳定性承诺 —— 本项目由个人维护

## 快速开始

### 方式一：订阅现成源（推荐）

在播放器中添加以下任一地址（路径含中文，已做 URL 编码）：

```text
# m3u（含 EPG，推荐）
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.m3u

# txt（DIYP / 影视类应用）
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.txt
```

| 客户端 | 操作 |
|---|---|
| DIYP / 影视类应用 | 在「直播配置 / 接口」中填入 txt 地址 |
| PotPlayer | 右键 → 打开 → 打开链接，粘贴 m3u 地址 |
| TiviMate / IPTVnator | 新建播放列表 → 远程 URL，粘贴 m3u 地址 |

也可直接下载 [`河南移动.m3u`](河南移动/河南移动.m3u) 或 [`河南移动.txt`](河南移动/河南移动.txt) 本地导入。两个地址的可达性由自检工作流每周核验。

### 方式二：本地探活

```bash
git clone https://github.com/nanxunzlq/iptv.git
cd iptv/tools/iptv-checker
npm install
npx iptv-checker ../../河南移动/河南移动.m3u -p 1 -t 8000 -r 1
```

- 依赖 Node.js >= 22.12 与 FFmpeg（`ffprobe` 需在 `PATH` 中）
- 常用参数：`-t` 超时（毫秒）、`-p` 并发数、`-d` 请求间隔（毫秒）、`-r` 失败重试次数
- 结果输出到 `iptv-checker_<时间戳>/`，含 `online.m3u` 与 `failed.m3u`

> **探活注意**：运营商 CDN 对高频请求会短暂返回 `404`，而非拒绝连接。务必降低并发、拉长间隔（运营商源建议 `-p 1 -d 1500`），判定失效前先冷却数分钟再复验，否则容易误删正常源。

### 方式三：初始化源生成工具

`tools/iptv-api` 是 git submodule，克隆后需初始化：

```bash
# 克隆时一并拉取
git clone --recurse-submodules --depth 1 https://github.com/nanxunzlq/iptv.git

# 已克隆的仓库补充初始化
git submodule update --init --depth 1 tools/iptv-api
```

初始化后按 `tools/iptv-api/README.md` 使用。

## 直播源与频道构成

移动源采集自**河南移动 IPTV**（`iptv.cdn.ha.chinamobile.com`），最近一次更新为 2026-10。两种格式内容等价：

| 文件 | 格式 | 条数 | 适用场景 |
|---|---|---|---|
| [`河南移动.m3u`](河南移动/河南移动.m3u) | M3U（含 tvg-id / EPG 地址） | **283** | PotPlayer、TiviMate、IPTVnator 等标准播放器，**推荐** |
| [`河南移动.txt`](河南移动/河南移动.txt) | DIYP（`频道名,URL` + `#genre#` 分组） | **283** | DIYP / 影视类安卓应用 |

> 两版频道名、URL、分组逐一相同，区别只在格式：m3u 带 `tvg-id` 与 EPG 地址，txt 为 DIYP 专用的 `频道名,URL` 分组格式。

### 频道构成（以 m3u 完整版为准）

| 分类 | 条数 | 内容 |
|---|---|---|
| 央视频道 | 50 | CCTV1~CCTV17 及备用线路（含 CCTV5+；**CCTV16 仅备用线路**） |
| 央视 | 7 | CGTN 多语种（俄 / 法 / 西 / 纪录 / 阿语）及备用线路（**主线路暂缺**） |
| 其它 | 58 | 中国教育 1~4 台、健康中原、武术世界、文物宝库、国学、都市剧场、财富天下、茶频道、快乐垂钓、先锋乒羽、环球旅游、书画频道、法治天地、老故事、中华特产、乐游、收藏天下、咪咕视频、优优宝贝、动漫秀场等（含备用线路） |
| 卫视频道 | 36 | 全国省级卫视主线路（含河南、三沙、延边、康巴、厦门等） |
| 卫视 | 55 | 上述卫视的备用线路（含 4K 版备用线路） |
| 山东 | 1 | 山东教育卫视 |
| 河南 | 35 | 河南新闻 / 都市 / 民生 / 公共 / 法治 / 电视剧 / 乡村 / 戏曲 / 梨园、大美河南、健康河南、河南移动电视、河南 4K 试验等（含备用线路） |
| 4K频道 | 10 | CCTV4K（含备用线路）、东方 / 江苏 / 浙江 / 山东 / 湖南 / 广东 / 四川 / 深圳卫视 4K |
| 数字付费 | 3 | CHC 家庭影院、CHC 动作电影、CHC 影迷电影 |
| 数字频道 | 15 | CCTV 数字频道（第一剧场 / 风云剧场 / 怀旧剧场、风云音乐 / 风云足球、高尔夫网球、央视台球、世界地理、兵器科技、卫生健康、央视文化精品）、新视觉、生活时尚、欢笑剧场、金鹰纪实 |
| 东方 | 3 | 东方财经及备用线路 |
| 少儿 | 5 | 卡酷少儿、金鹰卡通（含备用线路） |
| 卡通动漫 | 2 | 嘉佳卡通、金鹰卡通 |
| 江苏 | 3 | 江苏优漫卡通及备用线路 |

> 表中的「分类」即两个文件中 `group-title` / `#genre#` 的实际取值，数量由[自检工作流](#自动化与维护)强制校验。
> m3u 与 txt 使用同一套 14 个分组，频道名、URL、分组逐一相同（仅排列顺序不同）。
> 另附[《河南移动 ↔ 河南电信 频道对照表》](docs/河南移动-河南电信频道对照.md)：132 个移动频道逐一匹配电信源 57 条，命中 53 个、缺口 79 个。

### 河南电信源（57 条）

[`河南电信/`](河南电信/) 下另附一套河南电信 IPTV 源，同为 m3u + DIYP txt 双格式，共 **57 条**、3 个分组。

**频道构成**

- **央视 18 条**：CCTV-1 ~ CCTV-15、CCTV-17、CCTV-5+、CETV1
- **卫视 24 条**：浙江、东方、江苏、北京、广东、黑龙江、山东、安徽、辽宁、陕西、河北、江西、湖南、深圳、四川、湖北、天津、云南、重庆、吉林、东南、广西、海南、甘肃
- **河南 15 条**：河南卫视、都市、民生、法治、电视剧、新闻、公共、乡村、河南国际、睛彩中原、移动戏曲、收藏天下、河南戏曲、中华功夫、调节剧场

**使用方法**

| 订阅方式 | 地址 | 适用 |
|---|---|---|
| M3U | `https://raw.githubusercontent.com/nanxunzlq/iptv/main/河南电信/河南电信.m3u` | PotPlayer、TiviMate、IPTVnator 等标准播放器 |
| DIYP | `https://raw.githubusercontent.com/nanxunzlq/iptv/main/河南电信/河南电信.txt` | DIYP、影视类安卓应用 |

在播放器「添加订阅 / 打开 URL」里粘贴对应地址即可；m3u 已内置 EPG 地址与台标，txt 为 `频道名,URL` 分组格式。

**说明**

- **网络**：仅河南电信宽带可播。移动、联通或外省网络下全部无法连接，属网络限制而非源失效
- **跳转**：首次请求返回 `302` 并向地址追加 `IASHttpSessionId` 会话参数，播放器需支持 HLS 重定向（主流播放器默认支持）
- **抖动**：「移动戏曲」「调节剧场」约 3–4 成请求返回空分片（`HTTP 204` 或 0 字节），重连即可恢复；两者均无备用线路，不建议据此判定失效
- **无 4K**：原「河南卫视4K测试」二级清单长期为空（仅 53 字节、无 `#EXTINF`、无分片），已于 2026-10-23 移除，当前 57 条不含 4K 频道
- **命名**：与移动源不同（`CCTV-1综合` vs `CCTV1`、`新闻频道` vs `河南新闻`），混用前请对照[频道对照表](docs/河南移动-河南电信频道对照.md)

> 该源来自第三方 Gist，来源与许可证状态见 [THIRD-PARTY.md](THIRD-PARTY.md)。

### EPG 节目单

m3u 头部已内置 EPG 地址（`epg.51zmt.top` 的 `cc.xml` 与 `difang.xml`），标准播放器会自动拉取。个别频道无节目单通常是播放器与节目单源的匹配方式差异，不影响播放。

### 频道实测

**河南移动（2026-10-20，移动家宽）**：283 条全部可播——低速率单遍探测（每条约 1.5 秒间隔、单请求）下，280 条直接返回 HLS 清单，另 3 条首次请求返回跳转、复验即返回 `206`。

> 该结论依赖正确的探活方法：高并发探测会触发运营商的临时 `404`，把正常源误判为「间歇性失效」。同一批次先测出的 19 条「抖动」源，冷却 7 分钟后逐条复验全部恢复。

**河南电信（2026-10-23，电信家宽）**：57 条逐条验证（一级清单 → 二级 media playlist → 首个 TS 分片 `0x47`），55 条稳定可播；「移动戏曲」「调节剧场」地址有效但存在偶发空分片，低频复验即恢复，且无备用线路可替换。抽样 7 条 `ffprobe` 解出 H.264 / 1920×1080 / 25–50 fps。原 58 条中的「河南卫视4K测试」因二级清单长期为空（6 轮复验一致）已移除。

## 技术栈

| 层次 | 技术 | 说明 |
|---|---|---|
| 数据格式 | Extended M3U、DIYP txt | 标准播放列表与 DIYP 的 `频道名,URL` + `#genre#` 格式 |
| 节目单 | EPG（`x-tvg-url`） | m3u 头部指向 `epg.51zmt.top` 的节目单 |
| 探活工具 | Node.js >= 22.12（ESM）、axios、FFmpeg `ffprobe` | `tools/iptv-checker` |
| 生成工具 | Python 3.14、asyncio、Flask、PySide6、Pipenv | `tools/iptv-api`，支持 CLI / GUI / Docker |
| CI | GitHub Actions、Bash、Python 3 | 结构校验、等价性校验、订阅地址可达性检查 |
| 依赖管理 | npm、Pipenv、git submodule、Dependabot | 分别跟踪三类依赖 |

主仓库本身是**纯数据仓库**，没有运行时依赖与构建步骤；依赖只存在于 `tools/` 下的两个工具中。

## 目录说明

```text
.
├── 河南移动/
│   ├── 河南移动.m3u          # 完整版（283 条 / 14 分组，含 EPG）
│   └── 河南移动.txt          # DIYP 格式（283 条 / 14 分组）
├── 河南电信/
│   ├── 河南电信.m3u          # 57 条 / 3 分组（含 EPG 与台标）
│   └── 河南电信.txt          # DIYP 格式（57 条 / 3 分组）
├── tools/
│   ├── iptv-checker/         # m3u 链接批量探活 CLI（上游快照）
│   └── iptv-api/             # 源自动采集 / 测速 / 生成（git submodule）
├── .github/
│   ├── workflows/            # 仓库自检工作流
│   ├── scripts/              # m3u ↔ txt 等价性校验脚本
│   └── dependabot.yml        # 依赖与子模块更新
├── docs/
│   ├── ecosystem.md          # IPTV 生态索引
│   └── 河南移动-河南电信频道对照.md # 移动 ↔ 电信频道对照与缺口
├── THIRD-PARTY.md            # 第三方组件与许可证清单
├── LICENSE                   # MIT（仅适用于本仓库自有内容）
└── .gitmodules               # submodule 定义
```

## 配套工具

### `tools/iptv-checker/` — 链接探活

Node.js CLI，基于 `ffprobe` 批量检查 IPTV 播放列表中的链接是否可播放。用法见上文「方式二：本地探活」。

- 本目录是上游 `freearhey/iptv-checker` 的本地快照（0.30.3，MIT，上游已停更）
- 测试套件 16/16 通过；跑测试前建议剥离系统代理：`env -u http_proxy -u https_proxy npm test`
- 依赖安全状态见[自动化与维护](#自动化与维护)

### `tools/iptv-api/` — 源自动生成

直播源自动更新工具：采集 → 聚合 → 去重 → 可用性校验 → 测速筛选 → 生成播放列表，支持 M3U / TXT / API 输出、自定义频道、IPv4 / IPv6、Docker、GitHub Actions、CLI 与桌面 GUI。

以 git submodule 引入，钉在上游 `3.1.0`（commit `2a4d925`）。来源 `Guovin/iptv-api`，许可证 **AGPL-3.0**，使用前请阅读其条款。

## 自动化与维护

### 仓库自检（GitHub Actions）

`.github/workflows/iptv-health-check.yml` 每周一自动运行；推送 `河南移动/`、`README.md`、工作流或校验脚本时也会触发，并支持手动触发：

| 检查项 | 说明 |
|---|---|
| 频道数一致性 | m3u / txt 的实际频道数必须与上表声明一致，防止改了源忘了改 README |
| 结构完整性 | 每个 `#EXTINF` 须有对应 URL、URL 不重复、首行为 `#EXTM3U`、txt 含 `#genre#` 分组 |
| 分组质量 | 每个频道必须带 `group-title`；m3u 中不得出现 DIYP 专用的 `#genre#` 语法，分组名不得含逗号 |
| 分类数量一致 | README 的 14 个分类数量必须与 m3u 中各 `group-title` 的实际数量一致 |
| m3u ↔ txt 等价 | 两版频道名与 URL 必须一一对应（顺序允许不同），由 `.github/scripts/check_playlist_equivalence.py` 校验 |
| 订阅地址可达 | 两个 Raw 订阅地址须返回 HTTP 200 |

自检失败会自动创建或更新一条 `[自动巡检]` Issue（同标记只保留一条，持续更新，不会刷屏）。

> **为什么 CI 不实测直播源**：河南移动源仅在运营商宽带环境下可达，GitHub Actions runner 上必然全部失败。因此实测探活被设计为**手动可选**（手动触发时勾选 `probe_streams`），日常任务只做文件一致性与可达性校验。

### 依赖维护

| 目标 | 说明 |
|---|---|
| `tools/iptv-checker`（npm） | 第三方工具的本地快照，上游已停更，安全修复只能在本地锁文件上做 |
| `tools/iptv-api`（git submodule） | 指向上游仓库，由 Dependabot 提出指针升级 PR |
| `.github/workflows/`（Actions） | 工作流引用的 action 版本 |

依赖策略：只接受锁文件内的补丁 / 次版本更新（Dependabot 已忽略主版本）；不改上游源码，便于将来同步新版时干净比对。

**已知告警（2026-10-16 核验）**：全部位于 `tools/iptv-checker` 的 jest / babel 开发链路，根因为 `sprintf-js`（中危）与 `braces`（高危，上游暂无修复版本）；`npm audit` 路径级共 33 条，均为二者的传递计数，不影响工具运行时功能。彻底移除需将 `jest` / `babel-jest` 升至 30（主版本、破坏性变更），按快照策略暂不接收。

## 许可证

本仓库**并非单一许可证**，不同来源的组件适用不同条款：

| 路径 | 来源 | 许可证 | 传染性 |
|---|---|---|---|
| `河南移动/`、根目录自有文件 | 本仓库 | MIT | 无 |
| `tools/iptv-checker/` | `freearhey/iptv-checker` | MIT | 无 |
| `tools/iptv-api/` | `Guovin/iptv-api` | **AGPL-3.0** | **强 copyleft** |

完整第三方清单与来源见 [THIRD-PARTY.md](THIRD-PARTY.md)。

### 为什么 `iptv-api` 用子模块而不是直接并入

`iptv-api` 采用 **AGPL-3.0**，这是 copyleft 强度最高的许可证之一 —— 不仅要求开源，**即便只以网络服务形式提供，也必须向使用者提供完整源码**。

若将其代码直接并入本仓库，法律上会构成组合作品，**整个仓库都将被迫以 AGPL-3.0 发布**，本仓库原有 MIT 部分将无法继续保持宽松条款。

因此它被隔离为 git submodule：独立引用上游仓库，法律上属于独立作品，本仓库的 MIT 部分不受影响。使用时请自行遵守 AGPL-3.0 的要求。

## 相关链接

- [THIRD-PARTY.md](THIRD-PARTY.md) — 第三方组件、来源与许可证
- [docs/ecosystem.md](docs/ecosystem.md) — IPTV 生态索引与链路串接方式
- [docs/河南移动-河南电信频道对照.md](docs/河南移动-河南电信频道对照.md) — 移动 132 个频道与电信源的逐一对照及双向缺口
- [Actions 运行记录](https://github.com/nanxunzlq/iptv/actions) — 自检历史
- [Issues](https://github.com/nanxunzlq/iptv/issues) — 问题反馈与自动巡检报告
- 上游项目：[iptv-org/iptv](https://github.com/iptv-org/iptv)、[Guovin/iptv-api](https://github.com/Guovin/iptv-api)、[freearhey/iptv-checker](https://github.com/freearhey/iptv-checker)

## 说明

- 直播源采集 / 更新于 **2026-10**，可能因运营商策略调整而失效；若大量频道无法加载，通常是源地址失效，可用 `tools/iptv-checker` 复核后重新采集更新 `河南移动/` 下的文件
- 本仓库不做直播源自动存活检测（运营商内网源在 GitHub Actions 上无法连通），自检只校验**文件一致性**与**订阅地址可达性**
- 提交信息请遵循 Conventional Commits 规范（如 `docs:`、`feat:`、`fix:`）
- 直播流版权归各运营商与频道方所有，本仓库仅收录地址；内容仅供个人学习与研究使用，请勿用于商业用途
