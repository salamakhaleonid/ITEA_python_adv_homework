import operator
import time
import sys







def generate_bord(lenght=8,height=8):
    bord = {}
    for i in range(height):
        for j in range(lenght):
            bord[(i,j)] = 1
    return bord

def check_possible_moves_from_position(position):
    global real_bord
    bord = real_bord
    posible_move_positions = {}
    try:
        if bord[(position[0]-2,position[1]-1)] == 1:
            posible_move_positions[(position[0]-2,position[1]-1)] = 1
    except:
        pass

    try:
        if bord[(position[0]-2,position[1]+1)] == 1:
            posible_move_positions[(position[0]-2,position[1]+1)] = 1
    except:
        pass

    try:
        if bord[(position[0]-1,position[1]+2)] == 1:
            posible_move_positions[(position[0]-1,position[1]+2)] = 1
    except:
        pass

    try:
        if bord[(position[0]+1,position[1]+2)] == 1:
            posible_move_positions[(position[0]+1,position[1]+2)] = 1
    except:
        pass

    try:
        if bord[(position[0]+2,position[1]+1)] == 1:
            posible_move_positions[(position[0]+2,position[1]+1)] = 1
    except:
        pass

    try:
        if bord[(position[0]+2,position[1]-1)] == 1:
            posible_move_positions[(position[0]+2,position[1]-1)] = 1
    except:
        pass

    try:
        if bord[(position[0]+1,position[1]-2)] == 1:
            posible_move_positions[(position[0]+1,position[1]-2)] = 1
    except:
        pass

    try:
        if bord[(position[0]-1,position[1]-2)] == 1:
            posible_move_positions[(position[0]-1,position[1]-2)] = 1
    except:
        pass
    return posible_move_positions


def check_number_of_moves_from_position(position):
    global real_bord
    posible_move_positions = check_possible_moves_from_position(position)
    number_of_moves = len(posible_move_positions)
    return number_of_moves

def choose_new_position(possible_move_positions):
    global real_bord
    graph_dict = {}
    for item in possible_move_positions:
        number_of_moves = check_number_of_moves_from_position(item)
        graph_dict[item] = number_of_moves
    sorted_x = sorted(graph_dict.items(), key=operator.itemgetter(1))
    real_bord[sorted_x[0][0]]=0
    return sorted_x[0][0]




def put_horse(position):
    global real_bord
    real_bord[position] = 0


if __name__ == "__main__":
    ts = time.time()
    lenght = 8
    height = 8
    real_bord = generate_bord(lenght=lenght,height=height)
    position = (4,2)
    # print position, 1,
    # print real_bord
    put_horse(position)
    for i in range(lenght*height-1):
        print "---", position, "----"
        for i in range(lenght):
            for j in range(height):
                sys.stdout.write(str(real_bord[(i,j)])+" ")
            print
        # print "---------------"
        possible_move_positions = check_possible_moves_from_position(position)
        position = choose_new_position(possible_move_positions)
        put_horse(position)
        time.sleep(0.5)
    print "---", position, "----"
    for i in range(lenght):
        for j in range(height):
            sys.stdout.write(str(real_bord[(i, j)]) + " ")
        print
    # print "---------------"

