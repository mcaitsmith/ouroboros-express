# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define vivi = Character("Vivi", callback = name_callback, cb_name = "vivi", image="vivi",color="#FFFFFF")
define vivithinking = Character("Vivi", callback = name_callback, cb_name = "vivi", image="vivi",what_prefix='(', what_suffix=')',color="#FFFFFF")
define vivi_conductor = Character("Vivi", callback = name_callback, cb_name = "vivi", image="vivi_conductor",color="#FFFFFF")
define urshu = Character("Urshu", callback = name_callback, cb_name = "urshu", image="urshu",color="#FFFFFF", namebox_background=Frame("gui/namebox_urshu.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define urshudining = Character("Urshu", callback = name_callback, cb_name = "urshudining", image="urshudining",color="#FFFFFF", namebox_background=Frame("gui/namebox_urshu.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define ava = Character("Asha", callback = name_callback, cb_name = "ava",image="ava",color="#FFFFFF", namebox_background=Frame("gui/namebox_ava.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define darius = Character("Darius", callback = name_callback, cb_name = "darius",image="darius",color="#FFFFFF", namebox_background=Frame("gui/namebox_darius.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define susurha = Character("Susu'Rha", callback = name_callback, cb_name = "susurha",image="susurha",color="#FFFFFF", namebox_background=Frame("gui/namebox_susurha.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

init:
    call images_bgs from _images_bgs # define background/CG images
    call images_chars from _images_chars # define character sprite images

# define day for quick fix for a bug
define day = 0

# define custom positions for sprites
transform center_left:
    xalign 0.2 yalign 1.0
transform center_right:
    xalign 0.8 yalign 1.0

# define flash effect
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# define custom screen effects
transform bright:
    matrixcolor BrightnessMatrix (0.75)
transform flicker_opacity:
    linear 0.2 alpha 0.8
    linear 0.2 alpha 0.4
    repeat 4
transform train_shake:
    linear 0.3 xoffset -2 yoffset 2 
    linear 0.3 xoffset 2 yoffset -2
    # linear 0.3 xoffset 2 yoffset -2
    # linear 0.3 xoffset -3 yoffset 3
    # linear 0.3 xoffset 0 yoffset 0
    repeat

# add layer for eldritch overlay (currently not used)
define config.layers = [ 'background','master', 'transient', 'screens', 'overlay','eldritch_overlay']
# define layers of backgrounds and NPCs
$ config.tag_layer['observatory'] = 'background'
$ config.tag_layer['diningcar'] = 'background'
$ config.tag_layer['cabin'] = 'background'
$ config.tag_layer['lounge'] = 'background'
$ config.tag_layer['vivi'] = 'master'
$ config.tag_layer['urshu'] = 'master'
$ config.tag_layer['ava'] = 'master'
$ config.tag_layer['darius'] = 'master'
$ config.tag_layer['susurha'] = 'master'

label check_overlay: # call this label to display eldritch overlay
    # hide eldritch1 onlayer eldritch_overlay
    # hide eldritch2 onlayer eldritch_overlay
    # hide eldritch3 onlayer eldritch_overlay
    # hide eldritch4 onlayer eldritch_overlay
    # hide eldritch5 onlayer eldritch_overlay
    # with { "master" : Dissolve(1.0) }
    if dec_meter >= dec_threshold_5:
        show eldritch lv5 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_4:
        show eldritch lv4 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_3:
        show eldritch lv3 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_2:
        show eldritch lv2 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_1:
        show eldritch lv1 onlayer eldritch_overlay
    with { "background" : Dissolve(1.0) }
    return

label check_overlay_nofade: # call this label to display eldritch overlay
    # hide eldritch1 onlayer eldritch_overlay
    # hide eldritch2 onlayer eldritch_overlay
    # hide eldritch3 onlayer eldritch_overlay
    # hide eldritch4 onlayer eldritch_overlay
    # hide eldritch5 onlayer eldritch_overlay
    if dec_meter >= dec_threshold_5:
        show eldritch lv5 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_4:
        show eldritch lv4 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_3:
        show eldritch lv3 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_2:
        show eldritch lv2 onlayer eldritch_overlay
    elif dec_meter >= dec_threshold_1:
        show eldritch lv1 onlayer eldritch_overlay
    return

label hide_overlay: # call this label to hide eldritch overlay
    hide eldritch onlayer eldritch_overlay
    # with { "master" : Dissolve(1.0) }
    return

# define splashscreen with SLS logo
label splashscreen:
    scene black
    with Pause(1)

    #play sound twinkle fadein 2.0

    #pause 2.0

    # show splashlogo at truecenter with dissolve:
    #     zoom 2.0
    # with Pause(3)

    # $ renpy.movie_cutscene('images/SLS_Logo.mpg')
    show splashlogo

    pause 4.5

    #stop sound fadeout 2.0

    scene black with dissolve
    with Pause(3)

    return

init python:
    config.auto_voice = "audio/voice/{id}.ogg" # define location of voice files for VO
    config.keymap['save_delete'].append('K_d') # Add D key for deleting saves
    renpy.music.register_channel("sound2", "sfx", False) # add second channel for sfx

# The game starts here.

label start:

    $ quick_menu = False # hide quick menu at start
    $ _game_menu_screen = None # disable ESC menu at start
    
    call sounds from _call_sounds # define sounds
    call meters from _call_meters # define meter variables
    call journal from _call_journal 

    pause 1.0

    menu:
        "Photosensitive Warning: Read Before Playing?"
        "Yes":
            "A very small percentage of individuals may experience epileptic seizures when exposed to certain light patterns or flashing lights."
            "Exposure to certain patterns or backgrounds on a computer screen, or while playing video games, may induce an epileptic seizure in these individuals."
            "Certain conditions may induce previously undetected epileptic symptoms even in persons who have no history of prior seizures or epilepsy."
            "If you, or anyone in your family, have an epileptic condition, consult your physician prior to playing."
            "Symptoms may include dizziness, altered vision, eye or muscle twitches, loss of awareness, disorientation, any involuntary movement, or convulsions."
            "If you experience any of these symptoms while playing a video or computer game, IMMEDIATELY discontinue use and consult your physician before resuming play."
            window hide
        "No":
            window hide

    pause 1.0

    menu:
        "Press Shift+A to set accessibility options before beginning the game."
        "Continue":
            "Access the menu anytime by pressing the Escape key. A tutorial on the game features is available from the Settings option in the main menu."
            window hide dissolve
            stop music fadeout 3.0
            pause 5.0
            jump begin

label begin:

    # TRAIN BELL INTRO
    play sound trainbell
    pause 8.0
    

    play music mainmusic volume 0.5 # start main track
    $ has_journal = False

    # initialize Urshu path variables
    $ urshu_story_1 = False
    $ urshu_story_2 = False
    $ urshu_story_3 = False
    $ urshu_story_4 = False

    $ quick_menu = True # restore quick menu
    $ _game_menu_screen = "save" # restore menu access


    # jump to first scene
    jump introduction