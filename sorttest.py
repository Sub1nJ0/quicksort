from tools import time_mem, writecsvFile, csvtolist

if __name__ == "__main__":
    fname = input("정렬할 파일 이름: ").upper()
    n_list = csvtolist(fname)

    # sorted()
    start_time2, before_proc2 = time_mem()
    sorted_res = sorted(n_list)
    end_time2, after_proc2 = time_mem()

    writecsvFile(sorted_res, 'res2.csv')

    t2 = end_time2 - start_time2
    m2 = after_proc2 - before_proc2

    print(f"파일: {fname}.csv")
    print(f"내장 sorted 실행 시간: {t2}")
    print(f"내장 sorted 사용 메모리: {m2}MB")