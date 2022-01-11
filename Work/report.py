# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    """Read csv file with stock portfolio and return the list of stocks"""
    portfolio = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                holding = (row['name'], int(row['shares']), float(row['price']))
                portfolio.append(holding)
            except ValueError as err:
                print(f'Invalid line at name {row["name"]}'
                      f'\nThe line is discarded'
                      f'\nErrormessage: {err}')
    return portfolio

def compute_total(portfolio):
    """Compute total portfolio value

        portfolio: list of tuples containing stocks
                   in format (name, amount_shares, price)

        :return: total - total value as int
    """
    total = 0.0
    for _, shares, price in portfolio:
        total += shares*price
    return total

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    print(portfolio)

    total = compute_total(portfolio)
    print(f'Total value of the portfolio: {total}$')
