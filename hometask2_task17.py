import time


def timing(funk):

    def inner(*args, **kw):
        ts = time.time()
        result = funk(*args, **kw)
        te = time.time()

        print te-ts
        return result

    return inner



@timing
def test_list_long(number):
    my_list = []
    for i in range(number):
        my_list.append(i)
    return None


@timing
def test_list_advance(number):
    li = [True] * number
    for i in range(number):
        li[i] = i
    return None
@timing
def add_end(number):
    li=[]
    for i in range(number):
        li = li + [i]

@timing
def add_begining (number):
    li=[]
    for i in range(number):
        li = [i] + li


if __name__ == "__main__":
    test_list_long(100000)
    test_list_advance(100000)
    add_end(10000)
    add_begining(10000)