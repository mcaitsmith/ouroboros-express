# The scene starts here.

label epi_eldritch_ava:

    stop music fadeout 2.0
    pause 2.0
    scene black with fade
    play sound train loop fadein 1.0
    play sound2 horror loop fadein 1.0

    #Epilogue/Eldritch/Avatar of Asha
    #LOCATION: eldritchlandscape

    if att_meter_ava > 0:

        scene eldritch_asha with Fade(2,2,2)
        pause 2.0
        show urshu sad at left with dissolve:
            xzoom -1.0

        urshu sad "Alas, our goddess of the sun, Avatar of the Eternal Light, collapsed under the unbearable weight of her self-imposed hatred and inescapable emptiness." 
        urshu angry "Unable to connect, cut off from love, burning with pain as sharp as a scalpel, our lovely Avatar exploded into a supernova of fury and regret." 
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu sad "Soon after, her darkness reunited itself in the void as a ravenous Plutonian maw; a cosmic Eldritch whirlpool slaughtering all who crossed its path—just as she was slaughtered long ago."
        $ _skipping = True
    else:

        scene black with Fade(2,2,2)
        pause 2.0
        show urshu sad at center with dissolve:
            xzoom -1.0
            
        urshu sad "The Avatar of Asha retreated inward aboard the Ouroboros Express, neither giving into her grief nor opening up to the others. What better place for someone in such a transitory phase than the Express itself?"
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu "And so she found herself an unwitting passenger for yet another ride aboard, continuing in her quest to understand herself..."
        $ _skipping = True

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0

    # VISUAL: Ava as a cosmic horror in eldritch landscape

    return
