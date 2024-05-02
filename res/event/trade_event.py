time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
strength = character_info.get('strength', 'Unknown')
money = character_info.get('money', 'Unknown')
steps = character_info.get('steps')
print("Вы встретили торговца из дружественной фракции")
user_choice = input("Он показал вам свои товары, что вы купите:\n1) Аптечку\n2) Банку протеина\n3) Ничего")
if user_choice == "1":
    time.sleep(1)
    print("Вы восстановили здоровье.\n +50 health, -100 money")
    health += 50
    money -= 100
    steps += 1
    user_data['character']['steps'] = steps
    user_data['character']['health'] = health
    user_data['character']['money'] = money
    save_user_data(user_data)
    a = input()
elif user_choice == "2":
    print("// Спартак... бля, это не та игра")
    time.sleep(1)
    print("Вы купили банку протеина, спустя некоторое время вы стали сильнее.\n +30 strength, -150 money")
    strength += 30
    money -= 150
    steps += 1
    user_data['character']['steps'] = steps
    user_data['character']['strength'] = strength
    user_data['character']['money'] = money
    save_user_data(user_data)
    a = input()
elif user_choice == "3":
    print("Ну и не надо мне оно, деньги будто лишние есть...")
    time.sleep(1.5)
    print("Вы решили ничего не покупать.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else:
    print("Некорректный выбор, возвращаемся в главное меню")
    time.sleep(1)
    Main()