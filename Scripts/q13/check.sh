#!/usr/bin/env bash
set -e

echo "=== 1. Checking code format ==="
ruff format --check .

echo "=== 2. Checking code style ==="
ruff check .

echo "=== 3. Running tests ==="
pytest

echo "✅ All checks passed!"
