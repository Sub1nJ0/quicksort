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

def writeFile(quick):
    f = open('Result.csv', 'w', newline='')
    wr = csv.writer(f)
    for i in quick:
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


if __name__ == "__main__":
    n_list = csvtolist()

    start_p = psutil.Process()
    start_rss = start_p.memory_info().rss / 2 ** 20  # bytes to mb
    start_time = time.time()

    quick = quicksort(n_list)

    end_time = time.time()
    end_p = psutil.Process()
    end_rss = end_p.memory_info().rss / 2 ** 20  # bytes to mb

    t = end_time - start_time
    m = end_rss - start_rss

    print(quick)
    print(len(quick))
    print(f"실행 시간: {t}")
    print(f"사용 메모리: {m}MB")
    #print(start_p.memory_info())
    #print(end_p.memory_info())

    writeFile(quick)
