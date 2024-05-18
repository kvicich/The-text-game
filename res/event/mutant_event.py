time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
steps = character_info.get('steps')
strength = character_info.get('strength', 'Unknown')
print("Вы услышали странные шорохи в окрестностях и решили исследовать.")
time.sleep(3)
print("Вы обнаружили группу мутантов, которые напали на вас!")
print("1) Сражаться")
print("2) Убежать")
user_choice = input("Что вы хотите сделать?\n")
if user_choice == "1":
    print("Вы вступили в бой с мутантами.")
    time.sleep(1)
    luck = random.choice([True, False])
    if luck:
        print("Вы одолели мутантов, но получили несколько ушибов. -20 health +13 strength")
        health -= 20
        steps += 1
        strength += 13
        user_data['character']['health'] = health
        user_data['character']['steps'] = steps
        user_data['character']['strength'] = strength
        save_user_data(user_data)
    else:
        print("Мутанты оказались сильнее и вас захватили.")
        time.sleep(1)
        print("Вы сумели сбежать, но получили серьезные повреждения. -50 health")
        health -= 50
        steps += 1
        user_data['character']['health'] = health
        user_data['character']['steps'] = steps
        save_user_data(user_data)
elif user_choice == "2":
    print("Вы решили не рисковать и убежали от мутантов.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
else:
    print("Вы сделали некорректный выбор!")
    time.sleep(3)
    Main()