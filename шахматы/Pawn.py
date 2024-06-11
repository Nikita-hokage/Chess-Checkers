import Piece


class Pawn(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'black' else 'p'

    def get_possible_moves(self, board, row, col):
        possible_moves = []
        direction = -1 if self.color == 'white' else 1

        # Проверка для двойного хода из начальной позиции
        if (row == 6 and self.color == 'white') or (row == 1 and self.color == 'black'):
            if board[row + (2 * direction)][col] == '.':
                possible_moves.append((row + 2 * direction, col))

        # Проверка для обычного хода
        if board[row + direction][col] == '.':
            possible_moves.append((row + direction, col))

        # Проверка для атаки по диагонали
        if (0 <= col - 1 < 8) and (board[row + direction][col - 1] != '.'):
            if board[row + direction][col - 1].color != self.color:
                possible_moves.append((row + direction, col - 1))
        if (0 <= col + 1 < 8) and (board[row + direction][col + 1] != '.'):
            if board[row + direction][col + 1]:
                possible_moves.append((row + direction, col + 1))

        return possible_moves
