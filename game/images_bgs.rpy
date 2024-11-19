# Define images for backgrounds and CGs.

label images_bgs:

    ###BG VFX OVERLAYS

    image cabin_light_overlay:
        "images/backgrounds/vfx/cabin_lamps.png"
        alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        pause 5.0
        linear 2.0 alpha 1.0 matrixcolor BrightnessMatrix(0.4)
        linear 2.0 alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        repeat

    image diningcar_light_overlay:
        "images/backgrounds/vfx/diningcar_light.png"
        alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        pause 5.0
        linear 2.0 alpha 1.0 matrixcolor BrightnessMatrix(0.4)
        linear 2.0 alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        repeat

    image lounge_light_overlay:
        "images/backgrounds/vfx/lounge_lamps.png"
        alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        pause 5.0
        linear 2.0 alpha 1.0 matrixcolor BrightnessMatrix(0.4)
        linear 2.0 alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        repeat

    image observatory_light_overlay:
        "images/backgrounds/vfx/observatory_lamp.png"
        alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        pause 5.0
        linear 2.0 alpha 1.0 matrixcolor BrightnessMatrix(0.4)
        linear 2.0 alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        repeat
    image observatory_stars1_overlay:
        "images/backgrounds/vfx/observatory_stars1.png"
        # alpha 0.0 matrixcolor BrightnessMatrix(0.0)
        alpha 0.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0)
        # linear 2.0 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(1.5) * SaturationMatrix(1.0)
        linear 2.0 alpha 1.0 matrixcolor TintMatrix("#e031d4") * BrightnessMatrix(1.5) * SaturationMatrix(2.0)
        # linear 2.0 alpha 0.0 matrixcolor  TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0)
        linear 2.0 alpha 0.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0)
        repeat
    image observatory_stars2_overlay:
        "images/backgrounds/vfx/observatory_stars2.png"
        alpha 0.5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.75) * SaturationMatrix(1.5)
        linear 1.0 alpha 1.0 matrixcolor TintMatrix("#34e031") * BrightnessMatrix(1.5) * SaturationMatrix(2.0)
        linear 2.0 alpha 0.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0)
        linear 1.0 alpha 0.5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.75) * SaturationMatrix(1.5)
        repeat
    image observatory_stars3_overlay:
        "images/backgrounds/vfx/observatory_stars3.png"
        alpha 1.0 matrixcolor TintMatrix("#319de0") * BrightnessMatrix(1.5) * SaturationMatrix(2.0)
        linear 2.0 alpha 0.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0)
        linear 2.0 alpha 1.0 matrixcolor TintMatrix("#319de0") * BrightnessMatrix(1.5) * SaturationMatrix(2.0)
        repeat

    image terminalofdreams_dust1_overlay:
        "images/backgrounds/vfx/terminal_dust1.png"
        alpha 1.0 matrixcolor BrightnessMatrix(1.0)
        linear 1.5 alpha 0.0
        linear 1.5 alpha 1.0
        linear 1.5 alpha 0.0
        linear 1.5 alpha 1.0
        repeat
    image terminalofdreams_dust2_overlay:
        "images/backgrounds/vfx/terminal_dust2.png"
        alpha 0.0 matrixcolor BrightnessMatrix(1.5)
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
    
    # mote effect for title screen
    transform mote_fade:
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
    transform mote_fade2:
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        repeat
    transform mote_fade3:
        alpha 0.5
        linear 0.5 alpha 1.0
        linear 1.0 alpha 0.0
        linear 0.5 alpha 0.5
        repeat
    image title_motes = SnowBlossom(At("images/backgrounds/vfx/mote.png",mote_fade), count=30, border=10, xspeed=(100, -100), yspeed=(100,-100), fast=True)
    image title_motes2 = SnowBlossom(At("images/backgrounds/vfx/mote.png",mote_fade2), count=30, border=10, xspeed=(100, -100), yspeed=(100,-100), fast=True)
    image title_motes3 = SnowBlossom(At("images/backgrounds/vfx/mote.png",mote_fade3), count=30, border=10, xspeed=(100, -100), yspeed=(100,-100), fast=True)


    # flicker effect for title screen (not currently used)
    # transform title_flicker:
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.4) * TintMatrix("#fae388")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.6) * TintMatrix("#ffffff")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.6) * TintMatrix("#fbefc0")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.6) * TintMatrix("#ffffff")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.8) * TintMatrix("#fae388")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     pause 0.1
    #     linear 0.0 matrixcolor SaturationMatrix(0.8) * TintMatrix("#ffffff")
    #     pause 0.05
    #     linear 0.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    #     repeat

    # define SLS logo image
    # image splashlogo = "images/logo.png"
    image splashlogo = Movie(channel="movie_dp", loop = False, play = 'images/SLS_Logo.mpg')

    # define blurred background images
    image cabin blur = im.Blur("images/backgrounds/cabin.png", 5)
    image observatory blur = im.Blur("images/backgrounds/observatory.png", 5)
    image lounge blur = im.Blur("images/backgrounds/lounge.png", 5)
    image diningcar blur = im.Blur("images/backgrounds/diningcar.png", 5)

    # define decay overlay bg images
    layeredimage cabin:
        subpixel True
        always:
            "images/backgrounds/cabin.png"
        group light:
            attribute overlay default
        if day == 2:
            "decay_bedroom_1"
        elif day == 3:
            "decay_bedroom_2"
        elif day == 4 or day == 6:
            "decay_bedroom_3"
    layeredimage observatory:
        subpixel True
        always:
            "images/backgrounds/observatory.png"
        group light:
            attribute overlay default
        group stars1:
            attribute overlay default
        group stars2:
            attribute overlay default
        group stars3:
            attribute overlay default
        if day == 2:
            "decay_observatory_1"
        elif day == 3:
            "decay_observatory_2"
        elif day == 4 or day == 6:
            "decay_observatory_3"
    layeredimage lounge:
        subpixel True
        always:
            "images/backgrounds/lounge.png"
        group light:
            attribute overlay default
        if day == 2:
            "decay_lounge_1"
        elif day == 3:
            "decay_lounge_2"
        elif day == 4 or day == 6:
            "decay_lounge_3"
    layeredimage diningcar:
        subpixel True
        always:
            "images/backgrounds/diningcar.png"
        group light:
            attribute overlay default
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

    # VFX FOR CGS

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

    # define white background
    image white = "#ffffff"

    return
