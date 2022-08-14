import random

import pandas as pd
import time
import psutil
import csv

def csvtolist(fname):
    data = pd.read_csv(fname+'.csv', names=['num'])
    n = data['num']
    n_list = n.values.tolist()
    print(n_list)

    return n_list

def writecsvFile(res, fname):
    f = open(fname, 'w', newline='')
    wr = csv.writer(f)

    for i in res:
        list = [i]
        wr.writerow(list)

    f.close()

def time_mem():
    proc_state = psutil.Process()
    p_mem = proc_state.memory_info().rss / 2 ** 20  # bytes to mb
    t = time.time()

    return t, p_mem
