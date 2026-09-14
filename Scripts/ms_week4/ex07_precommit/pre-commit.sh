#!/usr/bin/env bash
# Git pre-commit 钩子示例
# Missing Semester 元编程课程练习 3
#
# 安装方法：将此文件复制到 .git/hooks/pre-commit 并赋予执行权限
#   cp pre-commit.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# 作用：在提交前运行质量检查，构建失败则拒绝提交

set -euo pipefail

echo "=== pre-commit: 运行代码质量检查 ==="

# 1. 运行 ruff 检查
if command -v ruff &> /dev/null; then
    echo "[1/3] ruff check..."
    ruff check .
else
    echo "[1/3] ruff 未安装，跳过"
fi

# 2. 运行测试
if command -v pytest &> /dev/null; then
    echo "[2/3] pytest..."
    pytest tests/ -q
else
    echo "[2/3] pytest 未安装，跳过"
fi

# 3. 尝试构建（如果有 Makefile）
if [ -f Makefile ]; then
    echo "[3/3] make..."
    make
else
    echo "[3/3] 无 Makefile，跳过构建"
fi

echo "=== pre-commit: 全部检查通过，允许提交 ==="
exit 0
