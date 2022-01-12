import csv
import sys

def portfolio_cost(filename):
    """Read csv file with stock portfolio and compute the total cost"""
    total_cost = 0
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for rowno, row in enumerate(reader):
            try:
                total_cost +=  int(row['shares']) * float(row['price'])
            except ValueError as err:
                print(f'Row {rowno}: Bad row: {row}'
                      f'\nThe line is not used in the computation of Total cost'
                      f'\nErrormessage: {err}')
    return total_cost

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    print(filename)
    cost = portfolio_cost(filename)
    print(f'Total cost {cost:0.2f}')
