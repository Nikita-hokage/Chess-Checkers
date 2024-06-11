import Piece
import copy


class King(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'black' else 'k'
        self.has_moved = False

    def get_possible_moves(self, board, row, col):
        board = copy.deepcopy(board)
        possible_moves = []

        # Все возможные соседние клетки короля
        neighbor_cells = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1), (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

        # Проверяем каждую соседнюю клетку
        for r, c in neighbor_cells:
            # Проверяем, находится ли клетка в пределах доски и свободна ли она
            if (0 <= r < 8) and (0 <= c < 8) and (board[r][c] == '.'):
                possible_moves.append((r, c))

            if (0 <= r < 8) and (0 <= c < 8) and isinstance(board[r][c], Piece.Piece):
                if board[r][c].color != self.color:
                    possible_moves.append((r, c))

        for r in range(8):
            for c in range(8):
                if isinstance(board[r][c], Piece.Piece):
                    if board[r][c].color != self.color:
                        for p in possible_moves:
                            if p in board[r][c].get_possible_moves(board, r, c):
                                possible_moves.remove(p)

        return possible_moves