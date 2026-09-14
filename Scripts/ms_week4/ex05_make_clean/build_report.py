text = open("report.md").read()
total = open("stats.txt").read()
with open("report.txt", "w") as f:
    f.write(f"{text}\nTotal: {total}\n")
