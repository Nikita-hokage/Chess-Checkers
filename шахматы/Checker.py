class Checker:
    def __init__(self, color):
        self.color = color
        self.was_kill_move = False
        self.kill_move = False

    def get_possible_moves(self, board, row, col):
        possible_moves = []
        direction = -1 if self.color == 'white' else 1

        if (0 <= col - 2 < 8) and (board[row + direction * 2][col - 2] == '.'):
            if (board[row + direction][col - 1] != '.') and (board[row + direction][col - 1].color != self.color):
                self.kill_move = True
                possible_moves.append((row + direction*2, col - 2))
        if (0 <= col + 2 < 8) and (board[row + direction*2][col + 2] == '.'):
            if (board[row + direction][col + 1] != '.') and (board[row + direction][col + 1].color != self.color):
                self.kill_move = True
                possible_moves.append((row + direction*2, col + 2))
        
        if self.kill_move != True:
            if (0 <= col - 1 < 8) and (board[row + direction][col - 1] == '.'):
                possible_moves.append((row + direction, col - 1))
            if (0 <= col + 1 < 8) and (board[row + direction][col + 1] == '.'):
                possible_moves.append((row + direction, col + 1))
        
        return possible_moves

    def __repr__(self):
        return 'B' if self.color == 'black' else 'W'