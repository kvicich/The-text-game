# -*- coding: utf-8 -*-
# Импорты
import os
import sys
import time
import json
import random

# Переменные
version = "1.3" # Версия игры, не забывайте её обновлять
story_file = "res/story.txt" # Один раз укажите если будете менять папку с ресурсами, и забейте хер
user_data_path = "res/user/user_data.json" # Тут сохраняем папку с юзердатой
splash_file = "res/splashes.txt" # А это сплеши
event_path = "res/event/" # Место с ивентами

def clear_console(): # Чистилка консоли
    os_name = os.name # Узнаём имя операционки
    if os_name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def load_splash(): # Рандомные сплешики
    with open(splash_file, 'r', encoding='utf-8') as file:
        splashes = file.readlines()
    splash = random.choice(splashes).strip()
    print(splash)

load_splash()

def load_user_data(): # Загружаем юзердату
    try:
        with open(user_data_path, 'r', encoding="UTF-8") as file:
            user_data = json.load(file)
        return user_data
    except FileNotFoundError:
        clear_console()
        print("Файл сохранения пользователя не найден, код ошибки: 0x01.")
        time.sleep(1) 
        Main()

def save_user_data(user_data): # Сохраняем юзердату
    try:
        with open(user_data_path, 'w') as file:
            json.dump(user_data, file)
            print("Ваши данные сохранены")
    except Exception as e:
        print(f"Ошибка сохранения данных пользователя: 0x02\nТехническая информация: {e}")

def load_cog_data(file_path, file): # Грузим ивентики
    with open(f'{file_path}{file}', 'r', encoding='UTF-8') as f:
        cog_data = f.read()
    return cog_data

def load_last_game(): # Загружаем последнюю игру
    while True:
        clear_console()
        try:
            user_data = load_user_data() # Получаем всю юзердату чтобы просто отобразить её
            character_info = user_data.get('character', {})
            name = character_info.get('name', 'Unknown')
            money = character_info.get('money', 'Unknown')
            health = character_info.get('health', 'Unknown')
            strength = character_info.get('strength', 'Unknown')
            agility = character_info.get('agility', 'Unknown')
            steps = character_info.get('steps')
            scheme = character_info.get('scheme')
        except Exception as e:
            print(f"Ошибка загрузки юзердаты, код ошибки: 0x04\nТехническая информация: {e}")
        try:
            money = int(money)
            health = int(health)
            strength = int(strength)
            agility = int(agility)
            steps = int(steps)
            scheme = int(scheme)
        except ValueError as e:
            print(f"Ошибка преобразования данных, код ошибки: 0x05\nТехническая информация: {e}")
        if health > 100: # Не будет вам 500 здоровья
            health = 100
            user_data['character']['health'] = health
        if strength > 100:
            strength = 100
            user_data['character']['strength'] = strength
        if agility > 100:
            agility = 100
            user_data['character']['agility'] = agility
        if health < 0:
            health = 0
            user_data['character']['health'] = health
        if strength < 0:
            health = 0
            user_data['character']['health'] = health
        if agility < 0:
            health = 0
            user_data['character']['health'] = health
        save_user_data(user_data)
        clear_console()
        load_splash()
        time.sleep(3)
        clear_console()
        print("Инфо о персонаже")
        # Вывод информации о персонаже
        print(f"Имя: {name}\nМонеты: {money}\nСхемы {scheme}\nЗдоровье: {health}\nСила: {strength}\nЛовкость: {agility}\nШаги: {steps}")
        main_1 = input("Чтобы перейти в главное меню нажмите 5: ")
        if main_1 == "5":
            Main()
        event_randomizer()

