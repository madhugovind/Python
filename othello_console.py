# Madhumitha Govindaraju ID 81772721
# othello_console.py

import othello

def _run_game():
    '''run the game, play the game, takes in 2 players, they alternate'''
    print("\nFULL")
    col = choose_num_col()
    row = choose_num_row()
    '''Asks user input for turn and winning criteria'''
    turn = input()
    winning_criteria = input()
    #board = get_board(col, row)
    board = [['.','.','.','.'], ['.','B','B','.'], ['.','B','B','.'], ['.','.','.','.']]
    '''creates an object of the class Othello'''
    ogame = othello.Othello(col, row, winning_criteria, turn, board)
    while True:
        '''principle while loop that runs through the steps of thello printing
        number of tiles, the board, current turn, and switching tiles'''
        try:
            if not ogame.no_more_empty_spaces():
                ogame.print_num_tiles()
                ogame.print_screen()
                ogame.print_player_turn()
                while not ogame.check_and_switch(get_coord()):
                    print("INVALID")
                print("VALID")
                ogame.change_player_turn()
            elif ogame.winner() == ogame.BLACK:
                ogame.print_num_tiles()
                ogame.print_screen()
                print("WINNER:", ogame_BLACK)
                break
            elif ogame.winner() == ogame.WHITE:
                ogame.print_num_tiles()
                ogame.print_screen()
                print("WINNER:", ogame.WHITE)
                break
            elif ogame.winner() == ogame.NONE:
                ogame.print_num_tiles()
                ogame.print_screen()
                print("WINNER: NONE")
                break
        except IndexError:
            pass        
            
def choose_num_col()-> int:
    '''choose number of columns on the board'''
    while True:
        try:
            col_choice  = int(input())
            if col_choice in range(4,17):
                return col_choice
        except ValueError:
            pass

def choose_num_row()-> int:
    '''choose num of rows on the board'''
    while True:
        try:
            row_choice  = int(input())
            if row_choice in range(4,17):
                return row_choice
        except ValueError:
            pass

def get_board(col:int, row:int) -> [] :
    '''input starting board'''
    temp_board = []
    for r in range(row): 
        each_row = input().split(" ")
        temp_board.append([])
        for c in range(col):
            temp_board[-1].append(each_row[c])
    return temp_board

def get_coord() -> []:
    '''choose dropping coordinate'''
    inp = input().split(" ")
    inp=[int(inp[0])-1, int(inp[1])-1]
    return inp

if __name__ == "__main__":
    _run_game()
