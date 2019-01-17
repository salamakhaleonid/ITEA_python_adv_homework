from random import randrange

# task 11
list_of_power = ['square', 'cubic', 'four', 'five']


def dict_generator(list_of_power):
    dict_power = {}
    func_power = lambda n: lambda x: x ** n
    for index, value in enumerate(list_of_power):
        y = index + 2
        dict_power[value] = func_power(y)
    return dict_power


def task11(number):
    dict_power = dict_generator(list_of_power)
    for item in dict_power:
        print dict_power[item](number)



if __name__ == "__main__":
    task11(randrange(10,20))


