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

###MUSIC
#TITLE MUSIC
# define titlemusic = "audio/music/orex_mx_menu.ogg"

#MOOD MUSIC
define mainmusic = "audio/music/orex_mx_main.ogg"
define mysterymusic = "audio/music/orex_mx_mystery.ogg" ## Noah Campodonico — Underneath the Mask
define mysterymusicpiano = "audio/music/orex_mx_mysterypiano.ogg" ## Noah Campodonico — Underneath the Mask (Piano arr.)
define horrormusic = "audio/music/orex_mx_horror.ogg" ## Noah Campodonico — Trepidation
define peacefulmusic = "audio/music/orex_mx_peaceful.ogg" ## Noah Campodonico — Lilacs and Hydrangeas
define confrontationmusic = "audio/music/orex_mx_confrontation.ogg" ## Charlie Armour — [untitled] Confrontation Theme
define spymusic = "audio/music/orex_mx_eavesdrop.ogg" ## Charlie Armour — [untitled] Eavesdropping Theme
define sorrowmusic = "audio/music/orex_mx_sorrow.ogg" ## Charlie Armour — [Untitled] Sorrow Theme
define revealmusic = "audio/music/orex_mx_reveal.ogg" ## Charlir Amour — [Untitled] Reveal Theme

#CHARACTER THEMES
define vivistorymusic = "audio/music/orex_mx_vivistory.ogg" ## Noah Campodonico — Vivienne's Story
define susumusic = "audio/music/orex_mx_susu.ogg"  ## Armoni Boone — untitled susu theme
define dariusmusic = "audio/music/orex_mx_darius.ogg" ## Armoni Boone — untitled darius theme
define ashamusic = "audio/music/orex_mx_asha.ogg" ## Armoni Boone - untitled asha theme

#ENDING THEMES
define finalemusic = "audio/music/orex_mx_finale.ogg" ## Noah Campodonico - Celestial Bodies, Swirling
define badendmusic = "audio/music/orex_mx_cosmicself.ogg" ## Armoni Boone — Cosmic Self [bad ending]

#CREDITS THEMES
define creditsmusicgood = "audio/music/orex_mx_creditsgood.ogg"
define creditsmusicbad = "audio/music/orex_mx_creditsbad.ogg"



# define silhouette images
image ava silhouette = "images/characters/ava/ava silhouette.png"
image darius silhouette = "images/characters/darius/darius silhouette.png"
image susurha silhouette = "images/characters/susurha/susurha silhouette.png"

# image cabin_light_overlay:
#     "images/backgrounds/cabin_overlay.png"
#     alpha 0.5
#     linear 2.0 alpha 0.2
#     linear 2.0 alpha 0.5
#     repeat

image terminalofdreams_dust1_overlay:
    "images/backgrounds/vfx/terminal_dust1.png"
    alpha 1.0 matrixcolor BrightnessMatrix(1.0)
    # linear 2.0 alpha 0.0 xoffset -4 yoffset -4
    # linear 2.0 alpha 1.0 xoffset 4 yoffset 4
    # linear 2.0 alpha 0.0 xoffset 4 yoffset -4
    # linear 2.0 alpha 1.0 xoffset -4 yoffset 4
    linear 1.5 alpha 0.0
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.0
    linear 1.5 alpha 1.0
    repeat
image terminalofdreams_dust2_overlay:
    "images/backgrounds/vfx/terminal_dust2.png"
    alpha 0.0 matrixcolor BrightnessMatrix(1.5)
    # linear 2.0 alpha 1.0 xoffset 4 yoffset -4
    # linear 2.0 alpha 0.0 xoffset -4 yoffset 4
    # linear 2.0 alpha 1.0 xoffset -4 yoffset -4
    # linear 2.0 alpha 0.0 xoffset 4 yoffset 4
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.0
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.0
    repeat
image terminalofdreams_sparkles_overlay:
    "images/backgrounds/vfx/terminal_sparkles.png"
    alpha 1.0 matrixcolor BrightnessMatrix(1.5)
    linear 3.0 alpha 0.0
    linear 3.0 alpha 1.0
    linear 3.0 alpha 0.0
    linear 3.0 alpha 1.0
    repeat

image terminalofdreams_petals_overlay = SnowBlossom("images/backgrounds/vfx/terminal_petals.png", count=10, border=0, xspeed=(20, 50), yspeed=(50, 100))

