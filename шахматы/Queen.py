import Piece

class Queen(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'black' else 'q'

    
    def get_possible_moves(self, board, row, col):
        possible_moves = []

        # Проверяем возможные ходы по диагоналям
        possible_moves += self.check_diagonal_moves(board, row, col)

        # Проверяем возможные ходы по вертикали и горизонтали
        possible_moves += self.check_horizontal_and_vertical_moves(board, row, col)

        return possible_moves

    def check_diagonal_moves(self, board, row, col):
        possible_moves = []

        # Проверяем возможные ходы по диагонали вправо и вниз
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

        # Проверяем возможные ходы по диагонали влево и вниз
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

    def check_horizontal_and_vertical_moves(self, board, row, col):
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