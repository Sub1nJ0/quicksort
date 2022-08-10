import pandas as pd

def csvtolist():
    data = pd.read_csv('UN.csv', names=['num'])
    n = data['num']
    n_list = n.values.tolist()
    print(n_list)

    return n_list

def quick_sort(n_list):
    if len(n_list) <= 1:
        return n_list
    pivot = n_list[len(n_list) // 2]
    lesser_list, equal_list, greater_list = [], [], []
    for num in n_list:
        if num < pivot:
            lesser_list.append(num)
        elif num > pivot:
            greater_list.append(num)
        else:
            equal_list.append(num)
    return quick_sort(lesser_list) + equal_list + quick_sort(greater_list)


if __name__ == "__main__":
    n_list = csvtolist()
    quick = quick_sort(n_list)

    print(quick)
    print(len(quick))