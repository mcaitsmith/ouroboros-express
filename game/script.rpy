# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vivi = Character("Vivi",image="vivi",color="#FFFFFF")
define vivithinking = Character("Vivi",image="vivi",what_italic=True,color="#FFFFFF")
define urshu = Character("Urshu",image="urshu",color="#FFFFFF",namebox_background=Frame("gui/namebox_urshu.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define ava = Character("Ava",image="ava",color="#FFFFFF",namebox_background=Frame("gui/namebox_ava.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define darius = Character("Darius",image="darius",color="#FFFFFF",namebox_background=Frame("gui/namebox_darius.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define susurha = Character("Susu'Rha",image="susurha",color="#FFFFFF",namebox_background=Frame("gui/namebox_susurha.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

define titlemusic = "audio/music/lavenders blue.ogg"
define mainmusic = "audio/music/OrEx_MainTrack1_v1.0.ogg"
define goodendmusic = "audio/music/Good Ending.ogg"
define badendmusic = "audio/music/CosmicSelf_Demo_BadEnding.wav"

# The game starts here.

default quest = Manager()

label start:

    # show screen button_open

    jump scene1 # jump to first scene

    # # This ends the game.

    # return
