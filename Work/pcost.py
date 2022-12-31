# pcost.py
#
# Exercise 1.27

import sys

import fileparse
import stock


def portfolio_cost(filename):
    with open(filename) as f:
        portfolio_dicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [stock.Stock(name=d['name'], shares=d['shares'], price=d['price']) for d in portfolio_dicts]
    return sum(stock.cost() for stock in portfolio)


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        return RuntimeError(f'Usage: {args[0]} filename')

    cost = portfolio_cost(filename)
    print('Total cost', cost)


if __name__ == '__main__':
    main(sys.argv)
