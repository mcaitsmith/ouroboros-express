# The scene starts here.

label bargaining_cs1:

    #Character Selector 1

    # LOCATION: cabin
    scene cabin with fade

    show vivi happy at left with dissolve:
        xzoom -1

    vivithinking "Okay. Let's think, Vivi. How am I gonna satisfy the conductor?"

    show vivi neutral blush at left

    vivithinking "Ahem... With a meal, I mean."

    show vivi neutral at left

    # <CHOICE>
    vivithinking "I need to figure out Urshu's likes and dislikes. Hopefully one of my fellow passengers knows something. But which one?"

    menu:
        # OPTION 1
        "Avatar of Asha":

            $ fr1_bargaining_choice = "Ava"

            vivithinking "I'm sure the goddess can help me out."

            hide vivi with dissolve
    
            # JUMP TO: Free Roam 1 / Ava
            jump bargaining_fr1_ava

        # OPTION 2
        "Darius Wrecker":

            $ fr1_bargaining_choice = "Darius"

            vivithinking "Darius must've gleaned something from the conductor's emotions."

            hide vivi with dissolve
        
            # JUMP TO: Free roam 1 / Darius
            jump bargaining_fr1_darius

        #OPTION 3
        "Susu'Rha Balrinn":

            $ fr1_bargaining_choice = "Susu'Rha"

            vivithinking "Susu'Rha is probably the friendliest with Urshu. They must know something."

            hide vivi with dissolve

            # JUMP TO: Free roam 1 / susurha
            jump bargaining_fr1_susurha