from random import shuffle, randint


def bubble_sort(data: list):
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
    num = 10
    data = [n for n in range(1, num+randint(1, 2))]
    shuffle(data)
    print('origin:', data)
    bubble_sort(data)
