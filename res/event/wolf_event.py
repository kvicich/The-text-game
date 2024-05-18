time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
strength = character_info.get('strength', 'Unknown')
agility = character_info.get('agility', 'Unknown')
steps = character_info.get('steps')
print("Вы встретили волка...")
user_choice = input("Что ты выберешь?\n"
                    "1) Попытаться отбиться\n"
                    "2) Убежать\n"
                    "3) Притвориться мёртвым\n")
if user_choice == "1":
    if strength < 50:
        print("Вы оказались слишком слабым...\n")
        time.sleep(1)
        print("Вас съели...")
        dead()
        a = input()
    else:
        print("Вам удалось отбится но вас поцарапали.\n -10 hp + 3 strength")
        health -= 10
        strength += 3
        steps += 1
        user_data['character']['steps'] = steps
        user_data['character']['health'] = health
        user_data['character']['strength'] = strength
        save_user_data(user_data)
        a = input()
elif user_choice == "2":
    if agility < 10:
        print("Вам удалось убежать.\n + 3 agility")
        agility += 3
        user_data['character']['agility'] = agility
        save_user_data(user_data)
        a = input()
    else:
        print("Вам не удалось убежать...")
        time.sleep(2)
        print("Вы умерли.")
        dead()
elif user_choice == "3":
    print("Ты и правда думал что это поможет?")
    time.sleep(1)
    print("Вы умерли")
    dead()
else: 
    print("Некорректный выбор!!!")
    time.sleep(3)
    Main()



