# IPTV 聚合仓库

个人 IPTV 直播源与配套工具合集。以**河南移动直播源**为核心，同时收纳频道列表、源生成工具与链接校验工具。

> 2026-09-16 由原 5 个独立仓库（`iptv`、`iptv-api`、`Beijing-IPTV`、`iptv-checker`、`iptv-org`）合并而成。

---

## 仓库结构

```
.
├── hn.txt                    ★ 河南移动直播源（97 频道，本仓库核心）
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

频道列表共 **97 个频道**，整理在 [`hn.txt`](hn.txt)，采用 `频道名,URL` 逐行格式。

### 频道统计

| 分类 | 频道数 | 内容 |
|---|---|---|
| 央视频道 | 17 | CCTV1 ~ CCTV17（含 CCTV5+） |
| 数字频道 | 13 | CGTN 系列、中国教育 1-4 台、凤凰三台 |
| 河南地方台 | 26 | 河南都市/民生/新闻/4K、梨园、武术世界等 |
| 卫视频道 | 36 | 全国省级卫视 |
| 卡通动漫 | 5 | 金鹰卡通、嘉佳卡通、哈哈炫动等 |

### 订阅地址

```
https://raw.githubusercontent.com/nanxunzlq/iptv/main/hn.txt
```

> ⚠️ **此地址请勿变动。** `hn.txt` 刻意保留在仓库根目录，以维持该 Raw 链接长期稳定 —— 已有使用者可能已将其填入播放器订阅。

### 使用方法

在播放器中添加上述地址即可自动导入全部频道：

- **DIYP / 影视类应用**：在「直播配置/接口」中填入该地址
- **PotPlayer**：右键 → 打开 → 打开链接
- **TiviMate / IPTVnator**：新建播放列表 → 选择远程 URL

也可直接下载 `hn.txt` 本地导入。

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

### 一个橙子Pro — Windows 端工具（Releases 分发）

IPTV 直播源检测 / 播放工具，Windows 安装包。

因安装包体积达 **110.16 MB**，超过 GitHub 单文件 **100 MiB** 的硬限制，无法作为仓库文件存放，改由 **Releases** 发布：

**下载地址**：https://github.com/nanxunzlq/iptv/releases

| 项 | 值 |
|---|---|
| 版本 | `1.4.16-beta.7`（x64） |
| 体积 | 110.16 MB |
| 打包方式 | NSIS 安装程序，**无数字签名** |
| 版权 | `Copyright © 2024 yigechengzi`（第三方工具，未提供许可证） |

> 本仓库仅作存档分发，不对该工具的安全性、功能性与合法性作任何保证。完整说明与校验值见 Releases 页面。

---

## 四、许可证

本仓库**并非单一许可证**，不同来源的组件适用不同条款：

| 路径 | 来源 | 许可证 | 传染性 |
|---|---|---|---|
| `hn.txt`、根目录自有文件 | 本仓库 | MIT | 无 |
| `lists/Beijing-IPTV/` | `qwerttvv/Beijing-IPTV` | CC0-1.0 | 无 |
| `tools/iptv-checker/` | `freearhey/iptv-checker` | MIT | 无 |
| `tools/iptv-api/` | `Guovin/iptv-api` | **AGPL-3.0** | **强 copyleft** |
| Releases 附件：一个橙子Pro | `yigechengzi` | 未提供许可证 | — |

完整第三方清单与来源见 [THIRD-PARTY.md](THIRD-PARTY.md)。

### 为什么 `iptv-api` 用子模块而不是直接并入

`iptv-api` 采用 **AGPL-3.0**，这是 copyleft 强度最高的许可证之一 —— 不仅要求开源，**即便只以网络服务形式提供，也必须向使用者提供完整源码**。

若将其代码直接并入本仓库，法律上会构成组合作品，**整个仓库都将被迫以 AGPL-3.0 发布**，本仓库原有 MIT 部分将无法再保持宽松条款。

因此它被隔离为 git submodule：独立引用上游仓库，法律上是独立作品，本仓库的 MIT 部分不受影响。使用时请自行遵守 AGPL-3.0 的要求。

---

## 五、说明

- 河南频道数据采集于 **2024-10**，直播源可能因运营商策略调整而失效
- 直播源一般需在对应运营商网络环境下才能访问
- 本仓库不包含自动存活检测。若大量频道无法加载，通常为源地址失效，需重新采集后更新 `hn.txt`
- 提交信息请遵循 Conventional Commits 规范（如 `docs:`、`feat:`、`fix:`）
- 仅供个人学习与研究使用，请勿用于商业用途
