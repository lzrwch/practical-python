# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if isinstance(lines, str):
        raise ValueError('lines should be an iterable')

    lines = csv.reader(lines, delimiter=delimiter)

    # read the file headers
    if has_headers:
        headers = next(lines)

    if select is not None and not has_headers:
        raise RuntimeError('select argument requires column headers')

    indices = None
    if select is not None:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for lineno, line in enumerate(lines, start=1):
        if not line:
            continue

        if indices is not None:
            line = [line[index] for index in indices]

        if types is not None:
            try:
                line = [func(val) for func, val in zip(types, line)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Cannot parse line {lineno}: {line}; reason: {e}')
                    continue

        record = dict(zip(headers, line)) if has_headers else tuple(line)
        records.append(record)

    return records
