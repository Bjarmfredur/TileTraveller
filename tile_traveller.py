NORTH = 'n'
WEST = 'w'
EAST = 'e'
SOUTH = 's'


def move(direction, col, row):
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def play_move(col, row, pick_direction):
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in pick_direction:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

def print_directions(directions_str, col, row):
    print("You can travel: ", end='')
    first = True
    for i in directions_str:
        if not first:
            print(" or ", end='')
        if i == NORTH:
            print("(N)orth", end='')
        elif i == EAST:
            print("(E)ast", end='')
        elif i == SOUTH:
            print("(S)outh", end='')
        elif i == WEST:
            print("(W)est", end='')
        first = False
    print(".")
    return None
     
def direction_finder(col, row):
    
    if col == 1 and row == 1:   # staðsetning = (1,1)
        pick_direction = NORTH
    elif col == 1 and row == 2: # staðsetning = (1,2)
        pick_direction = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # staðsetning = (1,3)
        pick_direction = EAST+SOUTH
    elif col == 2 and row == 1: # staðsetning = (2,1)
        pick_direction = NORTH
    elif col == 2 and row == 2: # staðsetning = (2,2)
        pick_direction = SOUTH+WEST
    elif col == 2 and row == 3: # staðsetning = (2,3)
        pick_direction = EAST+WEST
    elif col == 3 and row == 2: # staðsetning = (3,2)
        pick_direction = NORTH+SOUTH
    elif col == 3 and row == 3: # staðsetning = (3,3)
        pick_direction = SOUTH+WEST
    return pick_direction


def is_victory(col, row):
    return col == 3 and row == 1 # staðsetning (3,1) er victory   

#Byrjunin á leiknum er hér
victory = False
row = 1
col = 1

pick_direction = NORTH
print_directions(pick_direction, col, row)

while not victory:
    victory, col, row = play_move(col, row, pick_direction)
    if victory:
        print("Victory!")
    else:
        pick_direction = direction_finder(col, row)
        print_directions(pick_direction, col, row)