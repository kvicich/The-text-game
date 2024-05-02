time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
strength = character_info.get('strength', 'Unknown')
agility = character_info.get('agility', 'Unknown')
steps = character_info.get('steps')
print("Вы нашли аптечку, что вы выберете?")
user_choice1984 = input("1) Взять бинт\n"
                        "2) Взять ампулу\n"
                        "3) Ничего не брать")
                        
time.sleep(1)
if user_choice1984 == "1":
    print("Вы взяли бинт и перевезяли рану.\n +10 hp")
    health += 10
    steps += 1
    user_data['character']['steps'] = steps
    user_data['character']['health'] = health
    save_user_data(user_data)
    a = input()
elif user_choice1984 == "2":
    print("Ампула оказалась с ядом, вы умерли")
    os.remove("res/user/user_data.json")
    a = input()
else:
    print("Некорректный выбор")
    time.sleep(2)
    Main()