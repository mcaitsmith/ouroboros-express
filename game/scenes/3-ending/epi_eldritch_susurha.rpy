# The scene starts here.

label epi_eldritch_susurha:

    #Epilogue/Eldritch/Susu'Rha Balrinn
    #Naj's note: this should just be a brief description - about 100 words, if that. Kind of like the slides at the end of Fallout, but it'll be from Urshu's perspective  and they'll be against a black background.

    stop music fadeout 2.0
    pause 2.0
    scene black with fade
    #play sound train loop fadein 1.0
    #play sound2 horror loop fadein 1.0

    #LOCATION: eldritchlandscape

    if att_meter_susurha > 0:

        scene eldritch_susurha with Fade(2,2,2)
        play cd_ambience amb_cosmicdecay if_changed fadein 1.0
        play music sorrowmusic if_changed loop
        pause 2.0
        show urshu sad at left with dissolve:
            xzoom -1.0

        urshu sad "Despite the rebel prince's burning desire to live free, they could not escape the guilt that bound them to their past decisions."

        urshu sad "This growing rumination metastasized into their personal horror, who chained them at the wrists and ankles and dragged them into the furthest depths of the Dark Beyond."

        urshu sad "Muzzled so they would never again sing, scaled in nightmares so they would never again gladden or cheer, they became the very thing that haunted them..."
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu sad "...a grotesque prisoner, devoid of agency or expression, doomed to suffer for all eternity."
        play sound char_mirror
        pause 8.0
        $ _skipping = True
    else:

        scene black with Fade(2,2,2)
        pause 2.0
        show urshu sad at center with dissolve:
            xzoom -1.0
        urshu sad "Susu'Rha retreated inward aboard the Ouroboros Express, neither giving into their grief nor opening up to the others. What better place for someone in such a transitory phase than the Express itself?"
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu "And so they found themselves an unwitting passenger for yet another ride aboard, continuing in their quest to understand themselves..."
        $ _skipping = True

    stop cd_ambience fadeout 1.0
    stop music fadeout 5.0

    return

