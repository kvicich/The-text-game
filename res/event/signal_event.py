time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
steps = character_info.get('steps')
scheme = character_info.get('scheme')

print("Внезапно вы начинаете получать странный сигнал в своем устройстве.")
time.sleep(0.8)
print("Сигнал кажется нечто большим, чем просто шум фонового излучения.")
user_choice = input("Что вы сделаете?\n"
"1) Попробую отследить источник сигнала.\n"
"2) Игнорировать сигнал и продолжить движение.\n")
if user_choice == "1":
    time.sleep(0.5)
    print("Вы начинаете сканировать окружающую среду в поисках источника сигнала.")
    time.sleep(2.5)
    print("Через некоторое время вы обнаруживаете разрушенное здание, из которого исходит сигнал.")
    time.sleep(1)
    print("Внутри здания вы находите старый компьютер с доступом к базе данных.")
    time.sleep(0.5)
    print("Сигнал, оказывается, идет из старой записи, содержащей координаты крупного запаса ресурсов.")
    time.sleep(3)
    print("Вы сохраняете координаты и отправляетесь на поиски ресурсов.\n +1 scheme")
    steps += 1
    scheme += 1
    user_data['character']['steps'] = steps
    user_data['character']['scheme'] = scheme
    save_user_data(user_data)
    a = input()
elif user_choice == "2":
    print("Вы решаете проигнорировать странный сигнал и продолжить движение.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else:
    print("Некорректный выбор.")
    time.sleep(2)
    exit()