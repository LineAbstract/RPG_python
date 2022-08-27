
import functions
import hero_character
import enemy_characters


def run_game():
    functions.intro()
    functions.start_or_not()
    # functions.enemy_intro(enemy_characters.enemy1)
    functions.battle(hero_character.hero, enemy_characters.enemy1)
    functions.battle(hero_character.hero, enemy_characters.enemy2)
    functions.battle(hero_character.hero, enemy_characters.enemy3)
run_game()

