import random
import time
from Games import player_data
from Games import mob_data
from Games import items_data


def line():
    print("---" * 7)


def newline():
    print("\n")


def default_names():
    names = ["Charles", "Ayabee", "Caleb"]
    RNG = random.randint(1, len(names))
    return names[RNG - 1]


def delay_msg(msg, delay):
    msg_array = msg.split()
    for i in range(len(msg_array)):
        print(msg_array[i - 1])
        time.sleep(delay)


def sleep(delay):
    time.sleep(delay)


def choices_norm():
    loop_over = False
    while not loop_over:
        print("What do you want to do?")
        print("1) Explore")
        print("2) Hint")
        print("3) Pause")
        print("4) Craft")
        print("5) Check Inventory")
        choice = input("Choose one: ")
        if choice == "1":
            return "explore"
            loop_over = True
        elif choice == "2":
            return "hint"
            loop_over = True
        elif choice == "3":
            return "pause"
            loop_over = True
        elif choice == "4":
            pass
        elif choice == "5":
            for i in range(len(player_data.inventory)):
                print(player_data.inventory[i])
        else:
            choice = input("Please choose a valid option.(1, 2, 3): ")


def quit_fn():
    print("1) New Game")
    f = open("save.txt", "r")
    g = f.readline()
    x = g.split(".")
    if len(x) > 0:
        print("2) Continue")
    print("3) Quit")
    ans = input("Enter a number!: \n")
    if ans == "1":
        print("New Game starting!")
        return 1
    elif ans == "2":
        f = open("save.txt", "r")
        g = f.readline()
        x = g.split(".")
        if len(x) > 0:
            print("Continuing!")
            return 2
        else:
            print("New Game starting!")
            return 1
    else:
        print("Bye!")
        return 3


def intro():
    print("Welcome...")
    sleep(0.5)
    print("Welcome...")
    delay_msg(". . .", 0.5)
    sleep(0.5)
    print("What... is your name?")
    print("(Enter 'idk' if you want a default name)")
    name = input("Enter your name: ")
    if name == "idk":
        player_data.current_data["name"] = default_names()
    else:
        player_data.current_data["name"] = name
    print("Oh yes, " + player_data.current_data["name"] + ", Of course!")
    print("Welcome, " + player_data.current_data["name"] + "!")
    print("I was just joking, of course, I knew your name, " + player_data.current_data["name"])
    sleep(0.5)
    print("Now, you might be wandering where you are...")
    sleep(0.5)
    print("Well...")
    delay_msg(". . .", 0.5)
    print("Your'e kind of in a jungle...")
    sleep(0.5)
    print("You have to get back home")
    sleep(0.5)
    print("With my help I guess...")
    sleep(0.5)
    print("I did not intend this...")
    delay_msg(". . . ", 1)
    print("Anyways!")
    sleep(0.5)
    print("You should probably get going!")
    sleep(0.5)
    print("I'll be here if you need me!")
    sleep(0.5)
    print("Just ask for a hint!")


def init():
    print("You wake up...")
    player_data.current_data["zone"] = "jungle"
    sleep(0.5)
    print("The voice was right! You are in a jungle!")
    sleep(0.5)
    print("You probably should asked who he is...")
    sleep(0.5)
    print("Oh well")
    print("Let's get going, I guess")


def pause_mn():
    pass


def dmg_taken(att, defence):
    if att - (defence / 2) > 1:
        dmg = att - (defence / 2)
    else:
        dmg = 1
    return dmg


def lvl_up():
    exp_inc = player_data.current_data["lvl"] * 150
    return exp_inc


def lvl_add():
    if player_data.current_data["exp"] + mob_data.current_mob_data["exp_drop"] >= (
            player_data.current_data["lvl"] * 150):
        player_data.current_data["exp"] += mob_data.current_mob_data["exp_drop"]
        player_data.current_data["exp"] -= (player_data.current_data["lvl"] * 150)
        player_data.current_data["lvl"] += 1
    else:
        player_data.current_data["exp"] += mob_data.current_mob_data["exp_drop"]


def att_or_not():
    lvl = player_data.current_data["lvl"]
    dtm = lvl * random.random()
    return dtm


