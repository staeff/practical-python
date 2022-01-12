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
                f'\n\nread_prices():'
                f'\nRow {i} does not have the right format'
                f'\nError message: {err}\n'
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

def make_report(portfolio, prices):
    """Use price data to compute value of portfolio stocks

        :input: portfolio: data as dict (name, shares, price)
                price: dict with price changes of stocks

        :return: list of tuples containing the rows name,
                 share, price, change
    """
    report = []
    for row in portfolio:
        stock_name = row['name']
        curr_price = prices[stock_name]
        change = round((curr_price - row['price']),2)
        report.append((stock_name, row['shares'], curr_price, change))

    return report


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

    report = make_report(portfolio, prices)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
