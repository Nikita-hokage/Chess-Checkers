import Piece

class Horse(Piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'H' if color == 'black' else 'h'

    # Найти возможные ходы
    def get_possible_moves(self, board, row, col):
        possible_moves = []

        # Все возможные ходы коня относительно его текущей позиции
        moves = [
            (row - 2, col - 1), (row - 2, col + 1),
            (row - 1, col - 2), (row - 1, col + 2),
            (row + 1, col - 2), (row + 1, col + 2),
            (row + 2, col - 1), (row + 2, col + 1)
        ]

        # Проверяем каждый возможный ход 
        for r, c in moves:
            # Проверяем, находится ли ход в пределах доски и свободен ли он
            if (0 <= r <= 7) and (0 <= c <= 7) and isinstance(board[r][c], Piece.Piece):
                if board[r][c].color != self.color:
                    possible_moves.append((r, c))
            if (0 <= r <= 7) and (0 <= c <= 7) and not isinstance(board[r][c], Piece.Piece):
                possible_moves.append((r, c))

        return possible_moves