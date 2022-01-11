import csv
import sys

def portfolio_cost(filename):
    """Read csv file with stock portfolio and compute the total cost"""
    total_cost = 0
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_cost += int(row['shares']) * float(row['price'])
    return total_cost

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    print(filename)
    cost = portfolio_cost(filename)
    print(f'Total cost {cost:0.2f}')
