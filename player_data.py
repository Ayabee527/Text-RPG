import items_data

defending = False

current_data = {

}

default_data = {
    "name": "",
    "lvl": 1,
    "def": 0,
    "exp": 0,
    "hp": 50,
    "max hp": 50,
    "zone": "jungle",
    "att": 2,
    "in_inv": 0,
    "inv_max_space": 20,
}

default_inv = []

inventory = [

]

for i in range(len(items_data.items)):
    default_inv.append([items_data.items[i-1]["name"], 0])
