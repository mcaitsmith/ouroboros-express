# The scene starts here.

label denial_cs1:

    #Character Selector 1

    #LOCATION: cabin
    # scene cabin with fade

    # show vivi neutral at left with dissolve

    vivi neutral "This is all so much to process. I can't breathe. I need to talk to one of the other passengers. They might know what's going on here."

    # <CHOICE>
    vivi neutral "But which passenger should I talk to?"

    menu:

    # OPTION 1
        "Avatar of Asha":

            $ fr1_denial_choice = "Ava"

            vivi happy "Who better to help me than a goddess? She's gotta know where this train is going and how to get off. I think she's in the observatory."
            #JUMP to Free roam 1 / Avatar of Asha
            jump denial_fr1_ava

    # OPTION 2
        "Darius Wrecker":

            $ fr1_denial_choice = "Darius"

            vivi happy "That Darius looks like they would understand what's going on. Maybe they know where this train is going. I think they're in the lounge."
            #JUMP TO: Free roam 1 / Darius Wrecker
            jump denial_fr1_darius

    # OPTION 3
        "Susu'Rha Balrinn":

            $ fr1_denial_choice = "Susu'Rha"

            vivi happy "The druid seemed easy to talk to. Maybe they can help me figure out what's going on. I think they're in the dining car."
            #JUMP to Free roam 1 / Susu'Rha Balrinn
            jump denial_fr1_susurha