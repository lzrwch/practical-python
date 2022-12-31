# report.py
#
# Exercise 2.4

import sys

import fileparse


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
    with open(portfolio_filename) as f:
        portfolio = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    with open(prices_filename) as f:
        prices = dict(fileparse.parse_csv(f, has_headers=False, types=[str, float]))
    report = make_report(portfolio, prices)
    print_report(report)


def main(args):
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    main(sys.argv)
