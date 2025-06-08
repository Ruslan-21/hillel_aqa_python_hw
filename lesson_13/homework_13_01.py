import csv
from pathlib import Path

folder = Path(__file__).parent / "work_with_csv"

file_1 = folder / "random.csv"
file_2 = folder / "random-michaels.csv"

def read_csv_no_headers(file_path):
    with file_path.open('r', newline='', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        data = [tuple(row) for row in reader]
    return data

data1 = read_csv_no_headers(file_1)
data2 = read_csv_no_headers(file_2)

combined_data = set(data1 + data2)

output_file = folder / "result.csv"
with output_file.open('w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)

print(f"Результат: {output_file}")
