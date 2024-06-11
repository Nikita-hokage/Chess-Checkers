import Piece

class Rook(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'black' else 'r'
        self.has_moved = False


    def get_possible_moves(self, board, row, col):
        possible_moves = []

        # Проверяем возможные ходы вверх
        for r in range(row - 1, -1, -1):
            if board[r][col] == '.':
                possible_moves.append((r, col))
            elif board[r][col].color != self.color:
                possible_moves.append((r, col))
                break
            else:
                break

        # Проверяем возможные ходы вниз
        for r in range(row + 1, 8):
            if board[r][col] == '.':
                possible_moves.append((r, col))
            elif board[r][col].color != self.color:
                possible_moves.append((r, col))
                break
            else:
                break

        # Проверяем возможные ходы влево
        for c in range(col - 1, -1, -1):
            if board[row][c] == '.':
                possible_moves.append((row, c))
            elif board[row][c].color != self.color:
                possible_moves.append((row, c))
                break
            else:
                break

        # Проверяем возможные ходы вправо
        for c in range(col + 1, 8):
            if board[row][c] == '.':
                possible_moves.append((row, c))
            elif board[row][c].color != self.color:
                possible_moves.append((row, c))
                break
            else:
                break

        return possible_moves