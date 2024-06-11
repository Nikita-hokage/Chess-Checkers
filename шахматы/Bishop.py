import Piece


class Bishop(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'black' else 'b'

    def get_possible_moves(self, board, row, col):
        possible_moves = []

        # Проверяем возможные ходы по диагонали вправо и вверх
        r, c = row + 1, col + 1
        while r < 8 and c < 8:
            if board[r][c] == '.':
                possible_moves.append((r, c))
            elif board[r][c].color != self.color:
                possible_moves.append((r, c))
                break
            else:
                break
            r += 1
            c += 1

        # Проверяем возможные ходы по диагонали вправо и вниз
        r, c = row + 1, col - 1
        while r < 8 and c >= 0:
            if board[r][c] == '.':
                possible_moves.append((r, c))
            elif board[r][c].color != self.color:
                possible_moves.append((r, c))
                break
            else:
                break
            r += 1
            c -= 1

        # Проверяем возможные ходы по диагонали влево и вверх
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == '.':
                possible_moves.append((r, c))
            elif board[r][c].color != self.color:
                possible_moves.append((r, c))
                break
            else:
                break
            r -= 1
            c -= 1

        # Проверяем возможные ходы по диагонали вправо и вверх
        r, c = row - 1, col + 1
        while r >= 0 and c < 8:
            if board[r][c] == '.':
                possible_moves.append((r, c))
            elif board[r][c].color != self.color:
                possible_moves.append((r, c))
                break
            else:
                break
            r -= 1
            c += 1

        return possible_moves