# define blurred background images
image cabin blur = im.Blur("images/backgrounds/cabin.png", 5)
image observatory blur = im.Blur("images/backgrounds/observatory.png", 5)
image lounge blur = im.Blur("images/backgrounds/lounge.png", 5)
image diningcar blur = im.Blur("images/backgrounds/diningcar.png", 5)

# define day for quick fix for a bug
define day = 0

# define decay overlay bg images
layeredimage cabin:
    # subpixel True
    always:
        "images/backgrounds/cabin.png"
    # group light:
    #     attribute overlay default
    if day == 2:
        "decay_bedroom_1"
    elif day == 3:
        "decay_bedroom_2"
    elif day == 4 or day == 6:
        "decay_bedroom_3"
layeredimage observatory:
    always:
        "images/backgrounds/observatory.png"
    if day == 2:
        "decay_observatory_1"
    elif day == 3:
        "decay_observatory_2"
    elif day == 4 or day == 6:
        "decay_observatory_3"
layeredimage lounge:
    always:
        "images/backgrounds/lounge.png"
    if day == 2:
        "decay_lounge_1"
    elif day == 3:
        "decay_lounge_2"
    elif day == 4 or day == 6:
        "decay_lounge_3"
layeredimage diningcar:
    always:
        "images/backgrounds/diningcar.png"
    if day == 2:
        "decay_bar_1"
    elif day == 3:
        "decay_bar_2"
    elif day == 4 or day == 6:
        "decay_bar_3"
layeredimage terminalofdreams:
    subpixel True
    always:
        "images/backgrounds/terminalofdreams_base.png"
    group dust1:
        attribute overlay default
    group dust2:
        attribute overlay default
    group sparkles:
        attribute overlay default
    group petals:
        attribute overlay default

image vivi_window:
    "images/cgs/vivi_window.png"
    matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.5)
    linear 3.0 matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    repeat
image eldritch_vivi:
    "images/characters/eldritch_cgs/eldritch_vivi.png"
    matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#4b0000")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    repeat
image eldritch_asha:
    "images/characters/eldritch_cgs/eldritch_asha.png"
    matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#a3852b")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    repeat
image eldritch_darius:
    "images/characters/eldritch_cgs/eldritch_darius.png"
    matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#c66dd1")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    repeat
image eldritch_susurha:
    "images/characters/eldritch_cgs/eldritch_susurha.png"
    matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#00c3b4")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#5a3d5a")* BrightnessMatrix(0.0)
    linear 3.0 matrixcolor TintMatrix("#fff")* BrightnessMatrix(0.0)
    repeat

# add second channel for sfx
init python:
    renpy.music.register_channel("sound2", "sfx", False)

# define white background
image white = "#ffffff"

transform ex_neutral:
    zoom 1.0
transform ex_neutral_blush:
    zoom 1.02
transform ex_happy:
    zoom 1.02 yoffset 10
    linear 0.1 yoffset 0
    linear 0.2 yoffset 5
transform ex_sad:
    zoom 1.02
    linear 0.5 yoffset 10
transform ex_angry:
    zoom 1.02
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
transform ex_surprised:
    zoom 1.02 yoffset 20
    linear 0.2 yoffset 0

# define NPC expression and blush layered images
layeredimage ava neutral:
    at [sprite_highlight('ava'),ex_neutral]
    always:
        'images/characters/ava/ava_face_neutral.png'
layeredimage ava neutral blush:
    at [sprite_highlight('ava'),ex_neutral_blush]
    always:
        'images/characters/ava/ava_face_neutral.png'
    if day >= 0:
        'images/characters/ava/ava_overlay_blush.png'
layeredimage ava happy:
    at [sprite_highlight('ava'),ex_happy]
    always:
        'images/characters/ava/ava_face_happy.png'
    group overlay:
        attribute blush:
            "ava_overlay_blush"
layeredimage ava sad:
    at [sprite_highlight('ava'),ex_sad]
    always:
        'images/characters/ava/ava_face_sad.png'
    group overlay:
        attribute blush:
            "ava_overlay_blush"
layeredimage ava angry:
    at [sprite_highlight('ava'),ex_angry]
    always:
        'images/characters/ava/ava_face_angry.png'
    group overlay:
        attribute blush:
            "ava_overlay_blush"
