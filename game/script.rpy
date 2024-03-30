# The script of the game goes in this file.

init python:
    renpy.music.register_channel("blip", "sfx")
    def beepy_voice_high(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/sfx/468925__malakme__high-text-blip.ogg",channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
    def beepy_voice_medium(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/sfx/468927__malakme__medium-text-blip.ogg",channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
    def beepy_voice_low(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/sfx/468926__malakme__lowblip.ogg",channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vivi = Character("Vivi",image="vivi",color="#FFFFFF", callback=beepy_voice_medium)
define vivithinking = Character("Vivi",image="vivi",what_italic=True,color="#FFFFFF")
define urshu = Character("Urshu",image="urshu",color="#FFFFFF", callback=beepy_voice_high, namebox_background=Frame("gui/namebox_urshu.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define ava = Character("Asha",image="ava",color="#FFFFFF", callback=beepy_voice_medium, namebox_background=Frame("gui/namebox_ava.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define darius = Character("Darius",image="darius",color="#FFFFFF", callback=beepy_voice_low, namebox_background=Frame("gui/namebox_darius.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define susurha = Character("Susu'Rha",image="susurha",color="#FFFFFF", callback=beepy_voice_low, namebox_background=Frame("gui/namebox_susurha.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

# define titlemusic = "audio/music/lavenders blue.ogg"
define mainmusic = "audio/music/OrEx_MainTrack1_v1.0.ogg"
define goodendmusic = "audio/music/Good Ending.ogg"
define badendmusic = "audio/music/CosmicSelf_Demo_BadEnding.ogg"

# PLACEHOLDER UNTIL GET BLUSH OVERLAY FOR VIVI SPRITE
# image vivi neutral blush = "images/characters/vivi/vivi neutral.png"
# image vivi happy blush = "images/characters/vivi/vivi happy.png"
# image vivi sad blush = "images/characters/vivi/vivi sad.png"
# image vivi angry blush = "images/characters/vivi/vivi angry.png"
# image vivi surprised blush = "images/characters/vivi/vivi surprised.png"

# PLACEHOLDER UNTIL GET SILHOUETTES
image ava silhouette = "images/characters/ava/ava silhouette.png"
image darius silhouette = "images/characters/darius/darius silhouette.png"
image susurha silhouette = "images/characters/susurha/susurha silhouette.png"

image cabin blur = im.Blur("images/backgrounds/cabin.png", 5)
image observatory blur = im.Blur("images/backgrounds/observatory.png", 5)
image lounge blur = im.Blur("images/backgrounds/lounge.png", 5)
image diningcar blur = im.Blur("images/backgrounds/diningcar.png", 5)

image white = "#ffffff"

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

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

transform center_left:
    xalign 0.2 yalign 1.0
transform center_right:
    xalign 0.8 yalign 1.0
transform bright:
    matrixcolor BrightnessMatrix (0.75)
transform flicker_opacity:
    linear 0.2 alpha 0.8
    linear 0.2 alpha 0.4
    repeat 4
#Journal screen

# The game starts here.

# commenting out since not used yet
#default quest = Manager()

label start:
    
    call sounds from _call_sounds # define sounds
    call meters from _call_meters # define meter variables
    call journal from _call_journal 
    play music mainmusic volume 0.5 # start main track
    $ has_journal = False

    # jump to first scene
    jump introduction