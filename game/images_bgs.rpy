# Define images for backgrounds and CGs.

label images_bgs:

    ###BG VFX OVERLAYS

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
