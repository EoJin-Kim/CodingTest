def turn_left(direction):
    direction =(direction-1)%4
    return direction


def turn_right(direction):
    direction =(direction+1)%4
    return direction