
import random
import hero_character
import enemy_characters 

# functions to be used in main run_game() function

# intro story 
def intro():
    print("\n#############################\n***WHOOOSSHHH....ommm POP!*** \n#############################\n\n\
You hear what appears to be a mage utter under his breath: \n\
'Oh boy...I must've done it again didn't I...' \n\
\nMage: \n\
'Whelp, looks like I've cast the wrong spell, yet again! So sorry.. heh. Name's Merlin. \n\
'Terribly sorry for teleporting you here, but I do suppose that you are stuck here with me until either you slay these elementals before us, or we die. Sorry to tell you, but I can't help you as I'm all out of magic.'")
    player_name = input("\nDo tell, what might your name be?: ")
    hero_character.hero['name'] = player_name

# player deciding whether to start the game or not
def start_or_not():
    global advt_start
    advt_start = False
    while advt_start == False:
        start_or_not = input(f"\nWell {hero_character.hero['name']}, shall we begin? Enter yes/no: ")
        if start_or_not == "yes":
            print("\nLovely! Do me proud and best of luck!")
            print(f"\nYou are starting with {hero_character.hero['health']} health points.")
            advt_start = True
            return advt_start
        elif start_or_not == "no":
            print("\nGuess we'll just wait here until we get beaten.\nYou and the Mage have succumb to the enemies before you.\n\nThe End.\n")
            advt_start = False
            return advt_start


# function introducing enemy
def enemy_intro(enemy):
    if enemy['health'] == enemy['max_health']:
        print(f"\nBefore you stands {enemy['name']}. Get ready!")
        print(f"You have {hero_character.hero['health']} health points remaining.")
    return


# as a user, select hero attack based on input
def hero_attack_choice():
    while advt_start == True:
        hero_attack_choice = int(input(f"\nYou have the following abilities: \n\
Press 1 to use {hero_character.hero['attacks'][0][0]} which deals {hero_character.hero['attacks'][0][1]} damage.\n\
Press 2 to use {hero_character.hero['attacks'][1][0]} which deals {hero_character.hero['attacks'][1][1]} damage.\n\
Press 3 to use {hero_character.hero['attacks'][2][0]} which deals {hero_character.hero['attacks'][2][1]} damage.\n\n\
\
Which ability do you use: "))
        
        while hero_attack_choice < 1 or hero_attack_choice > 3:
            hero_attack_choice = int(input("Enter 1, 2, or 3 to select an attack! Attack: "))
        
        if hero_attack_choice == 1:
            hero_attack = hero_character.hero['attacks'][0][1]
            return hero_attack
        
        if hero_attack_choice == 2: 
            hero_attack = hero_character.hero['attacks'][1][1]
            return hero_attack

        if hero_attack_choice == 3: 
            hero_attack = hero_character.hero['attacks'][2][1]
            return hero_attack

# random hero on_attack phrase

# random hero on_defend phrase

# have enemy attack be selected at random
def random_enemy_attack(enemy):
    enemy_attack = random.choice(enemy['attacks'])[1]
    return enemy_attack

# collected equipment output text
def collected_equip(enemy):
    for e in enemy['equipment']:
        print(e)

# during attack, hero or enemy health will decrease based on power of attack
# must show these results to terminal
# hero and enemy must continue to attack until one reaches 0 health
def battle(hero, enemy):
    while advt_start == True:
        enemy_intro(enemy)
        # if enemy['health'] > 0:
        #     print(f"\nBefore you stands {enemy['name']}. Get ready!")
        while hero['health'] > 0 and enemy['health'] > 0: 
            # hero attacks first
            hero_attack = hero_attack_choice()
            enemy['health'] -= hero_attack
            if enemy['health'] <= 0:
                print(f"You deal {hero_attack} damage to {enemy['name']} and it succumbs to your strength!")
                loot_equip__and_monies(hero, enemy)
                return
            else:
                print(f"You deal {hero_attack} damage to {enemy['name']}! {enemy['name']} has {enemy['health']} health remaining.")

            # enemy attacks next if health > 0 
            if enemy['health'] > 0:
                enemy_attack = random_enemy_attack(enemy)
                hero['health'] -= enemy_attack
                print(f"{enemy['name']} deals {enemy_attack} damage to you! You have {hero['health']} health remaining. ")
    else:
        return


# hero will loot enemies including equipment and coins/monies
def loot_equip__and_monies(hero, enemy):
    if hero['health'] > 0 and enemy['health'] <= 0:
        # loot
        hero['equipment'].update(enemy['equipment'])
        equipment_collected = collected_equip(enemy)
        print(f"\nEquipment collected: {equipment_collected}")
        
        # monies - copper, max 100
        hero['coins']['copper'] = hero['coins']['copper'] + enemy['coins']['copper']
        if hero['coins']['copper'] > 100:
            hero['coins']['copper'] = hero['coins']['copper'] - 100
            hero['coins']['silver'] = hero['coins']['silver'] + 1
        # silver, max 100
        hero['coins']['silver'] = hero['coins']['silver'] + enemy['coins']['silver']
        if hero['coins']['silver'] > 100:
            hero['coins']['silver'] = hero['coins']['silver'] - 100
            hero['coins']['gold'] = hero['coins']['gold'] + 1
        # gold
        hero['coins']['gold'] = hero['coins']['gold'] + enemy['coins']['gold']

        print(f"Coins collected: Gold: {enemy['coins']['gold']}, Silver: {enemy['coins']['silver']}, Copper: {enemy['coins']['copper']}")
        print(f"Coin pouch: {hero['coins']['gold']}g {hero['coins']['silver']}s {hero['coins']['copper']}c")
        
        enemy['coins']['copper'] = 0
        enemy['coins']['silver'] = 0
        enemy['coins']['gold'] = 0
    else:
        hero['equipment'].clear()
        hero['coins']['copper'] = 0
        hero['coins']['silver'] = 0
        hero['coins']['gold'] = 0

# ending story if alive
# def ending_alive():

# ending story if dead
# def ending_dead():