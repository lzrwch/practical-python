# report.py
#
# Exercise 2.4

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
    portfolio = fileparse.parse_csv(portfolio_filename, select=['name', 'shares', 'price'], types=[str, int, float])
    prices = dict(fileparse.parse_csv(prices_filename, has_headers=False, types=[str, float]))
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
