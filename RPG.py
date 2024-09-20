from time import sleep
# from math import floor
# Ascend Tower, fight 9 waves of enemies until you reach the top. Boss every 3rd, Final Boss layer 10


def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.1)
    print()


def confirmation(repeat):
    x = repeat
    print("")
    confirm = input()
    while confirm not in ("Y", "y", "N", "n"):
        confirm = input("Try again: \n")
    if confirm == "Y":
        x = False
    elif confirm == "y":
        x = False
    return x


def level_up(stats, stat_points):
    x = stats
    p = stat_points
    while p != 0:
        print("\nThese are your current stats:  * LVL -- ", stats[0], " *")
        print("                                 HP  -- ", stats[1], "/", stats[2], )
        print("                                 Att -- ", stats[3])
        print("                                 Def -- ", stats[4])
        print("                                 Spd -- ", stats[5])
        print("Points Remaining: ", p)
        print("Select which stat you'd like to increase: \n")
        print("1. Max HP, 2. Attack, 3. Defense, 4. Speed")

        y = input()
        y = int(y)
        while y not in range(1, 5):
            y = input("Try again: ")
            y = int(y)
        if y == 1:
            stats[2] = stats[2] + 1
            stats[1] = stats[2]
        elif y == 2:
            stats[3] = stats[3] + 1
        elif y == 3:
            stats[4] = stats[4] + 1
        elif y == 4:
            stats[5] = stats[5] + 1
        p = p - 1
    print("\nThese are your current stats:  * LVL -- ", stats[0], " *")
    print("                                 HP  -- ", stats[1], "/", stats[2], )
    print("                                 Att -- ", stats[3])
    print("                                 Def -- ", stats[4])
    print("                                 Spd -- ", stats[5])
    print("Points Remaining: 0")
    return x, p


def main_menu():
    print(" ")
    print("             ====Welcome to RPG====")
    print(" ")
    print("1. Start Game")
    print("2. Exit")
    start_option = input()
    try:
        start_option = int(start_option)
    except ValueError:
        print("That wasn't a number")
        start_option = 0

    while start_option not in range(1, 2):
        print("Try Again: ")
        start_option = input()
        try:
            start_option = int(start_option)
        except ValueError:
            print("If it's not a number you'll crash the game.")
            start_option = input()
            start_option = int(start_option)
    if start_option == 1:
        running = True
        # not used, will add later
    elif start_option == 2:
        print("Ending Program")
        exit()


def checkpoint():
    print("???:'Would you like to continue or exit the game?'\n             *Progress will not be saved*")
    sleep(2)
    print("1. Continue    2. Quit")
    y = input()
    y = int(y)
    while y not in range(1, 3):
        y = input("Try again: ")
        y = int(y)
    if y == 1:
        return
    elif y == 2:
        exit()


def game_start():
    print(" ")
    print("             ====Welcome to RPG====")
    print(" ")
    repeat = True
    global player_name
    global player_class
    global player_class_num
    player_name = input("Enter Name:  ")
    class_list = ("1. Mercenary", "2. Hunter", "3. Assassin", "4. Enchanter", "5. Plague Doctor", "6. Summoner")
    while repeat:
        player_class = "Blank"
        print(" ")
        print(class_list)
        print(" ")
        player_class_num = input(player_name + ", Select a class:  ")
        player_class_num = int(player_class_num)
        while player_class == "Blank":
            if player_class_num in range(1, 7):
                player_class = class_list[player_class_num - 1]
                player_class = player_class[3:]
            else:
                print("wrong input, try again")
                player_class_num = input()
                player_class_num = int(player_class_num)

        print("\nWelcome to RPG " + player_name + ", you have chosen " + player_class + ", correct? (Y/N)")
        repeat = confirmation(repeat)
        print("")


def combat(stats, enemy_stats):
    print("")
    print("==== Begin Combat====\n                                                (:<")
    # rng damage?
    in_combat = True
    player = stats
    enemy = enemy_stats
    resource_amount = 0

