﻿# The scene starts here.

label anger_cs1:

    #Character Selector 1

    # LOCATION: cabin
    # scene cabin with fade
    # call check_overlay_nofade from _call_check_overlay_nofade
    play ambience amb_bedroom if_changed fadein 1.0

    # show vivi neutral at left with dissolve

    vivi neutral "Alright. Time to play. What better to do when trapped on a train speeding towards impending doom."

    # <CHOICE>
    vivi neutral "Who can I talk to?"

    menu:
        # OPTION 1
        "Avatar of Asha":

            $ fr1_anger_choice = "Ava"

            vivi neutral "Maybe the goddess would like a game. It'd be nice to talk to her more."
            stop ambience fadeout 1.0
            # JUMP TO: FREE ROAM 1 - Ava
            jump anger_fr1_ava

        # OPTION 2
        "Darius Wrecker":

            $ fr1_anger_choice = "Darius"

            vivi neutral "I want to know more about Darius. Maybe they'd be up for a game."
            stop ambience fadeout 1.0
            # JUMP TO: FREE ROAM 1 - DARIUS
            jump anger_fr1_darius

        # OPTION 3
        "Susu'Rha Balrinn":

            $ fr1_anger_choice = "Susu'Rha"

            vivi neutral "I'm sure Susu'Rha would like a game. They seem to make things more fun."
            stop ambience fadeout 1.0
            # JUMP TO: FREE ROAM 1 - SUSU'RHA
            jump anger_fr1_susurha