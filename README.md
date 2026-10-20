# IPTV 聚合仓库

[![仓库自检](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml/badge.svg)](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

个人 IPTV 直播源与配套工具合集：**河南移动 IPTV 直播源**（m3u / DIYP txt 双格式）+ **m3u 探活**、**源自动生成**工具链。

- **直播源**：河南移动宽带环境可用的 IPTV 频道（283 条 / 14 分组），m3u 与 txt 两版频道名、URL、分组完全一致
- **工具**：`iptv-checker` 链接批量探活（本地实测可用）、`iptv-api` 源自动采集生成（git submodule）
- **自动化**：仓库自检（结构 / 一致性 / 分组质量 / 订阅可达）+ Dependabot 依赖更新

## 目录

- [一、订阅地址](#一订阅地址)
- [二、河南移动直播源](#二河南移动直播源)
- [三、仓库结构](#三仓库结构)
- [四、配套工具](#四配套工具)
- [五、自动化与维护](#五自动化与维护)
- [六、许可证](#六许可证)
- [七、说明](#七说明)

---

## 一、订阅地址

在播放器中添加订阅地址即可自动导入（两种格式任选）：

```
m3u 完整版（推荐，含 EPG）：
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.m3u

txt 完整版（DIYP / 影视类应用）：
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.txt
```

> 路径含中文（URL 已编码）。两条地址 2026-10-20 核验均返回 HTTP 200；若播放器不支持编码地址，可直接下载对应文件导入，或使用仓库网页内点击链接。
>
> **网络要求**：直播源为河南移动宽带环境的内网源，需在河南移动网络下访问。

**使用方法：**

- **DIYP / 影视类应用**：在「直播配置 / 接口」中填入 txt 版地址
- **PotPlayer**：右键 → 打开 → 打开链接（m3u 地址）
- **TiviMate / IPTVnator**：新建播放列表 → 选择远程 URL（m3u 地址）
- 也可直接下载 `河南移动.m3u` / `河南移动.txt` 本地导入

---

## 二、河南移动直播源

直播源来自 **河南移动 IPTV**（`iptv.cdn.ha.chinamobile.com`），2026-10 采集更新。提供两种格式：

| 文件 | 格式 | 条数 | 适用场景 |
|---|---|---|---|
| [`河南移动.m3u`](河南移动/河南移动.m3u) | M3U（含 tvg-id / EPG 地址） | **283** | PotPlayer、TiviMate、IPTVnator 等标准播放器，**推荐** |
| [`河南移动.txt`](河南移动/河南移动.txt) | DIYP（`频道名,URL` + `#genre#` 分组） | **283** | DIYP / 影视类安卓应用 |

> 两版**完全一致**（283 条，频道名 / URL / 分组逐一相同），区别只在格式：m3u 带 `tvg-id` 与 EPG 地址，txt 是 DIYP 应用专用的 `频道名,URL` 分组格式。
> 播放器用户优先用 m3u（有 EPG 节目单），DIYP / 影视类应用用 txt。

### 频道构成（以 m3u 完整版为准）

| 分类 | 条数 | 内容 |
|---|---|---|
| 央视频道 | 50 | CCTV1~CCTV17 及备用线路（含 CCTV5+；**CCTV16 仅备用线路**） |
| 央视 | 7 | CGTN 多语种（俄/法/西/记录/阿语）及两条备用线路（**主线路暂缺**） |
| 其它 | 58 | 中国教育 1~4 台、健康中原、武术世界、文物宝库、国学、都市剧场、财富天下、茶频道、快乐垂钓、先锋乒羽、环球旅游、书画频道、法治天地、老故事、中华特产、乐游、收藏天下、咪咕视频、优优宝贝、动漫秀场等（含备用线路） |
| 卫视频道 | 36 | 全国省级卫视主线路（含河南、三沙、延边、康巴、厦门等） |
| 卫视 | 55 | 上述卫视的备用线路（含 4K 版备用线路） |
| 山东 | 1 | 山东教育卫视 |
| 河南 | 35 | 河南新闻/都市/民生/公共/法治/电视剧/乡村/戏曲/梨园、大美河南、健康河南、河南移动电视、河南4K试验等（含备用线路） |
| 4K频道 | 10 | CCTV4K（含备用线路）、东方/江苏/浙江/山东/湖南/广东/四川/深圳卫视 4K |
| 数字付费 | 3 | CHC 家庭影院、CHC 动作电影、CHC 影迷电影 |
| 数字频道 | 15 | CCTV 数字频道（第一/风云/怀旧剧场、风云音乐/足球、高尔夫网球、央视台球、世界地理、兵器科技、卫生健康、央视文化精品）、新视觉、生活时尚、欢笑剧场、金鹰纪实 |
| 东方 | 3 | 东方财经及备用线路 |
| 少儿 | 5 | 卡酷少儿、金鹰卡通（含备用线路） |
| 卡通动漫 | 2 | 嘉佳卡通、金鹰卡通 |
| 江苏 | 3 | 江苏优漫卡通及备用线路 |

> 表中的「分类」即两个文件中 `group-title` / `#genre#` 的实际取值，数量由[仓库自检](#五自动化与维护)强制校验。
> m3u 与 txt 使用**同一套 14 个分组**，频道名、URL、分组逐一相同（仅排列顺序不同）。

### EPG 节目单

m3u 头部已内置 EPG 地址（`epg.51zmt.top`），标准播放器会自动拉取节目单。若个别频道无节目单，通常是播放器与节目单源匹配方式差异，不影响播放。

### 频道实测（2026-10-20，本机河南移动宽带）

**283 条全部可播**：低速率单遍探测（每条约 1.5 秒间隔、单请求）280 条直出 HLS 清单，另 3 条首次请求返回跳转、复验即 206。

> **探活方法比结论更重要**：运营商 CDN 对高频请求不是拒连，而是短暂返回 `404`。用高并发探测（如 12 并发 × 6 采样）会把正常源判成「间歇性失效」，冷却数分钟后自动恢复——本次实测先得出 19 条「抖动」、7 分钟后逐条复验**全部恢复**。
>
> 自行实测时请降并发、拉长间隔（如 `iptv-checker -p 1`），或分批次隔几十秒再测；**判失效前务必冷却复验**，否则很容易误删正常源。

需要自行实测时：本地运行 `tools/iptv-checker`（见下节），或手动触发 workflow 的 `probe_streams` 参数。

---

## 三、仓库结构

```
.
├── 河南移动/
│   ├── 河南移动.m3u          ★ 河南移动直播源完整版（283 条 / 14 分组，含 EPG）
│   └── 河南移动.txt          河南移动直播源（283 条 / 14 分组，DIYP 格式）
├── tools/
│   ├── iptv-api/             源自动采集/校验/测速/生成（git submodule）
│   └── iptv-checker/         m3u 链接批量探活 CLI
├── .github/
│   ├── workflows/            仓库自检（频道数 / 分组质量 / 等价性 / 订阅地址可达性）
│   ├── scripts/              自检脚本（m3u ↔ txt 等价性校验）
│   └── dependabot.yml        依赖与子模块自动更新
├── docs/
│   └── ecosystem.md          IPTV 生态索引
├── THIRD-PARTY.md            第三方组件与许可证清单
├── LICENSE                   MIT（仅适用于本仓库自有内容）
└── .gitmodules               submodule 定义
```

> 2026-09-16 由原 5 个独立仓库合并而来（部分组件后续已移除）。各组件来源与许可证不同，详见[许可证](#六许可证)。

---

## 四、配套工具

### `tools/iptv-checker/` — m3u 链接探活

Node.js CLI，批量检查 IPTV 播放列表中的链接是否可用（基于 `ffprobe`，需先安装 [FFmpeg](https://ffmpeg.org/download.html)）。

```bash
cd tools/iptv-checker
npm install
npx iptv-checker /path/to/playlist.m3u
```

常用参数：`-t 8000`（超时毫秒）、`-p 1`（并发数，运营商源建议 1~2，高并发会被 CDN 判 404）、`-r 1`（失败重试次数）。检查结果输出到 `iptv-checker_<时间戳>/`（含 `online.m3u` / `failed.m3u` 明细）。

- 本目录是上游快照（`freearhey/iptv-checker`，MIT，上游已停更 0.30.3），测试套件 16/16 通过
- 跑测试前建议先剥离系统代理：`env -u http_proxy -u https_proxy npm test`（否则 axios + msw 组合可能因代理产生畸形请求）
- 依赖安全状态见下文「[依赖维护](#依赖维护)」

### `tools/iptv-api/` — 源自动生成（子模块）

直播源自动更新工具：采集 → 聚合 → 去重 → 测速 → 生成可播放结果，支持 M3U/TXT/API 输出、自定义频道、IPv4/IPv6、Docker、GitHub Actions、CLI 与 GUI。

**这是一个 git submodule（钉在上游 `3.1.0`，commit `2a4d925`），克隆后需初始化：**

```bash
# 方式一：克隆时一并拉取
git clone --recurse-submodules --depth 1 https://github.com/nanxunzlq/iptv.git

# 方式二：已克隆后补充初始化
git submodule update --init --depth 1

# 只拉取这个子模块
git submodule update --init --depth 1 tools/iptv-api
```

初始化后按 `tools/iptv-api/README.md` 使用。

来源：`Guovin/iptv-api`（**AGPL-3.0**，见下方许可证说明）

---

## 五、自动化与维护

### 仓库自检（GitHub Actions）

`.github/workflows/iptv-health-check.yml` 每周一自动运行，也可手动触发，推送核心文件时也会触发：

| 检查项 | 说明 |
|---|---|
| 频道数一致性 | m3u / txt 的实际频道数必须与上表声明一致，防止改了源忘了改 README |
| 结构完整性 | m3u 每个 `#EXTINF` 须有对应 URL、URL 不重复、首行为 `#EXTM3U`、txt 含 `#genre#` 分组 |
| 分组质量 | 每个频道必须带 `group-title`，且 m3u 中不得出现 DIYP 专用的 `#genre#` 语法、分组名不得含逗号 |
| 分类数量一致 | README 上表 14 个分类的数量必须与 m3u 中各 `group-title` 的实际数量一致 |
| m3u ↔ txt 等价 | 两版频道名与 URL 必须一一对应（顺序允许不同），由 `.github/scripts/check_playlist_equivalence.py` 校验 |
| 订阅地址可达 | 两个 Raw 订阅地址须返回 HTTP 200 |

自检失败会自动创建/更新一条 `[自动巡检]` Issue，不会刷屏（同标记 Issue 只保留一条，持续更新）。

> **为什么不在 CI 里实测直播源**：河南移动源属于运营商内网/宽带环境才可达的服务，GitHub Actions 的 runner 上必然全红。因此实测探活被设计为**手动可选**（手动触发时勾选 `probe_streams`），日常任务不跑。

### 依赖维护

本仓库自身没有运行时依赖清单，需维护的依赖有三处，均由 `.github/dependabot.yml` 自动检查（npm 与子模块每周一、Actions 每月）：

| 目标 | 说明 |
|---|---|
| `tools/iptv-checker`（npm） | 第三方工具的本地快照。上游已停更（最新版 0.30.3 / 2026-03），安全修复只能在本地锁文件上做 |
| `tools/iptv-api`（git submodule） | 指向上游仓库，由 Dependabot 提出指针升级 PR |
| `.github/workflows/`（Actions） | 工作流中引用的 action 版本 |

**依赖策略**：接受锁文件内的补丁 / 次版本更新（Dependabot 已忽略主版本）；不改上游源码，便于将来同步新版时干净比对。

**当前告警（2026-10-16 核验）**：全部位于 `tools/iptv-checker` 的 jest/babel 开发链路，根因为两个包——`sprintf-js`（中危，Dependabot 开放中）与 `braces`（高危，Dependabot 已自动忽略，上游暂无修复版本）；`npm audit` 路径级共 33 条，均为二者的传递计数，**不影响工具运行时功能**。彻底移除需将 `jest` / `babel-jest` 升至 30（主版本、破坏性变更），按快照策略暂不接收。

---

## 六、许可证

本仓库**并非单一许可证**，不同来源的组件适用不同条款：

| 路径 | 来源 | 许可证 | 传染性 |
|---|---|---|---|
| `河南移动/`、根目录自有文件 | 本仓库 | MIT | 无 |
| `tools/iptv-checker/` | `freearhey/iptv-checker` | MIT | 无 |
| `tools/iptv-api/` | `Guovin/iptv-api` | **AGPL-3.0** | **强 copyleft** |

完整第三方清单与来源见 [THIRD-PARTY.md](THIRD-PARTY.md)。

### 为什么 `iptv-api` 用子模块而不是直接并入

`iptv-api` 采用 **AGPL-3.0**，这是 copyleft 强度最高的许可证之一 —— 不仅要求开源，**即便只以网络服务形式提供，也必须向使用者提供完整源码**。

若将其代码直接并入本仓库，法律上会构成组合作品，**整个仓库都将被迫以 AGPL-3.0 发布**，本仓库原有 MIT 部分将无法再保持宽松条款。

因此它被隔离为 git submodule：独立引用上游仓库，法律上是独立作品，本仓库的 MIT 部分不受影响。使用时请自行遵守 AGPL-3.0 的要求。

---

## 七、说明

- 河南移动源采集/更新于 **2026-10**，直播源可能因运营商策略调整而失效；如大量频道无法加载，通常为源地址失效，可用 `tools/iptv-checker` 复核后重新采集更新 `河南移动/` 下的文件
- 本仓库不包含直播源的自动存活检测（运营商内网源在 GitHub Actions 上无法连通）；内置的[仓库自检](#五自动化与维护)只校验**文件一致性**与**订阅地址可达性**
- 提交信息请遵循 Conventional Commits 规范（如 `docs:`、`feat:`、`fix:`）
- 仅供个人学习与研究使用，请勿用于商业用途