def event_randomizer(): # Второй кусок кода на котором держится игра
    clear_console()
    load_splash()
    try:
        user_data = load_user_data()
        steps = user_data.get('character', {}).get('steps', 0)
        scheme = user_data.get('character', {}).get('scheme', 0)
        health = user_data.get('character', {}).get('health', 0)
    except Exception as e:
        print(f"Ошибка загрузки юзердаты, код ошибки: 0x04\nТехническая информация: {e}")

    # Пока не будет выполнено условие (steps != 0 и выбранный файл не start_event.py), продолжаем выбор случайного файла
    while True:
        # Если количество шагов равно 0, загружаем и выполняем start_event.py
        if steps == 0:
            file_path = 'res/event/'
            start_event_file = 'start_event.py'
            start_event_code = load_cog_data(file_path, start_event_file)
            clear_console()
            exec(start_event_code, globals(), locals())
            break
                
        if scheme > 105: # Если количество схем больше 105 пишем дискордик и всё
            print("Вам незачем играть дальше")
            print("Дискорд проекта этого и многих других моих проектов: https://discord.gg/xkwg3e2wUX")
            a = input()
            Main()

        if health == 0:
            print("Вы...")
            time.sleep(0.5)
            print("Умерли...")
            time.sleep(3)
            print("Это конец вашей истории")
            os.remove('res/user/user_data.json')

        if scheme > 100: # Если количество схем больше 100, загружаем и выполняем last_event.py
            file_path = 'res/event/'
            last_event_file = 'last_event.py'
            last_event_code = load_cog_data(file_path, last_event_file)
            clear_console()
            exec(last_event_code, globals(), locals())
            break
        
        # Получаем список всех файлов в директории res/event/
        event_files = [file for file in os.listdir(event_path) if file.endswith('.py')]
        
        # Удаляем не нужные ивенты
        if 'start_event.py' in event_files:
            event_files.remove('start_event.py')
        if 'last_event.py' in event_files:
            event_files.remove('last_event.py')

        # Если список файлов не пуст и все они не start_event.py, выбираем случайный файл и загружаем его
        if event_files:
            random_event_file = random.choice(event_files)
            file_path = event_path
            cog_data = load_cog_data(file_path, random_event_file)
            clear_console()
            exec(cog_data, globals(), locals())
            break

def load_new_game(): # Загружаем новую игру
    clear_console() # Моя спасительница
    checker = input("Вы уверены? (Да Нет)\n")
    if checker == 'Да':
        load_splash()
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
        difficulty = input("Выберите сложность (1 - легкая, 2 - средняя, 3 - сложная, 4 - кошмарная): ")
        if difficulty == "1":
            difficulty = "easy"
        elif difficulty == "2":
            difficulty = "normal"
        elif difficulty == "3":
            difficulty = "hard"
        elif difficulty == "4":
            difficulty = "extreme"
        else:
            print("Некорректный выбор сложности! Попробуйте снова.")
            continue

        # Генерация имени персонажа
        with open('res/names.txt', 'r', encoding='utf-8') as file:
            names = file.readlines()
        with open('res/subnames.txt', 'r', encoding='utf-8') as file:
            subnames = file.readlines()
        name = random.choice(names).strip()
        subname = random.choice(subnames).strip()

        # Определение характеристик в зависимости от сложности
        # Пиздец дохуя кода тут
        if difficulty == "easy":
            health = random.randint(70, 100)
            strength = random.randint(60, 100)
            agility = random.randint(55, 100)
            money = random.randint(150, 500)
        elif difficulty == "normal":
            health = random.randint(40, 70)
            strength = random.randint(40, 70)
            agility = random.randint(40, 70)
            money = random.randint(90, 250)
        elif difficulty == "hard":
            health = random.randint(30, 50)
            strength = random.randint(20, 50)
            agility = random.randint(30, 50)
            money = random.randint(0, 100)
        elif difficulty == "extreme":
            health = random.randint(7, 15)
            strength = random.randint(10, 30)
            agility = random.randint(1, 25)
            money = 0
        else:
            print("Неизвестная ошибка. Код: 0x03")

        # Создание словаря с характеристиками персонажа
        character = {
            "name": name + " " + subname,
            "money": money,
            "health": health,
            "strength": strength,
            "agility": agility,
            "steps": 0,  # Обязательно ставьте кол-во шагов на ноль если не хотите пропустить стартовый ивент
            "scheme": 0
        }

        # Проверяем существование папки, если её нет, создаем
        if not os.path.exists('res/user'):
            os.makedirs('res/user')

        # Запись пользовательских данных в файл user_data.json
        user_data = {"character": character}
        with open(user_data_path, "w", encoding="UTF-8") as file:
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

def exit(): # Функция для выхода
    clear_console()
    print("Выходим...\n    Подождите 3 секунды...")
    time.sleep(3)
    sys.exit()

