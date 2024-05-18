time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
steps = character_info.get('steps')
money = character_info.get('money')
print("Вы споткнулись и упали в подземелье.")
time.sleep(3)
print("Внутри подземелья вас поджидают разные опасности.")
print("1) Исследовать")
print("2) Попытаться выбраться")
user_choice = input("Что вы хотите сделать?\n")
if user_choice == "1":
    print("Вы начали исследовать подземелье.")
    time.sleep(1)
    print("Вы нашли сундук с сокровищами!")
    health -= 10
    money += random.randint(12, 130)
    steps += 1
    user_data['character']['health'] = health
    user_data['character']['steps'] = steps
    time.sleep(3.5)
    print(f"Вы успешно выбрались из подземелья. -10 health +{money} money")
    user_data['character']['money'] = money
    save_user_data(user_data)
elif user_choice == "2":
    print("Вы пытаетесь выбраться из подземелья.")
    time.sleep(1)
    print("Попытка безуспешна, и вы продолжаете блуждать в подземелье.")
    health -= 20
    steps += 1
    user_data['character']['health'] = health
    user_data['character']['steps'] = steps
    save_user_data(user_data)
else:
    print("Вы сделали некорректный выбор!")
    time.sleep(3)
    Main()