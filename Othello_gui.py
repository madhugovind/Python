# Madhumitha Govindaraju ID:81772721
# Othello_gui.py

import tkinter
import othello

# Since we use the same font in a few places, we'll specify a default here
# as a global constant and use the constant everywhere else.  We used a
# much larger font in lecture, so it could easily be read when projected
# in a large room; notice that all I needed to change was this one line
# when I wanted the posted code example to have a smaller font.
DEFAULT_FONT = ('Helvetica', 14)


class GameDialog:
    def __init__(self):
        # A Toplevel object is, to a dialog box, akin to the Tk object
        # of an application.  It's the window.  The difference is that
        # it's not the root window of an entire application; it's a
        # separate, additional window.
        self._dialog_window = tkinter.Toplevel()


        # We'll create and lay out widgets inside the Toplevel object,
        # using all of the same techniques we've used previously when
        # creating and laying out widgets in an application's root window.

        row_num_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of rows (4-16 inclusive): ', font = DEFAULT_FONT)
        row_num_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.r = tkinter.IntVar()
        self.r.set(4) 
        self.row = tkinter.OptionMenu(self._dialog_window, self.r, 4, 6, 8, 10, 12, 14, 16)
        self.row.grid(row=1, column=1, sticky=tkinter.N)
        self._dialog_window.rowconfigure(1, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        col_num_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of columns (4-16 inclusive): ', font = DEFAULT_FONT)
        col_num_label.grid(
            row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.c = tkinter.IntVar()
        self.c.set(4) 
        self._col_num = tkinter.OptionMenu(self._dialog_window, self.c, 4, 6, 8, 10, 12, 14, 16)
        self._col_num.grid(row=2, column=1, sticky=tkinter.N)
        self._dialog_window.rowconfigure(2, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        player_turn_label = tkinter.Label(
            master = self._dialog_window, text = 'Black or White - will move first: ', font = DEFAULT_FONT)
        player_turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.ptn = tkinter.StringVar()
        self.ptn.set('B')
        self._player_t = tkinter.OptionMenu(self._dialog_window, self.ptn, 'B', 'W')
        self._player_t.grid(row=3, column=1, sticky=tkinter.N)
        self._dialog_window.rowconfigure(3, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        win_crit_label = tkinter.Label(
            master = self._dialog_window, text = 'Winner has the most (>) or fewest tiles (<): ', font = DEFAULT_FONT)
        win_crit_label.grid(
            row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.wc = tkinter.StringVar()
        self.wc.set(">")
        self._writ_crit = tkinter.OptionMenu(self._dialog_window, self.wc, '>', '<')
        self._writ_crit.grid(row=4, column=1, sticky=tkinter.N)
        self._dialog_window.rowconfigure(4, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        black_placed_label = tkinter.Label(
            master = self._dialog_window, text = 'First, how many black tiles will be initially placed at once: ', font = DEFAULT_FONT)
        black_placed_label.grid(
            row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.bp = tkinter.IntVar()
        self.bp.set(2)
        self._black_placed = tkinter.OptionMenu(self._dialog_window, self.bp, 0, 1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self._black_placed.grid(row=5, column=1, sticky=tkinter.W)
        self._dialog_window.rowconfigure(5, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        white_placed_label = tkinter.Label(
            master = self._dialog_window, text = 'Then, how many white tiles will be initialy placed at once: ', font = DEFAULT_FONT)

        white_placed_label.grid(
            row = 6, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self.wp = tkinter.IntVar()
        self.wp.set(2)
        self._white_placed = tkinter.OptionMenu(self._dialog_window, self.wp, 0, 1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self._white_placed.grid(row=6, column=1, sticky=tkinter.N)
        self._dialog_window.rowconfigure(6, weight=1)
        self._dialog_window.columnconfigure(1, weight=1)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 7, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        play_button = tkinter.Button(
            master = button_frame, text = 'PLAY', font = DEFAULT_FONT,
            command = self._on_play_button)

        play_button.grid(row = 7, column = 0, padx = 10, pady = 10)

        quit_button = tkinter.Button(
            master = button_frame, text = 'QUIT', font = DEFAULT_FONT,
            command = self._on_quit_button)

        quit_button.grid(row = 7, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(7, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


        # Finally, we'll initialize some attributes that will carry information
        # about the outcome of this dialog box (i.e., whether the user clicked
        # "PLAY" to dismiss it, and what first and last name the user specified).

        self._play_clicked = False


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    # The next methods allow us to ask our dialog box, after it's
    # been dismissed, what happened.  (It's too late to ask the OptionMenu
    # widgets themselves by then, because the window will already have
    # been destroyed.)

    def was_play_clicked(self) -> bool:
        return self._play_clicked
    def return_row(self) -> int:
        return self.r.get()
    def return_col(self) -> int:
        return self.c.get()
    def return_turn(self) ->str:
        return self.ptn.get()
    def return_win_crit(self) ->str:
        return self.wc.get()
    def return_white_placed(self)->int:
        return self.wp.get()
    def return_black_placed(self) -> int:
        return self.bp.get()


    # Finally, we attached command handlers to our two buttons; these are
    # the command handler methods we attached.  Note that they both call
    # a destroy() method on the Toplevel object, which is how we make the
    # window go away.  But _on_play_button also explicitly sets that the
    # PLAY button was clicked and extracts the first and last name that the
    # user entered (by calling the get() method on the OptionsMenu widgets),
    # so that afterward we can determine what happened.	

    def _on_play_button(self) -> None:
        self._play_clicked = True
        self.row_num = self.return_row()
        self.col_num = self.return_col()
        self.player_turn = self.return_turn()
        self.win_crit = self.return_win_crit()
        self.white_placed = self.return_white_placed()
        self.black_placed = self.return_white_placed()

        self._dialog_window.destroy()


    def _on_quit_button(self) -> None:
        self._dialog_window.destroy()



# The OthelloApplication class is a fairly straightforward Tkinter
# application, in the same style as the ones we've written previously.
# The only interesting thing going on here that we haven't seen before
# is the use of something called a "control variable", which allows us
# to associate a widget with a value that we expect to change; changing
# the value of the control variable has an immediate impact on the way
# the widget looks (and, in the case of widgets whose state can be changed,
# like Checkbuttons and Spinboxes, vice versa).  In our case, we use a
# tkinter.StringVar (a control variable whose value is a string) to
# represent the text in a Label widget, so that any change to the value
# of the StringVar will automatically and correspondingly make the Label's
# text change.  (This is an example of a general technique called "data
# binding".)

class OthelloApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self.version_button = tkinter.Button(
            master = self._root_window, text = 'FULL', font = DEFAULT_FONT,
            command = self._on_version_label)

        self.version_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)


        # A StringVar is a "control variable" that contains a string.  We
        # get its value by calling a get() method on it; we change its value
        # by calling a set() method on it.  We'll associate it with a Label
        # widget, in which case any subsequent change to the StringVar's
        # value will automatically cause the Label to be redrawn with its
        # new text.
        self._intro_text = tkinter.StringVar()
        self._intro_text.set('Welcome to Othello!')

        # Notice that we didn't set the Label's "text" option.  Instead,
        # we set its "textvariable" option and passed it a control variable
        # (in this case, a StringVar).  This is how we ask the Label to
        # automatically redraw itself when the StringVar changes; the
        # "textvariable" option implies that the text is, indeed,
        # variable (i.e., that we expect it to change, and that we want
        # the Label to handle that change for us automatically).
        intro_label = tkinter.Label(
            master = self._root_window, textvariable = self._intro_text,
            font = DEFAULT_FONT)

        intro_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()


    def _on_version_label(self) -> None:
        # When the user clicks the FULL button, we pop up a GameDialog.
        # Since we've already encapsulate all of that in the GameDialog
        # class, all we need to do is create a GameDialog object, ask it
        # to show itself, and then ask it afterward what happened.
        #
        # Note that the call to show() isn't going to return until the user
        # has dismissed the dialog box.
        dialog = GameDialog()
        dialog.show()

        # After the dialog box is dismissed, we'll check if it was the PLAY
        # or the QUIT button that got clicked.  If PLAY was clicked, we'll
        # change the version label's text by setting its control variable.
        if dialog.was_play_clicked():
            self.row_num = dialog.return_row()
            self.col_num = dialog.return_col()
            self.player_turn = dialog.return_turn()
            self.win_crit = dialog.return_win_crit()
            self.white_placed = dialog.return_white_placed()
            self.black_placed = dialog.return_white_placed()
            self.ogame = othello.Othello(self.col_num, self.row_num, self.win_crit, self.player_turn)
            self.white_counter = 0
            self.black_counter = 0
            self.game_over = False

            self.version_button.destroy()
            self._canvas = tkinter.Canvas(master=self._root_window, width=self.col_num*100, height=self.row_num*100, background="GREEN")
            self._canvas.grid(
                row = 1, column = 0, columnspan = 3, padx = 10, pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)                         
            self.width = self._canvas.winfo_width()
            self.height = self._canvas.winfo_height()
            self.turn = tkinter.StringVar()
            self.turn.set("TURN: {}".format(self.ogame.get_turn()))
            self.bscore = tkinter.StringVar()
            self.bscore.set("B: {}".format(self.ogame.count_black_tiles()))
            self.wscore = tkinter.StringVar()
            self.wscore.set("W: {}".format(self.ogame.count_white_tiles()))
            
            self.turn_label = tkinter.Label(master=self._root_window, textvariable=self.turn)
            self.turn_label.grid(row=0, column=0, pady=5, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            self._root_window.rowconfigure(0, weight=0)
            self._root_window.columnconfigure(0, weight=1)

            self.bscore_label = tkinter.Label(master=self._root_window, textvariable=self.bscore)
            self.bscore_label.grid(row=0, column=1, pady=5, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            self._root_window.rowconfigure(0, weight=0)
            self._root_window.columnconfigure(1, weight=1)
            
            self.wscore_label = tkinter.Label(master=self._root_window, textvariable=self.wscore)
            self.wscore_label.grid(row=0, column=2, pady=5, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            self._root_window.rowconfigure(0, weight=0)
            self._root_window.columnconfigure(2, weight=1)

            self._canvas.bind("<Configure>", self.adjust_screen_dimensions)
            self._canvas.bind("<Button-1>", self.check_and_switch)


    def get_color(self, tile:str) -> str:
        '''returns color depending on parameter'''
        if tile == "B":
            return "BLACK"
        elif tile == "W":
            return "WHITE"

    def change_labels(self):
        '''changes tile count labels'''
        black_tiles = self.ogame.count_black_tiles()
        self.bscore.set('B: {}'.format(black_tiles))
        white_tiles = self.ogame.count_white_tiles()
        self.wscore.set('W: {}'.format(white_tiles))
    
    def store_tile(self, row:int, col:int, placed_color:str):
        '''stores given player_turn in coordinate given'''
        self.ogame.return_board()[row][col] = placed_color

    def draw_tile_at_coord(self, row, col, mycolor):
        '''draw a tile on given coordinates'''
        self._canvas.create_oval(col/self.col_num*self.width, row/self.row_num*self.height, (col+1)/self.col_num*self.width, (row+1)/self.row_num*self.height, fill=mycolor)
    
    def draw_tiles(self):
        '''draws all tiles on board'''
        for r in range(len(self.ogame.return_board())):
            for c in range(len(self.ogame.return_board()[0])):
                if self.ogame.return_board()[r][c] == "B":
                    self.draw_tile_at_coord(r,c, self.get_color("B"))
                elif self.ogame.return_board()[r][c] == "W":
                    self.draw_tile_at_coord(r,c, self.get_color("W"))
        
    def redraw_board(self):
        '''draws everything on board from boundaries to tiles'''
        self._canvas.delete(tkinter.ALL)
        self.width = self._canvas.winfo_width()
        self.height = self._canvas.winfo_height()
        for row in range(1, self.row_num):
            row = (row*self.height)/self.row_num
            self._canvas.create_line(0, row, self.width, row, fill='BLACK')
        for col in range(1, self.col_num):
            col = (col*self.width)/self.col_num
            self._canvas.create_line(col, 0, col, self.height, fill='BLACK')
        self.draw_tiles()
        if not self.game_over:
            self.change_labels()

    def play_game(self, event):
        '''principle while loop that runs through the steps of thello displaying and drawing
        number of tiles, the board, current turn, and switching tiles'''
        try:
            self.redraw_board()
            self._width = self._canvas.winfo_width()
            self._height = self._canvas.winfo_height()
            row = int(event.y/self._height*self.row_num)
            col = int(event.x/self._width*self.col_num)
            if self.ogame.check_and_switch([row, col], False):
                self.ogame.change_player_turn()
                if not self.ogame.valid_moves():
                    self.ogame.change_player_turn()
                self.turn.set("TURN: {}".format(self.ogame.get_turn()))
            if self.ogame.winner() != None:
                winner = self.ogame.winner()
                if winner == self.ogame.get_black():
                    self.turn.set('TURN: NONE')
                    black_tiles = self.ogame.count_black_tiles()
                    self.bscore.set('B: Better Luck Next Time: {}'.format(black_tiles))
                    white_tiles = self.ogame.count_white_tiles()
                    self.wscore.set('W: Winner: {}'.format(white_tiles))
                elif winner == self.ogame.get_white():
                    self.turn.set('TURN: NONE')
                    black_tiles = self.ogame.count_black_tiles()
                    self.bscore.set('B: Winner: {}'.format(black_tiles))
                    white_tiles = self.ogame.count_white_tiles()
                    self.wscore.set('W: Better Luck Next Time: {}'.format(white_tiles))
                elif winner == self.ogame.get_non_player():
                    self.turn.set('NO WINNER')
                    black_tiles = self.ogame.count_black_tiles()
                    self.bscore.set('B: {}'.format(black_tiles))
                    white_tiles = self.ogame.count_white_tiles()
                    self.wscore.set('W: {}'.format(white_tiles))
                self.game_over= True
        except IndexError:
            pass        
    
    def adjust_screen_dimensions(self, event:tkinter.Event):
        '''adjudts screen by drawing bard again depending on configured height and width'''
        self.redraw_board()

    def check_and_switch(self, event:tkinter.Event):
        '''check if can place tile and redraws board'''
        if self.black_counter < self.black_placed:
            self._width = self._canvas.winfo_width()
            self._height = self._canvas.winfo_height()
            row = int(event.y/self._height*self.row_num)
            col = int(event.x/self._width*self.col_num)
            self.store_tile(row, col, "B")
            self.redraw_board()
            self.black_counter+=1
        elif self.white_counter < self.white_placed:
            self._width = self._canvas.winfo_width()
            self._height = self._canvas.winfo_height()
            row = int(event.y/self._height*self.row_num)
            col = int(event.x/self._width*self.col_num)
            self.store_tile(row, col, "W")
            self.redraw_board()
            self.white_counter+=1
        elif not self.game_over:
            self.play_game(event)
        self.redraw_board()
                
if __name__ == '__main__':
    OthelloApplication().start()
