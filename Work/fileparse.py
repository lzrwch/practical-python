# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # read the file headers
        if has_headers:
            headers = next(rows)

        if select is not None and not has_headers:
            raise RuntimeError('select argument requires column headers')

        indices = None
        if select is not None:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices is not None:
                row = [row[index] for index in indices]

            if types is not None:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Cannot parse row {rowno}: {row}; reason: {e}')

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
