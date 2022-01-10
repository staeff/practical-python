import csv

def portfolio_cost(filename):
    """Read csv file with stock portfolio and compute the total cost"""
    total_cost = 0
    with open('Data/portfolio.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_cost += int(row['shares']) * float(row['price'])
    return total_cost

if __name__ == '__main__':
    cost = portfolio_cost('Data/portfolio.csv')
    print(f'Total cost {cost:0.2f}')
