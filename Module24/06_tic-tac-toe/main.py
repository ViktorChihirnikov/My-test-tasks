
class Cell:
    """
    Класс Cell
    """

    def __init__(self) -> None:
        """
        Конструктор класса Cell
        free указывает занята ли клетка
        """
        self.free = None


class Board:
    """
    Класс Board
    """

    def __init__(self) -> None:
        """
        Конструктор класса Board, генерит игровое поле
        """
        self.board = [[Cell().free for _ in range(num, num + 3)] for num in range(1, 10, 3)]


class Player:
    """
    Класс Player
    """

    def __init__(self, name: str) -> None:
        """
        Конструктор класса
        :param name: str Имя игрока
        """
        self.name = name

    def input_cell(self) -> int:
        """
        Метод класса Player, запрашивает номер клетки куда ходить и проверяет ввод
        :return: int номер клетки
        """

        choose_cell = input('Введите номер клетки от 1 до 9: ')
        while choose_cell.isalpha() or not 1 <= int(choose_cell) < 10:
            print('Ошибка ввода, проверьте данные')
            choose_cell = input('Введите номер клетки от 1 до 9: ')
        return int(choose_cell) - 1


class Game:
    """
    Класс Game
    """

    def __init__(self, list_name: list[str]) -> None:
        """
        Конструктор класса Game
        :param list_name: list[str] Список имён игроков
        """
        self.both_not_win = False
        self.players = [Player(name.title()) for name in list_name]
        self.game_board = Board().board
        self.count_win = {self.players[0].name: 0, self.players[1].name: 0}


    def check_board(self, flag: str) -> bool:
        """
        Метод класса Game, проверяет комбинации на выйгрыш или ничью
        :param flag: str получаемый аргумент используем для сравнения в генерации булевых значений
        :return: bool
        """

        if (all(cell == flag for cell in self.game_board[0]) or all(cell == flag for cell in self.game_board[1]) or
                all(cell == flag for cell in self.game_board[2])):
            return True
        elif all(cell == flag for cell in [self.game_board[0][0], self.game_board[1][0], self.game_board[2][0]]):
            return True
        elif all(cell == flag for cell in [self.game_board[0][1], self.game_board[1][1], self.game_board[2][1]]):
            return True
        elif all(cell == flag for cell in [self.game_board[0][2], self.game_board[1][2], self.game_board[2][2]]):
            return True
        elif all(cell == flag for cell in [self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]]):
            return True
        elif all(cell == flag for cell in [self.game_board[0][2], self.game_board[1][1], self.game_board[2][0]]):
            return True
        elif all(self.game_board[0] + self.game_board[1] + self.game_board[2]):
            self.both_not_win = True
        else:
            return False


    def one_step_game(self) -> bool:
        """
        Метод класса Game описывает логику игры одного хода
        :return: bool
        """
        list_player_and_flag = list(zip(self.players, ['x', '0']))  # список картежей (игрок, x или 0)
        count = 0
        while count < 2:
            player, flag = list_player_and_flag[count]
            print(f'Ходит {player.name.title()}')
            result = player.input_cell()  # запрашиваем номер клетки

            if not self.game_board[result // len(self.game_board)][result % len(self.game_board)]:  # проверка клетки
                self.game_board[result // len(self.game_board)][result % len(self.game_board)] = flag  # перезаписываем
                print(f'{self.game_board[0]}\n{self.game_board[1]}\n{self.game_board[2]}\n')  # Выводим доску

                if self.check_board(flag):    # Проверка комбинации выйгрыша
                    print(f'Победил {player.name}')  # Выводим победителя
                    self.count_win[player.name] += 1  # Увеличиваем количество выйгрыша
                    return True
                elif self.both_not_win:  # Проверяем на ничью
                    print('Ничья')
                    return True
                count += 1
            else:
                print('Клетка уже занята, выберите другую!!!')


    def one_game(self) -> bool:
        """
        Метод класса Game. Запускает метод одной игры и очищает доску
        :return: bool
        """
        self.game_board = Board().board
        while True:
            if self.one_step_game():
                return True


    def main_game(self):
        """
        Метод класса Game, запускает все игры/методы по результату выводит текущий счёт и предлагает продолжить игру
        :return: None
        """
        while True:
            if self.one_game():
                print('Текущий счёт!!')
                for name, score in self.count_win.items():
                    print(f'{name} - {score}')
                start_game = int(input('Хотите продолжить 1, если нет то 0: '))
                if start_game:
                    continue
                else:
                    return


Game(['Dima', 'petr']).main_game()
