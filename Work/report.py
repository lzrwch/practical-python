# report.py
#
# Exercise 2.4

import sys

import fileparse
import stock
import tableformat


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        current_price = prices.get(stock.name, None)
        if current_price is not None:
            report.append(
                (stock.name, stock.shares, current_price, current_price - stock.price)
            )

    return report


def print_report(reportdata, formatter):
    formatter.headings(('Name', 'Shares', 'Price', 'Change'))
    for name, shares, price, price_change in reportdata:
        rowdata = (name, str(shares), f'{price:.2f}', f'{price_change:.2f}')
        formatter.row(rowdata)


def read_portfolio(portfolio_filename):
    with open(portfolio_filename) as f:
        portfolio_dicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    return [stock.Stock(name=d['name'], shares=d['shares'], price=d['price']) for d in portfolio_dicts]


def read_prices(prices_filename):
    with open(prices_filename) as f:
        prices = fileparse.parse_csv(f, has_headers=False, types=[str, float])
    return dict(prices)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''

    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter =  tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    kwargs = {}
    if len(args) > 3:
        kwargs['fmt'] = args[3]
    portfolio_report(args[1], args[2], **kwargs)


if __name__ == '__main__':
    main(sys.argv)
