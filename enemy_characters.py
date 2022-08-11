# all 3 enemy characters

import random

enemy1 = {                                                  # DICT{} all encompassing
    'name': 'Grav, the Earthbreaker',                       # String
    'level': 1,                                             # Integer
    'health': 150,                                          # Integer
    'equipment': {"Savage Greatboots of the Mountain"},     # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('power1', random.randint(11, 19)),
        ('power2', random.randint(29, 39)),
        ('power3', random.randint(44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 4), 
    },
    'phrases': {
        'on_attack': ['saying1', 'saying2', 'saying3'],     # LIST[] of Strings
        'on_damage': ['dsaying1', 'dsaying2', 'dsaying3']   # LIST[] of Strings
    }
}

enemy2 = {                                                  # DICT{} all encompassing
    'name': 'Hurricane Voxis',                              # String
    'level': 1,                                             # Integer
    'health': 150,                                          # Integer
    'equipment': {"Stormfury Chainmail Chestplate"},        # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('power1', random.randint(11, 19)),
        ('power2', random.randint(29, 39)),
        ('power3', random.randint(44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 4), 
    },
    'phrases': {
        'on_attack': ['saying1', 'saying2', 'saying3'],     # LIST[] of Strings
        'on_damage': ['dsaying1', 'dsaying2', 'dsaying3']   # LIST[] of Strings
    }
}

enemy3 = {                                                  # DICT{} all encompassing
    'name': 'Galv, Lord of Lightning',                      # String
    'level': 1,                                             # Integer
    'health': 300,                                          # Integer
    'equipment': {"Infinite Light Necklace"},               # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('power1', random.randint(11, 19)),
        ('power2', random.randint(29, 39)),
        ('power3', random.randint(44, 56))
    ),        
    'coins': {                                              # DICT{}
        'copper': random.randint(0, 100),                   # Integer
        'silver': random.randint(0, 100), 
        'gold': random.randint(4, 10), 
    },
    'phrases': {
        'on_attack': ['saying1', 'saying2', 'saying3'],     # LIST[] of Strings
        'on_damage': ['dsaying1', 'dsaying2', 'dsaying3']   # LIST[] of Strings
    }
}