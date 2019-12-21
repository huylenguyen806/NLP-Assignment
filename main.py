from __future__ import absolute_import

import os
from models.depparsing import create_pos, malt_parser
from models.loaddata import load_data
from models.gramrel import grammarical_relation
from models.logicalform import logical_form
from models.proceduralsem import procedural_semantic


def main():
    _, queries = load_data()
    for q in queries:
        pos = create_pos(q)
        print("Query:")
        print(pos)
        print("Dependencies: ")
        alpha = malt_parser(pos)
        for i in alpha:
            print(i)
        print("Grammatical Rel: ")
        gram_rel = grammarical_relation(alpha)
        for i in gram_rel:
            print(i)
        print("Logical form: ")
        loc = logical_form(gram_rel)
        for i in loc:
            print(i)
        print("Procedural Sem: ")
        proc = procedural_semantic(loc)
        for i in proc:
            print(i)


if __name__ == '__main__':
    main()
