import hero_character
import enemy_characters
import functions
import random


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
#     }
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

print(random.choice(enemy_characters.enemy1['phrases']['on_attack']))

print(f"Equipment: {hero_character.hero['equipment']}")

functions.collected_equip(enemy_characters.enemy1)