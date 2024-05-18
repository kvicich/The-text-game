time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
money = character_info.get('money', 'Unknown')
scheme = character_info.get('scheme', 'Unknown')
steps = character_info.get('steps')
print("Вы обнаружили старый бункер и решили его исследовать.")
print("Внутри вы нашли сундук.")
print("1) Открыть сундук")
print("2) Пройти мимо")
user_choice = input("Что вы хотите сделать?\n")
if user_choice == "1":
    print("Вы открыли сундук.")
    time.sleep(1)
    luck = random.choice([True, False])
    if luck:
        print("В сундуке вы нашли немало ценностей.")
        money += random.randint(50, 200)
        scheme += random.randint(1, 3)
        print(f"Вы получили {money} монет и {scheme} новых схем.")
        steps += 1
        user_data['character']['money'] = money
        user_data['character']['scheme'] = scheme
        user_data['character']['steps'] = steps
        save_user_data(user_data)
    else:
        print("Кажется, сундук был пуст.")
        steps += 1
        user_data['character']['steps'] = steps
        save_user_data(user_data)
elif user_choice == "2":
    print("Вы решили не рисковать и пройти мимо.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
else:
    print("Вы сделали некорректный выбор!")
    time.sleep(3)
    Main()