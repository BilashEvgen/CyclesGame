# Портуемо модуль random та colorama.
import random
import colorama

# ініціалізуємо колораму. У функцію init написали autoreset=True для того, щоб заданий колір тексту працював в одному принті.
colorama.init(autoreset=True)

# створюємо константи в яких зберігаються кольори тексту для консолі
TEXT_COLOR = colorama.Fore.CYAN
INPUT_COLOR = colorama.Fore.BLUE
CHOICE_COLOR = colorama.Fore.MAGENTA
WIN_COLOR = colorama.Fore.GREEN
LOSE_COLOR = colorama.Fore.RED
STAT_AND_INVENTORI_COLOR = colorama.Fore.YELLOW

# створюємо флаг (змінна з типом данних bool), який відповідає за те, чи був взятий той чи інший предмет
bread = 0
Bottle_of_water = 0
mana_potion = 0
health_potion = 0
latchkey = 0
lether = 0
wood = 0
iron = 0
wood_sword = False
iron_sword = False
lether_armor = False
iron_armor = False
book_of_fire_ball = False
base_damage = 15
base_armor = 0
dairy = False
fireball_buff_applied = False
mana_debuff_applied = False

# створюємо характеристику персонажа
health = 100 # Життя (від 0 до 100)
mana = 200 # Кількість мани (від 0 до 200)
stamina = 10 # Енергія (від 0 до 20)
hunger = 10 # Ситість (від 0 до 25)
money = 0 # Гроші (від 0 до ∞)

# створюємо функції def
def state_check(health, stamina, hunger):
    if hunger <= 0:
        hunger = 0
        print(f"{TEXT_COLOR}Ви дуже зголодніли та втратили житті.")
        if stamina <= 0:
            stamina = 0 
            print(f"{TEXT_COLOR}А токож дуже втомились.")
        health -= random.randint(1, 3)
    elif stamina <= 0: 
        stamina = 0
        print(f"{TEXT_COLOR}Ви дуже втомились та втратили житті.")
        if hunger <= 0:
            hunger = 0
            print(f"{TEXT_COLOR}А також дуже зголодніли.")
        health -= random.randint(1, 3)
    return health, stamina, hunger
# health, stamina, hunger = state_check(health, stamina, hunger)

def open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor):
    print("\n--- Статус персонажа ---")
    print(f"{STAT_AND_INVENTORI_COLOR}Життя: {health}")
    print(f"{STAT_AND_INVENTORI_COLOR}Мана: {mana}")
    print(f"{STAT_AND_INVENTORI_COLOR}Енергія: {stamina}")
    print(f"{STAT_AND_INVENTORI_COLOR}Ситість: {hunger}")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {money} грошей")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {bread} хлібу")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {Bottle_of_water} пляшок води")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {mana_potion} зілль мани")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {health_potion} зілль регенерації")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {latchkey} відмичок")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {lether} шкіри")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {wood} дерева")
    print(f"{STAT_AND_INVENTORI_COLOR}У вас {iron} злитків заліза")
    if wood_sword == True:
        print(f"{STAT_AND_INVENTORI_COLOR}У вас є дерев'яний меч")
    if iron_sword == True:
        print(f"{STAT_AND_INVENTORI_COLOR}У вас є залізний меч")
    if lether_armor == True:
        print(f"{STAT_AND_INVENTORI_COLOR}У вас є шкіряна броня")
    if iron_armor == True:
        print(f"{STAT_AND_INVENTORI_COLOR}У вас є залызна броня")
    if book_of_fire_ball == True:
        print(f"{STAT_AND_INVENTORI_COLOR}У вас є магія Вогняна куля")

def live_or_dead_check():
    if health <= 0:
        return True

def opening_the_lock(latchkey):
    if latchkey > 0:
        chance = random.randint(1, 2)
        if chance == 1:
            print(f"{TEXT_COLOR}Ви зламали замок.")           
        elif chance == 2:
            print(f"{TEXT_COLOR}У вас зламалась відмичка")
            latchkey -= 1
        return latchkey, chance
    else:
        print(f"{TEXT_COLOR}У вас нема відмичок")
        return latchkey, None
# latchkey, chance = opening_the_lock(latchkey)

