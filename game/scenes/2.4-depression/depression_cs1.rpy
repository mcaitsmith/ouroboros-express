# The scene starts here.

label depression_cs1:

    # Character Selector 1

    # LOCATION: cabin
    # scene cabin with fade
    # call check_overlay_nofade from _call_check_overlay_nofade_1

    # show vivi neutral at left with dissolve

    vivithinking angry "I really wish he'd get off my back. I don't need this."
    vivithinking sad "I am sick of running around chasing my tail with no end in sight. It's exhausting."

    #<CHOICE>
    vivithinking neutral "I'm gonna get a drink. I'm sure I'm not the only one who'd want one."
    vivithinking "As Urshu said, the person I choose now won't be available later. They won't be able to see my final moments."
    menu:

        #OPTION 1
        "Avatar of Asha":

            $ fr1_depression_choice = "Ava"

            vivithinking neutral "Can a goddess get drunk? Let's find out."
            stop music fadeout 5.0
            stop ambience fadeout 1.0
            # JUMP TO: Free roam 1 / Avatar of Asha
            jump depression_fr1_ava

        #OPTION 2
        "Darius Wrecker":

            $ fr1_depression_choice = "Darius"

            vivithinking neutral "I wonder what Darius is like when they're drunk."
            stop music fadeout 5.0
            stop ambience fadeout 1.0
            #JUMP TO: Free roam 1 / Darius Wrecker
            jump depression_fr1_darius

        #OPTION 3
        "Susu'Rha Balrinn":

            $ fr1_depression_choice = "Susu'Rha"

            vivithinking neutral "Susu'Rha might like to get drunk with me."
            stop music fadeout 5.0
            stop ambience fadeout 1.0
            # JUMP TO: Free roam 1 / Susu'Rha Balrinn
            jump depression_fr1_susurha