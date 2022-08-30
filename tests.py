import hero_character
import enemy_characters
import functions
import random
import sys, time


# print(f"Press 1 to use {hero_character.hero['attacks'][0][0]} which deals {hero_character.hero['attacks'][0][1]} damage.")

# print(enemy_characters.enemy_list[0])

# print(f"{enemy_characters.enemy1['attacks']}")
# print(random.choice(enemy_characters.enemy1['attacks'])[1])

# a_random_attack = random.choice(enemy_characters.enemy3['attacks1'])[1]
# print(a_random_attack)
# attack_damage = random.randint(a_random_attack[0], a_random_attack[1])
# print(attack_damage)

# being = {
#     'name': 'xyz',
#     'coins': {
#         'copper': random.randint(0, 100),
#         'silver': random.randint(0, 100)
#     },
#     'attacks': (                                            # TUPLE of TUPLES (each tuple will have attack_name: String, attack_power: Integer)
#         ('Barbarous Slice', (11, 19)),
#         ('Seeking Blade', (29, 39)),
#         ('Dragon Slash', (44, 56))
#     )
# }

# being2 = {
#     'name': 'xyz',
#     'coins': {
#         'copper': random.randint(0, 100),
#         'silver': random.randint(0, 100)
#     }
# }

# print(f"Being has Copper: {being['coins']['copper']} | Silver: {being['coins']['silver']}.")
# print(f"Being 2 has {being2['coins']['copper']} copper.")
# being['coins']['copper'] = being['coins']['copper'] + (being2['coins']['copper'])
# if being['coins']['copper'] > 100:
#             being['coins']['copper'] = being['coins']['copper'] - 100
#             being['coins']['silver'] = being['coins']['silver'] + 1
# being2['coins']['copper'] = 0
# print(f"Being has {being['coins']['copper']} copper.")
# print(f"Being has {being['coins']['silver']} silver.")
# print(f"Being 2 has {being2['coins']['copper']} copper")

# print(random.choice(enemy_characters.enemy1['phrases']['on_attack']))

# print(f"Equipment: {hero_character.hero['equipment']}")

# functions.collected_equip(enemy_characters.enemy1)


# def new_attack():
#     new_attack_name = input('Enter new attack name: ')
#     new_attack_damage = random.randint(15, 75)

#     temp_attack_list = []
#     temp_attack_list.append(new_attack_name)
#     temp_attack_list.append(new_attack_damage)
#     temp_attack_list = tuple(temp_attack_list)
#     attack_list = list(being['attacks'])
#     attack_list.append(temp_attack_list)
#     being['attacks'] = tuple(attack_list)
#     return being['attacks']

# new_attack()

# def random_attack_number():
#     random_attack = random.choice(being['attacks'])
#     enemy_attack_name = random_attack[0]
#     print(random_attack)
#     print(enemy_attack_name)
#     enemy_attack = random.randint(random_attack[1][0], random_attack[1][1])
#     print(enemy_attack)

# random_attack_number()



# def slow_print(string_to_slow_print, delay_time):
#     for letter in string_to_slow_print:
#         sys.stdout.write(letter) # queues up the letter to be printed
#         sys.stdout.flush() # 'flushes' buffer and prints to terminal
#         time.sleep(delay_time) # pauses program for a given amount of time
#         print('')

# slow_print("\033[1;33;48m" + "Hello world, but slowly", 0.05)
# slow_print("Hello world, but slowly", 0.04)

# colored text prints
# utilizing ANSI escape codes
# \033[1;33;48m = Bold Yellow on Black Background
# \033[1;31;48m = Bold Red on Black Background
# \033[1;32;48m = Bold Green on Black Background