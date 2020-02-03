import os
import sys
sys.path.append(os.getcwd())
from util import test_func


def insertion_sort(data):
    '''
    # TODO: 補上註釋。

    Arguments:
        data: Input data, the datatype is list.
    '''
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i])
        for j in range(len(new_data)-1, 0, -1):
            if new_data[j] < new_data[j-1]:
                new_data[j], new_data[j-1] = (
                    new_data[j-1], new_data[j])
        print('第', i+1, '回', new_data)


if __name__ == "__main__":
    test_func(insertion_sort)