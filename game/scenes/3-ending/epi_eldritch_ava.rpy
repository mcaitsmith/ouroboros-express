# The scene starts here.

label epi_eldritch_ava:

    stop music fadeout 1.0
    pause 1.0
    play sound train loop

    #Epilogue/Eldritch/Avatar of Asha
    #LOCATION: eldritchlandscape
    scene black with fade
    show urshu sad at center with dissolve

    if att_meter_ava > 0:
        urshu sad "Alas, our goddess of the sun, Avatar of the Eternal Light, collapsed under the unbearable weight of her self-imposed hatred and inescapable emptiness." 
        urshu angry "Unable to connect, cut off from love, burning with pain as sharp as a scalpel, our lovely Avatar exploded into a supernova of fury and regret." 
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu sad "Soon after, her darkness reunited itself in the void as a ravenous Plutonian maw; a cosmic Eldritch whirlpool slaughtering all who crossed its path—just as she was slaughtered long ago."
        $ _skipping = True
    else:
        urshu sad "The Avatar of Asha retreated inward aboard the Ouroboros Express, neither giving into her grief nor opening up to the others. What better place for someone in such a transitory phase than the Express itself?"
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu "And so she found herself an unwitting passenger for yet another ride aboard, continuing in her quest to understand herself..."
        $ _skipping = True

    # VISUAL: Ava as a cosmic horror in eldritch landscape

    return
