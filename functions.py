
import random
import hero_character
import enemy_characters 

# functions to be used in main run_game() function

# intro story 
def intro():
    print("\n#############################\n  ***WHOOOSSHHH... POP!*** \n#############################\n\n ")
    print("You hear what appears to be a mage utter under his breath: \n\
'Let's hope our hero can do it this time...' \n\
\nMage: \n\
'*Uhummm.*' \n'Hello young champion! You are here in a training simulation in the Elemental Plains where you will gain worthwhile experience, preparing you for the defense of our world.' \n\
'You must slay these elementals before us, or we will perish. Sorry to tell you, but I can't help you as I'm all out of magic.'")
    player_name = input("\nRemind me, what might your name be?: ")
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
            print("\nGuess we'll just wait here until we get beaten.\nYou and the Mage have succumb to the enemies before you.\n\nGame Over.\n")
            advt_start = False
            return advt_start


# during attack, hero or enemy health will decrease based on power of attack
# must show these results to terminal
# hero and enemy must continue to attack until one reaches 0 health
def battle(hero, enemy):
    while advt_start == True:
        while hero['health'] > 0 and enemy['health'] > 0: 
            enemy_intro(enemy)
            # hero attacks first
            hero_attack = hero_attack_choice()
            enemy['health'] -= hero_attack[1]
            if enemy['health'] <= 0:
                print(f"\n'{hero_phrase_on_attack(hero)}'You deal {hero_attack[1]} damage to {enemy['name']} with {hero_attack[0]} and it succumbs to your might!")
                print(f"\nYou have defeated {enemy['name']}!")
                loot_equip_and_monies(hero, enemy)
                hero_level_up(hero)
                new_hero_attack(hero)
                return
            else:
                print('\n~~~Battle~~~')
                print(f"'{hero_phrase_on_attack(hero)}' You deal {hero_attack[1]} damage to {enemy['name']} with {hero_attack[0]}! {enemy['name']} has {enemy['health']} health remaining.")

            # enemy attacks next if health > 0 
            if enemy['health'] > 0:
                enemy_attack = random_enemy_attack(enemy)
                hero['health'] -= enemy_attack[1]
                
                # is hero alive after attack? 
                if hero['health'] <= 0:
                    print(f"{enemy['name']} deals {enemy_attack[1]} damage to you with {enemy_attack[0]}! '{hero_phrase_on_defend(hero)}' You have 0 health remaining.")
                else:
                    print(f"{enemy['name']} deals {enemy_attack[1]} damage to you with {enemy_attack[0]}! '{hero_phrase_on_defend(hero)}' You have {hero['health']} health remaining. ")
            

            if enemy['health'] > 0 and hero['health'] <= 0:
                print(f"\nYou have been defeated by {enemy['name']}. You have failed.")
                return
        return
    else:
        return


# function introducing enemy
def enemy_intro(enemy):
    if enemy['health'] == enemy['max_health']:
        print(f"\nMage: \n\
Before you stands {enemy['name']} who has {enemy['health']} health. Get ready!")
        print(f"You have {hero_character.hero['health']} health points remaining.")
    return

# as a user, select hero attack based on input
def hero_attack_choice():
    while advt_start == True:
        print(f"\nYou have the following abilities:")
        counter = 1
        for attack in hero_character.hero['attacks']:
            print(f"Enter {counter} to use {attack[0]} which deals {attack[1]} damage.")
            counter += 1

        '''hero_attack_choice = int(input(f"Which ability do you use: ") or 0)
        
        while hero_attack_choice < 1 or hero_attack_choice > len(hero_character.hero['attacks']):
            hero_attack_choice = int(input(f"Enter {list(range(1, len(hero_character.hero['attacks']) + 1))} to select an attack! Ability choice: ".replace("[", "").replace("]", "")) or 0)

        hero_attack = hero_character.hero['attacks'][hero_attack_choice - 1][1]
        return hero_attack'''

        # refactoring to allow for user input error handling
        # don't convert to integer
        hero_attack_choice = input(f"Which ability do you use: ")
        
        # check if isdigit FIRST
        while not hero_attack_choice.isdigit() or int(hero_attack_choice) < 1 or int(hero_attack_choice) > len(hero_character.hero['attacks']):
            hero_attack_choice = input(f"Enter {list(range(1, len(hero_character.hero['attacks']) + 1))} to select an attack! Ability choice: ".replace("[", "").replace("]", ""))
        
        # now convert to integer
        hero_attack = hero_character.hero['attacks'][int(hero_attack_choice) - 1][1]
        # pull out hero attack name
        hero_attack_name = hero_character.hero['attacks'][int(hero_attack_choice) -1][0]
        return hero_attack_name, hero_attack
        


# for bonus: random hero phrase on_attack
def hero_phrase_on_attack(hero):
    on_attack = random.choice(hero['phrases']['on_attack'])
    return on_attack


# for bonus: random hero phrase on_attack
def hero_phrase_on_defend(hero):
    on_defend = random.choice(hero['phrases']['on_defend'])
    return on_defend

# have enemy attack be selected at random
    # may add at a later time: random enemy phrase on attack and defend
def random_enemy_attack(enemy):
    random_attack = random.choice(enemy['attacks'])
    enemy_attack_name = random_attack[0]
    enemy_attack = random.randint(random_attack[1][0], random_attack[1][1])
    return enemy_attack_name, enemy_attack


# hero will loot enemies including equipment and coins/monies
def loot_equip_and_monies(hero, enemy):
    if hero['health'] > 0 and enemy['health'] <= 0:
        # equipment loot
        hero['equipment'].update(enemy['equipment'])
        # equipment_collected = collected_equip(enemy)
        print(f"\nEquipment collected: {collected_equip(enemy)}")
        
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


# collected equipment output text
def collected_equip(enemy):
    for e in enemy['equipment']:
        return e


# for bonus: hero levels up on enemy defeat
def hero_level_up(hero):
    hero['level'] += 1
    print(f"\nYou have gained a level! You are now Level {hero['level']}")


# for bonus: new hero attack input
def new_hero_attack(hero):
    new_hero_attack_name = input("You've gained a new skill. Please enter a new attack name: ")
    new_hero_attack_damage = random.randint(15, 75)
    print(f'Your new attack {new_hero_attack_name} deals a randomly generated {new_hero_attack_damage} damage.')

    temp_attack_list = []
    temp_attack_list.append(new_hero_attack_name)
    temp_attack_list.append(new_hero_attack_damage)
    temp_attack_list = tuple(temp_attack_list)

    attack_list = list(hero['attacks'])
    attack_list.append(temp_attack_list)
    hero['attacks'] = tuple(attack_list)
    return hero['attacks']


# create ending story if hero alive or dead
def outro(hero):
    while advt_start == True:
        if hero['health'] <= 0:
            print(f"\nMage: \n\
Eh, don't worry about it {hero['name']}! You're not the first to not complete this training exercise.\
\nWe'll come back to these elementals when you are better prepared!\
\nI'll teleport you back now, get some rest.")
            print('\n#############################\n  ***WHOOOSSHHH... POP!*** \n#############################')
            print('\nGAME OVER.\n')
            return
        if hero['health'] > 0:
            print(f"\nMage: \n\
Well done {hero['name']}! You have completed your Elemental Trials with {hero['health']} health remaining! \nMy energy is restored and I will now teleport you back to the training grounds for your next session. See you there! ;)")
            print('\n#############################\n  ***WHOOOSSHHH... POP!*** \n#############################')
            print('\nCongratulations, you have completed the game.')
            print('\nGame Over.\n')
            return
    return