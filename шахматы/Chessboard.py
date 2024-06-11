import copy

# Импорт класса всех фигур
import Piece, Pawn, Rook, Horse, Bishop, Queen, King

from colorama import init, Back, Style

init()


class Chessboard:
    def __init__(self):
        self.board = [['.' for i in range(8)] for i in range(8)]
        self.history = []
        self.initialize_board()
        self.current_player = 'white'
        self.podskazka_board = copy.deepcopy(self.board)
        self.copy_desk = copy.deepcopy(self.board)

    def initialize_board(self):
        # Расставляем черные фигуры
        # Расставляем черные фигуры
        self.board[0] = [Rook.Rook('black'), Horse.Horse('black'), Bishop.Bishop('black'), Queen.Queen('black'),
                         King.King('black'), Bishop.Bishop('black'), Horse.Horse('black'), Rook.Rook('black')]
        self.board[1] = [Pawn.Pawn('black') for _ in range(8)]
        # Расставляем белые фигуры
        self.board[7] = [Rook.Rook('white'), Horse.Horse('white'), Bishop.Bishop('white'), Queen.Queen('white'),
                         King.King('white'), Bishop.Bishop('white'), Horse.Horse('white'), Rook.Rook('white')]
        self.board[6] = [Pawn.Pawn('white') for _ in range(8)]

        self.history.append([list(row) for row in self.board])


    def print_board(self):
        letters = "ABCDEFGH"
        print('   ', *letters, '    ')
        for i, s in enumerate(self.board):
            print(f'{i + 1}  ', *s, f'  {i + 1}')
        print('   ', *letters, '    ')

    def give_podskazka(self, start_row, start_col):
        self.podskazka_board = copy.deepcopy(self.board)
        piece = self.podskazka_board[start_row][start_col]

        possible_moves = piece.get_possible_moves(self.podskazka_board, start_row, start_col)

        for pos in possible_moves:
            if isinstance(self.podskazka_board[pos[0]][pos[1]], Piece.Piece):
                self.podskazka_board[pos[0]][pos[1]] = (
                        Back.RED + self.podskazka_board[pos[0]][pos[1]].symbol + Style.RESET_ALL)
            else:
                self.podskazka_board[pos[0]][pos[1]] = (Back.GREEN + '.' + Style.RESET_ALL)

    def print_podskazka_board(self):
        letters = "ABCDEFGH"
        print('   ', *letters, '    ')
        for i, s in enumerate(self.podskazka_board):
            print(f'{i + 1}  ', *s, f'  {i + 1}')
        print('   ', *letters, '    ')

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]

        if not isinstance(piece, Piece.Piece):
            return False

        # Проверка, принадлежит ли фигура текущему игроку
        if piece.color != self.current_player:
            return False

        # Получение возможных ходов для фигуры
        possible_moves = piece.get_possible_moves(self.board, start_row, start_col)

        # Проверка, является ли конечная позиция одним из возможных ходов
        if (end_row, end_col) not in possible_moves:
            return False

        return True

    # Двигаем фигуру
    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '.'

        if isinstance(piece, King.King) or isinstance(piece, Rook.Rook):
            piece.has_moved = True

        #  Проверка на преварщение в королеву пешки
        if isinstance(piece, Pawn.Pawn):
            if end_row == 0:
                # Ищем белую королеву на доске
                queen_exists = any(
                    isinstance(piece, Queen.Queen) and piece.color == 'white' for row in self.board for piece in row)
                # Если нет белой королевы
                if queen_exists == False:
                    self.board[end_row][end_col] = Queen.Queen('white')

            if end_row == 7:
                # Ищем черную королеву на доске
                queen_exists = any(
                    isinstance(piece, Queen.Queen) and piece.color == 'black' for row in self.board for piece in row)
                # Если нет черной королевы
                if queen_exists == False:
                    self.board[end_row][end_col] = Queen.Queen('black')

        self.history.append([list(row) for row in self.board])
        self.current_player = 'black' if self.current_player == 'white' else 'white'  # смена цвета игрока

    def check_win(self, color):
        # Ищем короля нужного цвета на доске

        king_row, king_col = None, None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King.King):
                    if piece.color == color:
                        king_row, king_col = row, col
                        break

        if king_row is not None:
            king = self.board[king_row][king_col]
            # Получаем все возможные ходы короля
            king_moves = king.get_possible_moves(self.board, king_row, king_col)
            other_moves = []
            enemy_places = []

            # Проверяем, находится ли король под ударом
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if isinstance(piece, Piece.Piece):
                        if piece.color != color:
                            if (king_row, king_col) in piece.get_possible_moves(self.board, row, col):
                                enemy_places.append((row, col))
                                for moves in piece.get_possible_moves(self.board, row, col):
                                    other_moves.append(moves)
                                    self.copy_desk = copy.deepcopy(self.board)

                                    for pos in king_moves:
                                        self.copy_desk[pos[0]][pos[1]] = '.'


            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if isinstance(piece, Piece.Piece):
                        if piece.color == color:
                            for p in enemy_places:
                                if p in piece.get_possible_moves(self.board, row, col):
                                    enemy_places.remove(p)
                                    break

            if set(king_moves).issubset(other_moves) and len(other_moves) != 0 and len(enemy_places) != 0:
                return False

            if set(king_moves).issubset(other_moves) and len(other_moves) != 0 and self.current_player != color:
                return False

        # Если все хорошо, мата нет!
        return True

    def check_shah(self, color):
        # Проверяем наличие короля нужного цвета на доске

        king_row, king_col = None, None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King.King) and piece.color == color:
                    king_row, king_col = row, col
                    break


        # Проверяем, находится ли король под ударом
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, Piece.Piece) and piece.color != color:
                    if (king_row, king_col) in piece.get_possible_moves(self.board, row, col):
                        return True

        return False

    def check_mat_for_rakirivcka(self, king_row, king_col, color):
        # Проверяем, находится ли король под ударом
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, Piece.Piece) and piece.color != color:
                    if (king_row, king_col) in piece.get_possible_moves(self.board, row, col):
                        return False

        return True

    def check_rakirovka(self, type_rakirovka, color):
        if color == 'white' and self.current_player == 'white':
            if type_rakirovka == 'shortR':
                if isinstance(self.board[7][4], King.King) and isinstance(self.board[7][7],
                                                                          Rook.Rook) and not isinstance(
                    self.board[7][5], Piece.Piece) and not isinstance(self.board[7][6], Piece.Piece):
                    if (self.check_mat_for_rakirivcka(7, 6, 'white')):
                        if self.board[7][4].has_moved == False and self.board[7][7].has_moved == False:
                            if self.check_shah('white') != True:
                                return True
            if type_rakirovka == 'longR':
                if isinstance(self.board[7][4], King.King) and isinstance(self.board[7][0],
                                                                          Rook.Rook) and not isinstance(
                    self.board[7][3], Piece.Piece) and not isinstance(self.board[7][2],
                                                                      Piece.Piece) and not isinstance(
                    self.board[7][1], Piece.Piece) and (self.check_mat_for_rakirivcka(7, 2, 'white')):
                    if self.board[7][4].has_moved == False and self.board[7][0].has_moved == False:
                        if self.check_shah('white') != True:
                            return True

        if color == 'black' and self.current_player == 'black':
            if type_rakirovka == 'shortR':
                if isinstance(self.board[0][4], King.King) and isinstance(self.board[0][7],
                                                                          Rook.Rook) and not isinstance(
                    self.board[0][5], Piece.Piece) and not isinstance(self.board[0][6], Piece.Piece) and (
                        self.check_mat_for_rakirivcka(0, 4, 'black')):
                    if self.board[0][4].has_moved == False and self.board[0][7].has_moved == False:
                        if self.check_shah('black') != True:
                            return True
            if type_rakirovka == 'longR':
                if isinstance(self.board[0][4], King.King) and isinstance(self.board[0][0],
                                                                          Rook.Rook) and not isinstance(
                    self.board[0][3], Piece.Piece) and not isinstance(self.board[0][2],
                                                                      Piece.Piece) and not isinstance(
                    self.board[0][1], Piece.Piece) and (self.check_mat_for_rakirivcka(0, 2, 'black')):
                    if self.board[0][4].has_moved == False and self.board[0][0].has_moved == False:
                        if self.check_shah('black') != True:
                            return True

    def rakirovka(self, type_rakirovka, color):
        if color == 'white':
            if type_rakirovka == 'shortR':
                self.board[7][4] = '.'
                self.board[7][6] = King.King('white')
                self.board[7][7] = '.'
                self.board[7][5] = Rook.Rook('white')
                self.current_player = 'black' if self.current_player == 'white' else 'white'  # смена цвета игрока после ракировки
            if type_rakirovka == 'longR':
                self.board[7][4] = '.'
                self.board[7][2] = King.King('white')
                self.board[7][0] = '.'
                self.board[7][3] = Rook.Rook('white')
                self.current_player = 'black' if self.current_player == 'white' else 'white'  # смена цвета игрока после ракировки

        if color == 'black':
            if type_rakirovka == 'shortR':
                self.board[0][4] = '.'
                self.board[0][6] = King.King('blask')
                self.board[0][7] = '.'
                self.board[0][5] = Rook.Rook('black')
                self.current_player = 'black' if self.current_player == 'white' else 'white'  # смена цвета игрока после ракировки
            if type_rakirovka == 'longR':
                self.board[0][4] = '.'
                self.board[0][2] = King.King('black')
                self.board[0][0] = '.'
                self.board[0][3] = Rook.Rook('black')
                self.current_player = 'black' if self.current_player == 'white' else 'white'  # смена цвета игрока после ракировки

    def check_pat(self):
        # Проверяем, находится ли король под ударом и могут ли другие фигуры ходить
        if self.check_shah(self.current_player) != True:
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if isinstance(piece, Piece.Piece) and piece.color == self.current_player:
                        if len(piece.get_possible_moves(self.board, row, col)) != 0:
                            return False
        else:
            return False

        # Если ни одна фигура не может походить, пат есть!
        return True

    def undo_moves(self, num_moves):
        if num_moves > 0 and len(self.history) > num_moves:
            for move in range(num_moves):
                self.history.pop()
            self.board = [list(row) for row in self.history[-1]]
        else:
            print('Невозможно откатиться на введенное количество ходов!')
