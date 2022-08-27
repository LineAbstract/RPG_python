# 3 enemy characters

import random

enemy1 = {                                                  # DICT{} all encompassing
    'name': 'Marble, the Earthbreaker',                       # String
    'level': 1,                                             # Integer
    'health': 150,
    'max_health': 150,                                          # Integer
    'equipment': {"Savage Greatboots of the Mountain"},     # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Rock Throw', random.randint(11, 19)),
        ('Stone Spike', random.randint(29, 39)),
        ('Earthquake', random.randint(44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 2), 
    },
    'phrases': {
        'on_attack': ['The Earth crumbles under you!', "You're stuck between a rock and a hard place!", 'Mama said knock you out!'],     # LIST[] of Strings
        'on_defend': ['That will leave a mark...', 'Noooooo', 'I was not expecting that...']   # LIST[] of Strings
    }
}

enemy2 = {                                                  # DICT{} all encompassing
    'name': 'Hurricane Voxis',                              # String
    'level': 1,                                             # Integer
    'health': 150,
    'max_health': 150,                                          # Integer
    'equipment': {"Stormfury Chainmail Chestplate"},        # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Air Blast', random.randint(11, 19)),
        ('Wind Cut', random.randint(29, 39)),
        ('Hurricane', random.randint(44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 2), 
    },
    'phrases': {
        'on_attack': ['Almighty wind!', 'Huzzah!', 'You will get blown away!'],     # LIST[] of Strings
        'on_defend': ['Ruh roh...', 'Ease up on me will ya?', 'I will get you for that one!']   # LIST[] of Strings
    }
}

enemy3 = {                                                  # DICT{} all encompassing
    'name': 'Galvatron, Lord of Lightning',                      # String
    'level': 1,                                             # Integer
    'health': 300,
    'max_health': 300,                                          # Integer
    'equipment': {'Infinite Light Necklace'},               # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Electric Zap', random.randint(11, 19)),
        ('Electric Shock', random.randint(29, 39)),
        ('Lightning Storm', random.randint(44, 56))
    ),
    'attacks1': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Electric Zap', (11, 19)),
        ('Electric Shock', (29, 39)),
        ('Lightning Storm', (44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(3, 7), 
    },
    'phrases': {
        'on_attack': ['Welcome to the THUNDERDOME', 'Zip Zap!', 'Electrification!'],     # LIST[] of Strings
        'on_defend': ['Ooooof!', 'How did you do that?!', 'Oh jeez, oh no!']   # LIST[] of Strings
    }
}


# enemy_list = []
# enemy_list.append(enemy1)
# enemy_list.append(enemy2)
# enemy_list.append(enemy3)
# print(enemy_list)

enemy_list = [enemy1, enemy2, enemy3]