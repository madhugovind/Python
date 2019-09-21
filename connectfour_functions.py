#  Madhu Govindaraju 81772721 and Jonathan Moon 24553368 ICS 32
import connectfour
import connectfour_protocol

#create a connect four choice namedtuple
#like drop or pop

class Move:
    def __init__(self,choice:str, column:int):
        '''make a game move'''
        self._choice = choice
        self._column = column


    def choice(self):
        '''return move'''
        return self._choice

    def column(self):
        '''return the column number chosen'''
        return self._column



def choose_col()-> int:
    ''' choose a column that you want to use'''
    call = 0
    while True:
        try:
            col_choice  = int(input("Choose a column from 1 to " + str(connectfour.BOARD_COLUMNS) + ": "))
            if col_choice in range(1,connectfour.BOARD_COLUMNS+1):
                call = col_choice - 1
                break
            else:
                print("Not in range.\n")
        except ValueError:
            print("Needs to be a valid input.\n")
    return call


def print_screen(GS: connectfour.GameState) -> None:
    '''pass in a GameState and use the board to print the screen '''
    print()
    print('  '.join(str(x) for x in range(1,connectfour.BOARD_COLUMNS+1)))
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if GS.board[col][row] == 0:
                pixel = '.  '
            else:
                if GS.board[col][row] == 1:
                    pixel = 'R  '
                elif GS.board[col][row] == 2:
                    pixel = 'Y  '
            print(pixel, sep="", end="")
        print()  # Print newline at end of row
    print()
    return

def start_game(new_g: bool):
    ''' start the game'''
    print("\nWe are going to play Connect Four.\nRed always goes first.")

    #makes our gameboard, starts with all empty
    GS = connectfour.new_game()

    #prints player turn
    print_player_turn(GS, new_g)

    #prints the empty board
    print_screen(GS)
    return GS



def update_board(gm :Move,GS:connectfour.GameState)->connectfour.GameState:
    '''update the board taking in a namedtuple called game_move and see if its drop or pop, and which column it is'''
    if gm.choice()== 'DROP':
        return connectfour.drop(GS,gm.column())
    elif gm.choice() == 'POP':
        return connectfour.pop(GS,gm.column())



def print_player_turn(GS:connectfour.GameState, new_g: bool):
    if connectfour.winner(GS) == connectfour.NONE:
        if new_g:
            print("\nRED, it's your turn.")
        elif GS.turn == connectfour.RED:
            print("\nYELLOW has finished. RED, it's your turn.")
        elif GS.turn == connectfour.YELLOW:
            print("\nRED has finished. YELLOW, it's your turn.")

def play_check(GS:connectfour.GameState, new_g: bool):
    '''passes in a GameState, checks to see if the user put drop or pop,
    if the user put drop, creates a drop namedtuple, and vice versa for pop,
    and then it updates the board, as well as printing it'''
    ## create a game movie so I can use the gamestate to update the board
    while True:
        if connectfour.winner(GS) == connectfour.NONE:
            command = input("Would you like to pop, or drop. Enter 'DROP' or 'POP': ").strip().upper()
            if command == 'DROP' or command == 'POP':
                num_col = choose_col()

                #fix the number based index
                #create a game_move namedtuple

                gNT = Move(command,num_col)                #print_player_turn(GS, new_g)
                GS = update_board(gNT,GS)
                break
        else:
            if connectfour.winner(GS)==connectfour.RED:
                print("You, Red, have won")
                break
            elif connectfour.winner(GS) == connectfour.YELLOW:
                print("I'm sorry, the server has won. You lose!")
                break


    return (GS,gNT)
