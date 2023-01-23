# pcost.py
#
# Exercise 1.27

import sys

import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        return RuntimeError(f'Usage: {args[0]} filename')

    cost = portfolio_cost(filename)
    print('Total cost', cost)


if __name__ == '__main__':
    main(sys.argv)
