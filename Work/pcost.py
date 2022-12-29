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


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
