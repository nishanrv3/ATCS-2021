import random


class TicTacToe:

    #initialize
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    #print instructions
    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("X is Player 1, O Player 2")
        print("Get 3 in a row to win")
        return

    #print out board
    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        count = 0
        for a in self.board:
            print(str(count), end='')
            second_count = 0
            for b in a:
                if second_count == 2:
                    print("\t" + b)
                else:
                    print("\t" + b, end='')
                second_count += 1
            count += 1
        return

    #check if move valid
    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        # if it is actually inside the 3x3 grid
        if (row >= 0 and row <= 2) and (col >= 0 and col <= 2):
            # if the tile is not already occupied
            if self.board[row][col] != 'X' and self.board[row][col] != 'O':
                return True
        return False

    #places player
    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    #takes turn
    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given then place the player's icon in the right spot
        player_row = 10
        player_col = 10
        while self.is_valid_move(player_row, player_col) == False:
            user_row = int(input("Enter a row"))
            user_col = int(input("Enter a col"))
        self.place_player(player, player_row, player_col)
        self.print_board()
        return

    #calls take turn
    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + " 's Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            self.take_minimax_turn(player)
        return

    #random turn
    def take_random_turn(self, player):
        list = [0, 1, 2]
        row = 30
        col = 30
        while self.is_valid_move(row, col) == False:
            row = random.choice(list)
            col = random.choice(list)
        self.place_player(player, row, col)
        return

    #algorithm turn
    def take_minimax_turn(self, player):
        results = self.minimax(player, 3)
        row = int(results[1])
        col = int(results[2])
        self.place_player(player, row, col)

    #checks col win
    def check_col_win(self, player):
        # TODO: Check col win
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[y][x] == player:
                    count += 1
            if y == (len(self.board[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    #checks row win
    def check_row_win(self, player):
        # TODO: Check row win
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == player:
                    count += 1
            if y == (len(self.board[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    #checks diagonal win
    def check_diag_win(self, player):
        # TODO: Check diagonal win
        # if (0,0), (1,1), (2,2) are all equal and all equal to player then return True
        value = 0
        for a in range(0, len(self.board)):
            if a == 2:
                break
            for b in range(0, len(self.board[a])):
                if (a + b + 1) == 3:
                    if self.board[x][y] == self.board[a + 1][b - 1] and self.board[a][b] == player:
                        value += 1
        if value == 2:
            return True
        value = 0
        for a in range(0, len(self.board) - 1):
            for b in range(0, len(self.board[a]) - 1):
                if a == b:
                    if self.board[a][b] == self.board[a + 1][b + 1] and self.board[a][b] == player:
                        value += 1
        if value == 2:
            return True

    #checks for win
    def check_win(self, player):
        # TODO: Check
        if self.check_col_win(player) == True:
            return True
        if self.check_diag_win(player) == True:
            return True
        if self.check_row_win(player) == True:
            return True
        return False

    #checks for tie
    def check_tie(self):
        # TODO: Check tie
        num = 0
        for a in range(len(self.board)):
            for b in range(len(self.board[a])):
                if self.board[a][b] != '-':
                    num += 1
        x_win = self.check_win('X')
        o_win = self.check_win('O')
        if num_occupied == 9 and x_win == False and o_win == False:
            return True
        return False

    #minimax algorithm
    def minimax(self, player, depth):
        opt_row = -1
        opt_col = -1
        if self.check_win('O'):
            return (10, None, None)
        if self.check_win('X'):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)
        if player == 'O':
            best = -100
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.is_valid_move(int(row), int(col)):
                        self.place_player('O', int(row), int(col))
                        score = self.minimax('X', depth - 1)[0]
                        self.place_player('-', int(row), int(col))
                        if best < score:
                            best = score
                            opt_row = int(row)
                            opt_col = int(col)
            return (best, opt_row, opt_col)

        if player == 'X':
            worst = 100
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.is_valid_move(int(row), int(col)):
                        self.place_player('X', int(row), int(col))
                        score = self.minimax('O', depth - 1)[0]
                        self.place_player('-', int(row), int(col))
                        if worst > score:
                            worst = score
                            opt_row = int(row)
                            opt_col = int(col)
            return (worst, opt_row, opt_col)

    #alpha beta version of minimax algorithm
    def minimax_alpha_beta(self, player, alpha, beta, depth):
        opt_row = -1
        opt_col = -1
        if self.check_win('O'):
            return (10, None, None)
        if self.check_win('X'):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)
        if player == 'O':
            best = -100
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.is_valid_move(int(row), int(col)):
                        self.place_player('O', int(row), int(col))
                        score = self.minimax_alpha_beta('X', alpha, beta, depth - 1)[0]
                        self.place_player('-', int(row), int(col))
                        if score > best:
                            best = score
                            opt_row = int(row)
                            opt_col = int(col)
                        if score > alpha:
                            alpha = score
                        if beta <= alpha:
                            return (best, opt_row, opt_col)
            return (best, opt_row, opt_col)
        if player == 'X':
            worst = 100
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.is_valid_move(int(row), int(col)):
                        self.place_player('X', int(row), int(col))
                        score = self.minimax_alpha_beta('O', alpha, beta, depth - 1)[0]
                        self.place_player('-', int(row), int(col))
                        if worst > score:
                            worst = score
                            opt_row = int(row)
                            opt_col = int(col)
                        if score < beta:
                            beta = score
                        if beta <= alpha:
                            return (worst, opt_row, opt_col)
            return (worst, opt_row, opt_col)

    #play game function
    def play_game(self):
        # TODO: Play game
        player = 'X'
        self.print_instructions()
        while True:
            self.print_board()
            self.take_turn(player)
            if self.check_win(player) == True:
                print(player + " Wins!")
                break
            if self.check_tie() == True:
                print("Tie!")
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        return

