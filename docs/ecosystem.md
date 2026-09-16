# IPTV 生态索引

> 本文档由原 `nanxunzlq/iptv-org` 仓库的 README 整理而来。该仓库原为独立仓库，已于 2026-09-16 合并进本仓库。

---

## 上游总源库（本仓库不镜像）

**[iptv-org/iptv](https://github.com/iptv-org/iptv)** — 全球公开 IPTV 频道索引

- 体积约 **1.3 GB**（全球公开频道的 m3u 文本，持续自动更新）
- ⚠️ **本仓库不镜像它** —— 整库克隆/镜像成本高，且上游已有成熟维护机制
- 需要时直接引用上游对应文件即可，无需本地复制

---

## 本仓库内的组件

| 组件 | 路径 | 来源 | 许可证 |
|---|---|---|---|
| 河南移动直播源 | [`hn.txt`](../hn.txt) | 自有 | MIT |
| 北京频道列表 | [`lists/Beijing-IPTV/`](../lists/Beijing-IPTV/) | qwerttvv/Beijing-IPTV | CC0-1.0 |
| m3u 链接探活 | [`tools/iptv-checker/`](../tools/iptv-checker/) | freearhey/iptv-checker | MIT |
| 源自动生成 | `tools/iptv-api/` | Guovin/iptv-api | AGPL-3.0 |

---

## 典型链路的串接方式

```
① 采集/生成    tools/iptv-api   →  产出 M3U / TXT 源
                      ↓
② 质量校验     tools/iptv-checker  →  剔除失效链接
                      ↓
③ 分发使用     hn.txt / lists/Beijing-IPTV/*.m3u  →  填入播放器订阅
```

- **只要现成源**：直接用 `hn.txt` 或 `lists/Beijing-IPTV/` 下的 m3u
- **要自建可持续的源**：用 `tools/iptv-api` 生成，再用 `tools/iptv-checker` 校验

---

## 相关参考

- [iptv-org/iptv](https://github.com/iptv-org/iptv) — 全球公开频道总源
- [Guovin/iptv-api](https://github.com/Guovin/iptv-api) — 源自动更新工具上游
- [freearhey/iptv-checker](https://github.com/freearhey/iptv-checker) — 链接探活工具上游
- [qwerttvv/Beijing-IPTV](https://github.com/qwerttvv/Beijing-IPTV) — 北京频道列表上游

---

## 许可证提示

本仓库为多来源聚合，**组件的许可证各不相同**，尤其 `tools/iptv-api/` 为 **AGPL-3.0**（强 copyleft，提供网络服务亦须开源）。使用前请查阅 [THIRD-PARTY.md](../THIRD-PARTY.md)。
