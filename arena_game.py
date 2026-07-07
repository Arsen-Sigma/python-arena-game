print("📖 Сюжет\nТы выходишь на арену.\nПеред тобой 3 противника.\nТвоя задача — победить их всех.")  #  Этап 1  Сюже

#  противики урон и хп и игрока
hp = 100
damage = 20
enemy_hp_1 = 40
enemy_damage_1 = 14
enemy_hp_2 = 50
enemy_damage_2 = 15
enemy_hp_3 = 80
enemy_damage_3 = 18

game = input("Начало игры (да/нет) ").lower()   #  Этап 2 Начало игры

if game == "да":
    print("=========================\n⚔️ АРЕНА\n=========================\nТебя ждут 3 противника.")
    print(f"=========================\n 👤 ТВОЙ ПЕРСОНАЖ\n=========================\n ❤️  Здоровье: {hp}\n ⚔️  Урон: {damage}")  #  Этап 3 показать характеристики игрока.
    print("\n⚔️  Противник выходит на арену!\n")
elif game == "нет":
    print("Игра завершена.")
    exit()
else:
    print("Неверный ввод.")
    exit()

# Этап 5 бой и противики
if game == "да":
    print(f"====================\n 👹 Противник № 1\n ❤️  HP: {enemy_hp_1}\n ⚔️  Урон: {enemy_damage_1}\n====================")
    print("Первый противник нападает.\n")
    print("Что будешь делать?")

while True:
    #  1  бой
    if game == "да":
        print("\n 1. Ударить\n 2. Ничего не делать")
        action = int(input("Веди свой вариант: "))

        if action > 2 or action < 1:
            print("❌  Введите только 1 или 2.")
            continue

        elif action == 1:
            enemy_hp_1 = max(0, enemy_hp_1 - damage)
            print(f"\nТы ударил противника.\n❤️  HP противника: {enemy_hp_1}")

            if enemy_hp_1 > 0:  
                hp = max(0, hp - enemy_damage_1)
                print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        elif action == 2:
            hp = max(0, hp - enemy_damage_1)
            print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        if enemy_hp_1 == 0:
            print("\n🏆  Ты победил первого противника!")
            print("\n👹  Второй противник уже бежит к тебе.")
            break

        if hp == 0:
            print("\n👹  К сожалению, но ты умер.")
            exit()


if game == "да":
    if enemy_hp_1 == 0:
        print(f"\n====================\n 👹 Противник № 2\n ❤️  HP: {enemy_hp_2}\n ⚔️  Урон: {enemy_damage_2}\n====================")

while True:
    # 2  бой
    if game == "да":
        print("\n 1. Ударить\n 2. Ничего не делать")
        action = int(input("Веди свой вариант: "))

        if action > 2 or action < 1:
            print("❌  Введите только 1 или 2.")
            continue

        elif action == 1:
            enemy_hp_2 = max(0, enemy_hp_2 - damage)
            print(f"\nТы ударил противника.\n❤️  HP противника: {enemy_hp_2}")

            if enemy_hp_2 > 0:
                hp = max(0, hp - enemy_damage_2)
                print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        elif action == 2:
            hp = max(0, hp - enemy_damage_2)
            print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        if enemy_hp_2 == 0:
            print("🏆  Ты победил Второго противника!\n\n👹 Третий противник уже бежит к тебе.")
            break

        if hp == 0:
            print("👹  К сожалению, но ты умер.")
            exit()


if game == "да":
    if enemy_hp_2 == 0:
        print(f"\n====================\n 👹 Противник № 3\n ❤️  HP: {enemy_hp_3}\n ⚔️  Урон: {enemy_damage_3}\n====================")

while True:
    # 3  бой
    if game == "да":
        print("\n 1. Ударить\n 2. Ничего не делать")
        action = int(input("Веди свой вариант: "))

        if action > 2 or action < 1:
            print("❌  Введите только 1 или 2.")
            continue

        elif action == 1:
            enemy_hp_3 = max(0, enemy_hp_3 - damage)
            print(f"\nТы ударил противника.\n❤️  HP противника: {enemy_hp_3}")

            if enemy_hp_3 > 0:
                hp = max(0, hp - enemy_damage_3)
                print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        elif action == 2:
            hp = max(0, hp - enemy_damage_3)
            print(f"\nПротивник ударил тебе.\n❤️  HP игрока: {hp}")

        if enemy_hp_3 == 0:
            print("\n=========================\nИГРА ОКОНЧЕНА\n=========================")
            print("\n=========================\n🏆  ПОБЕДА!\n=========================\n\nТы победил всех противников!\n\nСпасибо за игру!\n")
            break

        if hp == 0:
            print("👹  К сожалению, но ты умер.") 
            exit()
