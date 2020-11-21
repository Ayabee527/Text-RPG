from Games import weapons_data
from Games import armors_data

berry = {
    "name": "berry",
    "heals": True,
    "craftable": False,
    "ingredient": True,
    "healing amount": 5,
    "spawn chance": 0.5,
    "drop_amount": [1, 5],
    "ingredients": [["", 0]]
}

gel = {
    "name": "gel",
    "heals": False,
    "craftable": False,
    "ingredient": True,
    "healing amount": 0,
    "spawn chance": 0,
    "drop_amount": [0, 0],
    "ingredients": [["", 0]]
}

nut = {
    "name": "nut",
    "heals": True,
    "craftable": False,
    "ingredient": True,
    "healing amount": 8,
    "spawn chance": 0.25,
    "drop_amount": [1, 5],
    "ingredients": [["", 0]]
}

iron_scrap = {
    "name": "iron scrap",
    "heals": False,
    "craftable": False,
    "ingredient": True,
    "healing amount": 0,
    "spawn chance": 0,
    "drop_amount": [0, 0],
    "ingredients": [["", 0]]
}

iron_ingot = {
    "name": "iron ingot",
    "heals": False,
    "craftable": True,
    "ingredient": True,
    "healing amount": 0,
    "spawn chance": 1,
    "drop_amount": [1,1],
    "ingredients": [["iron_scrap", 2]]
}

healing_items = [nut, berry]
crafting_ingredients = [iron_scrap, iron_ingot, gel, nut, berry]
craftable_items = [iron_ingot, armors_data.iron_armor, weapons_data.iron_sword]
armors = [armors_data.iron_armor]
weapons = [weapons_data.iron_sword]
items = [berry, gel, nut, iron_scrap, iron_ingot, armors_data.iron_armor, weapons_data.iron_sword]
