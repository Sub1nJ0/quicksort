import pandas as pd
import time
import psutil
import csv

def csvtolist():
    data = pd.read_csv('RN.csv', names=['num'])
    n = data['num']
    n_list = n.values.tolist()
    print(n_list)

    return n_list

def writeFile(res, fname):
    f = open(fname, 'w', newline='')
    wr = csv.writer(f)

    for i in res:
        list = [i]
        wr.writerow(list)

    f.close()


def quicksort(n_list):
    if len(n_list) <= 1:
        return n_list

    pivot = n_list[len(n_list) // 2]
    left, mid, right = [], [], []

    for num in n_list:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)
    return quicksort(left) + mid + quicksort(right)


def time_mem():
    proc_state = psutil.Process()
    p_mem = proc_state.memory_info().rss / 2 ** 20  # bytes to mb
    t = time.time()

    return t, p_mem

if __name__ == "__main__":
    n_list = csvtolist()

    # quicksort
    start_time1, before_proc1 = time_mem()
    quick_res = quicksort(n_list)
    writeFile(quick_res, 'quick_res.csv')
    end_time1, after_proc1 = time_mem()

    t1 = end_time1 - start_time1
    m1 = after_proc1 - before_proc1

    # print(quick_res)
    # print(len(quick_res))
    print(f"quicksort 실행 시간: {t1}")
    print(f"quicksort 사용 메모리: {m1}MB")

    # sorted()
    start_time2, before_proc2 = time_mem()
    sorted_res = sorted(n_list)
    writeFile(sorted_res, 'sorted_res.csv')
    end_time2, after_proc2 = time_mem()

    t2 = end_time2 - start_time2
    m2 = after_proc2 - before_proc2

    print(f"내장 sorted 실행 시간: {t2}")
    print(f"내장 sorted 사용 메모리: {m2}MB")