def check():
    mob_health = mob_data.current_mob_data["hp"]
    mob_def = mob_data.current_mob_data["def"]
    mob_att = mob_data.current_mob_data["att"]
    player_health = player_data.current_data["hp"]
    player_def = player_data.current_data["def"]
    player_att = player_data.current_data["att"]
    line()
    print("The {} has {} health".format(mob_data.current_mob_data["name"], mob_health))
    print("The {} has {} defence".format(mob_data.current_mob_data["name"], mob_def))
    print("The {} has {} attack strength".format(mob_data.current_mob_data["name"], mob_att))
    line()
    print("You have {} health".format(player_health))
    print("You have {} defence".format(player_def))
    print("You have {} attack strength".format(player_att))
    line()


def flee_fn():
    if mob_data.current_mob_data["hp"] * player_data.current_data["lvl"] <= 0:
        exp_loss = mob_data.current_mob_data["hp"]
    else:
        exp_loss = mob_data.current_mob_data["hp"] * player_data.current_data["lvl"]

    if player_data.current_data["exp"] - exp_loss < 0:
        if player_data.current_data["lvl"] - 1 < 0:
            print("You have 0 levels and 0 exp")
        else:
            player_data.current_data["exp"] += (player_data.current_data["lvl"] * 150)
            player_data.current_data["exp"] -= exp_loss
            player_data.current_data["lvl"] -= 1
    else:
        player_data.current_data["exp"] -= exp_loss

    return exp_loss


def heal():
    heals = []
    num = 1
    name = ""
    line()
    for i in range(len(player_data.inventory)):
        if player_data.inventory[i][0] == items_data.healing_items[i]["name"]:
            print("{}) Item: {}, Amount: {}".format(num, player_data.inventory[i - 1][0].capitalize(),
                                                    player_data.inventory[i - 1][1]))
            heals.append(player_data.inventory[i - 1][0])
            num += 1
    line()
    print("Choose an number from 1 to {}".format(len(heals)))
    line()
    ans = int(input())
    player_data.inventory[ans - 1][1] -= 1
    for i in range(len(items_data.healing_items)):
        if heals[ans - 1] == items_data.healing_items[i - 1]["name"]:
            for j in range(len(player_data.inventory)):
                if heals[ans - 1] == player_data.inventory[j][0]:
                    name_2 = player_data.inventory[j][0]
                    if player_data.inventory[j][1] > 0:
                        if player_data.current_data["hp"] + items_data.healing_items[i - 1]["healing amount"] <= \
                                player_data.current_data["max hp"]:
                            player_data.current_data["hp"] += items_data.healing_items[i - 1]["healing amount"]
                            for h in range(len(items_data.healing_items)):
                                if heals[ans - 1] == items_data.healing_items[h]["name"]:
                                    print("You healed yourself by {}!".format(
                                        items_data.healing_items[h]["healing amount"]))
                        else:
                            player_data.current_data["hp"] = player_data.current_data["max hp"]
                            line()
                            print("You are at max hp!")
                            line()
                    else:
                        line()
                        print("You have no more of it!")
                        line()


def inv_count():
    for i in range(len(player_data.inventory)):
        player_data.current_data["in_inv"] += player_data.inventory[i - 1][1]
    return player_data.current_data["in_inv"]


def crafting(item):
    for i in range(len(items_data.craftable_items)):
        if item == items_data.craftable_items[i-1]["name"]:
            print(items_data.craftable_items[i-1]["name"])
        break


def add_to_inv(item, amount):
    for i in range(len(player_data.inventory)):
        if item == player_data.inventory[i - 1][0]:
            player_data.inventory[i - 1][1] += amount
            if inv_count() > player_data.current_data["inv_max_space"]:
                print("Your inventory is full")
                player_data.inventory[i - 1][1] -= (player_data.current_data["in_inv"] - player_data.current_data["inv_max_space"])
                player_data.current_data["in_inv"] = player_data.current_data["inv_max_space"]
            else:
                print("You added {} {} to your inventory!".format(amount, item))
        break


def take_from_inv(item, amount):
    for i in range(len(player_data.inventory)):
        if item == player_data.inventory[i - 1][0]:
            player_data.inventory[i - 1][1] -= amount
            if player_data.inventory[i - 1][1] < 0:
                print("You dont have anymore of this item")
                player_data.inventory[i - 1][1] += amount
            else:
                print("You removed {} {} from your inventory!".format(amount, item))


