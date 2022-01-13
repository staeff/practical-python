# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
import sys

def type_conversion(type_list, row):
    """Convert values of a row into defined types

        :input: type_list - list of python functions to coerce
                types, e.g. [str, int, float]
                row - list of values all strings as they are
                loaded from csv, e.g. ['A', '1', '1']
        return: update row with converted values

    >>> type_list = [str, int, float]
    >>> row = ['a', '1', '1']
    >>> type_conversion(type_list, row)
    ['a', 1, 1.0]
    """
    type_row = list(zip(type_list, row))
    converted = [func(val) for func, val in type_row]
    return converted

def read_portfolio(filename):
    """Read csv file with stock portfolio and return the list of stocks"""
    portfolio = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        # Fill select with field names if you only want a subset of the data
        # For now we take all
        select = headers
        type_list = [str, int, float]
        indices = [ headers.index(colname) for colname in select ]
        for row in reader:
            try:
                row = type_conversion(type_list, row)
                # dict-comprehension
                # record = { colname: row[index] for colname, index in zip(select, indices) }
                # Do it all in on dict comprehension just to show of. The line above is better, I'd say
                record = { name: func(row[index]) for name, func, index in zip(select, type_list, indices) }
                portfolio.append(record)
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

    # This is an example of map-reduce. The list comprehension is mapping
    # an operation across the list. The sum() function is performing a
    # reduction across the result.
    return sum([s['shares'] * prices[s['name']] for s in portfolio])

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

def print_report(report, header):
    """Print out the portfolio report nicely formatted"""
    h = ''.join([f'{i:>10} ' for i in header])
    l = ''.join(['{:_<10} '.format('') for i in range(4)])
    output = f'{h}\n{l}\n'
    for name, shares, price, change in report:
        price_in_dollar = f'${price:.2f}'
        output += (f'{name:>10s} {shares:>10d} {price_in_dollar:>10} {change:>10.2f}\n')

    print(output)



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

    headers = ('Name', 'Shares', 'Price', 'Change')
    print_report(report, headers)
