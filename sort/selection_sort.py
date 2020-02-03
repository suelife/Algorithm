import os
import sys
sys.path.append(os.getcwd())
from util import test_func


def selection_sort_no_func(data):
    '''
    1. 找出最小值
    2. 移至最左或最右側(自行決定)
    3. 固定此數值
    4. 從剩餘數字找最小值，並重複2~4步驟，直到排序過所有數字

    Arguments:
        data: Input data, the datatype is list.
    '''
    for i in range(0, len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j

        if min_index != 1:
            data[i], data[min_index] = data[min_index], data[i]

        print('第', i+1, '回', data)


def selection_sort_func(data):
    '''
    1. 找出最小值
    2. 移至最左或最右側(自行決定)
    3. 固定此數值
    4. 從剩餘數字找最小值，並重複2~4步驟，直到排序過所有數字

    Arguments:
        data: Input data, the datatype is list.
    '''
    for i in range(len(data)-1):
        min_num = min(data[i:len(data)])
        min_index = data.index(min_num)
        if data[i] > data[min_index]:
            data[i], data[min_index] = data[min_index], data[i]

        print('第', i+1, '回', data)



if __name__ == "__main__":
    print('不使用Function版')
    test_func(selection_sort_no_func)

    print('使用Function版')
    test_func(selection_sort_func)
