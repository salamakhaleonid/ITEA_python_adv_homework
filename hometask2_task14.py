#task13
from random import randint

func = lambda x: x*randint(1,11)
main_list = [x for x in range(1,11)]
new_list = map(func,main_list)
no_odd_list = filter(lambda x: x % 2 == 0, new_list)
sum_number = reduce((lambda x, y: x + y), no_odd_list) # CHOGO REDUCE PRACJUJE Z LJAMBDA A MAP NI???


if __name__ == "__main__":
    print main_list
    print new_list
    print no_odd_list
    print sum_number

