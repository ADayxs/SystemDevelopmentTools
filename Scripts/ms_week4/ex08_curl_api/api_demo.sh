#!/usr/bin/env bash
# 使用 curl + jq 调用公共 API 示例
# Missing Semester 大杂烩课程 - API 主题
#
# 本脚本调用美国国家气象局 API 获取天气预报
# 无需认证，返回 JSON 格式

set -euo pipefail

echo "=== 1. 使用 curl 获取 API 数据 ==="
# 获取指定坐标（波士顿 MIT 附近）的气象站点信息
curl -fsS "https://api.weather.gov/points/42.3604,-71.0941" -o points.json
echo "已保存 points.json"

echo ""
echo "=== 2. 使用 jq 提取 forecast URL ==="
FORECAST_URL=$(jq -r '.properties.forecast' points.json)
echo "forecast URL: $FORECAST_URL"

echo ""
echo "=== 3. 获取天气预报并提取前 3 个时段 ==="
curl -fsS "$FORECAST_URL" \
  | jq '.properties.periods[0:3] | .[] | {name, temperature, shortForecast}'

echo ""
echo "=== 4. 生成 Markdown 格式报告 ==="
curl -fsS "$FORECAST_URL" \
  | jq -r '
    .properties.periods[0:5]
    | .[]
    | "| \(.name) | \(.temperature)\(.temperatureUnit) | \(.shortForecast) |"
  ' > forecast_report.md

# 添加表头
{
    echo "# Weather Forecast Report"
    echo ""
    echo "| Period | Temperature | Forecast |"
    echo "|--------|-------------|----------|"
    cat forecast_report.md
} > forecast_report.md.tmp
mv forecast_report.md.tmp forecast_report.md

echo "已生成 forecast_report.md"
cat forecast_report.md
