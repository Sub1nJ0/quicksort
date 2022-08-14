import random
from tools import time_mem, writecsvFile, csvtolist

# 2번
def quicksort(n_list):
    if len(n_list) <= 1:
        return n_list
    pivot = random.choice(n_list)
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
    fname = input("정렬할 파일 이름: ").upper()
    n_list = csvtolist(fname)

    # quicksort
    start_time1, before_proc1 = time_mem()
    quick_res = quicksort(n_list)
    end_time1, after_proc1 = time_mem()

    writecsvFile(quick_res, 'res1.csv')

    t1 = end_time1 - start_time1
    m1 = after_proc1 - before_proc1

    print(f"파일: {fname}.csv")
    print(f"quicksort 실행 시간: {t1}")
    print(f"quicksort 사용 메모리: {m1}MB")


