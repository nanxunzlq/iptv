#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 河南移动.m3u 与 河南移动.txt 的频道与 URL 是否一一对应。

README 声明两版「频道完全一致（283 条、URL 逐一相同）」，本脚本是该声明的守门人。
两文件的**频道顺序允许不同**，但「频道名 -> URL」的映射必须完全相同：
  - 频道名集合一致（不多不少）
  - URL 集合一致
  - 同名频道的 URL 必须相同

任一不满足即退出码 1，并由 workflow 转换为 ::error:: 注解。
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
M3U = ROOT / "河南移动" / "河南移动.m3u"
TXT = ROOT / "河南移动" / "河南移动.txt"

# m3u: #EXTINF 行 -> 下一行 URL；频道名为 EXTINF 行最后一个逗号之后的部分
M3U_ENTRY = re.compile(r"^#EXTINF[^\r\n]*?,(.*?)\r?\n(https?://\S+)", re.M)


def parse_m3u(path):
    text = path.read_text(encoding="utf-8")
    return [(name.strip(), url.strip()) for name, url in M3U_ENTRY.findall(text)]


def parse_txt(path):
    """DIYP 格式：`频道名,URL`；跳过空行、#genre# 分组行与注释行。"""
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, _, url = line.partition(",")
        if url.strip().startswith("http"):
            pairs.append((name.strip(), url.strip()))
    return pairs


def main():
    for path in (M3U, TXT):
        if not path.exists():
            print(f"::error::缺少文件 {path.relative_to(ROOT)}")
            return 1

    m3u = parse_m3u(M3U)
    txt = parse_txt(TXT)
    errors = []

    if not m3u:
        errors.append("河南移动.m3u 未解析到任何频道条目")
    if not txt:
        errors.append("河南移动.txt 未解析到任何频道条目")

    dm = dict(m3u)
    dt = dict(txt)

    only_m3u = sorted(n for n in dm if n not in dt)
    only_txt = sorted(n for n in dt if n not in dm)
    url_diff = sorted(n for n in dm if n in dt and dm[n] != dt[n])

    if only_m3u:
        errors.append(f"仅存在于 m3u 的频道（{len(only_m3u)}）：{'、'.join(only_m3u)}")
    if only_txt:
        errors.append(f"仅存在于 txt 的频道（{len(only_txt)}）：{'、'.join(only_txt)}")
    if url_diff:
        errors.append(f"同名频道 URL 不一致（{len(url_diff)}）：{'、'.join(url_diff)}")
    if len(m3u) != len(txt):
        errors.append(f"条目数不同：m3u={len(m3u)} txt={len(txt)}")

    ok = not errors
    print(f"m3u 条目={len(m3u)}  txt 条目={len(txt)}  映射一致={ok}")
    print(f"m3u 唯一频道名={len(set(dm))}  txt 唯一频道名={len(set(dt))}")

    summary = [
        "## m3u / txt 等价性",
        "",
        "| 项目 | 结果 |",
        "|---|---|",
        f"| m3u 条目数 | {len(m3u)} |",
        f"| txt 条目数 | {len(txt)} |",
        f"| 频道名与 URL 一一对应 | {'✅ 是' if ok else '❌ 否'} |",
    ]
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write("\n".join(summary) + "\n")

    if errors:
        for err in errors:
            print(f"::error::{err}")
        return 1

    print("OK：m3u 与 txt 的频道与 URL 逐一相同（顺序允许不同）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
