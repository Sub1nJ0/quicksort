import random
import csv

"""rn_list = np.random.randint(low=-500000, high=500000, size=1000000)
rn_list = np.transpose(rn_list)
rn_list = rn_list.tolist()
print(rn_list)"""

# 랜덤 정렬
def makeRN():
    f = open('RN.csv', 'w', newline='')
    wr = csv.writer(f)
    for i in range(1000000):
        x = random.randint(1, 1000001)
        list = [x]
        print(list)
        wr.writerow(list)
    f.close()

# 순방향 정렬
def makeON():
    f = open('ON.csv', 'w', newline='')
    wr = csv.writer(f)
    for i in range(1, 1000001):
        list = [i]
        print(list)
        wr.writerow(list)
    f.close()

# 역방향 정렬
def makeUN():
    f = open('UN.csv', 'w', newline='')
    wr = csv.writer(f)
    for i in range(1000000, 0, -1):
        list = [i]
        print(list)
        wr.writerow(list)
    f.close()

if __name__ == "__main__":
    makeUN()
    makeON()
    makeRN()
