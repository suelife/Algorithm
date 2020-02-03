import os
import sys
sys.path.append(os.getcwd())
from util import test_func


def selection_sort(data: list):
    for i in range(len(data)):
        num_min = min(data[i:len(data)])
        num_ind = data.index(num_min)
        data[i], data[num_ind] = data[num_ind], data[i]
        print('第', i+1, '回', data)


if __name__ == "__main__":
   test_func(selection_sort)
