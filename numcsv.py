import random
import csv

# 1번
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
    #makeUN()
    #makeON()
    makeRN()
