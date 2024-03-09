# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen",show_two_window=False)


# The game starts here.

default quest = Manager()

label start:

    show screen button_open

    jump scene1 # jump to first scene

    # # This ends the game.

    # return
