# The scene starts here.

label epi_eldritch_darius:

    # Epilogue/Eldritch/Darius Wrecker

    # The two paragraphs below are context
    # The mindflayer Darius could not forgive themselves for the atrocities they had been responsible for in life. Without a vehicle through which to reconcile their own actions, nor chance for atonement, the resentment they held only grew. In the end, Darius realized he became what he had grown to despise. Perhaps he always was. What he feared on the Express wasn't his master, but himself. His clean and perfectly groomed visage morphed and shifted, becoming the monstrous figure they so feared. Somewhere deep down he knew this was the fate fitting for him, a horror in body to reflect the monster within. 

    # The mindflayer Darius could not forgive themselves for the atrocities they had been responsible for in life. Without a vehicle through which to reconcile their own actions, nor chance for atonement, the resentment they held only grew. In the end, Darius realized he became what he had grown to despise. Perhaps he always was. He stared at his hands, clean and groomed, the horrors they had inflicted invisible to all but him. He couldn't take it, and his body responded in kind. He morphed and shifted, the hands he so despised growing, the fingers elongating. He grew and grew, his body cracking and bending under the stress, until he resembled the very horror he so feared. Somewhere deep down he knew this was the fate fitting for him, a nightmare in body to reflect the monster within. 

    stop music fadeout 2.0
    pause 2.0
    scene black with fade
    #play sound train loop fadein 1.0
    #play sound2 horror loop fadein 1.0

    #LOCATION: eldritchlandscape

    if att_meter_darius > 0:

        scene eldritch_darius with Fade(2,2,2)
        pause 2.0
        show urshu sad at left with dissolve:
            xzoom -1.0

        urshu sad "The illithid Darius could not forgive himself for the atrocities he had been responsible for in life."

        urshu sad "With neither a vehicle through which to reconcile his own actions, nor a chance for atonement, the resentment he held only grew. "

        urshu sad "In the end, Darius realized he became what he had grown to despise. Perhaps, he thought, he had always been this way."

        urshu sad "He stared at his hands, clean and groomed, the horrors they had inflicted invisible to all but him. He could not take it, and his body responded in kind."

        urshu sad "He morphed and shifted, the hands he so despised growing, the fingers elongating. He grew and grew, his body cracking and bending under the stress, until he resembled the very horror he so feared."
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu sad "Somewhere deep down, he knew this was a fitting fate for him—a nightmare in body to reflect the monster within."
        $ _skipping = True
    else:

        scene black with Fade(2,2,2)
        pause 2.0
        show urshu sad at center with dissolve:
            xzoom -1.0
        urshu sad "Darius retreated inward aboard the Ouroboros Express, neither giving into his grief nor opening up to the others. What better place for someone in such a transitory phase than the Express itself?"
        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False
        urshu "And so he found himself an unwitting passenger for yet another ride aboard, continuing in his quest to understand himself..."
        $ _skipping = True

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    
    return