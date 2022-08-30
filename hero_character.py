
# main hero character

hero = {                                                    # DICT{} all encompassing
    'name': 'test',                                             # String
    'level': 1,                                             # Integer
    'health': 350,                                          # Integer
    'equipment': {"Father's Broadsword"},                   # SET{} of strings
    'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
        ('Barbarous Slice', 25),
        ('Seeking Blade', 50),
        ('Dragon Slash', 75)
    ),        
    'coins': {                                              # DICT{}
        'copper': 0,                                        # Integer
        'silver': 0, 
        'gold': 0, 
    },
    'phrases': {
        'on_attack': ["and...stay down!", 'SMASH!', 'Feel my RAGEEEE!'],     # LIST[] of Strings
        'on_defend': ["Yikes!", 'Ouch!', 'Zoinks!']   # LIST[] of Strings
    }
}
