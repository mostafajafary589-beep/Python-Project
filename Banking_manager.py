import csv
from pathlib import Path
from collections import defaultdict

FILE = Path("expenses.csv")

def add_expense(category, amount):
    is_new = not FILE.exists()
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["category", "amount"])
        writer.writerow([category, amount])

def summary():
    totals = defaultdict(float)
    with open(FILE, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            totals[row["category"]] += float(row["amount"])
    return totals

add_expense("food", 25.5)
add_expense("transport", 10)
add_expense("food", 14)

for category, total in summary().items():
    print(f"{category}: {total}")