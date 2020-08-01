import os
import csv

with open('names.csv') as f:
    lines = csv.reader(f)
    for line in lines:
        os.rename(line[0], line[1])
