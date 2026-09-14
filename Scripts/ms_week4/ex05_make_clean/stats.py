import csv

with open("data.csv") as f:
    total = sum(int(r["value"]) for r in csv.DictReader(f))

with open("stats.txt", "w") as f:
    f.write(str(total))