#    if player_class_num == 1:
#        mercenary_intro()
#    elif player_class_num == 2:            Might need later for combat
#        hunter_intro()
#    elif player_class_num == 3:
#        assassin_intro()
#    elif player_class_num == 4:
#        enchanter_intro()
#    elif player_class_num == 5:
#        print("plague in combat")
#    elif player_class_num == 6:
#        summoner_intro()

    # if player_class_num == 6:
    #    print(stats)
    # player[3] = player[2]/3
    #   print(player[3])
    #  round(player[3])
    # print(player[3])
    # floor(player[3])
    # print(player[3])
    # print(player)
    # print(stats)
    # input("good? ")


    while in_combat:
        print("-----------------------------------------------------------------------------------------------------"
              "\nCombat Menu:                           Your HP: ", player[1], "        Enemy HP: ", enemy[1])
        print("")
        print("Your Abilities:   1. " + ability1 + "   2. " + ability2 + "   "
              "3. " + ability3 + "       " + resource + " available: ", resource_amount)
        print("")
        confirm = input("   Select an Option: ")
        confirm = int(confirm)
        while confirm not in (1, 2, 3):
            confirm = input("   Try again: ")

        if player[5] <= enemy[5]:                           # Enemy attacking first if faster
            hp_turn = player[1]
            player[1] = player[1] - (2 * enemy[3]) + player[4]
            if hp_turn < player[1]:
                player[1] = hp_turn
            their_damage = hp_turn - player[1]
            sleep(1)
            print("")
            print("Enemy damage done:", their_damage)
            if player[1] <= 0:
                print("\n==============")
                print("=  You Lose  =")
                print("==============")
                print("\nSorry " + player_name + " the " + player_class + ", ??? didn't save you. . .")
                exit()

        if confirm == 1:                                # You attacking
            hp_turn = enemy[1]
            enemy[1] = enemy[1] - (ability1_damage + player[3]) + enemy[4]
            if hp_turn < enemy[1]:
                enemy[1] = hp_turn
            your_damage = hp_turn - enemy[1]
            print("\n You use ", ability1)
            sleep(1)
            print("")
            print("Damage done: ", your_damage)
            resource_amount = resource_amount + 10

        elif confirm == 2:
            if ability2_damage < 0:
                player[1] = player[1] - ability2_damage
                print("\nYou use ", ability2)
                sleep(1)
                print("\nYou healed yourself for ", abs(ability2_damage), " HP.")
                if player[1] > player[2]:
                    player[1] = player[2]
            else:
                hp_turn = enemy[1]
                enemy[1] = enemy[1] - (ability2_damage + player[3]) + enemy[4]
                if hp_turn < enemy[1]:
                    enemy[1] = hp_turn
                your_damage = hp_turn - enemy[1]
                sleep(1)
                print("\nYou use ", ability2)
                print("")
                print("Damage done: ", your_damage)

        elif confirm == 3:
            hp_turn = enemy[1]
            enemy[1] = enemy[1] - (ability3_damage + player[3]) + enemy[4]
            if hp_turn < enemy[1]:
                enemy[1] = hp_turn
            your_damage = hp_turn - enemy[1]
            sleep(1)
            print("\nYou use ", ability3)
            sleep(1)
            print("\nDamage done: ", your_damage)

        if enemy[1] <= 0:
            print("\n==============")
            print("=  You  Win  =")
            print("==============")
            stats[0] = stats[0] + 1
            stats[1] = stats[2]
            break

        if player[5] > enemy[5]:                            # Enemy attacking second if slower
            hp_turn = player[1]
            player[1] = player[1] - (2 * enemy[3]) + player[4]
            if hp_turn < player[1]:
                player[1] = hp_turn
            their_damage = hp_turn - player[1]
            print("")
            print("Enemy damage done: ", their_damage)
            print("")
            if player[1] <= 0:
                print("\n==============")
                print("=  You Lose  =")
                print("==============")
                print("\nSorry " + player_name + " the " + player_class + ", ??? didn't save you. . .")
                exit()
        sleep(2)


