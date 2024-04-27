time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
money = character_info.get('money', 'Unknown')
agility = character_info.get('agility', 'Unknown')
steps = character_info.get('steps')
print("Вы услышали странные звуки из ближайшего здания.")
user_choice = input("Что будете делать?\n"
                    "1) Осмотреться и пойти внутрь.\n"
                    "2) Обойти здание стороной и продолжить путь.\n")
if user_choice == "1":
    if agility > 40:
        print("Ваши рефлексы помогли вам избежать ловушек внутри здания.")
        print("Вы нашли небольшой запас продовольствия и немного полезных предметов.\n +8 agility +40 money")
        steps += 1
        agility += 8
        money += 40
        user_data['character']['money'] = money
        user_data['character']['agility'] = agility
        user_data['character']['steps'] = steps
        save_user_data(user_data)
        a = input()
    else:
        print("Вы вошли в здание, но были внезапно атакованы засадой.")
        print("Вас оглушили и обокрали, когда пришли в себя.\n -30 hp -10 money")
        health -= 30
        money -= 10
        steps += 1
        user_data['character']['money'] = money
        user_data['character']['health'] = health
        user_data['character']['steps'] = steps
        save_user_data(user_data)
        a = input()
elif user_choice == "2":
    print("Вы решили не рисковать и обошли здание стороной.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else:
    print("Некорректный выбор.")
    time.sleep(2)
    exit()