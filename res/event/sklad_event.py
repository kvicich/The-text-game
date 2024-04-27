time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
money = character_info.get('money', 'Unknown')
strength = character_info.get('strength', 'Unknown')
agility = character_info.get('agility', 'Unknown')
steps = character_info.get('steps')
scheme = character_info.get('scheme')
print("В вашем пути возникает старый заброшенный склад 'Новой Эры'.")
print("Известно, что здесь могут храниться ценные ресурсы и информация.")
user_choice = input("Что вы сделаете?\n"
                    "1) Разыскать способ войти в склад и исследовать его.\n"
                    "2) Обойти склад и не рисковать.\n")
if user_choice == "1":
    print("Вы решаете исследовать склад.")
    print("После длительного поиска вы находите схемы и данные, которые могут помочь разгадать причину сбоя системы 'Новой Эры'.\n +1 схема")
    steps += 1
    scheme += 1
    user_data['character']['steps'] = steps
    user_data['character']['scheme'] = scheme
    save_user_data(user_data)
    a = input()
elif user_choice == "2":
    print("Вы решаете не рисковать и обойти склад стороной.")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else:
    print("Некорректный выбор.")
    time.sleep(2)
    exit()