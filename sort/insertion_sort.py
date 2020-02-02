from random import shuffle, randint


def insertion_sort(data: list):
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i])
        for j in range(len(new_data)-1, 0, -1):
            if new_data[j] < new_data[j-1]:
                new_data[j], new_data[j-1] = (
                    new_data[j-1], new_data[j])
        print('第', i+1, '回', new_data)


def insertion_sort_new(data: list):
    for i in range(1, len(data)):
        j = i - 1
        tmp = data[i]
        while j >= 0 and tmp < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = tmp
        print('第', i, '回', data)


if __name__ == "__main__":
    num = 10
    data = [n for n in range(1, num+randint(1, 2))]
    shuffle(data)
    print('origin:', data)
    insertion_sort_new(data)
