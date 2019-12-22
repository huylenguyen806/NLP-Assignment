from __future__ import absolute_import

import os
import platform

quote = "\\" if platform.system() == 'Windows' else '/'
dirname = os.path.dirname(os.path.abspath(__file__))

data_path = quote.join([dirname, '..', 'input', 'data.csv'])
queries_path = quote.join([dirname, '..', 'input', 'queries.txt'])


def load_data():
    with open(data_path, "r", encoding="utf-8") as d:
        data = d.read().splitlines()
        data = data[1:]
        for i in range(len(data)):
            data[i] = data[i].split(",")
            temp = data[i]
            data[i] = {
                'BUS': temp[0],
                'ATIME': temp[1],
                'DEST': temp[2],
                'DTIME': temp[3],
                'SOURCE': temp[4],
                'RUN_TIME': temp[5]
            }
    with open(queries_path, "r", encoding="utf-8") as q:
        queries = q.read().splitlines()
    return data, queries