def trash(item, amount):
    for i in range(len(player_data.inventory)):
        if item == player_data.inventory[i]["name"]:
            player_data.inventory[i][1] -= amount
            print("You trashed {} {}".format(amount, item))


def choices_fight():
    print("What do you want to do?")
    line()
    print("1) Attack")
    print("2) Defend")
    print("3) Heal")
    print("4) Flee")
    print("5) Check")
    print("6) Hint")
    line()
    choice = input("Choose a number: ")
    if choice == "1":
        attack = att_or_not()
        line()
        print("You attempt to attack the {}".format(mob_data.current_mob_data["name"]))
        if attack <= (player_data.current_data["lvl"] * 0.5):
            print("You successfully attacked!")
            mob_data.current_mob_data["hp"] -= dmg_taken(player_data.current_data["att"],
                                                         mob_data.current_mob_data["def"])
            print("You did {} damage to the {}".format(
                str(dmg_taken(player_data.current_data["att"], mob_data.current_mob_data["def"])),
                mob_data.current_mob_data["name"]))
            line()
        else:
            line()
            print("You missed!")
            line()
        # print(attack)
        # print(player_data.current_data["lvl"] * 0.5)
    elif choice == "2":
        defending = True
        player_data.current_data["def"] += player_data.current_data["lvl"] / 2
        line()
        print("You defended! Your defence increased by " + str(player_data.current_data["lvl"] / 2) + " for this turn!")
        print("Your defence is now " + str(player_data.current_data["def"]) + "!")
        line()
        return defending
    elif choice == "3":
        heal()
    elif choice == "4":
        flee_fn()
        if player_data.current_data["lvl"] >= 0 and player_data.current_data["exp"] >= 0:
            line()
            print("You fled the fight when the {} was at {} health! You lost {} exp!".format(
                mob_data.current_mob_data["name"], mob_data.current_mob_data["hp"], flee_fn() * 2))
            line()
        else:
            line()
            print("You fled the fight!")
            line()
            player_data.current_data["lvl"] = 0
            player_data.current_data["exp"] = 0
        return "over"
    elif choice == "5":
        check()
    elif choice == "6":
        hint()
    else:
        line()
        print("You entered an invalid number and therefore did nothing...")
        line()
        return True


def choose_mob():
    mob_data.current_mob_data = []
    RNG = random.randint(0, len(mob_data.mobs) - 1)
    if player_data.current_data["zone"] == "jungle" or player_data.current_data["zone"] == "jungle_temple":
        mob_data.current_mob_data = mob_data.jungle_mobs[RNG]


def drops():
    for i in range(len(mob_data.current_mob_data["drops"])):
        RNG = random.random()
        if RNG <= mob_data.current_mob_data["drop chance"][i - 1]:
            for item in range(len(player_data.inventory)):
                if mob_data.current_mob_data["drops"][i - 1] == player_data.inventory[item - 1][0]:
                    for j in range(len(player_data.inventory)):
                        if mob_data.current_mob_data["drops"][i - 1] == player_data.inventory[j - 1][0]:
                            drop_amount = random.randint(mob_data.current_mob_data["drop amount"][i - 1][0],
                                                         mob_data.current_mob_data["drop amount"][i][1])
                            print("You got {} {} from the {}".format(drop_amount,
                                                                     mob_data.current_mob_data["drops"][i - 1],
                                                                     mob_data.current_mob_data["name"]))
                            add_to_inv(mob_data.current_mob_data["drops"][i - 1], drop_amount)
                        break
                break
        else:
            print("You got nothing...")
        break


def mob_attack():
    hp_loss = 0
    RNG = random.random() * player_data.current_data["lvl"]
    if RNG <= (player_data.current_data["lvl"] * 0.5):
        if (mob_data.current_mob_data["att"] - (player_data.current_data["def"] / 2)) <= 0:
            hp_loss = 1
        else:
            hp_loss = (mob_data.current_mob_data["att"] - (player_data.current_data["def"] / 2))
    return hp_loss


