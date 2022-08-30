
import random

# 3 enemy characters

enemy1 = {                                                  # DICT{} all encompassing
    'name': 'Marble, the Earthbreaker',                       # String
    'level': 1,                                             # Integer
    'health': 160,
    'max_health': 160,                                          # Integer
    'equipment': {"Savage Greatboots of the Mountain"},     # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Rock Throw', (11, 19)),
        ('Stone Spike', (29, 39)),
        ('Earthquake', (44, 56))
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
    'health': 160,
    'max_health': 160,                                          # Integer
    'equipment': {"Stormfury Chainmail Chestplate"},        # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Air Blast', (11, 19)),
        ('Wind Cut', (29, 39)),
        ('Hurricane', (44, 56))
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
