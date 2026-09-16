#!/usr/bin/env bash
# Regenerate the styled twins, then run the suite. Pairs are the comparison, so no ablation arm.
# Extra arguments go to `claude plugin eval` (e.g. --runs 1 --case 'report-*').
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/gen-evals.py
exec claude plugin eval plugins/fluent-korean --ablation none --no-publish --judge-model sonnet "$@"
