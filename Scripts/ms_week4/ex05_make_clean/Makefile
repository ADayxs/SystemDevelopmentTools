.PHONY: all clean

all: report.txt

data.csv:
	echo name,value > data.csv
	echo alpha,2 >> data.csv
	echo beta,3 >> data.csv

stats.txt: data.csv stats.py
	python stats.py

report.txt: report.md stats.txt build_report.py
	python build_report.py

clean:
	del /Q stats.txt report.txt 2>nul || rm -f stats.txt report.txt