def mercenary_intro():
    # weapon: Great swords/Axes
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    repeat = True
    x = 0
    weapon = "Great Sword"
    ability1 = "Impale"
    ability2 = "Bolster"        # Raise Defense by 2, Attack by 1
    ability3 = "Overwhelm"
    resource = "Rage"
    ability1_damage = 1
    ability2_damage = 0
    ability3_damage = 8
    while repeat:
        print(
            "You are a " + player_class + " - equipped with a " + weapon + ", your abilities are " + ability1
            + ", " + ability2 + ", and " + ability3 + ".\n"
            "Your resource is " + resource + ", generated from your primary ability - " + ability1 +
            ".\n" + ability2 + " increases your Defense by 2 and Attack by 1, costing 10 " + resource
            + ".\n" + ability3 + " is your finisher, dealing a large amount of damage for 30 " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 2:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        # Count variable, closes game after 3 attempts
        # (Add to the earlier function, not in each intro.)


def hunter_intro():
    print("you are hunter >>>>>----------------------->")
    # Big Buck in the distance
    # Snap! Branch! Bird!, tutorial to shoot the bird
    # weapon: Longbow/Axes
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    repeat = True
    x = 0
    weapon = "Longbow"
    ability1 = "Shoot"
    ability2 = "Rapid Fire"
    ability3 = "Volley"
    resource = "Focus"
    ability1_damage = 1
    ability2_damage = 4
    ability3_damage = 5
    while repeat:
        print(
            "You are a " + player_class + " - equipped with a " + weapon + ", your abilities are " + ability1
            + ", " + ability2 + ", and " + ability3 + ".\n"
            "Your resource is " + resource + ", generated from your primary ability.\n" + ability1 +
            " will generate " + resource + " while " + ability2 + " and "
            + ability3 + " will consume " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 2:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        # Count variable, closes game after 3 attempts


def assassin_intro():
    print("you are assassin --\═══>")
    #weapon: /Daggers
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    x = 0
    repeat = True
    weapon = "Dual Daggers"
    ability1 = "Stab"
    ability2 = "Eviscerate"
    ability3 = "Shadow Strike"
    resource = "Energy"
    ability1_damage = 1
    ability2_damage = 4
    ability3_damage = 5
    while repeat:
        print(
            "You are a " + player_class + " - equipped with " + weapon + ", your abilities are " + ability1 + ", " + ability2 + ", and " + ability3 + ".\n"
            "Your resource is " + resource + ", generated from your primary ability.\n" + ability1 +
            " will generate " + resource + " while " + ability2 + " and " + ability3 + " will consume " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 2:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        # Count variable, closes game after 3 attempts


def enchanter_intro():
    print("you are enchanter")
    #weapon: Wands/Staff
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    x = 0
    repeat = True
    weapon = "Wand"
    ability1 = "Arcane Bolt"
    ability2 = "Runic Power"
    ability3 = "Elemental Blast"
    resource = "Mana"
    ability1_damage = 1
    ability2_damage = 4
    ability3_damage = 5
    while repeat:
        print(
            "You are a " + player_class + " - equipped with a " + weapon + ", your abilities are " + ability1 + ", " + ability2 + ", and " + ability3 + ".\n"
                                                                                                                                                                  "Your resource is " + resource + ", generated from your primary ability.\n" + ability1 +
            " will generate " + resource + " while " + ability2 + " and " + ability3 + " will consume " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 2:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        # Count variable, closes game after 3 attempts


def plague_doctor_intro():
    #weapon: Crossbow/Daggers
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    x = 0
    repeat = True
    weapon = "Crossbow"
    ability1 = "Toxic Arrow"  # Fire an arrow coated with poison at enemy
    ability2 = "Self-Medicate"  # Consume resource to heal yourself
    ability3 = "Unkindness"  # Means a flock of ravens - Birds afflict enemy with plague
    resource = "Noxious Vapor"
    ability1_damage = 1
    ability2_damage = -4
    ability3_damage = 5
    while repeat:
        print("You are a " + player_class +" - equipped with a " + weapon + ", your abilities are " + ability1 + ", " + ability2 + ", and " + ability3 + ".\n"
              "Your resource is " + resource + ", generated from your primary ability.\n" + ability1 +
              " will generate " + resource + " while "+ ability2 + " and " + ability3 + " will consume " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 2:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        #Count variable, closes game after 3 attempts


def summoner_intro():
    print("you are summoner")
    #weapon: Tomes/Staff
    global weapon
    global ability1
    global ability1_damage
    global ability2
    global ability2_damage
    global ability3
    global ability3_damage
    global resource
    x = 0
    repeat = True
    weapon = "Tome"
    ability1 = "Imp"
    ability2 = "Demon"
    ability3 = "idk"
    resource = "Insanity"
    ability1_damage = 1
    ability2_damage = 4
    ability3_damage = 5
    while repeat:
        print(
            "You are a " + player_class + " - equipped with a " + weapon + ", your abilities are " + ability1 + ", " + ability2 + ", and " + ability3 + ".\n"
                                                                                                                                                                  "Your resource is " + resource + ", generated from your primary ability.\n" + ability1 +
            " will generate " + resource + " while " + ability2 + " and " + ability3 + " will consume " + resource + ".")

        print("\n      Understood? Y/N")
        repeat = confirmation(repeat)
        if repeat:
            print("\n???\n")
            x = x + 1
        if x == 3:
            print_slow("\n User Error Detected: Closing Program")
            sleep(0.5)
            exit()
        # Count variable, closes game after 3 attempts


def floor_1(stats):
    print("First Fight")
    print("")
    sleep(1)
    print_slow(".    .    .")
    sleep(1)
    enemy_stats = [1, 12, 12, 2, 1, 1]
    combat(stats, enemy_stats)

def floor_2(stats):
    print("2nd floor")
    print("")
    sleep(1)
    print_slow("\n.    .    .")
    sleep(1)
    enemy_stats = [2, 14, 14, 3, 1, 2]
    combat(stats, enemy_stats)


main_menu()
player_name = "Blank"
player_class_num = 10
player_class = "Blank"
game_start()
stat_points = 0
weapon = "sword"
ability1 = ""
ability1_damage = 0
ability2 = ""
ability2_damage = 0
ability3 = ""
ability3_damage = 0
resource = ""
stats = [1, 10, 10, 1, 1, 1]

if player_class_num == 1:       #Slightly higher att/def
    stats = [1, 10, 10, 2, 2, 1]
    mercenary_intro()
elif player_class_num == 2:     #Slightly lower hp, high att
    stats = [1, 8, 8, 3, 1, 1]
    hunter_intro()
elif player_class_num == 3:     #High speed, low def
    stats = [1, 10, 10, 1, 0, 3]
    assassin_intro()
elif player_class_num == 4:     #High attack, low defense
    stats = [1, 9, 9, 3, 0, 1]
    enchanter_intro()
elif player_class_num == 5:     #Slightly higher hp/att
    stats = [1, 12, 12, 2, 1, 1]
    plague_doctor_intro()
elif player_class_num == 6:     #High hp, low attack - minion damage scales based on health
    stats = [1, 16, 16, 0, 1, 1]
    summoner_intro()
else:
    print("Error")

print("Welcome to RPG " + player_name + "!\n\n")

print("These are your current stats:  * LVL -- ", stats[0], " *")
print("                                 HP  -- ", stats[1],"/",stats[2],)
print("                                 Att -- ", stats[3])
print("                                 Def -- ", stats[4])
print("                                 Spd -- ", stats[5])
print("")

sleep(3)
print("???: 'Hey " + player_name + "'")
sleep(3)
print_slow("???: 'First fight:'")
print("")
sleep(2)

floor_1(stats)
print("")
sleep(2)
print("???: 'Congratulations on clearing the first floor!'")
print("")
sleep(2)
print("???: 'You've reached level ", stats[0], "! spend points to increase your stats!\n")
sleep(2)
stat_points = stat_points + 3
stats, stat_points = level_up(stats, stat_points)

checkpoint()

print("\n???: 'Alright next floor!'")
print("Don't forget to add rng to combat")
sleep(5)

floor_2(stats)

print("")
sleep(2)
print("???: 'Congratulations on clearing the second floor!'")
print("")
sleep(2)
print("???: 'You've reached level ", stats[0], "! spend points to increase your stats\n")
sleep(2)
stat_points = stat_points + 3
stats, stat_points = level_up(stats, stat_points)
