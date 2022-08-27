# main hero character

hero = {                                                    # DICT{} all encompassing
    'name': 'test',                                             # String
    'level': 1,                                             # Integer
    'health': 500,                                          # Integer
    'equipment': {"Father's Broadsword"},                   # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Barbarous Slice', 50),
        ('Seeking Blade', 75),
        ('Dragon Slash', 100)
    ),        
    'coins': {                                              # DICT{}
        'copper': 0,                                        # Integer
        'silver': 0, 
        'gold': 0, 
    },
    'phrases': {
        'on_attack': ["and...stay down!", 'SMASH!', 'Feel my RAGEEEE!'],     # LIST[] of Strings
        'on_defend': ['Owwies', 'Ouchies', "That's going to leave a mark"]   # LIST[] of Strings
    }
}
