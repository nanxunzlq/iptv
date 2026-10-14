# IPTV 聚合仓库

[![仓库自检](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml/badge.svg)](https://github.com/nanxunzlq/iptv/actions/workflows/iptv-health-check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

个人 IPTV 直播源与配套工具一站式合集：

- **河南移动直播源**（核心）—— m3u 完整版 94 频道 + txt 完整版 94 频道（DIYP 格式），收录在 [`河南移动/`](河南移动/) 目录
- **北京联通/移动频道列表** —— 组播与单播 m3u 全套
- **工具箱** —— `iptv-api` 源自动采集生成（submodule）、`iptv-checker` 链接批量探活

> 2026-09-16 由原 5 个独立仓库（`iptv`、`iptv-api`、`Beijing-IPTV`、`iptv-checker`、`iptv-org`）合并而成。各组件来源与许可证不同，详见[许可证说明](#四许可证)。

---

## 仓库结构

```
.
├── 河南移动/
│   ├── 河南移动.m3u          ★ 河南移动直播源完整版（94 频道，含 EPG）
│   └── 河南移动.txt          河南移动直播源（94 频道，8 分组，DIYP 格式）
├── lists/
│   └── Beijing-IPTV/         北京联通/移动频道列表
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

---

## 一、河南移动直播源（本仓库自有）

直播源来自 **河南移动 IPTV**（`iptv.cdn.ha.chinamobile.com`），2026-09 更新采集，提供两种格式：

| 文件 | 格式 | 频道数 | 适用场景 |
|---|---|---|---|
| [`河南移动.m3u`](河南移动/河南移动.m3u) | M3U（含 tvg-id / EPG 地址） | **95** | PotPlayer、TiviMate、IPTVnator 等标准播放器，**推荐** |
| [`河南移动.txt`](河南移动/河南移动.txt) | DIYP（`频道名,URL` + `#genre#` 分组） | **94** | DIYP / 影视类安卓应用 |

> 两版频道**完全一致**（94 个频道、URL 逐一相同），区别只在格式：m3u 带 `tvg-id` 与 EPG 地址，txt 是 DIYP 应用专用的 `频道名,URL` 分组格式。
> 播放器用户优先用 m3u（有 EPG 节目单），DIYP / 影视类应用用 txt。

### 频道构成（以 m3u 完整版为准）

| 分类 | 频道数 | 内容 |
|---|---|---|
| 央视频道 | 17 | CCTV1~CCTV15、CCTV17（含 CCTV5+；**CCTV16 暂缺**） |
| 卫视频道 | 36 | 全国省级卫视（含河南、三沙、延边、康巴、厦门等） |
| 卡通动漫 | 5 | 金鹰卡通、金鹰纪实、嘉佳卡通、哈哈炫动、欢笑剧场 |
| 河南地方及其他 | 36 | 河南都市/民生/新闻/法治/4K/梨园/武术世界、中国教育系列、CGTN 多语种、安多卫视、山东教育卫视等 |

> 表中的「分类」即 m3u 中各频道 `group-title` 的实际取值，数量由[仓库自检](#六仓库自检)强制校验。
> txt（DIYP 格式）按其自身的 8 个分组组织，分组划分与 m3u 不同，但**频道名与 URL 完全相同**。

### 频道实测状态（2026-10-12）

> 以下结果在**公网环境（非河南移动宽带）**下对全部 94 个频道做了两轮独立测试、每轮 3 次采样
> （判据：HTTP 200/206 且返回有效响应体），并对两轮结果交叉比对。
> 运营商源在河南移动宽带内的真实可用率**可能高于此结果**，本表仅作换源参考，不据此删减频道。

| 状态 | 数量 | 说明 |
|---|---|---|
| ❌ 高置信失效 | 18 | 两轮 × 3 次采样全部 404/502，重新采集时应优先替换 |
| ❓ 疑似失效 | 6 | 仅最新一轮全失败、早前轮次可用，倾向视为 CDN 抖动 |
| ✅ 可用或抖动 | 70 | 至少部分采样通过；其中约 40 个时通时不通，本地网络下大概率正常 |

**❌ 高置信失效（18）**：CCTV2、CCTV5、CCTV6、CCTV8、CCTV10、CCTV14、湖南卫视、浙江卫视、宁夏卫视、西藏卫视、兵团卫视、安多卫视、河南导视、移动戏曲、晴彩中原、中国教育1台、嘉佳卡通、哈哈炫动

**❓ 疑似失效（6）**：CCTV12、CCTV15、山西卫视、河北卫视、武术世界、江苏优漫卡通

> 另发现部分频道对 User-Agent 敏感：播放器 UA 被拒、浏览器 UA 可通。若某频道在你的播放器中黑屏而列表未标注失效，换一个播放器或自定义 UA 可能即可恢复。

### 订阅地址

```
m3u 完整版：
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.m3u

txt 完整版：
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.txt
```

> 路径含中文（URL 已编码）。若播放器不支持编码地址，可直接下载对应文件导入，或使用仓库网页内点击链接。

### 使用方法

在播放器中添加上述订阅地址即可自动导入：

- **DIYP / 影视类应用**：在「直播配置/接口」中填入 txt 版地址
- **PotPlayer**：右键 → 打开 → 打开链接（m3u 地址）
- **TiviMate / IPTVnator**：新建播放列表 → 选择远程 URL（m3u 地址）

也可直接下载 `河南移动.m3u` / `河南移动.txt` 本地导入。

---

## 二、北京频道列表

`lists/Beijing-IPTV/` 收录北京联通、北京移动的 IPTV 频道列表（组播与单播），另有配套的扫描工具源码与网页。

| 文件 | 说明 |
|---|---|
| `IPTV-Unicom.m3u` | 北京联通单播列表 |
| `IPTV-Unicom-Multicast.m3u` | 北京联通组播列表 |
| `IPTV-Mobile.m3u` | 北京移动单播列表 |
| `IPTV-Mobile-Multicast.m3u` | 北京移动组播列表 |
| `*-Scan-*.m3u` | 扫描生成的备选列表 |
| `index.html` / `howto.md` | 网页索引与使用说明 |
| `iptvscanner.go` | 扫描工具源码（Go） |

来源：`qwerttvv/Beijing-IPTV`（CC0-1.0）

---

## 三、工具

### `tools/iptv-checker/` — m3u 链接探活

Node.js CLI，批量检查 IPTV 播放列表中的链接是否可用。

```bash
cd tools/iptv-checker
npm install
npx iptv-checker /path/to/playlist.m3u
```

来源：`freearhey/iptv-checker`（MIT）

### `tools/iptv-api/` — 源自动生成（子模块）

直播源自动更新工具：采集 → 聚合 → 去重 → 测速 → 生成可播放结果，支持 M3U/TXT/API 输出、自定义频道、IPv4/IPv6、Docker、GitHub Actions、CLI 与 GUI。

**这是一个 git submodule，克隆后需初始化：**

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

### 依赖维护

本仓库自身没有依赖清单，需要维护的依赖只有两处，均由 `.github/dependabot.yml` 每周自动检查：

| 目标 | 说明 |
|---|---|
| `tools/iptv-checker`（npm） | 第三方工具的本地快照。上游已停更（最新版 0.30.3 / 2026-03），因此安全修复只能在本地锁文件上做 |
| `tools/iptv-api`（git submodule） | 指向上游仓库，由 Dependabot 提出指针升级 PR |
| `.github/workflows/`（Actions） | 工作流中引用的 action 版本 |

`tools/iptv-checker/package-lock.json` 已于 2026-10 做过一轮定向安全刷新（`axios` 1.13.6 → 1.20.0 等）。剩余 2 个告警（`braces`、`sprintf-js`）**上游尚无修复版本**，且仅存在于 jest/babel 开发链路，不影响工具运行时；升级 `babel-jest` 到 30 可移除该链路，但属破坏性变更，需单独评估。

> 该目录是**上游快照**，接受本地依赖补丁（锁文件级），但不改动上游源码，以便将来同步新版时能干净地比对差异。

---

## 四、许可证

本仓库**并非单一许可证**，不同来源的组件适用不同条款：

| 路径 | 来源 | 许可证 | 传染性 |
|---|---|---|---|
| `河南移动/`、根目录自有文件 | 本仓库 | MIT | 无 |
| `lists/Beijing-IPTV/` | `qwerttvv/Beijing-IPTV` | CC0-1.0 | 无 |
| `tools/iptv-checker/` | `freearhey/iptv-checker` | MIT | 无 |
| `tools/iptv-api/` | `Guovin/iptv-api` | **AGPL-3.0** | **强 copyleft** |

完整第三方清单与来源见 [THIRD-PARTY.md](THIRD-PARTY.md)。

### 为什么 `iptv-api` 用子模块而不是直接并入

`iptv-api` 采用 **AGPL-3.0**，这是 copyleft 强度最高的许可证之一 —— 不仅要求开源，**即便只以网络服务形式提供，也必须向使用者提供完整源码**。

若将其代码直接并入本仓库，法律上会构成组合作品，**整个仓库都将被迫以 AGPL-3.0 发布**，本仓库原有 MIT 部分将无法再保持宽松条款。

因此它被隔离为 git submodule：独立引用上游仓库，法律上是独立作品，本仓库的 MIT 部分不受影响。使用时请自行遵守 AGPL-3.0 的要求。

---

## 五、说明

- 河南移动源采集/更新于 **2026-09**，直播源可能因运营商策略调整而失效
- 直播源一般需在**河南移动宽带网络**环境下才能访问
- 本仓库不包含直播源的自动存活检测（运营商内网源在 GitHub Actions 上无法连通）。
  已内置的[仓库自检](#六仓库自检)只校验**文件一致性**与**订阅地址可达性**；
  若要实测频道存活，请本地运行 `tools/iptv-checker`，或手动触发 workflow 的 `probe_streams` 参数
- 若大量频道无法加载，通常为源地址失效，需重新采集后更新 `河南移动/` 下的文件
- 提交信息请遵循 Conventional Commits 规范（如 `docs:`、`feat:`、`fix:`）
- 仅供个人学习与研究使用，请勿用于商业用途

---

## 六、仓库自检

`.github/workflows/iptv-health-check.yml` 每周一自动运行，也可手动触发，推送核心文件时也会触发。

| 检查项 | 说明 |
|---|---|
| 频道数一致性 | m3u / txt 的实际频道数必须与上表声明一致，防止改了源忘了改 README |
| 结构完整性 | m3u 每个 `#EXTINF` 须有对应 URL、URL 不重复、首行为 `#EXTM3U`、txt 含 `#genre#` 分组 |
| 分组质量 | 每个频道必须带 `group-title`，且 m3u 中不得出现 DIYP 专用的 `#genre#` 语法、分组名不得含逗号 |
| 分类数量一致 | README 上表 4 个分类的数量必须与 m3u 中各 `group-title` 的实际数量一致 |
| m3u ↔ txt 等价 | 两版频道名与 URL 必须一一对应（顺序允许不同），由 `.github/scripts/check_playlist_equivalence.py` 校验 |
| 订阅地址可达 | 两个 Raw 订阅地址须返回 HTTP 200 |

自检失败会自动创建/更新一条 `[自动巡检]` Issue，不会刷屏（同标记 Issue 只保留一条，持续更新）。

> 「分组质量」与「分类数量一致」是 2026-10 新增的守门项：此前 m3u 有 58 个频道的 `group-title`
> 误混入了 DIYP 的 `#genre#` 语法、另有 36 个频道完全无分组（播放器里会显示成「未分组」）。
> 这两类缺陷不会影响频道数与 URL 校验，所以单靠旧版自检发现不了。

**为什么不在 CI 里实测直播源**：河南移动源属于运营商内网/宽带环境才可达的服务，
GitHub Actions 的 ubuntu runner 上必然全红。因此直播源探活被设计为**手动可选**参数
（手动触发时勾选 `probe_streams`），日常定时任务不跑它。
