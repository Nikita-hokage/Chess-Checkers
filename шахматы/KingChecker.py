class King:
    def __init__(self, color):
        self.color = color
        self.kill_move = False
        self.was_kill_move = False

    def get_possible_moves(self, board, row, col):
        possible_moves = []

        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] != '.':
                        if board[new_row][new_col].color != self.color:
                            if (0 <= new_row + dr < 8 and 0 <= new_col + dc < 8) and board[new_row + dr][new_col + dc] == '.':
                                self.kill_move = True
                                possible_moves.append((new_row + dr, new_col + dc))
                            else:
                                break

        if self.kill_move != True:
            for dr, dc in directions:
                for i in range(1, 8):
                    new_row, new_col = row + dr * i, col + dc * i
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        if board[new_row][new_col] == '.':
                            possible_moves.append((new_row, new_col))
                        else:
                            break

        return possible_moves

    def __repr__(self):
        return 'K' if self.color == 'black' else 'k'