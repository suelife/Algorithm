from random import shuffle, randint

def test_func(func):
    num = 10
    data = [n for n in range(1, num+randint(1, 2))]
    shuffle(data)
    print('origin:', data)
    func(data)