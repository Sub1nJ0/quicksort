import random
from tools import time_mem, writecsvFile, csvtolist

# 3번
def myquicksort(n_list):
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
    return myquicksort(left) + mid + myquicksort(right)

if __name__ == "__main__":
    fname = input("정렬할 파일 이름: ").upper()
    n_list = csvtolist(fname)
    # myquicksort
    start_time3, before_proc3 = time_mem()
    sorted_res = myquicksort(n_list)
    end_time3, after_proc3 = time_mem()

    writecsvFile(sorted_res, 'res3.csv')

    t3 = end_time3 - start_time3
    m3 = after_proc3 - before_proc3
    print(f"파일: {fname}.csv")
    print(f"myquicksort 실행 시간: {t3}")
    print(f"myquicksort 사용 메모리: {m3}MB")