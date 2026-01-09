from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml


def main() -> None:
    data = Path("INDEX.yaml").read_text(encoding="utf-8")
    items = yaml.safe_load(data) or []

    grouped = defaultdict(list)
    for item in items:
        comp = item.get("competition", "")
        year = item.get("year", "")
        grouped[(comp, year)].append(item)

    lines = ["# 赛题索引", ""]
    for (comp, year) in sorted(grouped, key=lambda x: (str(x[0]).lower(), int(x[1]) if str(x[1]).isdigit() else str(x[1]))):
        lines.append(f"## {comp} {year}")
        lines.append("")
        for item in sorted(grouped[(comp, year)], key=lambda x: (x.get("category", ""), x.get("title", ""))):
            category = item.get("category", "")
            title = item.get("title", "")
            path = item.get("path", "")
            lines.append(f"- {category}: [{title}]({path})")
        lines.append("")

    Path("INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
