# Импорты
import os
import sys
import time

# Переменные
version = "0.01"

def load_last_game():
    clear_console()
    print("Загружаю...")

def load_new_game():
    clear_console()
    checker = input("Вы уверены?\n Да\n Нет\n")
    if checker == 'Да':
        print("Загружаю...")
    elif checker == 'Нет':
        print("Возвращаюсь в главное меню...")
        time.sleep(1)
        Main()
    else: 
        print("Некорректный выбор, возвращаюсь в главное меню...")
        time.sleep(1)
        Main()

def settings():
    print("Настройки")

def exit():
    print("Выходим...\n Подождите 3 секунды...")
    time.sleep(3)
    sys.exit()

def clear_console():
    os_name = os.name
    if os_name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def Main(): # Главная функция
    clear_console()
    print("Версия игры: " + version)
    print("Начать игру?")
    user_choice = input("Выберите что то из этого:\n"
                        "1) Загрузить текущую игру\n"
                        "2) Начать заново\n"
                        "3) Настройки\n"
                        "4) Выход\n")
    
    try: # Пытаемся превратить переменную в строку дабы исключить постоянный неправильный выбор
        user_choice = int(user_choice)
    except ValueError:
        clear_console()
        print("Некорректный выбор! Возвращаемся в главное меню...")
        time.sleep(1)
        Main()

    if user_choice == 1: # Тонна сравнений, лень урезать/убирать
        load_last_game()
    elif user_choice == 2:
        load_new_game()
    elif user_choice == 3:
        settings()
    elif user_choice == 4:
        exit()
    else:
        clear_console()
        print("Некорректный выбор!\n Возвращаемся в главное меню...")
        time.sleep(1)
        Main()

if __name__ == "__main__":
    Main()