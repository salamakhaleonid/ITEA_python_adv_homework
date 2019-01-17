from random import randrange
# task12


def gen_random():
    number = randrange(1, 11)
    if number == 1:
        return number
    else:
        raise ImportError


def retry(func):
    def inner(*args, **kwargs):
        for i in range(20):
            try:
                result = func(*args, **kwargs)
                return result
            except ImportError:
                continue
        return "NO RESULT"
    return inner



@retry
def run():
    return gen_random()


if __name__ == "__main__":
    print run()
