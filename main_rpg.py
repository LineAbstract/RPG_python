
import functions
import hero_character
import enemy_characters


def run_game():
    functions.intro()
    functions.start_or_not()
    functions.battle(hero_character.hero, enemy_characters.enemy1)
    functions.battle(hero_character.hero, enemy_characters.enemy2)
    functions.battle(hero_character.hero, enemy_characters.enemy3)
    functions.outro(hero_character.hero)
run_game()


'''
intro
start_or_not
battle
    enemy_intro
    hero_attack_choice
                            hero_attack_phrase
    random_enemy_attack
                            hero_defend_phrase
    loot_equip_and_monies
        collected_equip (print)
    hero_level_up
    new_hero_attack
ending
'''