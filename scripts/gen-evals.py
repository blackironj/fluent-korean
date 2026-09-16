#!/usr/bin/env python3
"""Generate the styled twin of every eval case.

`claude plugin eval` runs each case in a throwaway configuration where no output style
can be selected, so the plugin's style never activates in the with-arm. Instead, for each
plain case `evals/<name>/` this writes `evals/<name>--styled/`: the same prompt and graders
with `append_system_prompt` set to the current body of fluent-korean.md. The pair is the
comparison; run the suite with `--ablation none`. Generated directories are gitignored, so
run this before every eval to pick up the current rules.
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "fluent-korean"
EVALS = PLUGIN / "evals"
STYLE = PLUGIN / "output-styles" / "fluent-korean.md"
SUFFIX = "--styled"


def split_frontmatter(text: str) -> tuple[list[str], str]:
    if text.startswith("---\n"):
        head, _, rest = text[4:].partition("\n---\n")
        return head.splitlines(), rest
    return [], text


def main() -> None:
    rules = STYLE.read_text(encoding="utf-8").split("---\n", 2)[2].strip()
    plain = sorted(
        d for d in EVALS.iterdir()
        if d.is_dir() and (d / "prompt.md").exists() and not d.name.endswith(SUFFIX)
    )
    for src in plain:
        dst = EVALS / f"{src.name}{SUFFIX}"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        fm, body = split_frontmatter((src / "prompt.md").read_text(encoding="utf-8"))
        fm.append("append_system_prompt: " + json.dumps(rules, ensure_ascii=False))
        (dst / "prompt.md").write_text("---\n" + "\n".join(fm) + "\n---\n" + body, encoding="utf-8")
        print(dst.name)


if __name__ == "__main__":
    main()
