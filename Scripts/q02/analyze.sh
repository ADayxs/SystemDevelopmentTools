if [ ! -f "$1" ]; then
    echo "Error: file '$1' not found" >&2
    exit 1
fi
echo "=== Top 2 paths with most 5xx errors ==="
awk -F',' 'NR>1 && $4 ~ /^5/ {print $3}' "$1" | sort | uniq -c | sort -k1,1nr -k2,2 | head -2 | awk '{print $2, $1}'
echo ""
echo "=== Average latency (ms) ==="
awk -F',' 'NR>1 {sum+=$5; count++} END {printf "%.2f\n", sum/count}' "$1"
