import os
import sys
sys.path.append(os.getcwd())
from util import test_func


def bubble_sort(data):
    '''
    由 '右至左' 或 '左至右'
    兩兩比較後重新排序，直至完成排序。

    Arguments:
        data: Input data, the datatype is list.
    '''

    count = 1
    while True:
        flag = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                flag = True
                data[i], data[i+1] = data[i+1], data[i]
        if flag == False:
            break
        print('第', count, '回', data)
        count += 1


if __name__ == "__main__":
    test_func(bubble_sort)
