# The scene starts here.

label bargaining_cs2:

    #Character Selector 2

    # LOCATION: cabin
    scene cabin with fade

    show vivi angry at left with dissolve:
        xzoom -1

    vivithinking "Ughhhh. I've spent all morning trying to learn about Urshu but found NOTHING useful."

    show vivi neutral at left

    vivithinking "I guess I'm gonna have to wing it. Urshu better get ready for a meal greater than any he's had for eons."

    show vivi surprised at left

    #<CHOICE>
    vivithinking "On second thought, I could use some help in the kitchen. Now, who can help me?"

    menu:

        # OPTION 1
        "Avatar of Asha" if fr1_bargaining_choice != "Ava":

            $ fr2_bargaining_choice = "Asha"

            show vivi neutral at left

            vivithinking "I could use the palate of a goddess. Nothing but the best, right?"
        
            # JUMP TO: Free roam 2 / Ava
            jump bargaining_fr2_ava

        # OPTION 2
        "Darius Wrecker" if fr1_bargaining_choice != "Darius":

            $ fr2_bargaining_choice = "Darius"

            show vivi neutral at left

            vivithinking "Darius would be an excellent sous chef. Those deft hands of his would work wonders in the kitchen."

            # JUMP TO: Free roam 2 / Darius
            jump bargaining_fr2_darius

        # OPTION 3
        "Susu'Rha Balrinn" if fr1_bargaining_choice != "Susu'Rha":

            $ fr2_bargaining_choice = "Susu'Rha"

            show vivi neutral at left

            vivithinking "Susu'Rha could definitely help me win over the conductor."

            # JUMP TO: Free roam 2 / Susu'Rha
            jump bargaining_fr2_susurha