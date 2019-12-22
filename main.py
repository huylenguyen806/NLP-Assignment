from __future__ import absolute_import

import os
import sys

from models.depparsing import create_pos, malt_parser
from models.loaddata import load_data, data_path, queries_path, output_path, quote
from models.gramrel import grammarical_relation
from models.logicalform import logical_form
from models.proceduralsem import procedural_semantic
from models.query import query, conduct_query

if len(sys.argv) > 1 and len(sys.argv) < 3:
    print("Must provide enough arguments: $data_file, $queries_file, $output_dir")
    sys.exit(0)

d_path = sys.argv[1] if len(sys.argv) == 3 else data_path
q_path = sys.argv[2] if len(sys.argv) == 3 else queries_path
o_path = sys.argv[3] if len(sys.argv) == 3 else output_path


def main():
    data, queries = load_data(data_path=d_path, queries_path=q_path)
    output_a = []
    output_b = []
    output_c = []
    output_d = []
    for q in queries:
        pos = create_pos(q)
        alpha = malt_parser(pos)
        gram_rel = grammarical_relation(alpha)
        output_a.append(gram_rel)

        loc = logical_form(gram_rel)
        output_b.append(loc)

        proc = procedural_semantic(loc)
        output_c.append(proc)

        q = query(proc)
        output_d.append(conduct_query(q, data))
    with open(quote.join([o_path, "output_a.txt"]), "w", encoding='utf-8') as a:
        for line in output_a:
            a.write(str(line) + "\n")
    with open(quote.join([o_path, "output_b.txt"]), "w", encoding='utf-8') as b:
        for line in output_b:
            b.write(str(line) + "\n")
    with open(quote.join([o_path, "output_c.txt"]), "w", encoding='utf-8') as c:
        for line in output_c:
            c.write(str(line) + "\n")
    with open(quote.join([o_path, "output_d.txt"]), "w", encoding='utf-8') as d:
        for line in output_d:
            d.write(str(line) + "\n")



if __name__ == '__main__':
    main()
