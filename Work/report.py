# report.py
#
# Exercise 2.4

import csv


def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices



def read_portfolio(filename):
    portfolio = []

    types = [str, int, float]

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            try:
                stock_dict = {name: func(val) for name, func, val in zip(headers, types, row)}
                portfolio.append(stock_dict)
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')

    return portfolio


def make_report(portfolio, prices):
    report = []
    for entry in portfolio:
        current_price = prices.get(entry['name'], None)
        if current_price is not None:
            report.append(
                (entry['name'], entry['shares'], current_price, current_price - entry['price'])
            )

    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, price_change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {price_change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
