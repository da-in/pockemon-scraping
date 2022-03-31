import csv
import json

csv_file = './poketmon.csv'
json_path = 'pokemon.json'

data=[]
with open(csv_file, 'rt', encoding='utf-8') as data_csv:
    csv_reader = csv.DictReader(data_csv)
    for row in csv_reader:
        data.append(row)

with open(json_path, 'tw', encoding='utf-8') as data_json:
    data_json.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))