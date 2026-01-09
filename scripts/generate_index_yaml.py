from __future__ import annotations

from pathlib import Path

import yaml


def is_challenge_dir(path: Path) -> bool:
    has_readme = (path / "README.md").is_file()
    has_yaml = (path / "challenge.yaml").is_file()
    has_dockerfile = (path / "Dockerfile").is_file() or (path / "build" / "Dockerfile").is_file()
    return has_readme and (has_yaml or has_dockerfile)


def parse_entry(repo_root: Path, path: Path) -> dict:
    rel = path.relative_to(repo_root)
    if len(rel.parts) < 3:
        raise ValueError(f"Invalid challenge path: {rel}")

    competition = rel.parts[0]
    year = rel.parts[1]
    challenge = rel.parts[2]
    if "-" not in challenge:
        raise ValueError(f"Invalid challenge name (expected type-title): {challenge}")

    category, title = challenge.split("-", 1)
    return {
        "competition": competition,
        "year": int(year) if str(year).isdigit() else year,
        "category": category,
        "title": title,
        "path": f"{competition}/{year}/{challenge}",
        "status": "done",
        "tags": [],
        "note": "",
    }


def main() -> None:
    repo_root = Path(".").resolve()
    entries = []
    missing_sources = []
    for path in repo_root.iterdir():
        if not path.is_dir() or path.name.startswith("."):
            continue
        for year_dir in path.iterdir():
            if not year_dir.is_dir():
                continue
            if not (year_dir / "SOURCE.md").is_file():
                missing_sources.append(year_dir)
            for challenge_dir in year_dir.iterdir():
                if not challenge_dir.is_dir():
                    continue
                if is_challenge_dir(challenge_dir):
                    entries.append(parse_entry(repo_root, challenge_dir))

    if missing_sources:
        missing = "\n".join(str(p.relative_to(repo_root)) for p in missing_sources)
        raise SystemExit(f"Missing SOURCE.md in competition year dir:\n{missing}")

    entries.sort(
        key=lambda x: (
            str(x["competition"]).lower(),
            int(x["year"]) if str(x["year"]).isdigit() else str(x["year"]),
            x["category"],
            x["title"],
        )
    )

    Path("INDEX.yaml").write_text(
        yaml.safe_dump(entries, allow_unicode=False, sort_keys=False),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
