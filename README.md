# IPTV 聚合仓库

个人 IPTV 直播源与配套工具一站式合集：

- **河南移动直播源**（核心）—— m3u 完整版 94 频道 + txt 精简版 54 频道，收录在 [`河南移动/`](河南移动/) 目录
- **北京联通/移动频道列表** —— 组播与单播 m3u 全套
- **工具箱** —— `iptv-api` 源自动采集生成（submodule）、`iptv-checker` 链接批量探活

> 2026-09-16 由原 5 个独立仓库（`iptv`、`iptv-api`、`Beijing-IPTV`、`iptv-checker`、`iptv-org`）合并而成。各组件来源与许可证不同，详见[许可证说明](#四许可证)。

---

## 仓库结构

```
.
├── 河南移动/
│   ├── 河南移动.m3u          ★ 河南移动直播源完整版（94 频道，含 EPG）
│   └── 河南移动.txt          河南移动直播源精简版（54 频道，DIYP 格式）
├── lists/
│   └── Beijing-IPTV/         北京联通/移动频道列表
├── tools/
│   ├── iptv-api/             源自动采集/校验/测速/生成（git submodule）
│   └── iptv-checker/         m3u 链接批量探活 CLI
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
| [`河南移动.m3u`](河南移动/河南移动.m3u) | M3U（含 tvg-id / EPG 地址） | **94** | PotPlayer、TiviMate、IPTVnator 等标准播放器，**推荐** |
| [`河南移动.txt`](河南移动/河南移动.txt) | DIYP（`频道名,URL` + `#genre#` 分组） | 54 | DIYP / 影视类安卓应用 |

> m3u 为完整版，txt 是其子集（缺少 CCTV3/5/6/8、河南卫视及部分省级卫视等 40 个频道）。**优先使用 m3u 版本。**

### 频道构成（以 m3u 完整版为准）

| 分类 | 频道数 | 内容 |
|---|---|---|
| 央视频道 | 17 | CCTV1 ~ CCTV17（含 CCTV5+） |
| 卫视频道 | 36 | 全国省级卫视（含河南、三沙、延边、康巴、安多等） |
| 卡通动漫 | 5 | 金鹰卡通、嘉佳卡通、哈哈炫动等 |
| 河南地方及其他 | 36 | 河南都市/民生/新闻/4K/梨园/武术世界、中国教育系列、CGTN 多语种等 |

### 订阅地址

```
m3u 完整版：
https://raw.githubusercontent.com/nanxunzlq/iptv/main/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8/%E6%B2%B3%E5%8D%97%E7%A7%BB%E5%8A%A8.m3u

txt 精简版：
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
- 本仓库不包含自动存活检测。若大量频道无法加载，通常为源地址失效，需重新采集后更新 `河南移动/` 下的文件
- 提交信息请遵循 Conventional Commits 规范（如 `docs:`、`feat:`、`fix:`）
- 仅供个人学习与研究使用，请勿用于商业用途
