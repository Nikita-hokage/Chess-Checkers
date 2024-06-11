import Checker, King


class Board:
    def __init__(self):
        self.current_player = 'white'
        self.board = [['.' for i in range(8)] for i in range(8)]
        self.initialize_board()

    def switch_player(self):
        self.current_player = 'white' if self.current_player == 'black' else 'black'

    def initialize_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker.Checker('black')
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker.Checker('white')

    def print_board(self):
        letters = 'ABCDEFGH'
        print('   ', *letters, '    ')
        for i, row in enumerate(self.board):
            print(f'{i + 1}  ', *row, f'  {i + 1}')
        print('   ', *letters, '    ')

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if self.board[start_row][start_col] == '.':
            return False

        if self.board[end_row][end_col] != '.':
            return False

        if self.board[start_row][start_col].color != self.current_player:
            return False

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, Checker.Checker) and piece.color == self.current_player:
                    if piece.kill_move == True:
                        if row != start_row and col != start_col:
                            print('Ходите фигурой, которая может съесть!')
                            return False

        if (end_row, end_col) in self.board[start_row][start_col].get_possible_moves(self.board, start_row, start_col):
            return True

        return False

    def move_piece(self, start_row, start_col, end_row, end_col):
        # Выполняем ход
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '.'

        if isinstance(self.board[end_row][end_col], Checker.Checker):
            if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
                jumped_row = (start_row + end_row) // 2
                jumped_col = (start_col + end_col) // 2
                self.board[jumped_row][jumped_col] = '.'

        if isinstance(self.board[end_row][end_col], King.King):
            r = start_row
            c = start_col
            if start_row > end_row:
                if start_col < end_col:
                    while r != end_row and c != end_col:
                        self.board[r][c] = '.'
                        r -= 1
                        c += 1
                if start_col > end_col:
                    while r != end_row and c != end_col:
                        self.board[r][c] = '.'
                        r -= 1
                        c -= 1
            if start_row < end_row:
                if start_col < end_col:
                    while r != end_row and c != end_col:
                        self.board[r][c] = '.'
                        r += 1
                        c += 1
                if start_col > end_col:
                    while r != end_row and c != end_col:
                        self.board[r][c] = '.'
                        r += 1
                        c -= 1

        if (self.current_player == 'black' and end_row == 7) or (self.current_player == 'white' and end_row == 0):
            if self.board[end_row][end_col].kill_move == True:
                self.board[end_row][end_col] = King.King(self.current_player)
                self.board[end_row][end_col].kill_move = True
            else:
                self.board[end_row][end_col] = King.King(self.current_player)

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (isinstance(piece, Checker.Checker) or isinstance(piece, King.King)) and piece.kill_move == True:
                    piece.kill_move = False
                    piece.was_kill_move = True
