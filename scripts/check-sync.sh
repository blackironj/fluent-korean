#!/usr/bin/env bash
# Both output styles must share an identical body; only the frontmatter may differ.
set -euo pipefail
cd "$(dirname "$0")/.."
dir=plugins/fluent-korean/output-styles
body() { awk 'f{print} /^---$/{c++; if(c==2)f=1}' "$1"; }
diff <(body "$dir/fluent-korean.md") <(body "$dir/fluent-korean-not-coding.md") \
  && echo "output-style bodies are in sync"
