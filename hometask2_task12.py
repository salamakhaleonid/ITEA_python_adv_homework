from random import randrange


# task 12
if __name__ == "__main__":
    main_list = [[randrange(0,10) for x in xrange(5)] for x in range(5)]
    print main_list
    main_list.sort(key=lambda x: x[3])
    print main_list
