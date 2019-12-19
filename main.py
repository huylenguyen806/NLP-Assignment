from __future__ import absolute_import

import os
from models.depparsing import create_pos, malt_parser
from models.loaddata import load_data


def main():
    _, queries = load_data()
    pos = create_pos(queries[0])
    print("Query:")
    print(pos)
    print("Dependencies: ")
    alpha = malt_parser(pos)
    for i in alpha:
        print(i)


if __name__ == '__main__':
    main()
