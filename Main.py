# -*- coding: utf-8 -*-
# Импорты
import os
import sys
import time
import json
import random

# Переменные
version = "0.02"
story_file = "story.txt"

def clear_console():
    os_name = os.name
    if os_name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def load_user_data():
    try:
        with open('user_data.json', 'r', encoding="UTF-8") as file:
            user_data = json.load(file)
        return user_data
    except FileNotFoundError:
        clear_console()
        print("Файл сохранения пользователя не найден.")
        time.sleep(1)
        Main()

def save_user_data(user_data):
    with open(f'user_data.json', 'w') as file:
        json.dump(user_data, file)
        print("Ваши данные сохранены")

def load_last_game():
    clear_console()
    print("Загружаю...")
    time.sleep(1)
    clear_console()
    print("Инфо о персонаже")
    user_data = load_user_data()
    character_info = user_data.get('character', {})
    name = character_info.get('name', 'Unknown')
    health = character_info.get('health', 'Unknown')
    strength = character_info.get('strength', 'Unknown')
    agility = character_info.get('agility', 'Unknown')
    steps = character_info.get('steps')
    # Вывод информации о персонаже
    print(f"Имя: {name}\nЗдоровье: {health}\nСила: {strength}\nЛовкость: {agility}")

    if steps == 0:
        print("Вы очнулись посреди ошмётков научной станции...")
        time.sleep(2)
        print("Оглядевшись и никого не увидив вы нашли в своём кармане бумажку...")
        time.sleep(2)
        user_choice = input("Прочитать? Да/Нет\n")
        if user_choice == "Да":
            time.sleep(1)
            print("На бумаге были написаны координаты, вы решили пойти туда, спустя 2 часа вы увидели лагерь выживших.\n Вы всё таки осмелились туда пойти, через пару часов вы уже знали всех в этом лагере, тут и началась ваша история выживания...")
            steps += 1
            user_data['character']['steps'] = steps
            save_user_data(user_data)
        elif user_choice == "Нет":
            print("Это было раковой ошибкой.\n Спустя несколько часов скитания по обломкам вы начали терять надежду.\n Еще через пару часов на вас упала одна из балок, придавив вас, на ваши крики пришёл только местный медведь. \n Медведь вкусно пообедал, а вы умерли")
            os.remove('user_data.json')
        else: 
            print("Некорректный выбор.")
            exit()
    a = input("\n")
    Main()

def load_new_game():
    clear_console()
    checker = input("Вы уверены?\n Да\n Нет\n")
    if checker == 'Да':
        print("Загружаю...")
        time.sleep(1)
    elif checker == 'Нет':
        print("Возвращаюсь в главное меню...")
        time.sleep(1)
        Main()
    else: 
        print("Некорректный выбор, возвращаюсь в главное меню...")
        time.sleep(1)
        Main()
    clear_console()
    print("Создание персонажа")

    while True:
        # Выбор сложности
        difficulty = input("Выберите сложность (1 - легкая, 2 - средняя, 3 - сложная): ")
        if difficulty == "1":
            difficulty = "easy"
        elif difficulty == "2":
            difficulty = "normal"
        elif difficulty == "3":
            difficulty = "hard"
        else:
            print("Некорректный выбор сложности! Попробуйте снова.")
            continue

        # Генерация имени персонажа
        with open('names.txt', 'r', encoding='utf-8') as file:
            names = file.readlines()
        with open('subnames.txt', 'r', encoding='utf-8') as file:
            subnames = file.readlines()
        name = random.choice(names).strip()
        subname = random.choice(subnames).strip()

        # Определение характеристик в зависимости от сложности
        if difficulty == "easy":
            health = random.randint(50, 70)
            strength = random.randint(30, 50)
            agility = random.randint(40, 60)
            money = random.randint(100, 200)
        elif difficulty == "normal":
            health = random.randint(40, 60)
            strength = random.randint(40, 60)
            agility = random.randint(40, 60)
            money = random.randint(70, 150)
        elif difficulty == "hard":
            health = random.randint(30, 50)
            strength = random.randint(50, 70)
            agility = random.randint(30, 50)
            money = random.randint(0, 100)

        # Создание словаря с характеристиками персонажа
        character = {
            "name": name + " " + subname,
            "money": money,
            "health": health,
            "strength": strength,
            "agility": agility,
            "steps": 0  # Устанавливаем количество шагов на 0
        }

        # Запись пользовательских данных в файл user_data.json
        user_data = {"character": character}
        with open("user_data.json", "w", encoding="UTF-8") as file:
            json.dump(user_data, file)

        # Вывод информации о персонаже
        print("Персонаж создан:")
        print("Имя:", character["name"])
        print("Здоровье:", character["health"])
        print("Сила:", character["strength"])
        print("Ловкость:", character["agility"])

        # Запрос на повторное создание персонажа
        reroll = input("Желаете пересоздать персонажа? (да/нет): ")
        if reroll.lower() != "да":
            break

    # Вызов функции загрузки последней игры
    load_last_game()

def settings():
    print("     Настройки     ")
    a = input()
    Main()

def exit():
    print("Выходим...\n Подождите 3 секунды...")
    time.sleep(3)
    sys.exit()

def Main(): # Главная функция
    clear_console()
    print("Версия игры: " + version)
    print("Начать игру?")
    user_choice = input("Выберите что то из этого:\n"
                        "1) Загрузить текущую игру\n"
                        "2) Начать заново\n"
                        "3) Сюжет\n"
                        "4) Настройки\n"
                        "5) Выход\n")
    
    try: # Пытаемся превратить переменную в строку дабы исключить постоянный неправильный выбор
        user_choice = int(user_choice)
    except ValueError:
        clear_console()
        print("Некорректный выбор! Возвращаемся в главное меню...")
        time.sleep(1)
        Main()

    if user_choice == 1: # Тонна 6, лень урезать/убирать
        load_last_game()
    elif user_choice == 2:
        load_new_game()
    elif user_choice == 3:
        try:
            with open(story_file, 'r', encoding="UTF-8") as file:
                story_text = file.read()
                print("                                                             Сюжет")
                print(story_text)
                a = input()
                Main()
        except FileNotFoundError:
            print(f"Файл '{story_file}' не найден.")
            a = input()
            Main()
    elif user_choice == 4:
        settings()
    elif user_choice == 5:
        exit()
    else:
        clear_console()
        print("Некорректный выбор!\n Возвращаемся в главное меню...")
        time.sleep(1)
        Main()

if __name__ == "__main__":
    Main()