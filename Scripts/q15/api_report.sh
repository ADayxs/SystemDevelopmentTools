#!/usr/bin/env bash
set -e

curl -fsS http://127.0.0.1:8000/packages.json | \
# 先转成数组处理：筛选→排序→格式化
jq -r '[.[] | select(.status == "active" and .downloads >= 100)] | sort_by(-.downloads, .name)[] | "- **\(.name)** (v\(.version)) - \(.downloads) downloads"' | \
sed '1i# Active Packages' > summary.md