def debug(): # Дебааааааг (чтоб я не ебался с тестом ивентов)
    clear_console()
    load_splash()
    user_data = load_user_data() # Получаем всю юзердату
    character_info = user_data.get('character', {})
    name = character_info.get('name', 'Unknown')
    money = character_info.get('money', 'Unknown')
    health = character_info.get('health', 'Unknown')
    strength = character_info.get('strength', 'Unknown')
    agility = character_info.get('agility', 'Unknown')
    steps = character_info.get('steps')
    scheme = character_info.get('scheme')
    clear_console()
    print(f"Ваш персонаж:\nИмя: {name}\nМонеты: {money}\nСхемы {scheme}\nЗдоровье: {health}\nСила: {strength}\nЛовкость: {agility}\nШаги: {steps}\n")
    print("Что вы хотите выбрать?")
    debug_choice = input("1) Изменение характеристик персонажа\n2) Удалить даннные персонажа\n3) raw данные персонажа\n4) Запустить ивент\n5) В главное меню\n")
    
    if debug_choice == "1":
        harc = input("Какую характеристику персонажа хотите изменить? (Пример: name)\n")
        load_splash()
        harc2 = character_info.get(harc, 'Unknown')
        clear_console()
        print(f"Имя вашей характеристики: {harc}\nЗначение: {harc2}")
        value = input("Введите значение для этой характеристики: ")
        clear_console()
        load_splash()
        try:
            value_int = int(value)
        except(ValueError):
            print("Вы ввели не число!")
            a = input()
            Main()
        user_data['character'][harc] = value_int
        save_user_data(user_data)
        a = input()
        Main()
    elif debug_choice == "2":
        clear_console()
        checker = input("Вы уверены?\n Да\n Нет\n")
        if checker == 'Да':
            load_splash()
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
        os.remove(user_data_path)
        print("Пользовательские данные удалены")
        a = input()
        Main()
    elif debug_choice == "3":
        print("Пожалуйста подождите...")
        time.sleep(0.5)
        clear_console()
        print(user_data)
        a = input()
        Main()
    elif debug_choice == "4":
        user_choice = input("Введите имя файла ивента, либо exit если хотите выйти в главное меню\n")
        if user_choice == "exit":
            print("Переходим в главное меню...")
            time.sleep(3)
            Main()
        else:
            try:
                cog_data = load_cog_data(event_path, user_choice)
                clear_console()
                exec(cog_data, globals(), locals())
            except FileNotFoundError:
                print("Файл ивента не найден.")
        a = input()
        Main()
    elif debug_choice == "5":
        Main()
    elif debug_choice == "6":
        for _ in range(100):
            time.sleep(0.01)
            print("Дебаг в дебаге")
        time.sleep(3)
        print("Вы сломали дебаг")
        time.sleep(3)
        exit()
    else:
        clear_console()
        print("Некорректный выбор!\n Возвращаемся в главное меню...")
        time.sleep(1)
        Main()

def Main(): # Главное меню
    clear_console()
    print("Версия игры: " + version)
    print("Начать игру?")
    user_choice = input("Выберите что то из этого:\n"
                        "1) Загрузить текущую игру\n"
                        "2) Начать заново\n"
                        "3) Сюжет\n"
                        "4) Выход\n")
    
    if user_choice == "1": # Тонна сравнений
        load_last_game()
    elif user_choice == "2": # Функция для создания новой игры
        load_new_game()
    elif user_choice == "3":
        try: # Грузим сюжитик
            with open(story_file, 'r', encoding="UTF-8") as file:
                story_text = file.read()
                print("Сюжет")
                print(story_text)
                a = input()
                Main()
        except FileNotFoundError:
            print(f"Файл '{story_file}' не найден.")
            a = input()
            Main()
    elif user_choice == "4":
        exit()
    elif user_choice == "debug":
        debug()
    elif user_choice == "5":
        print("Как-нибудь потом")
    else:
        clear_console()
        print("Некорректный выбор!\n    Возвращаемся в главное меню...")
        time.sleep(1)
        Main() # Рекурсия подъехала

if __name__ == "__main__": # На этих двух строчках кода держится вся игра
    Main()