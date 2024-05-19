user_data = load_user_data() # Получаем всю юзердату чтобы просто отобразить её
character_info = user_data.get('character', {})
name = character_info.get('name', 'Unknown')
money = character_info.get('money', 'Unknown')
health = character_info.get('health', 'Unknown')
steps = character_info.get('steps')
time.sleep(0.5)
print("В ходе разговора с одним из ваших друзей вы узнали местоположение капсул с 'материей'")
time.sleep(2.5)
print("Он предложил вам вместе сходить и забрать её, ведь она поможет в разгадке тайны 'Новой эры'")
time.sleep(2)
user_choice = input("Что ты выберешь?\n1) Сходим вместе заберём материю и дело в шляпе\n2) Да ну его!\n")
if user_choice == "1":
    lucky = random.randint(0, 1000)
    if lucky > 300:
        print("Вы собираетесь на вылазку...")
        time.sleep(5)
        print("Вы отправились...")
        time.sleep(3)
        materia_bottle = random.randint(1, 3)
        print(f"Вы нашли {materia_bottle} бутылки(ок) материи")
        time.sleep(3)
        if materia_bottle == 1:
            money += 100
        elif materia_bottle == 2:
            money += 200
        else:
            money += 300
        print(f"Когда вы пришли домой, вы продали их за {money} монет.\n +{money} money")
        steps += 1
        user_data['character']['money'] = money
        user_data['character']['steps'] = steps
        save_user_data(user_data)
        a = input()
    else:
        print("Вы собираетесь на вылазку...")
        time.sleep(5)
        print("Вы отправились...")
        time.sleep(3)
        print("Ваш друг решил пойти первым...")
        time.sleep(1.45)
        print("Через несколько минут вы слышите крик: *ОСАДА*")
        time.sleep(0.5)
        print("Прибежав к другу, вы спасаете его, отделавшись ушибами.\n -30 health")
        health -= 30
        steps += 1
        user_data['character']['health'] = health
        user_data['character']['steps'] = steps
        save_user_data(user_data)
        a = input()
elif user_choice == "2":
    time.sleep(1)
    print("Вы решили что оно вам не надо...")
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
else:
    print("Некорректный выбор!!!")
    a = input()
    exit()