def fight():
    player_turn = True
    mob_turn = False
    turns = 0
    choose_mob()
    fighting = True
    line()
    print("You encountered a {}".format(mob_data.current_mob_data["name"]))
    player_data.current_data["zone"] = "fight"
    while fighting:
        if player_data.current_data["hp"] <= 0:
            line()
            print("You died!")
            line()
            fighting = False

            f = open("inv.txt", "w")
            g = open("save.txt", "w")
            f.write("")
            g.write("")
            f.close()
            g.close()
            player_data.current_data = player_data.default_data
            player_data.inventory = player_data.default_inv

            break
        elif mob_data.current_mob_data["hp"] <= 0:
            line()
            print("You defeated the {}! You gained {} exp!".format(mob_data.current_mob_data["name"],
                                                                   mob_data.current_mob_data["exp_drop"]))
            lvl_add()
            print("Your level is {} and your exp is {}".format(player_data.current_data["lvl"],
                                                               player_data.current_data["exp"]))
            line()
            drops()
            fighting = False
            break
        else:
            line()
            print("Its your turn!")
            print(
                "The {} has {} health left!".format(mob_data.current_mob_data["name"], mob_data.current_mob_data["hp"]))
            choice = choices_fight()
            line()
            if choice:
                player_data.defending = True
            if not fighting:
                break

            line()
            print("Its the {}'s turn!".format(mob_data.current_mob_data["name"]))
            print("You have {} health left".format(player_data.current_data["hp"]))
            hp_loss = mob_attack()
            player_data.current_data["hp"] -= hp_loss
            if hp_loss > 0:
                print("The {} did {} damage!".format(mob_data.current_mob_data["name"], hp_loss))
            else:
                print("The {} missed!".format(mob_data.current_mob_data["name"]))
            line()

            turns += 1

        if turns % 2 == 0 and player_data.defending:
            player_data.current_data["def"] -= player_data.current_data["lvl"] / 2
            line()
            print("Your defence is back down to " + str(player_data.current_data["def"]) + "!")
            player_data.defending = False
            line()


def random_event():
    print("Random event...")


def find_heal():
    print("You looked for some food.")
    for i in range(len(items_data.healing_items)):
        RNG = random.random()
        print(RNG)
        if RNG <= items_data.healing_items[i-1]["spawn chance"]:
            RNG_2 = random.randint(items_data.healing_items[i-1]["drop_amount"][0], items_data.healing_items[i-1]["drop_amount"][1])
            if RNG_2 != 1 and items_data.healing_items[i-1]["name"] == "berry":
                print("You got {} berries".format(RNG_2))
            elif RNG_2 == 1:
                print("You got {} {}".format(RNG_2, items_data.healing_items[i - 1]["name"]))
            else:
                print("You got {} {}s".format(RNG_2, items_data.healing_items[i - 1]["name"]))



def explore():
    RNG = random.random()
    if RNG <= 0.5:
        choose_mob()
        RNG_2 = random.random()
        if RNG_2 <= mob_data.current_mob_data["spawn_chance"]:
            fight()
        else:
            print("You encountered ... nothing")
    else:
        RNG_3 = random.random()
        if RNG_3 <= 0.33:
            print("You encountered... nothing")
        elif 0.33 < RNG_3 <= 0.67:
            random_event()
        else:
            find_heal()


def hint():
    jungle_hints = ["Look for a key. You can probably find one somewhere...",
                    "I've heard rumors that some enemies in the jungle drop some rare items. Maybe one of them can give you a key?",
                    "Notice how you have skill and level attributes? Yeah, those can help you dodge attacks. All you have to do is level yourself up.",
                    "To level yourself up you need to kill some enemies, simple enough right?",
                    "Try exploring, You might find something that might help you progress, But beware... Monsters lurk.",
                    "You can craft some stuff, as long as your'e not in a fight. All you have to do is press C!",
                    "Low on health? Explore a bit. You might find some healing foods!",
                    "In a fight but don't want to die? Just flee by pressing F. Only flee in dire situations though because it will cost you a lot of skill which you will need..."]
    fight_hints = ["If you founds some berries or nuts while exploring, you can heal yourself with them",
                   "Watch your health! You might die if you take too much damage!",
                   "You can flee a fight if your health gets too low, at the cost of some exp...",
                   "You can check you and your enemy's stats during the fight!",
                   "Defence is an important part of combat! The more defence you have, the less damage you'll take!",
                   "Anytime you find something new, look in the crafting menu! You can make weapons and armor!",
                   "Some weapons have a chance of dropping from different mobs! So try to complete as many fights as possible!"]
    if player_data.current_data["zone"] == "jungle":
        RNG = random.randint(0, len(jungle_hints) - 1)
        line()
        print(jungle_hints[RNG])
        line()
    elif player_data.current_data["zone"] == "fight":
        RNG = random.randint(0, len(fight_hints))
        line()
        print(fight_hints[RNG])
        line()


