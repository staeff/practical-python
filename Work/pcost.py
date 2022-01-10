import csv

total_cost = 0

with open('Data/portfolio.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_cost += int(row['shares']) * float(row['price'])

print(f'Total cost {total_cost:0.2f}')
