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

def read_prices(filename):
    with open(filename) as csvfile:
        price_dict = {}
        reader = csv.reader(csvfile)
        try:
            for i, row in enumerate(reader, 1):
                price_dict[row[0]] = float(row[1])
        except IndexError as err:
            print(
                f'Row {i} does not have the right format\n'
                f'Error message: {err}'
            )
        return price_dict

def compute_value(portfolio, prices):
    """Compute portfolio value

        :input: portfolio: list of dicts containing stocks
                in format (name, amount_shares, price)
                prices: dictionary of price changes

        :return: total - total value as int
    """
    total = 0.0
    for item in portfolio:
        total += item['shares'] * prices[item['name']]
    return total

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    pprint(portfolio)

    price_file = 'Data/prices.csv'
    prices = read_prices(price_file)

    portfolio_value = compute_value(portfolio, prices)
    print(f'Current value of the portfolio: ${portfolio_value}')