layeredimage ava surprised:
    at [sprite_highlight('ava'),ex_surprised]
    always:
        'images/characters/ava/ava_face_surprised.png'
    group overlay:
        attribute blush:
            "ava_overlay_blush"

layeredimage darius neutral:
    at [sprite_highlight('darius'),ex_neutral]
    always:
        'images/characters/darius/darius_face_neutral.png'
    # group overlay:
    #     attribute blush:
    #         "darius_overlay_blush"
layeredimage darius neutral blush:
    at [sprite_highlight('darius'),ex_neutral_blush]
    always:
        'images/characters/darius/darius_face_neutral.png'
    if day >= 0:
        'images/characters/darius/darius_overlay_blush.png'
    # group overlay:
    #     attribute blush:
    #         "darius_overlay_blush"
layeredimage darius happy:
    at [sprite_highlight('darius'),ex_happy]
    always:
        'images/characters/darius/darius_face_happy.png'
    group overlay:
        attribute blush:
            "darius_overlay_blush"
layeredimage darius sad:
    at [sprite_highlight('darius'),ex_sad]
    always:
        'images/characters/darius/darius_face_sad.png'
    group overlay:
        attribute blush:
            "darius_overlay_blush"
layeredimage darius angry:
    at [sprite_highlight('darius'),ex_angry]
    always:
        'images/characters/darius/darius_face_angry.png'
    group overlay:
        attribute blush:
            "darius_overlay_blush"
layeredimage darius surprised:
    at [sprite_highlight('darius'),ex_surprised]
    always:
        'images/characters/darius/darius_face_surprised.png'
    group overlay:
        attribute blush:
            "darius_overlay_blush"

layeredimage susurha neutral:
    at [sprite_highlight('susurha'),ex_neutral]
    always:
        'images/characters/susurha/susurha_face_neutral.png'
layeredimage susurha neutral blush:
    at [sprite_highlight('susurha'),ex_neutral_blush]
    always:
        'images/characters/susurha/susurha_face_neutral.png'
    if day >= 0:
        'images/characters/susurha/susurha_overlay_blush.png'
layeredimage susurha happy:
    at [sprite_highlight('susurha'),ex_happy]
    always:
        'images/characters/susurha/susurha_face_happy.png'
    group overlay:
        attribute blush:
            "susurha_overlay_blush"
layeredimage susurha sad:
    at [sprite_highlight('susurha'),ex_sad]
    always:
        'images/characters/susurha/susurha_face_sad.png'
    group overlay:
        attribute blush:
            "susurha_overlay_blush"
layeredimage susurha angry:
    at [sprite_highlight('susurha'),ex_angry]
    always:
        'images/characters/susurha/susurha_face_angry.png'
    group overlay:
        attribute blush:
            "susurha_overlay_blush"
layeredimage susurha surprised:
    at [sprite_highlight('susurha'),ex_surprised]
    always:
        'images/characters/susurha/susurha_face_surprised.png'
    group overlay:
        attribute blush:
            "susurha_overlay_blush"

layeredimage urshu neutral:
    at [sprite_highlight('urshu'),ex_neutral]
    always:
        'images/characters/urshu/urshu_face_neutral.png'
layeredimage urshu neutral blush:
    at [sprite_highlight('urshu'),ex_neutral_blush]
    always:
        'images/characters/urshu/urshu_face_neutral.png'
    if day >= 0:
        'images/characters/urshu/urshu_overlay_blush.png'
layeredimage urshu happy:
    at [sprite_highlight('urshu'),ex_happy]
    always:
        'images/characters/urshu/urshu_face_happy.png'
    group overlay:
        attribute blush:
            "urshu_overlay_blush"
layeredimage urshu sad:
    at [sprite_highlight('urshu'),ex_sad]
    always:
        'images/characters/urshu/urshu_face_sad.png'
    group overlay:
        attribute blush:
            "urshu_overlay_blush"
layeredimage urshu angry:
    at [sprite_highlight('urshu'),ex_angry]
    always:
        'images/characters/urshu/urshu_face_angry.png'
    group overlay:
        attribute blush:
            "urshu_overlay_blush"
