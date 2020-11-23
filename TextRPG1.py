import random
import functions
import player_data
import time

player_data.current_data = player_data.default_data
player_data.inventory = player_data.default_inv

game_exit = False

quiting = functions.quit_fn()

if quiting == 3:
    game_exit = True
elif quiting == 2:
    functions.continuing()
else:
    f = open("save.txt", "w")
    f.write("")
    f.close()
    f = open("inv.txt", "w")
    f.write("")
    f.close()
    functions.intro()
    functions.init()
    functions.save_game()
    functions.game()

while not game_exit:

    #functions.inv_count()

    #functions.choices_norm()

    functions.save_game()

    functions.find_heal()
    quitz = functions.quiting()

    if quitz == "continue":
        pass
    elif quitz == "quit":
        functions.save_game()
        game_exit = True

functions.save_game()

game_exit = True

exit()
