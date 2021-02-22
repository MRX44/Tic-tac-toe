from os import system

# PARAMETERS
SIZE = 3            # board length (must be positive and more than 2)
TTT = ['X', 'O']    # shapes (must be different and only two)
THICK_BOX = 1       # box shape

# box shape selector
if THICK_BOX == 0:
    BOX = ['╔╦╗', '║║║', '╠╬╣', '╚╩╝', '═']
elif THICK_BOX == 1:
    BOX = ['┌┬┐', '│││', '├┼┤', '└┴┘', '─']
else:  # THICK_BOX == 2
    BOX = ['+++', '|||', '+++', '+++', '-']


class Board:
    def __init__(self):
        # define cells
        self.cell = [[str(j+i*SIZE+1) for j in range(SIZE)] for i in range(SIZE)]
        # define max cell length (must be odd number)
        self.max_len = len(str(SIZE**2)) + ((len(str(SIZE**2))+1)%2)
        # write counter
        self.counter = 0

    def reset(self):
        # loop over all cells to reset
        for x in range(SIZE):
            for y in range(SIZE):
                # reset value
                self.cell[x][y] = str(y + x*SIZE + 1)
        # reset counter
        self.counter = 0

    def display_row(self, t, r=-1):
        # display first char from row
        print(BOX[t][0], end='')
        # loop over SIZE to print all row elements correctly
        for j in range(SIZE):
            # display line if -1 (notice -1 is by default)
            if r == -1:
                print(BOX[4]*(self.max_len + 2), end='')
            else:
                # display cell with two white spaces
                print(' ' + self.cell[r][j].center(self.max_len), end=' ')
            # check if not last char
            if j != SIZE - 1:
                # display mid char
                print(BOX[t][1], end='')
        # display last char
        print(BOX[t][2])
        
    def display(self):
        # simplify references
        c, b, l = self.cell, BOX, self.max_len + 2
        # display top row
        self.display_row(0)
        # loop over SIZE to display all rows correctly
        for r in range(SIZE):
            self.display_row(1, r)
            # check if not last row
            if r != SIZE - 1:
                # display middle row separator
                self.display_row(2)
            else:
                # display bottom row
                self.display_row(3)

    def check_empty(self, x, y):
        # check if cell in the defined TicTacToe symbols
        return self.cell[x][y] not in TTT

    def write_to_cell(self, x, y, symbol):
        # write to cell
        self.cell[x][y] = symbol
        # increment write counter
        self.counter += 1


class TTTEngine:
    def __init__(self):
        # display welcome text
        print('Welcome to Tic Tac Toe Championship')
        print('-----------------------------------')
        # name array [player_1, player_2]
        self.name = self.get_player_names()
        # score array [player_1, player_2, draw]
        self.score = [0, 0, 0]
        # create object from board using the two names
        self.board = Board()

    def get_player_names(self):
        p1 = input('Enter 1st player name: ')
        p2 = input('Enter 2nd player name: ')
        return p1, p2

    def display_score(self):
        # simplify references
        name, score = self.name, self.score
        # show header
        print('> Tic Tac Toe Championship')
        print('--------------------------')
        print(f'Players: {name[0]} vs {name[1]}\n')
        # show scores
        print('> Scores:')
        print('---------')
        print(f'P1: {score[0]}, P2: {score[1]}, Draw: {score[2]}\n')

    def refresh(self):
        # clear screen
        system('cls')
        # display scores
        self.display_score()
        # display board section
        print('> Board:')
        # display board
        self.board.display()
        # display empty line
        print()

    def get_valid_position_from_user(self, player):
        # ask for position
        pos = input(f'[Player {player+1}] enter ({TTT[player]}) position: ')
        # check if user not entered a number
        if pos.isnumeric() is False:
            # repeat
            return self.get_valid_position_from_user(player)
        # check if number is in range
        if 0 < int(pos) < (SIZE**2 + 1):
            # convert to number starting from 0
            pos = int(pos) - 1
            # extract pos(x, y)
            x, y = pos//SIZE, pos%SIZE
            # check if cell is empty
            if self.board.check_empty(x, y):
                # return pos(x, y)
                return x, y
            else:
                # repeat
                return self.get_valid_position_from_user(player)
        else:
            # repeat
            return self.get_valid_position_from_user(player)

    def player_has_won(self, player):
        # update player score
        self.score[player] += 1
        # refresh screen
        self.refresh()
        # display message
        print(f'[Player {player+1}] {self.name[player]} playing with ({TTT[player]}) has won!')
        # return fales (break from game)
        return False
    
    def check_board(self, player):
        win = False     # win flag
        
        # check rows
        # loop over y
        for y in range(SIZE):
            # set start cell
            win, cell = True, self.board.cell[y][0]
            # loop over x
            for x in range(SIZE):
                # check if cell is not the same
                if cell != self.board.cell[y][x]:
                    win = False
                    break
            # if all cells is the same (win must not be changed)
            if win is True:
                return self.player_has_won(player)

        # check columns
        # loop over x
        for x in range(SIZE):
            # set start cell
            win, cell = True, self.board.cell[0][x]
            # loop over y
            for y in range(SIZE):
                # check if cell is not the same
                if cell != self.board.cell[y][x]:
                    win = False
                    break
            # if all cells is the same (win must not be changed)
            if win is True:
                return self.player_has_won(player)

        # check diagonal '\'
        win, cell = True, self.board.cell[0][0]
        for d in range(SIZE):
            # check if cell is not the same
            if cell != self.board.cell[d][d]:
                win = False
                break
        # if all cells is the same (win must not be changed)
        if win is True:
            return self.player_has_won(player)

        # check diagonal '/'
        win, cell = True, self.board.cell[0][SIZE-1]
        for d in range(SIZE):
            # check if cell is not the same
            if cell != self.board.cell[d][SIZE-1-d]:
                win = False
                break
        # if all cells is the same (win must not be changed)
        if win is True:
            return self.player_has_won(player)

        # check for draw
        if self.board.counter == SIZE*SIZE:
            # update draw score
            self.score[2] += 1
            # refresh screen
            self.refresh()
            # display message
            print('The game is Draw')
            # return fales (break from game)
            return False

        # continue and do not mind :)
        return True
    
    def start_game(self, player):
        while True:
            # refresh screen
            self.refresh()
            # get valid pos(x, y)
            x, y = self.get_valid_position_from_user(player)
            # write to cell
            self.board.write_to_cell(x, y, TTT[player])
            # check if game is finished
            continue_game_flag = self.check_board(player)
            # check flag
            if continue_game_flag == False:
                input('\nPress <enter> to continue... ')
                break
            # update current player
            player = (player + 1) % 2
        # reset board after a game is finished
        self.board.reset()
        
    def mainloop(self):
        # starting player
        p_start = 0
        # enter mainloop
        while True:
            # start game with starting player first
            self.start_game(p_start)
            # update starting player
            p_start = (p_start + 1) % 2

            
if __name__ == '__main__':
    # create TTTEngine
    test = TTTEngine()
    # enter main loop
    test.mainloop()
    


