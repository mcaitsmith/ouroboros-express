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

# PLACEHOLDER UNTIL GET BLUSH OVERLAY FOR VIVI SPRITE
image vivi neutral blush = "images/characters/vivi/vivi neutral.png"
image vivi happy blush = "images/characters/vivi/vivi happy.png"
image vivi sad blush = "images/characters/vivi/vivi sad.png"
image vivi angry blush = "images/characters/vivi/vivi angry.png"
image vivi surprised blush = "images/characters/vivi/vivi surprised.png"

image cabin blur = im.Blur("images/backgrounds/cabin.png", 1.5)
image observatory blur = im.Blur("images/backgrounds/observatory.png", 1.5)


layeredimage ava:
    group face auto:
        attribute neutral default
    group overlay:
        attribute blush:
            "ava_overlay_blush"
layeredimage darius:
    group face auto:
        attribute neutral default
    group overlay:
        attribute blush:
            "darius_overlay_blush"
layeredimage susurha:
    group face auto:
        attribute neutral default
    group overlay:
        attribute blush:
            "susurha_overlay_blush"
layeredimage urshu:
    group face auto:
        attribute neutral default
    group overlay:
        attribute blush:
            "urshu_overlay_blush"

# The game starts here.

default quest = Manager()
# define _scene_show_hide_transition = Dissolve(0.25)

label start:

    call sounds # define sounds

    play music mainmusic # start main track

    # jump scene1 # jump to first scene
    jump denial_briefing

    # # This ends the game.

    # return
