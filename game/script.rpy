# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define vivi = Character("Vivi",image="vivi")
define vivithinking = Character("Vivi",image="vivi",what_italic=True)
define urshu = Character("Urshu",image="urshu")
define ava = Character("Ava",image="ava")
define darius = Character("Darius",image="darius")
define susurha = Character("Susu'Rha",image="susurha")

# The game starts here.

default quest = Manager()

label start:

    show screen button_open

    jump scene1 # jump to first scene

    # # This ends the game.

    # return
