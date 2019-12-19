from __future__ import absolute_import

import os
import platform
import pandas as pd

quote = "\\" if platform.system() == 'Windows' else '/'
dirname = os.path.dirname(os.path.abspath(__file__))

data_path = quote.join([dirname, '..', 'input', 'data.csv'])
queries_path = quote.join([dirname, '..', 'input', 'queries.txt'])


def load_data():
    data = pd.read_csv(data_path)
    with open(queries_path, "r", encoding="utf-8") as q:
        queries = q.read().splitlines()
    return data, queries
