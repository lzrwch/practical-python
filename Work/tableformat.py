
class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        header_string = ''.join([f'<th>{h}</th>' for h in headers])
        print(f'<tr>{header_string}</tr>')

    def row(self, rowdata):
        row_string = ''.join([f'<td>{r}</td>' for r in rowdata])
        print(f'<tr>{row_string}</tr>')


def create_formatter(name):
    name_to_formatter_cls = {
        'txt': TextTableFormatter,
        'csv': CSVTableFormatter,
        'html': HTMLTableFormatter,
    }
    if name not in name_to_formatter_cls:
        raise FormatError(f'Unknown format {name}')
    return name_to_formatter_cls[name]()


def print_table(data, headers, formatter):
    formatter.headings(headers)
    for row in data:
        rowdata = [f'{getattr(row, h)}' for h in headers]
        formatter.row(rowdata)
