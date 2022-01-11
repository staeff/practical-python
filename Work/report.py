# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
import sys

def read_portfolio(filename):
    """Read csv file with stock portfolio and return the list of stocks"""
    portfolio = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['shares'] = int(row['shares'])
                row['price'] = float(row['price'])
                portfolio.append(row)
            except ValueError as err:
                print(f'Invalid line at name {row["name"]}'
                      f'\nThe line is discarded'
                      f'\nErrormessage: {err}')
    return portfolio

def compute_total(portfolio):
    """Compute total portfolio value

        portfolio: list of dicts containing stocks
                   in format (name, amount_shares, price)

        :return: total - total value as int
    """
    total = 0.0
    for item in portfolio:
        total += item['shares']*item['price']
    return total

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    pprint(portfolio)

    total = compute_total(portfolio)
    print(f'Total value of the portfolio: {total}$')
