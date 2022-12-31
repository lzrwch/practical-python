# pcost.py
#
# Exercise 1.27

import sys

import fileparse


def portfolio_cost(filename):
    report = fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])
    pcost = 0
    for row in report:
        pcost += row['shares'] * row['price']
    return pcost


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        return RuntimeError(f'Usage: {args[0]} filename')

    with open(filename) as f:
        cost = portfolio_cost(f)
    print('Total cost', cost)


if __name__ == '__main__':
    main(sys.argv)
