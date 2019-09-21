# Madhumitha Govindaraju ID 81772721
# othello.py

class Othello:

    def __init__(self, col:int, row :int, win:str, turn:str):
        '''inititializes constants and attributes of class'''
        self._COLUMNS = col
        self._ROWS = row
        self.BLACK = "B"
        self.WHITE = "W"
        self.NONE = "."
        self._WIN_CRIT = win
        self._TURN = turn
        self._BOARD = self.get_board(self._COLUMNS, self._ROWS)
        
    def get_board(self, col:int, row:int) -> [] :
        '''input starting board'''
        temp_board = []
        for r in range(row): 
            temp_board.append([])
            for c in range(col):
                temp_board[-1].append(self.NONE)
        return temp_board

    def get_black(self) -> str:
        '''return attribute BLACK of othello'''
        return self.BLACK

    def get_white(self)-> str:
        '''return attribute of WHITE of othello'''
        return self.WHITE

    def get_non_player(self) -> str:
        '''return attribute of NONE of othello'''
        return self.NONE

    def return_board(self):
        '''return the board'''
        return self._BOARD
    
    def drop(self, row: int, col:int):
        '''drops single peice at given coordinate'''
        self._BOARD[row][col]= self._TURN

    def get_coord() -> []:
        '''choose dropping coordinate'''
        inp = input().split(" ")
        inp=[int(inp[0])-1, int(inp[1])-1]
        return inp
    
    def print_screen(self):
        ''' Prints the board in visually appealing manner'''
        for row in range(self._ROWS):
            for col in range(self._COLUMNS):
                print(self._BOARD[row][col], sep="", end=" ")
            print()  # Print newline at end of row
        
    def winner(self)->str:
        '''checks if there is a winner and returns he winner'''
        current_player = self.valid_moves()
        self.change_player_turn()
        opp_player = self.valid_moves()
        self.change_player_turn()
        
        if self.no_more_empty_spaces() or not current_player and not opp_player:
            if self.count_black_tiles() == self.count_white_tiles():
                return self.NONE
            elif self._WIN_CRIT == ">":
                if self.count_black_tiles() > self.count_white_tiles():
                    return self.BLACK
                elif self.count_white_tiles() > self.count_black_tiles():
                    return self.WHITE
            elif self._WIN_CRIT == "<":
                if self.count_black_tiles() < self.count_white_tiles():
                    return self.BLACK
                elif self.count_white_tiles() < self.count_black_tiles():
                    return self.WHITE
        return None

    def count_black_tiles(self) -> int:
        '''returns total number of black tiles on the board'''
        black = 0
        for r in range(self._ROWS):
            for c in range(self._COLUMNS):
                if self._BOARD[r][c] == self.BLACK:
                    black+=1
        return black
    
    def count_white_tiles(self) -> int:
        '''returns total number of white tiles on the board'''
        white = 0
        for r in range(self._ROWS):
            for c in range(self._COLUMNS):
                if self._BOARD[r][c] == self.WHITE:
                    white+=1
        return white
    
    def print_player_turn(self):
        '''prints who the current player is'''
        print("TURN:", self._TURN)

    def change_player_turn(self):
        ''' changes the player to the opposite'''
        if self._TURN == self.BLACK:
            self._TURN = self.WHITE
        else:
            self._TURN = self.BLACK
    
    def print_num_tiles(self):
        '''prints total black and white tiles on the board'''
        print("{}: {} {}: {}".format(self.BLACK, self.count_black_tiles(), self.WHITE, self.count_white_tiles()))

    def no_more_empty_spaces(self) -> bool:
        '''checks if the board is full or not'''
        for r in range(self._ROWS):
            for c in range(self._COLUMNS):
                if self._BOARD[r][c] == self.NONE:
                    return False
        return True

    def _empty_space(self, row:int, col:int) -> bool:
        '''checks if passed coordinate on board is empty'''
        if self._BOARD[row][col] == self.NONE:
            return True
        return False

    def valid_moves(self) -> bool:
        '''checks if there are any remaining valid moves on the board'''
        for r in range(self._ROWS):
            for c in range(self._COLUMNS):
                if self.check_and_switch([r,c], True):
                    return True
        return False
    
    def check_and_switch(self, coord: [], check:bool) -> bool:
        '''checks and switches all tiles on baord according to othello rules'''
        valid_move = False
        
        if self._empty_space(coord[0], coord[1]):
            if self._switch_left(coord[0], coord[1], check): valid_move = True
            if self._switch_down(coord[0], coord[1], check): valid_move = True
            if self._switch_up(coord[0], coord[1], check): valid_move = True
            if self._switch_right(coord[0], coord[1], check): valid_move = True
            if self._switch_top_right(coord[0], coord[1], check): valid_move = True
            if self._switch_bottom_right(coord[0], coord[1], check): valid_move = True
            if self._switch_top_left(coord[0], coord[1], check): valid_move = True
            if self._switch_bottom_left(coord[0], coord[1], check): valid_move = True
            if valid_move and not check:
                self._BOARD[coord[0]][coord[1]] = self._TURN
        return valid_move

    def _switch_down(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles under the passed coordinate'''
        spaces = 0
        while(row+spaces+1 < self._ROWS and not self._empty_space(row+spaces+1, col) and self._BOARD[row+spaces+1][col] != self._TURN):
              spaces+=1
        if (row+spaces+1< self._ROWS and self._BOARD[row+spaces+1][col] == self._TURN and self._BOARD[row+1][col] != self._TURN):
              spaces2 = 1
              while (row+spaces2 < self._ROWS and self._BOARD[row+spaces2][col] !=self._TURN):
                  if not check:
                      self._BOARD[row+spaces2][col] = self._TURN
                  spaces2 += 1
              return True
        return False

    def _switch_up(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles above the passed coordinate'''
        spaces = 0
        while(row-spaces-1 >= 0 and not self._empty_space(row-spaces-1, col) and self._BOARD[row-spaces-1][col] != self._TURN):
              spaces+=1
        if (row-spaces-1 >= 0 and self._BOARD[row-spaces-1][col] == self._TURN and self._BOARD[row-1][col] != self._TURN):
              spaces2 = 1
              while (row-spaces2 >=0 and self._BOARD[row-spaces2][col] !=self._TURN):
                  if not check:
                      self._BOARD[row-spaces2][col] = self._TURN
                  spaces2 += 1
              return True
        return False
    
    def _switch_left(self, row: int, col: int, check:bool) -> bool:
        '''checks and switches all tiles left of the passed coordinate'''
        spaces = 0
        while(col-spaces-1 >= 0 and not self._empty_space(row, col-spaces-1) and self._BOARD[row][col-spaces-1] != self._TURN):
              spaces+=1
        if (col-spaces-1 >= 0 and self._BOARD[row][col-spaces-1] == self._TURN and self._BOARD[row][col-1] != self._TURN):
              spaces2 = 1
              while (col-spaces2 >= 0 and self._BOARD[row][col-spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row][col-spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False

    def _switch_right(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles right of the passed coordinate'''
        spaces = 0
        while(col+spaces+1 < self._COLUMNS and not self._empty_space(row, col+spaces+1) and self._BOARD[row][col+spaces+1] != self._TURN):
              spaces+=1
        if (col+spaces+1 < self._COLUMNS and self._BOARD[row][col+spaces+1] == self._TURN and self._BOARD[row][col+1] != self._TURN):
              spaces2 = 1
              while (col-spaces2 <= self._COLUMNS and self._BOARD[row][col+spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row][col+spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False

    def _switch_top_right(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles top right of the passed coordinate'''
        spaces = 0
        while(col+spaces+1 < self._COLUMNS and row-spaces-1 >=0 and not self._empty_space(row-spaces-1, col+spaces+1) and self._BOARD[row-spaces-1][col+spaces+1] != self._TURN):
              spaces+=1
        if (col+spaces+1 < self._COLUMNS and row-spaces-1 >= 0 and self._BOARD[row-spaces-1][col+spaces+1] == self._TURN and self._BOARD[row-1][col+1] != self._TURN):
              spaces2 = 1
              while (col-spaces2 < self._COLUMNS and row-spaces-1 >= 0 and self._BOARD[row-spaces2][col+spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row-spaces2][col+spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False
        
    def _switch_bottom_right(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles bottom right of the passed coordinate'''
        spaces = 0
        while(col+spaces+1 < self._COLUMNS and row+spaces+1 < self._ROWS and not self._empty_space(row+spaces+1, col+spaces+1) and self._BOARD[row+spaces+1][col+spaces+1] != self._TURN):
              spaces+=1
        if (col+spaces+1 < self._COLUMNS and row+spaces+1 < self._ROWS and self._BOARD[row+spaces+1][col+spaces+1] == self._TURN and self._BOARD[row+1][col+1] != self._TURN):
              spaces2 = 0
              while (col+spaces2 < self._COLUMNS and row+spaces2 < self._ROWS and self._BOARD[row+spaces2][col+spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row+spaces2][col+spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False

    def _switch_top_left(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles top left of the passed coordinate'''
        spaces = 0
        while(col-spaces-1 >= 0 and row-spaces-1 >= 0 and not self._empty_space(row-spaces-1, col-spaces-1) and self._BOARD[row-spaces-1][col-spaces-1] != self._TURN):
              spaces+=1
        if (col-spaces-1 >= 0 and row-spaces-1 >= 0 and self._BOARD[row-spaces-1][col-spaces-1] == self._TURN and self._BOARD[row-1][col-1] != self._TURN):
              spaces2 = 1
              while (col-spaces2 >= 0 and row-spaces2 >= 0 and self._BOARD[row-spaces2][col-spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row-spaces2][col-spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False

    def _switch_bottom_left(self, row: int, col: int, check:bool)->bool:
        '''checks and switches all tiles bottom lef of the passed coordinate'''
        spaces = 0
        while(col-spaces-1 >= 0 and row+spaces+1 < self._ROWS and not self._empty_space(row+spaces+1, col-spaces-1) and self._BOARD[row+spaces+1][col-spaces-1] != self._TURN):
              spaces+=1
        if (col-spaces-1 >= 0 and row+spaces+1 < self._ROWS and self._BOARD[row+spaces+1][col-spaces-1] == self._TURN and self._BOARD[row+1][col-1] != self._TURN):
              spaces2 = 1
              while (col-spaces2 >= 0 and row+spaces2 < self._ROWS and self._BOARD[row+spaces2][col-spaces2] !=self._TURN):
                  if not check:
                      self._BOARD[row+spaces2][col-spaces2] = self._TURN
                  spaces2 += 1
              return True
        return False
    
    def return_board(self)->[[str]]:
        '''Returns the game board as a list of list of strings'''
        return self._BOARD
    
    def get_turn(self)->str:
        '''Returns which player's turn it is'''
        return self._TURN