while True:
    print(f"{TEXT_COLOR}Прокинувшись в старому домі ви вирішили оглянути його. Оглядаючи дім на полиці ви знайшли 2 хліба пляшку води та відмичку, в кутку кімнати стояв сундук на замці та двері які вели на вулицю.")
    bread += 2
    Bottle_of_water += 1
    latchkey += 1
    print(f"{TEXT_COLOR}Що оберете?")
    print(f"{CHOICE_COLOR}1: Вийти з дому\n2: Скористатися відмичкою та спробувати відкрити сундук\n3: Подивитись характеристику та відкрити інвентар")
    us_decis = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
    if us_decis == 1:
        print(f"{TEXT_COLOR}Ви виходите на вулицю")
    elif us_decis == 2:
        latchkey, chance = opening_the_lock(latchkey)
        if chance == 1:
            lether += 1
            bread += 1
            wood_sword = True
            print(f"{TEXT_COLOR}В сундуці ви знайшли шматок шкіри, 1 хліб і дерев'яний меч.")
        print(f"{TEXT_COLOR}Що оберете?")
        print(f"{CHOICE_COLOR}1: Вийти з дому\n2: Подивитись характеристику та відкрити інвентар")
        us_decis1 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
        if us_decis1 == 1:
            print(f"{TEXT_COLOR}Ви виходите на вулицю")
        elif us_decis1 == 2:
            open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey, wood_sword, iron_sword, lether_armor, iron_armor)
            print(f"{TEXT_COLOR}Ви виходите на вулицю")
    elif us_decis == 3:
        open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey, wood_sword, iron_sword, lether_armor, iron_armor)
        print(f"{TEXT_COLOR}Що оберете?")
        print(f"{CHOICE_COLOR}1: Вийти з дому\n2: Скористатися відмичкою та спробувати відкрити сундук")
        us_decis2 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
        if us_decis2 == 1:
            print(f"{TEXT_COLOR}Ви виходите на вулицю")
        elif us_decis2 == 2:
            latchkey, chance = opening_the_lock(latchkey)
            if chance == 1:
                lether += 2
                bread += 1
                wood_sword = True
                print(f"{TEXT_COLOR}В сундуці ви знайшли 2 шматки шкіри, 1 хліб і дерев'яний меч.")
                print(f"{TEXT_COLOR}Ви виходите на вулицю")
    print(f"{TEXT_COLOR}Вийшовши на вулицю вас зустрічає дуже гарний краєвид. Оглянувшись ви побачили поблизу дому верстак, підійшовши до нього ви знайшли залізний злиток та рецепти на яких було зображено як зробити дерев'яний меч та шкіряну броню.")
    iron += 1
    print(f"{TEXT_COLOR}Для того щоб зробити меч вам потрібно 3 дерева.\nДля того щоб зробити шкіряну броню вам потрібно 5  кусків шкіри.")
    print(f"{TEXT_COLOR}Відійовши далі від дому ви пішли по єдиній дорозі")
    print(f"{TEXT_COLOR}Через деякий час ви побачили пересувающися караван з продавцями")
    print(f"{TEXT_COLOR}Поки ви йшли ви трохи зголодніли")
    hunger -= 2
    health, stamina, hunger = state_check(health, stamina, hunger)
    print(f"{TEXT_COLOR}Ви відкрили інвентар")
    print(f"{CHOICE_COLOR}Ви можете з'їсти хліб який поповнить голод на 3 одиниці\nПопити води яка поповнить запас сил на 3\nВипити зілля життів яке відновить вам 10 життів\nВипити зілля мани яке поповнить вам 30 мани\nАбо нічого не робити.")
    print(f"{TEXT_COLOR}Що оберете?")
    while True:
        us_decis4 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
        if us_decis4 == "З'їсти хліб":
            if bread == 0:
                print(f"{TEXT_COLOR}У вас немає хлібу")
                continue
            num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
            while num > bread:
                print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                if num <= bread:
                    break
            bread -= num
            hunger += num * 3
            if hunger > 25:
                hunger = 25
            print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
        elif us_decis4 == "Випити води":
            if Bottle_of_water == 0:
                print(f"{TEXT_COLOR}У вас немає води")
                continue
            num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
            while num1 > Bottle_of_water:
                print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                if num1 <= Bottle_of_water:
                    break
            Bottle_of_water -= num1
            stamina += num1 * 3
            if stamina > 20:
                stamina = 20
            print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
        elif us_decis4 == "Випити зілля життів":
            if health_potion == 0:
                print(f"{TEXT_COLOR}У вас немає зілля життів")
                continue
            num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
            while num2 > health_potion:
                print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                if num2 <= health_potion:
                    break
            health_potion -= num2
            health += num2 * 10
            if health > 100:
                health = 100
            print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
        elif us_decis4 == "Випити зілля мани":
            if mana_potion == 0:
                print(f"{TEXT_COLOR}У вас немає зілля мани")
                continue
            num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
            while num3 > mana_potion:
                print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                if num3 <= mana_potion:
                    break
            mana_potion -= num3
            mana += num3 * 30
            if mana > 200:
                mana = 200
            print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
        elif us_decis4 == "Нічого не робити" or "Закрити інвентар":
            break
    print(f"{TEXT_COLOR}Ви закрили інвентар")
    print(f"{TEXT_COLOR}Що оберете?")
    print(f"{CHOICE_COLOR}1: Піти повз нього караван.\n2: Зайти до цього каравану та розпитати продавців про ціни та чи є в них для нас робота, бо грошей в нас немає.")
    us_decis2 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
    if us_decis2 == 2:
        print(f"{TEXT_COLOR}Зайшовши до каравану ви побачили продавця і вирішили підійти до нього")
        print(f"{CHOICE_COLOR}1: Подивитися що він продає\n2: Чи треба йому чимось допомогти")
        us_decis5 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
        if us_decis5 == 1:
            print(f"{TEXT_COLOR}--------Предмети на продаж--------\nХліб = 15 монет\nПляшка води = 20 монет\nЗілля поповнення життів = 100 монет\nЗілля поповнення мани = 100 монет\nДерево = 10 монет\nЗалізні злитки = 40 монет\nШкіра = 15 монет\nВідмички = 30 монет\nТом заклинань вогненна куля = 250 монет")
            while True:
                print(f"{TEXT_COLOR}Щоб вийти з магазину напишіть 'вихід'")
                print(f"{TEXT_COLOR}Що оберете?")
                us_decis6 = input(f"{INPUT_COLOR}Введіть що зробити: ")
                if us_decis6 == "Купити хліб":
                    num4 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num4 * 15 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num4 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num4 * 15:
                            break
                    bread += num4
                    money -= num4 * 15
                    print(f"{TEXT_COLOR}У вас {money} монет і {bread} хлібу")
                elif us_decis6 == "Купити воду":
                    num5 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num5 * 20 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num5 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num5 * 20:
                            break
                    Bottle_of_water += num5
                    money -= num5 * 20
                    print(f"{TEXT_COLOR}У вас {money} монет і {Bottle_of_water} бутилок води")
                elif us_decis6 == "Купити зілля життів":
                    num6 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num6 * 100 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num6 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num6 * 100:
                            break
                    health_potion += num6
                    money -= num6 * 100
                    print(f"{TEXT_COLOR}У вас {money} монет і {health_potion} зілль життів")
                elif us_decis6 == "Купити зілля мани":
                    num7 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num7 * 100 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num7 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num7 * 100:
                            break
                    mana_potion += num7
                    money -= num7 * 100
                    print(f"{TEXT_COLOR}У вас {money} монет і {mana_potion} зілль мани")
                elif us_decis6 == "Купити дерево":
                    num8 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num8 * 100 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num8 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num8 * 10:
                            break
                    wood += num8
                    money -= num8 * 10
                    print(f"{TEXT_COLOR}У вас {money} монет і {wood} дерева")
                elif us_decis6 == "Купити залізні злитки":
                    num9 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num9 * 40 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num9 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num9 * 40:
                            break
                    iron += num9
                    money -= num9 * 40
                    print(f"{TEXT_COLOR}У вас {money} монет і {iron} злитків заліза")
                elif us_decis6 == "Купити шкіру":
                    num10 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num10 * 15 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num10 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num10 * 15:
                            break
                    lether += num10
                    money -= num10 * 15
                    print(f"{TEXT_COLOR}У вас {money} монет і {lether} шкіри")
                elif us_decis6 == "Купити відмички":
                    num11 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    while num11 * 30 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num11 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num11 * 30:
                            break
                    latchkey += num11
                    money -= num11 * 30
                    print(f"{TEXT_COLOR}У вас {money} монет і {latchkey} відмичок")
                elif us_decis6 == "Купити том заклинань вогненна куля":
                    num13 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                    if money == 0:
                        print(f"{TEXT_COLOR}У вас немає грошей")
                        continue
                    if book_of_fire_ball == True:
                        print(f"{TEXT_COLOR}Ви не можете мати більше одного і того самого тому заклинань")
                        continue
                    while num13 * 250 > money:
                        print(f"{TEXT_COLOR}У вас недостатньо монет.")
                        num13 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money >= num13 * 250:
                            break
                    if num13 > 1:
                        print(f"{TEXT_COLOR}Ви не можете купити більше одного й того самого тому заклинань.")
                        continue
                    book_of_fire_ball = True
                    money -= num13 * 250
                    print(f"{TEXT_COLOR}У вас {money} монет і нове заклинання 'Вогняна куля: вона наносить 20 урону и витрачає 40 мани'")
                elif us_decis6 == "вихід":
                    break
        print(f"{TEXT_COLOR}Купець розповідає вам що вор вкрав в нього його щоденник і попросив повернути його, зрозуміло він вам заплатить за це. Купець розповів вам що вор заснував своє сховище у печері на сході.")
        print(f"{TEXT_COLOR}Що оберете?")
        print(f"{CHOICE_COLOR}1: Допомогти купцю\n2: Чи не допомагати")
        us_decis7 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
        if us_decis7 == 1:
            print(f"{TEXT_COLOR}Ви відправились до печери.\nОсь ви вже біля печери але ви дуже зголодніли і трохи втомилися")
            hunger -= 7
            stamina -= 3
            health, stamina, hunger = state_check(health, stamina, hunger)
            print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
            us_decis8 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі в печеру нічого не роблячи: ")
            if us_decis8 == "так":
                open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
                while True:
                    us_decis9 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
                    if us_decis9 == "З'їсти хліб":
                        if bread == 0:
                            print(f"{TEXT_COLOR}У вас немає хлібу")
                            continue
                        num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                        while num > bread:
                            print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                            num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                            if num <= bread:
                                break
                        bread -= num
                        hunger += num * 3
                        if hunger > 25:
                            hunger = 25
                        print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
                    elif us_decis9 == "Випити води":
                        if Bottle_of_water == 0:
                            print(f"{TEXT_COLOR}У вас немає води")
                            continue
                        num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num1 > Bottle_of_water:
                            print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                            num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num1 <= Bottle_of_water:
                                break
                        Bottle_of_water -= num1
                        stamina += num1 * 3
                        if stamina > 20:
                            stamina = 20
                        print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
                    elif us_decis9 == "Випити зілля життів":
                        if health_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля життів")
                            continue
                        num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num2 > health_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                            num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num2 <= health_potion:
                                break
                        health_potion -= num2
                        health += num2 * 10
                        if health > 100:
                            health = 100
                        print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
                    elif us_decis9 == "Випити зілля мани":
                        if mana_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля мани")
                            continue
                        num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num3 > mana_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                            num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num3 <= mana_potion:
                                break
                        mana_potion -= num3
                        mana += num3 * 30
                        if mana > 200:
                            mana = 200
                        print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
                    elif us_decis9 == "Закрити інвентар":
                        break
            health, stamina, hunger = state_check(health, stamina, hunger)
            print(f"{TEXT_COLOR}Ви зайшли до печери, пройшовши трохи в глиб бачите одного вора який сидить біля костра, вдача сьогодні не на вашій стороні і він вас побачив. Ви почали битися.")
            oponent_health = 50
            oponent_damage = 15 - base_armor
            if wood_sword == True:
                    base_damage += 5
            if iron_sword == True:
                base_damage -= 5 
            if iron_sword == True:
                base_damage += 20
            if lether_armor == True:
                base_armor += 3
                if iron_armor == True:
                    base_armor -= 3
            if iron_armor == True:
                base_armor += 7
            if book_of_fire_ball == True:
                if mana > 0:
                    base_damage += 20
            while oponent_health > 0:
                oponent_health -= base_damage
                print(f"{TEXT_COLOR}Ви напали та нанесли {base_damage} шкоди")
                health -= oponent_damage
                print(f"{TEXT_COLOR}Вор зробив свій хід і наніс вас {oponent_damage} шкоди")
            if live_or_dead_check():
                break
            health_potion += 2
            bread += 3
            Bottle_of_water += 4
            mana_potion += 1
            money += 400
            dairy = True
            stamina -= 2
            latchkey += 2
            health, stamina, hunger = state_check(health, stamina, hunger)
            print(f"{TEXT_COLOR}Ви вбили його, оглядаючи печеру ви знайшли 2 зілля життів, 3 хліба, 4 пляшки води, 1 зілля мани, мішечок з 400 золотими, 2 відмички і щоденник купця.")
            print(f"{TEXT_COLOR}Після битви ви втомилися і у вас залишилось {health} життів")
            print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
            us_decis10 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі нічого не роблячи: ")
            if us_decis10 == "так":
                open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
                while True:
                    us_decis11 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
                    if us_decis11 == "З'їсти хліб":
                        if bread == 0:
                            print(f"{TEXT_COLOR}У вас немає хлібу")
                            continue
                        num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                        while num > bread:
                            print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                            num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                            if num <= bread:
                                break
                        bread -= num
                        hunger += num * 3
                        if hunger > 25:
                            hunger = 25
                        print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
                    elif us_decis11 == "Випити води":
                        if Bottle_of_water == 0:
                            print(f"{TEXT_COLOR}У вас немає води")
                            continue
                        num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num1 > Bottle_of_water:
                            print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                            num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num1 <= Bottle_of_water:
                                break
                        Bottle_of_water -= num1
                        stamina += num1 * 3
                        if stamina > 20:
                            stamina = 20
                        print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
                    elif us_decis11 == "Випити зілля життів":
                        if health_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля життів")
                            continue
                        num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num2 > health_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                            num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num2 <= health_potion:
                                break
                        health_potion -= num2
                        health += num2 * 10
                        if health > 100:
                            health = 100
                        print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
                    elif us_decis11 == "Випити зілля мани":
                        if mana_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля мани")
                            continue
                        num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num3 > mana_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                            num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num3 <= mana_potion:
                                break
                        mana_potion -= num3
                        mana += num3 * 30
                        if mana > 200:
                            mana = 200
                        print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
                    elif us_decis11 == "Закрити інвентар":
                        break
            health, stamina, hunger = state_check(health, stamina, hunger)
            if live_or_dead_check():
                break
            hunger -= 4
            stamina -= 2
            health, stamina, hunger = state_check(health, stamina, hunger)
            print(f"{TEXT_COLOR}Повертатись вам було легше але ви всеодно втомились та зголодніли")
            print(f"{TEXT_COLOR}Ви повернулись до каравану та віддали щоденник купцю. за це він вам дав 300 золотих, 2 хліба, 2 залізних злитків та пляшку води.")
            money += 300
            bread += 2
            Bottle_of_water += 1
            iron += 2
            print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
            us_decis8 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі нічого не роблячи: ")
            if us_decis8 == "так":
                open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
                while True:
                    us_decis9 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
                    if us_decis9 == "З'їсти хліб":
                        if bread == 0:
                            print(f"{TEXT_COLOR}У вас немає хлібу")
                            continue
                        num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                        while num > bread:
                            print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                            num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                            if num <= bread:
                                break
                        bread -= num
                        hunger += num * 3
                        if hunger > 25:
                            hunger = 25
                        print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
                    elif us_decis9 == "Випити води":
                        if Bottle_of_water == 0:
                            print(f"{TEXT_COLOR}У вас немає води")
                            continue
                        num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num1 > Bottle_of_water:
                            print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                            num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num1 <= Bottle_of_water:
                                break
                        Bottle_of_water -= num1
                        stamina += num1 * 3
                        if stamina > 20:
                            stamina = 20
                        print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
                    elif us_decis9 == "Випити зілля життів":
                        if health_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля життів")
                            continue
                        num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num2 > health_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                            num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num2 <= health_potion:
                                break
                        health_potion -= num2
                        health += num2 * 10
                        if health > 100:
                            health = 100
                        print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
                    elif us_decis9 == "Випити зілля мани":
                        if mana_potion == 0:
                            print(f"{TEXT_COLOR}У вас немає зілля мани")
                            continue
                        num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        while num3 > mana_potion:
                            print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                            num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                            if num3 <= mana_potion:
                                break
                        mana_potion -= num3
                        mana += num3 * 30
                        if mana > 200:
                            mana = 200
                        print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
                    elif us_decis9 == "Закрити інвентар":
                        break
            print(f"{CHOICE_COLOR}1: Купити речі у купця\n2: Піти з каравану\n3: Спробувати щось викрасти у купця")
            us_decis12 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
            if us_decis12 == 3:
                print(f"{TEXT_COLOR}Купець поміти це та покликав охоронців і вони вас вбили.")
                break
            elif us_decis12 == 1:
                print(f"{TEXT_COLOR}--------Предмети на продаж--------\nХліб = 15 монет\nПляшка води = 20 монет\nЗілля поповнення життів = 100 монет\nЗілля поповнення мани = 100 монет\nДерево = 10 монет\nЗалізні злитки = 40 монет\nШкіра = 15 монет\nВідмички = 30 монет\nТом заклинань вогненна куля = 250 монет")
                while True:
                    print(f"{TEXT_COLOR}Щоб вийти з магазину напишіть 'вихід'")
                    print(f"{TEXT_COLOR}Що оберете?")
                    us_decis6 = input(f"{INPUT_COLOR}Введіть що зробити: ")
                    if us_decis6 == "Купити хліб":
                        num4 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num4 * 15 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num4 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num4 * 15:
                                break
                        bread += num4
                        money -= num4 * 15
                        print(f"{TEXT_COLOR}У вас {money} монет і {bread} хлібу")
                    elif us_decis6 == "Купити воду":
                        num5 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num5 * 20 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num5 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num5 * 20:
                                break
                        Bottle_of_water += num5
                        money -= num5 * 20
                        print(f"{TEXT_COLOR}У вас {money} монет і {Bottle_of_water} бутилок води")
                    elif us_decis6 == "Купити зілля життів":
                        num6 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num6 * 100 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num6 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num6 * 100:
                                break
                        health_potion += num6
                        money -= num6 * 100
                        print(f"{TEXT_COLOR}У вас {money} монет і {health_potion} зілль життів")
                    elif us_decis6 == "Купити зілля мани":
                        num7 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num7 * 100 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num7 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num7 * 100:
                                break
                        mana_potion += num7
                        money -= num7 * 100
                        print(f"{TEXT_COLOR}У вас {money} монет і {mana_potion} зілль мани")
                    elif us_decis6 == "Купити дерево":
                        num8 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num8 * 100 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num8 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num8 * 10:
                                break
                        wood += num8
                        money -= num8 * 10
                        print(f"{TEXT_COLOR}У вас {money} монет і {wood} дерева")
                    elif us_decis6 == "Купити залізні злитки":
                        num9 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num9 * 40 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num9 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num9 * 40:
                                break
                        iron += num9
                        money -= num9 * 40
                        print(f"{TEXT_COLOR}У вас {money} монет і {iron} злитків заліза")
                    elif us_decis6 == "Купити шкіру":
                        num10 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num10 * 15 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num10 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num10 * 15:
                                break
                        lether += num10
                        money -= num10 * 15
                        print(f"{TEXT_COLOR}У вас {money} монет і {lether} шкіри")
                    elif us_decis6 == "Купити відмички":
                        num11 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        while num11 * 30 > money:
                            print(f"{TEXT_COLOR}У вас недостатньо монет.")
                            num11 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                            if money >= num11 * 30:
                                break
                        latchkey += num11
                        money -= num11 * 30
                        print(f"{TEXT_COLOR}У вас {money} монет і {latchkey} відмичок")
                    elif us_decis6 == "Купити том заклинань вогненна куля":
                        num13 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        if money == 0:
                            print(f"{TEXT_COLOR}У вас немає грошей")
                            continue
                        if book_of_fire_ball == True:
                            print(f"{TEXT_COLOR}Ви не можете мати більше одного і того самого тому заклинань")
                            continue
                        while num13 > 1:
                            print(f"{TEXT_COLOR}Ви не можете купити більше одного й того самого тому заклинань.")
                            num13 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете купити: "))
                        book_of_fire_ball = True
                        money -= num13 * 250
                        print(f"{TEXT_COLOR}У вас {money} монет і нове заклинання 'Вогняна куля: вона наносить 20 урону и витрачає 40 мани'")
                    elif us_decis6 == "вихід":
                        break
                print(f"{CHOICE_COLOR}1: Піти з каравану\n2: Спробувати щось викрасти у купця")
                us_decis13 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
                if us_decis13 == 2:
                    print(f"{TEXT_COLOR}Купець помітив це та покликав охоронців і вони вас вбили.")
                    break
    print(f"{TEXT_COLOR}Вийшовши з каравану ви пішли далі, через деякий час ви побачили кузню, а біля неї сундук")
    print(f"{CHOICE_COLOR}1: Спробувати взломати його.\n2: Піти далі до кузні.")
    us_decis15 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
    if us_decis15 == 1:
        latchkey, chance = opening_the_lock(latchkey)
        while chance == 2:
            print(f"{TEXT_COLOR}Спробувати ще раз?")
            us_decis16 = input(f"{INPUT_COLOR}'так' або 'ні': ")
            if us_decis16 == "так":
                latchkey, chance = opening_the_lock(latchkey)
            elif us_decis16 == "ні":
                break
        if chance == 1:
            iron += 2
            wood += 1
            health_potion += 2
            print(f"{TEXT_COLOR}В сундуці ви знайшли 2 злитка заліза, 2 дерева та 3 шкіри.")
    print(f"{TEXT_COLOR}Пройшовши до кузні в ній ви знашли рецепти для крафту залізного меча і броні, 4 зілля відновлення життів, 2 зілля мани, 3 шкіри і 2 дерева.")
    health_potion += 2
    mana_potion += 2
    lether += 3
    wood += 2
    print(f"{TEXT_COLOR}Для того щоб зробити меч вам потрібно 2 залізних злитків.\nДля того щоб зробити залізну броню вам потрібно 5 залізних злитків.")
    print(f"{TEXT_COLOR}Ви виснажені та зголодніли бо дорога була не близька")
    hunger -= 4
    stamina -= 5
    health, stamina, hunger = state_check(health, stamina, hunger)
    print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
    us_decis10 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі нічого не роблячи: ")
    if us_decis10 == "так":
        open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
        while True:
            us_decis11 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
            if us_decis11 == "З'їсти хліб":
                if bread == 0:
                    print(f"{TEXT_COLOR}У вас немає хлібу")
                    continue
                num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                while num > bread:
                    print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                    num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                    if num <= bread:
                        break
                bread -= num
                hunger += num * 3
                if hunger > 25:
                    hunger = 25
                print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
            elif us_decis11 == "Випити води":
                if Bottle_of_water == 0:
                    print(f"{TEXT_COLOR}У вас немає води")
                    continue
                num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                while num1 > Bottle_of_water:
                    print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                    num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    if num1 <= Bottle_of_water:
                        break
                Bottle_of_water -= num1
                stamina += num1 * 3
                if stamina > 20:
                    stamina = 20
                print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
            elif us_decis11 == "Випити зілля життів":
                if health_potion == 0:
                    print(f"{TEXT_COLOR}У вас немає зілля життів")
                    continue
                num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                while num2 > health_potion:
                    print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                    num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    if num2 <= health_potion:
                        break
                health_potion -= num2
                health += num2 * 10
                if health > 100:
                    health = 100
                print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
            elif us_decis11 == "Випити зілля мани":
                if mana_potion == 0:
                    print(f"{TEXT_COLOR}У вас немає зілля мани")
                    continue
                num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                while num3 > mana_potion:
                    print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                    num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    if num3 <= mana_potion:
                        break
                mana_potion -= num3
                mana += num3 * 30
                if mana > 200:
                    mana = 200
                print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
            elif us_decis11 == "Закрити інвентар":
                break
    print(f"{CHOICE_COLOR}Ви можете зробити\n1: Дерев'яний меч\n2: Шкіряну броню\n3: Залізний меч\n4: Залізну броню")
    while True:
        print(f"{TEXT_COLOR}Щоб вийти напишіть 'вихід'.")
        us_decis14 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
        if us_decis14 == 1:
            if wood >= 3:
                wood_sword = True
                print(f"{TEXT_COLOR}Ви зробили дерев'яний меч")
            else:
                print(f"{TEXT_COLOR}У вас недостатньо дерева")
            continue
        elif us_decis14 == 2:
            if lether >= 5:
                lether_armor = True
                print(f"{TEXT_COLOR}Ви зробили шкіряну броню")
            else:
                print(f"{TEXT_COLOR}У вас недостатньо шкіри")
            continue
        elif us_decis14 == 3:
            if iron >= 3:
                iron_sword = True
                print(f"{TEXT_COLOR}Ви зробили залізний меч")
            else:
                print(f"{TEXT_COLOR}У вас недостатньо заліза")
            continue
        elif us_decis14 == 4:
            if iron >= 3:
                iron_armor = True
                print(f"{TEXT_COLOR}Ви зробили залізну броню")
            else:
                print(f"{TEXT_COLOR}У вас недостатньо заліза")
            continue
        elif us_decis14 == "вихід":
            break
    print(f"{TEXT_COLOR}Після того як ви закінчили крафтити на вас з кущів напав скелет")
    oponent_health1 = 200
    oponent_armor1 = 5
    if wood_sword == True:
        base_damage += 5
        if iron_sword == True:
            base_damage -= 5 
    if iron_sword == True:
        base_damage += 20
    if lether_armor == True:
        base_armor += 3
        if iron_armor == True:
            base_armor -= 3
    if iron_armor == True:
        base_armor += 7
    base_damage -= oponent_armor1
    oponent_damage1 = 15 - base_armor
    while oponent_health1 > 0:
        if book_of_fire_ball == True and mana > 0 and not fireball_buff_applied == True:
            base_damage += 20
            fireball_buff_applied = True
        if mana > 0:
            mana -= 40
        if mana <= 0 and not mana_debuff_applied == True:
            base_damage -= 20 
            mana_debuff_applied = True
        oponent_health1 -= base_damage
        print(f"{TEXT_COLOR}Ви напали та нанесли {base_damage} шкоди")
        if oponent_health1 <= 0:
            print(f"{TEXT_COLOR}Вы перемогли ворога!")
            break
        health -= oponent_damage1
        print(f"{TEXT_COLOR}Вор зробив свій хід і наніс вам {oponent_damage1} шкоди")
        if live_or_dead_check():
            print(f"{LOSE_COLOR}В вас закінчили житті, ви програли.")
            quit()
    stamina -= 5
    health, stamina, hunger = state_check(health, stamina, hunger)
    print(f"{TEXT_COLOR}Після битви ви втомилися і у вас залишилось {health} життів, і втратили багато сил")
    print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
    us_decis10 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі нічого не роблячи: ")
    if us_decis10 == "так":
            open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
            while True:
                us_decis11 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
                if us_decis11 == "З'їсти хліб":
                    if bread == 0:
                        print(f"{TEXT_COLOR}У вас немає хлібу")
                        continue
                    num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                    while num > bread:
                        print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                        num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                        if num <= bread:
                            break
                    bread -= num
                    hunger += num * 3
                    if hunger > 25:
                        hunger = 25
                    print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
                elif us_decis11 == "Випити води":
                    if Bottle_of_water == 0:
                        print(f"{TEXT_COLOR}У вас немає води")
                        continue
                    num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num1 > Bottle_of_water:
                        print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                        num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num1 <= Bottle_of_water:
                            break
                    Bottle_of_water -= num1
                    stamina += num1 * 3
                    if stamina > 20:
                        stamina = 20
                    print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
                elif us_decis11 == "Випити зілля життів":
                    if health_potion == 0:
                        print(f"{TEXT_COLOR}У вас немає зілля життів")
                        continue
                    num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num2 > health_potion:
                        print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                        num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num2 <= health_potion:
                            break
                    health_potion -= num2
                    health += num2 * 10
                    if health > 100:
                        health = 100
                    print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
                elif us_decis11 == "Випити зілля мани":
                    if mana_potion == 0:
                        print(f"{TEXT_COLOR}У вас немає зілля мани")
                        continue
                    num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num3 > mana_potion:
                        print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                        num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num3 <= mana_potion:
                            break
                    mana_potion -= num3
                    mana += num3 * 30
                    if mana > 200:
                        mana = 200
                    print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
                elif us_decis11 == "Закрити інвентар":
                    break
    print(f"{TEXT_COLOR}Обшукуючи скелет в його сумці ви побачили записку на якій було сказано що на заході знаходиться логово демону і якщо перемогти його то ти отримаєш повну владу над світом.")
    print(f"{TEXT_COLOR}Ви пішли туди. На ваше здивування ви дібралися швидко.")
    print(f"{TEXT_COLOR}Ти опинився перед масивними дверима входу у печеру. На ній три сталеві стрілки, кожна з яких може повернутися в один із чотирьох напрямків. На стіні поруч із дверима вибито старе послання:\n'Коли сонце сходить, світ оживає.\nКоли ніч опускається, тіні подовжуються.\nВітер з півдня несе тепло, але північний холод його перемагає.\nА минуле завжди залишається позаду…'")
    us_decis17 = input(f"{INPUT_COLOR}Введіть напрямок першої стрілки.")
    if us_decis17 == "Вправо":
        print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали")               
    else:
        while us_decis17 != "Вправо":
            health -= 5
            if live_or_dead_check():
                print(f"{LOSE_COLOR}В вас закінчили житті, ви програли.")
                quit()
            print(f"{TEXT_COLOR}Напрямок введено неправельно")
            us_decis17 = input(f"{INPUT_COLOR}Введіть правильний напрямок першої стрілки.")
            if us_decis17 == "Вправо":
                print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали") 
                break
    us_decis18 = input(f"{INPUT_COLOR}Введіть напрямок другої стрілки.")
    if us_decis18 == "Вліво":
        print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали")               
    else:
        while us_decis18 != "Вліво":
            health -= 5
            if live_or_dead_check():
                print(f"{LOSE_COLOR}В вас закінчили житті, ви програли.")
                quit()
            print(f"{TEXT_COLOR}Напрямок введено неправельно")
            us_decis17 = input(f"{INPUT_COLOR}Введіть правильний напрямок другої стрілки.")
            if us_decis18 == "Вліво":
                print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали") 
                break
    us_decis19 = input(f"{INPUT_COLOR}Введіть напрямок третьої стрілки.")
    if us_decis19 == "Вверх":
        print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали")               
    else:
        while us_decis19 != "Вверх":
            health -= 5
            if live_or_dead_check():
                print(f"{LOSE_COLOR}В вас закінчили житті, ви програли.")
                quit()
            print(f"{TEXT_COLOR}Напрямок введено неправельно")
            us_decis19 = input(f"{INPUT_COLOR}Введіть правильний напрямок третьої стрілки.")
            if us_decis19 == "Вверх":
                print(f"{TEXT_COLOR}Стрілка заїхала в стіну і більше не рушиться, ви вгадали") 
                break
    print(f"{CHOICE_COLOR}Відкрити інвентар та статистику?")
    us_decis10 = input(f"{INPUT_COLOR}Введіть 'так' якщо відкрити 'ні' якщо піти далі нічого не роблячи: ")
    if us_decis10 == "так":
            open_status_inventori(money, health, stamina, hunger, mana, bread, lether, wood, iron, Bottle_of_water, mana_potion, health_potion, latchkey,wood_sword, iron_sword, lether_armor, iron_armor)
            while True:
                us_decis11 = input(f"{INPUT_COLOR}Напишіть що зробити: ")
                if us_decis11 == "З'їсти хліб":
                    if bread == 0:
                        print(f"{TEXT_COLOR}У вас немає хлібу")
                        continue
                    num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                    while num > bread:
                        print(f"{TEXT_COLOR}У вас недостатньо хліба.")
                        num = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете з'їсти: "))
                        if num <= bread:
                            break
                    bread -= num
                    hunger += num * 3
                    if hunger > 25:
                        hunger = 25
                    print(f"{TEXT_COLOR}У вас {hunger} ситості і {bread} хлібу")
                elif us_decis11 == "Випити води":
                    if Bottle_of_water == 0:
                        print(f"{TEXT_COLOR}У вас немає води")
                        continue
                    num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num1 > Bottle_of_water:
                        print(f"{TEXT_COLOR}У вас недостатньо бутилок води.")
                        num1 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num1 <= Bottle_of_water:
                            break
                    Bottle_of_water -= num1
                    stamina += num1 * 3
                    if stamina > 20:
                        stamina = 20
                    print(f"{TEXT_COLOR}У вас {stamina} енергії і {Bottle_of_water} бутилок води")
                elif us_decis11 == "Випити зілля життів":
                    if health_potion == 0:
                        print(f"{TEXT_COLOR}У вас немає зілля життів")
                        continue
                    num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num2 > health_potion:
                        print(f"{TEXT_COLOR}У вас недостатньо зілль життів.")
                        num2 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num2 <= health_potion:
                            break
                    health_potion -= num2
                    health += num2 * 10
                    if health > 100:
                        health = 100
                    print(f"{TEXT_COLOR}У вас {health} життів і {health_potion} зілль життів")
                elif us_decis11 == "Випити зілля мани":
                    if mana_potion == 0:
                        print(f"{TEXT_COLOR}У вас немає зілля мани")
                        continue
                    num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                    while num3 > mana_potion:
                        print(f"{TEXT_COLOR}У вас недостатньо зілль мани.")
                        num3 = int(input(f"{INPUT_COLOR}Введіть кількість яку хочете випити: "))
                        if num3 <= mana_potion:
                            break
                    mana_potion -= num3
                    mana += num3 * 30
                    if mana > 200:
                        mana = 200
                    print(f"{TEXT_COLOR}У вас {mana} мани і {mana_potion} зілль мани")
                elif us_decis11 == "Закрити інвентар":
                    break
    print(f"{TEXT_COLOR}Зайшовши до печери ви бачите чийсь склеп")
    print(f"{CHOICE_COLOR}1: Підійти до склепу\n2: піти звідси бо тут дуже підозріло")
    us_decis20 = int(input(f"{INPUT_COLOR}Введіть номер вашого вибору: "))
    if us_decis20 == 1:
        print(f"{TEXT_COLOR}Підійшовши до склепу і відкривши його звідти виліз скелет, він був весь в артифактах і виглядав дуже сильно")
        print(f"{TEXT_COLOR}Він вбив вас з обного заклинання")
        break
    elif us_decis20 == 2:
        print(f"{TEXT_COLOR}Вийшовши з печери ви пішли далі досліджувати простори цього світу. Під час вашої мандрівки ви знову зустріли мандруючий караван, і поговорив з тим торговцем ви дізнались що якщо б ви відкрили тот склеп вас би прокляли і ви заняли б місце того скелето до того моменту як такий самий мандрівник як ви не прийшов би досліджувати цю печеру.")            
        print(f"{WIN_COLOR}Вы перемогли і далі жили в цьому світі де майже кожен день бились з якимись монстрами і ставали все сильніше і сильніше")
        quit()
                
                
                
print(f"{LOSE_COLOR}В вас закінчили житті, ви програли.")