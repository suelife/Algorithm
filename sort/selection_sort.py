from random import shuffle, randint


def selection_sort(data: list):
    for i in range(len(data)):
        num_min = min(data[i:len(data)])
        num_ind = data.index(num_min)
        data[i], data[num_ind] = data[num_ind], data[i]
        print('第', i+1, '回', data)


if __name__ == "__main__":
    num = 10
    data = [n for n in range(1, num+randint(1, 2))]
    shuffle(data)
    print('origin:', data)
    selection_sort(data)
