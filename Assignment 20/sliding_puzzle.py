# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()



def get_current_pos(puzzle_board, num):
    for i in range(DIM):
        for j in range(DIM):
            if(puzzle_board[i][j] == num):
                return (i, j)



def get_new_pos(puzzle_board, num, current_pos):
    i, j = current_pos
    if(j < DIM - 1 and puzzle_board[i][j+1] == EMPTYSLOT): #right
        return (i, j+1)

    if(j > 0 and puzzle_board[i][j-1] == EMPTYSLOT): #left
        return (i, j-1)

    if(i < DIM - 1 and puzzle_board[i+1][j] == EMPTYSLOT): #down
        return (i+1, j)

    if(i > 0 and puzzle_board[i-1][j] == EMPTYSLOT): #up
        return (i-1, j)

    return None



def move(puzzle_board, current_pos, new_pos, num):
    c_i, c_j = current_pos
    n_i, n_j = new_pos
    puzzle_board[c_i][c_j] = EMPTYSLOT
    puzzle_board[n_i][n_j] = num





def update_board(num, puzzle_board):
    current_pos = get_current_pos(puzzle_board, num)
    new_pos = get_new_pos(puzzle_board, num, current_pos)
    if new_pos != None:
        move(puzzle_board, current_pos, new_pos, num)



def main():
    puzzle_board = initialize_board()
    num = -1
    while num != QUIT:
        display(puzzle_board)
        num = int(input())
        update_board(num, puzzle_board)

main()