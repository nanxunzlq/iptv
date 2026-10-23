# 第三方组件与许可证清单

本仓库聚合了来自多个上游项目的代码与数据。**各组件版权归原作者所有，适用各自的许可证条款**，本仓库的 MIT 许可证仅覆盖自有内容。

快照时间：工具链 2026-09-16；河南电信源 2026-07-10

---

## 一、清单

| 路径 | 上游仓库 | 许可证 | 纳入方式 | 快照 commit |
|---|---|---|---|---|
| `tools/iptv-checker/` | [freearhey/iptv-checker](https://github.com/freearhey/iptv-checker) | MIT | 文件快照 | `6265833d` |
| `tools/iptv-api/` | [Guovin/iptv-api](https://github.com/Guovin/iptv-api) | **AGPL-3.0** | git submodule | `2a4d925`（随上游滚动） |
| `河南电信/` | [pdszhh/河南电信IPTV.m3u](https://gist.github.com/pdszhh/2191e41f635dd6db19ece147c32cdcae) | 未声明 | 格式转换（M3U → DIYP） | 2026-07-10 |

`docs/ecosystem.md` 由本仓库原有的 `iptv-org` 仓库内容整理而来（本项目自有）。

---

## 二、版权与许可证全文

### `tools/iptv-checker/`
- **许可证**：MIT License
- **版权**：Copyright 2023 Arhey
- **全文**：见 [`tools/iptv-checker/LICENSE`](tools/iptv-checker/LICENSE)
- **条款要点**：允许自由使用、修改、分发乃至商业使用，**唯一要求是保留原始版权声明与许可证文本**（本目录内 `LICENSE` 已保留）。

### `tools/iptv-api/`
- **许可证**：GNU Affero General Public License v3.0（AGPL-3.0）
- **版权**：Copyright (c) 2024-PRESENT Govin &lt;https://github.com/guovin&gt;
- **全文**：初始化子模块后见 `tools/iptv-api/LICENSE`
- **条款要点**：
  - 允许使用、修改、分发，但**衍生作品必须以 AGPL-3.0 开源**
  - **网络服务条款**：即使只在服务器上运行而不分发二进制，只要通过网络向用户提供服务，**也必须向使用者提供完整源码**
  - 保留版权声明与许可证文本

### `河南电信/`

- **来源**：GitHub Gist [`pdszhh/河南电信IPTV.m3u`](https://gist.github.com/pdszhh/2191e41f635dd6db19ece147c32cdcae)（2026-07-10 更新）
- **许可证**：上游未声明许可证。本仓库仅做**格式转换**（M3U → DIYP txt）并补齐 m3u 的 EPG 头，未改动频道名、播放地址与分组
- **可播性**：不属本仓库保证范围；2026-10-23 实测 58 条中 57 条可播，且仅河南电信宽带可用
- **移除机制**：若上游或权利人提出异议，可整目录删除，不影响 `河南移动/` 与工具链

---

## 三、合规说明

### 为什么 `iptv-api` 采用子模块隔离

AGPL-3.0 的 copyleft 范围覆盖"组合作品"（combined work）。若将其源代码直接复制进本仓库的普通目录，本仓库在法理上会被视为包含 AGPL 代码的组合作品，从而**整个仓库都需要以 AGPL-3.0 发布** —— 这将使本仓库的自有部分（`河南移动/` 等）无法继续以 MIT 提供。

采用 git submodule 后，它是主仓库中一个**指向独立仓库的引用**（仅记录一个 commit SHA），上游内容独立存在于其自身仓库中，法律上是独立作品。本仓库的 MIT 部分因此不受 AGPL 传染。

### 使用者的义务

- 使用 `tools/iptv-checker/`：保留其版权声明与 LICENSE
- 使用 `tools/iptv-api/`：**须遵守 AGPL-3.0**，包括但不限于衍生作品同许可证开源；若以网络服务形式对外提供，须向服务使用者提供源码

### 更新上游内容

各组件为 2026-09-16 的快照，如需同步上游最新版本：

```bash
# 子模块（iptv-api）：直接跟随上游
git submodule update --remote --depth 1 tools/iptv-api

# 文件快照（iptv-checker）：需手动重新拉取并覆盖
# 参考上游仓库地址见上方清单
```

> ⚠️ 更新 `tools/iptv-api/` 后，若上游许可证发生变更，请同步更新本文件。