def save_inv():
    f = open("inv.txt", "w")
    for i in range(len(player_data.inventory)):
        inv = "," + player_data.inventory[i-1][0] + "," + str(player_data.inventory[i-1][1])
        f.write(inv)
    f.close()


def save_game():
    zone = player_data.current_data["zone"]
    hp = player_data.current_data["hp"]
    defence = player_data.current_data["def"]
    att = player_data.current_data["att"]
    name = player_data.current_data["name"]
    lvl = player_data.current_data["lvl"]
    exp = player_data.current_data["exp"]
    in_inv = player_data.current_data["in_inv"]
    inv_max_space = player_data.current_data["inv_max_space"]
    max_hp = player_data.current_data["max hp"]
    f = open("save.txt", "w")
    f.write("{},{},{},{},{},{},{},{},{},{}".format(name, lvl, defence, exp, hp, max_hp, zone, att, in_inv, inv_max_space))
    f.close()
    save_inv()
    print("Your game has been saved!")


def inv_restore():
    f = open("inv.txt", "r")
    x = f.readline()
    list_1 = x.split(",")

    inv = []
    item = []

    for i in range(len(list_1)):
        if i == 1:
            pass
        if i % 2 == 1 and i != 1:
            item[1] = int(list_1[i-1])
            inv.append(item)
        if i % 2 == 0 and i != 1:
            item = [0, 0]
            item[0] = str(list_1[i-1])
        if len(inv) == player_data.default_inv:
            break

    player_data.inventory = inv


def continuing():
    f = open("save.txt", "r")
    g = f.readline()
    x = g.split(",")

    inv_restore()

    player_data.current_data["name"] = x[0]
    player_data.current_data["lvl"] = int(x[1])
    player_data.current_data["def"] = int(x[2])
    player_data.current_data["exp"] = int(x[3])
    player_data.current_data["hp"] = int(x[4])
    player_data.current_data["max hp"] = int(x[5])
    player_data.current_data["zone"] = x[6]
    player_data.current_data["att"] = int(x[7])
    player_data.current_data["in_inv"] = int(x[8])
    player_data.current_data["inv_max_space"] = int(x[9])

    print("Welcome back, {}!".format(player_data.current_data["name"]))

    f.close()


def game():
    print("You see something in the distance.")
    sleep(0.5)
    print("Go towards it?")
    ans = input("Yes or No?(Y/N): \n")
    if ans.lower() == "y":
        print("You went towards it...")
        sleep(0.5)
        player_data.current_data["zone"] = "jungle temple"
        print("Looks like a temple. Theres a door at the end.")
        ans = input("Open it(Y/N): ")
        if ans.lower() == "y":
            loop_over = False
            while not loop_over:
                sleep(0.5)
                print("Its locked...")
                print("What would you like to do?")
                print("1) Hint")
                force_hint = input("Choose one: ")
                if force_hint == "1":
                    sleep(0.75)
                    print("You called for the voice")
                    sleep(0.75)
                    print("The voice: You need help?")
                    sleep(0.75)
                    print("With a locked door!!!")
                    sleep(0.75)
                    print("Just look for a key!")
                    sleep(0.75)
                    print("Its that simple! Jeez...")
                    loop_over = True
                    choices_norm()
                else:
                    print("Please choose a valid option(1): ")
            print("Welp,...,Guess we better go look for a key.")
            loop_over_2 = False
            while not loop_over_2:
                choices_norm()
    else:
        choice_thing = choices_norm()
        if choice_thing == "explore":
            print("Exploring...")
            explore()
        elif choice_thing == "hint":
            hint()
        elif choice_thing == "pause":
            print("Pausing...")
            pause_mn()
        else:
            pass
