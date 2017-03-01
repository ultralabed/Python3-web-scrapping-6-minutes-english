import csv
import json

with open('data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('data.json', 'w') as f:
    json.dump(rows, f)