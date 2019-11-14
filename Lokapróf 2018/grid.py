# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'


def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move



def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid



def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end =  ' ')
        print()



def overflow(pos):
    if pos >= DIM or pos < 0:
        return True
    else:
        return False



def update_pos_x(current_pos, user_move):
    if(user_move == 'r'):
        current_x = current_pos[0] + 1 

        if(overflow(current_x)):
            current_x = 0

    
    elif(user_move == 'l'):
        current_x = current_pos[0] - 1 

        if(overflow(current_x)):
            current_x = DIM - 1

    return current_x



def update_pos_y(current_pos, user_move):
    if(user_move == 'u'):
        current_y = current_pos[1] - 1

        if(overflow(current_y)):
            current_y = DIM - 1 
    
    elif(user_move == 'd'):
        current_y = current_pos[1] + 1 

        if(overflow(current_y)):
            current_y = 0

    return current_y




def update_pos(current_pos, user_move):
    if(user_move == 'r' or user_move == 'l'):
        current_x = update_pos_x(current_pos, user_move)
        current_y = current_pos[1]
    
    elif(user_move == 'u' or user_move == 'd'):
        current_y = update_pos_y(current_pos, user_move)
        current_x = current_pos[0]

    current_pos = [current_x, current_y]
    
    return current_pos



def update_grid(current_pos, grid):
    for row in grid:
        for index, element in enumerate(row):
            if element == POSITION:
                row[index] = EMPTY
                break
    grid[current_pos[1]][current_pos[0]] = 'o'


# Main program starts here


grid = initialize_grid()
current_pos = [0,0]

print_grid(grid)

user_move = get_move()
while user_move != 'q':
    #print(user_move)

    current_pos = update_pos(current_pos, user_move)


    update_grid(current_pos, grid)
    print_grid(grid)
    user_move = get_move()


# In your implementation, you have to use the functions and the constants given above