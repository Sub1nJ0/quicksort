import random
import csv
import numpy as np

"""rn_list = np.random.randint(low=-500000, high=500000, size=1000000)
rn_list = np.transpose(rn_list)
rn_list = rn_list.tolist()
print(rn_list)"""
f = open('RN.csv', 'w', newline='')
wr = csv.writer(f)
for i in range(1000000):
    list = []
    x = random.randint(-500000, 500000)
    list.append(x)
    print(list)
    wr.writerow(list)
f.close()