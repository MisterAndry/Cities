# -*- coding: utf-8 -*-
class Cities(object):
    db_cities = {}                                           # словарь с городами
    dnt_use_let = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')  # буквы, с которых не начинаются города в словаре
    current_city = ''                                        # текущий названный город

    def __init__(self, file_name):
        # считываем города и помещаем их в словарь
        # изначально в словаре каждому городу поставлено значение 1,
        # когда город называется, значение становится 0
        with open(file_name, 'r', encoding="utf-8") as f:
            data_tmp = f.read().splitlines()
            if len(data_tmp) < 10:
                print('В файле менее десяти городов. Дополните его.')
                exit()
            self.db_cities = {a: 1 for a in data_tmp}

            # буквы, с которых НЕ начинаются города во входном файле
            for key in self.db_cities.keys():
                letter = key[0]
                if self.dnt_use_let.count(letter) != 0:
                    self.dnt_use_let.remove(letter)
            # первый ход за программой
            print('Игра Города!')
            self.current_city = next(iter(self.db_cities.keys()))
            self.db_cities[self.current_city] = 0
            print(self.current_city)

    # на какую букву надо назвать город
    @staticmethod
    def which_letter(city, dnt_use_let):
        count = -1
        while dnt_use_let.count(city[count]) != 0:
            count -= 1
        return city[count]

    # окончена ли игра (игра окначивается если больше нет городов, начинающихся на нужную букву)
    def is_game_over(self):
        cur_let = self.which_letter(self.current_city, self.dnt_use_let)
        for city, value in self.db_cities.items():
            if value == 1 and city[0] == cur_let:
                return False
        return True

    # ход программы
    def pc_turn(self):
        cur_let = self.which_letter(self.current_city, self.dnt_use_let)
        for city, value in self.db_cities.items():
            if value == 1 and city[0] == cur_let:
                self.db_cities[city] = 0
                self.current_city = city
                print(city)
                return

    # ход игрока
    def user_turn(self):
        cur_let = self.which_letter(self.current_city, self.dnt_use_let)
        print('Веедите город, начинающийся на \'' + cur_let + '\':')
        # проверка на корректность введённого города
        wrong = True
        while wrong:
            wrong = False
            user_city = input().lower().strip()
            if user_city == '' or user_city[0] != cur_let:
                print('Ваш город должен начинаьться на \'' + cur_let + '\'!')
                wrong = True
                continue
            if self.db_cities.get(user_city) is None:
                print('Такой город не существует. Введите другой.')
                wrong = True
                continue
            for ct, value in self.db_cities.items():
                if user_city == ct and value == 0:
                    print('Данный город уже назывался. Введите другой.')
                    wrong = True
                    break
        self.db_cities[user_city] = 0
        self.current_city = user_city


game = Cities('ru_cities')
while True:
    game.user_turn()
    if game.is_game_over():
        print('You win!')
        break
    game.pc_turn()
    if game.is_game_over():
        print('You lose!')
        break
exit()
