# main hero character

# from functions import player_name
# player_name

hero = {                                                    # DICT{} all encompassing
    'name': # player_name,                                    # String
    'level': 1,                                             # Integer
    'health': 500,                                          # Integer
    'equipment': {"Father's Broadsword"},                   # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('power1', 50),
        ('power2', 75),
        ('power3', 100)
    ),        
    'coins': {                                              # DICT{}
        'copper': 0,                                        # Integer
        'silver': 0, 
        'gold': 0, 
    },
    'phrases': {
        'on_attack': ['saying1', 'saying2', 'saying3'],     # LIST[] of Strings
        'on_damage': ['dsaying1', 'dsaying2', 'dsaying3']   # LIST[] of Strings
    }
}