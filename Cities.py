# -*- coding: utf-8 -*-


# какая справа по счёту буква текущего города будет использоваться для следующего города
def which_letter(city, dnt_use_let):
    count = -1
    while dnt_use_let.count(city[count]) != 0:
        count -= 1
    return count


# окончена ли игра (игра окначивается если больше нет городов, начинающихся на нужную букву)
def is_game_over(db_cities, city, dnt_use_let):
    cur_let = city[which_letter(city, dnt_use_let)]
    for ct, value in db_cities.items():
        if value == 1 and ct[0] == cur_let:
            return False
    return True


# ход программы
def pc_turn(db_cities, city, dnt_use_let):
    cur_let = city[which_letter(city, dnt_use_let)]
    for ct, value in db_cities.items():
        if value == 1 and ct[0] == cur_let:
            db_cities[ct] = 0
            print(ct)
            return ct


# ход игрока
def user_turn(db_cities, city, dnt_use_let):
    cnt = which_letter(city, dnt_use_let)
    print('Веедите город, начинающийся на \'' + city[cnt] + '\':')
    # проверка на корректность введённого города
    wrong = True
    while wrong:
        wrong = False
        user_city = input()
        user_city = user_city.lower().strip()
        if db_cities.get(user_city) is None:
            print('Такой город не существует. Введите другой.')
            wrong = True
            continue
        for ct, value in db_cities.items():
            if user_city == ct and value == 0:
                print('Данный город уже назывался. Введите другой.')
                wrong = True
                break
    data[user_city] = 0
    return user_city


# считываем города и помещаем их в словарь
# изначально в словаре каждому городу поставлено значение 1, когда город называется, значение становится 0
with open('ru_cities', 'r', encoding="utf-8") as f:
    data_tmp = f.read().splitlines()
    if len(data_tmp) < 2:
        print('В файле менее двух городов!')
        exit()
    data = {a: 1 for a in data_tmp}

    # находим буквы, с которых НЕ начинаются города во входном файле
    no_use_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    for key in data.keys():
        letter = key[0]
        if no_use_letters.count(letter) != 0:
            no_use_letters.remove(letter)

    # программа ходит первой
    print('Игра Города!')
    next_city = next(iter(data.keys()))
    data[next_city] = 0
    print(next_city)
    # основной цикл
    while True:
        next_city = user_turn(data, next_city, no_use_letters)
        if is_game_over(data, next_city, no_use_letters):
            print('You win!')
            break

        next_city = pc_turn(data, next_city, no_use_letters)
        if is_game_over(data, next_city, no_use_letters):
            print('You lose!')
            break
    exit()
