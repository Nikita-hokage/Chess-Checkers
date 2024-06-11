import Piece, Chessboard
import Checker, Board


class GameChess:
    def __init__(self):
        self.board = Chessboard.Chessboard()

    def mainChess(self):
        Letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        self.board.print_board()

        while True:
            from_move = input('Введите фигуру для хода: ')

            if 'back' in from_move:
                undo = from_move.split()
                self.board.undo_moves(int(undo[1]))

            elif from_move != 'shortR' and from_move != 'longR':
                try:
                    start_col = Letters[from_move[0]]
                    start_row = int(from_move[1]) - 1

                    piece = self.board.board[start_row][start_col]

                    if not isinstance(piece, Piece.Piece):
                        print("На этой позиции нет фигуры!")
                        continue

                    if piece.color != self.board.current_player:
                        print("Сейчас не ваш ход.")
                        continue

                    self.board.give_podskazka(start_row, start_col)

                    self.board.print_podskazka_board()

                    while True:
                        to_move = input('Куда поставить фигуру: ')

                        end_col = Letters[to_move[0]]
                        end_row = int(to_move[1]) - 1

                        if not self.board.is_valid_move(start_row, start_col, end_row, end_col):
                            print("Не корректный ход.")
                            continue
                        else:
                            break
                    self.board.move_piece(start_row, start_col, end_row, end_col)
                except IndexError:
                    print('Неверный ввод!')
            else:
                if from_move == 'shortR':
                    if self.board.check_rakirovka(from_move, self.board.current_player):
                        self.board.rakirovka('shortR', self.board.current_player)
                    else:
                        print('Короткая Ракировка невозможна!')
                if from_move == 'longR':
                    if self.board.check_rakirovka(from_move, self.board.current_player):
                        self.board.rakirovka('longR', self.board.current_player)
                    else:
                        print('Длинная Ракировка невозможна!')

            self.board.print_board()

            if self.board.check_win('black') == False:
                print('Мат! Черные проиграли')
                break

            if self.board.check_win('white') == False:
                print('Мат! Белые проиграли')
                break

            if self.board.check_shah('black') == True:
                print('Шах для черных!')

            if self.board.check_shah('white') == True:
                print('Шах для белых!')


class GameCheckers:
    def __init__(self):
        self.board = Board.Board()
        self.game_over = False

    def check_win(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if isinstance(piece, Checker.Checker):
                    if piece.color != color and len(piece.get_possible_moves(self.board.board, row, col)) != 0:
                        return False
        return True

    def run(self):
        Letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        while True:
            self.board.print_board()
            move_from = input('Введите фигуру для хода: ')
            try:
                start_col = Letters[move_from[0]]
                start_row = int(move_from[1]) - 1

                piece = self.board.board[start_row][start_col]

                while True:
                    move_to = input('Куда поставить фигуру: ')

                    end_col = Letters[move_to[0]]
                    end_row = int(move_to[1]) - 1

                    if self.board.is_valid_move(start_row, start_col, end_row, end_col):
                        self.board.move_piece(start_row, start_col, end_row, end_col)
                        piece = self.board.board[end_row][end_col]
                        piece.get_possible_moves(self.board.board, end_row, end_col)
                        if piece.kill_move == True and piece.was_kill_move == True:
                            print('Ходите еще раз!')
                            break
                        else:
                            piece.was_kill_move = False
                            self.board.switch_player()
                            if self.check_win('black'):
                                print('Черные выиграли!')
                                exit()
                            if self.check_win('white'):
                                print('Белые выиграли!')
                                exit()
                            break
                    else:
                        print("Не корректный ход.")
                        break
            except IndexError:
                print('Неверный ввод!')


a = input('Введите игру: ')
if a == 'Chess':
    game = GameChess()
    game.mainChess()
elif a == 'Checkers':
    game_loop = GameCheckers()
    game_loop.run()
