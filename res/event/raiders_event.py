time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
money = character_info.get('money', 'Unknown')
steps = character_info.get('steps')
print("Ваше поселение атакует банда налётчиков!")
user_choice = input("Что вы сделает?\n"
                    "1) Организовать защиту и сразиться с нападающими.\n"
                    "2) Попытаться скрыться и уйти незамеченным.\n"
                    "3) Предложить деньги взамен на ваше спокойствие.\n")
if user_choice == "1":
    print("Вы собрали своих товарищей и успешно отбили нападение.")
    print("Несмотря на потери, вы смогли защитить поселение.\n -10 health")
    health -= 10
    steps += 1
    user_data['character']['health'] = health
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
elif user_choice == "2":
    print("Вы спрятались и избежали нападения, но ваше поселение понесло потери.")
    print("Теперь вам придётся восстанавливать утраченное.\n -500 money")
    money -= 500
    steps += 1
    user_data['character']['money'] = money
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
elif user_choice == "3":
    print("Вы предложили деньги налётчикам в обмен на мирное урегулирование.")
    print("Они приняли ваше предложение и ушли.\n -700 money")
    money -= 700
    steps += 1
    user_data['character']['money'] = money
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else: 
    print("Некорректный выбор!!!")
    time.sleep(3)
    Main()