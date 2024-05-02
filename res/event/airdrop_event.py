time.sleep(1)
user_data = load_user_data()
character_info = user_data.get('character', {})
health = character_info.get('health', 'Unknown')
money = character_info.get('money', 'Unknown')
agility = character_info.get('agility', 'Unknown')
steps = character_info.get('steps')
scheme = character_info.get('scheme')
print("Неподалёку упал воздушный груз")
user_choice = input("Что ты выберешь?\n1) Пойду и заберу всё что там есть\n2) У меня своих дел полно, пропущу\n3) Осторожно подберусь, убью всех кому груз так-же интересен и спокойно всё заберу\n")
if user_choice == "1":
    luck = random.choice([True, False])
    if luck == True:
        print("Удача на вашей стороне!")
        time.sleep(1)
        steps += 1
        scheme += random.randint(0, 3)
        money += random.randint(10,300)
        print(f"Вы успешно обнесли воздушный груз!\n +{money} money +{scheme} scheme")
        user_data['character']['steps'] = steps
        user_data['character']['scheme'] = scheme
        user_data['character']['money'] = money
        save_user_data(user_data)
        a = input()
    elif luck == False:
        print("Там была засада!\nВас подстрелили!\nВы кое как убежали\n -70 health")
        time.sleep(1)
        steps += 1
        health -= 70
        user_data['character']['steps'] = steps
        user_data['character']['health'] = health
        save_user_data(user_data)
        a = input()
elif user_choice == "2":
    print("Вы пропустили воздушный груз.\nНичего не произошло, может это и к лучшему...")
    steps += 1
    user_data['character']['steps'] = steps
    save_user_data(user_data)
    a = input()
elif user_choice == "3":
    print("Вы начали крастся...")
    time.sleep(2.5)
    luck_2 = random.choice([True, False])
    if luck_2 == True:
        raiders = random.choice(['1', '2', '3'])
        print(f"Вам повезло, вы пристрелили {raiders} рейдеров, и спокойно обнесли воздушный груз\n +250 money + 2 scheme")
        steps += 1
        scheme += 1
        money += 150
        user_data['character']['steps'] = steps
        user_data['character']['scheme'] = scheme
        user_data['character']['money'] = money
        save_user_data(user_data)
        a = input()
    else:
        print("Рейдеров оказалось слишком много, вы решили их обойти")
        steps += 1
        money += 150
        user_data['character']['steps'] = steps
        user_data['character']['money'] = money
        save_user_data(user_data)
        a = input()

else: 
    print("Некорректный выбор!!!")
    time.sleep(3)
    Main()


