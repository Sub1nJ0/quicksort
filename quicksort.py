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

    start_p1 = psutil.Process()
    start_rss1 = start_p1.memory_info().rss / 2 ** 20  # bytes to mb
    start_time1 = time.time()

    quick = quicksort(n_list)

    end_time1 = time.time()
    end_p1 = psutil.Process()
    end_rss1 = end_p1.memory_info().rss / 2 ** 20  # bytes to mb

    t1 = end_time1 - start_time1
    m1 = end_rss1 - start_rss1

    print(quick)
    print(len(quick))
    print(f"실행 시간: {t1}")
    print(f"사용 메모리: {m1}MB")
    # print(start_p.memory_info())
    # print(end_p.memory_info())

    writeFile(quick)

    start_p2 = psutil.Process()
    start_rss2 = start_p2.memory_info().rss / 2 ** 20  # bytes to mb
    start_time2 = time.time()

    result = sorted(n_list)

    end_time2 = time.time()
    end_p2 = psutil.Process()
    end_rss2 = end_p2.memory_info().rss / 2 ** 20  # bytes to mb

    t2 = end_time2 - start_time2
    m2 = end_rss2 - start_rss2

    print(f"내장 sorted 실행 시간: {t2}")
    print(f"내장 sorted 사용 메모리: {m2}MB")