layeredimage urshu surprised:
    at [sprite_highlight('urshu'),ex_surprised]
    always:
        'images/characters/urshu/urshu_face_surprised.png'
    group overlay:
        attribute blush:
            "urshu_overlay_blush"

# define vivi images
image vivi neutral:
    At('images/characters/vivi/vivi neutral.png', sprite_highlight('vivi'))
    zoom 1.0
image vivi happy:
    At('images/characters/vivi/vivi happy.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 10
    linear 0.1 yoffset 0
    linear 0.2 yoffset 5
image vivi sad:
    At('images/characters/vivi/vivi sad.png', sprite_highlight('vivi'))
    zoom 1.01
    linear 0.5 yoffset 10
image vivi angry:
    At('images/characters/vivi/vivi angry.png', sprite_highlight('vivi'))
    zoom 1.01
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
image vivi surprised:
    At('images/characters/vivi/vivi surprised.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 20
    linear 0.2 yoffset 0
image vivi neutral blush:
    At('images/characters/vivi/vivi neutral blush.png', sprite_highlight('vivi'))
    zoom 1.01
image vivi happy blush:
    At('images/characters/vivi/vivi happy blush.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 10
    linear 0.1 yoffset 0
    linear 0.2 yoffset 5
image vivi sad blush:
    At('images/characters/vivi/vivi sad blush.png', sprite_highlight('vivi'))
    zoom 1.01
    linear 0.5 yoffset 10
image vivi angry blush:
    At('images/characters/vivi/vivi angry blush.png', sprite_highlight('vivi'))
    zoom 1.01
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
    linear 0.1 xoffset -2
    linear 0.1 xoffset 2
image vivi surprised blush:
    At('images/characters/vivi/vivi surprised blush.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 20
    linear 0.2 yoffset 0
image vivi floating_happy = At('images/characters/vivi/vivi_floating/vivi floating_happy.png', sprite_highlight('vivi'))
image vivi_conductor neutral:
    At('images/characters/vivi/vivi_conductor/vivi_conductor neutral.png', sprite_highlight('vivi'))
    zoom 1.0
image vivi_conductor happy:
    At('images/characters/vivi/vivi_conductor/vivi_conductor happy.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 10
    linear 0.1 yoffset 0
    linear 0.2 yoffset 5
image vivi_conductor surprised:
    At('images/characters/vivi/vivi_conductor/vivi_conductor surprised.png', sprite_highlight('vivi'))
    zoom 1.01 yoffset 20
    linear 0.2 yoffset 0

# define urshu dining images
image urshudining neutral = At('images/characters/urshu/urshu dining/urshu_neutral_table.png', sprite_highlight('urshudining'))
image urshudining happy = At('images/characters/urshu/urshu dining/urshu_happy_table.png', sprite_highlight('urshudining'))
image urshudining sad = At('images/characters/urshu/urshu dining/urshu_sad_table.png', sprite_highlight('urshudining'))
image urshudining angry = At('images/characters/urshu/urshu dining/urshu_angry_table.png', sprite_highlight('urshudining'))
image urshudining surprised = At('images/characters/urshu/urshu dining/urshu_surprised_table.png', sprite_highlight('urshudining'))
image urshudining neutral blush = At('images/characters/urshu/urshu dining/urshu_neutral_table_blush.png', sprite_highlight('urshudining'))
image urshudining happy blush = At('images/characters/urshu/urshu dining/urshu_happy_table_blush.png', sprite_highlight('urshudining'))
image urshudining sad blush = At('images/characters/urshu/urshu dining/urshu_sad_table_blush.png', sprite_highlight('urshudining'))
image urshudining angry blush = At('images/characters/urshu/urshu dining/urshu_angry_table_blush.png', sprite_highlight('urshudining'))
image urshudining surprised blush = At('images/characters/urshu/urshu dining/urshu_surprised_table_blush.png', sprite_highlight('urshudining'))




# define flash effect
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# define custom positions for sprites
transform center_left:
    xalign 0.2 yalign 1.0
transform center_right:
    xalign 0.8 yalign 1.0

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

init python:
    config.keymap['save_delete'].append('K_d') # Add D key for deleting saves

# add layer for eldritch overlay
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

init python:
    config.auto_voice = "audio/voice/{id}.ogg"

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
    pause 5.0
    stop sound fadeout 3.0
    pause 3.0

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