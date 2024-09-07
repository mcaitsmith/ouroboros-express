# The scene starts here.

label anger_cs2:

    #Character Selector 2

    # LOCATION: cabin
    call check_overlay
    scene cabin with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking angry "I feel like I'm getting nowhere! How the hell am I supposed to escape this?"

    vivithinking neutral "I can already see the outside affecting the train. There are black tendrils wrapping around the outside of the cars. And those noises! They're awful. It sounds like demonic whales fighting. This whole place is slowly dissolving into... I don't know, and I don't wanna find out."

    vivithinking neutral "I need some time to make a plan of escape."

    # fade out

    # fade in
    show cabin with fade

    vivithinking angry "I can't think straight! My mind is a mess. I need to cool off if there's any chance of me creating a solid plan."

    # <CHOICE>
    vivithinking neutral "I think I saw a dartboard in the dining car. It may be a good way to blow off some steam. Maybe I can get a fellow passenger to join me. Competition always helps me think clearer."

    menu:
        # OPTION 1 
        "Avatar of Asha" if fr1_anger_choice != "Ava":

            vivi neutral "Let's see how good the goddess is at darts, shall we?"
            # JUMP TO: Free Roam 2 / Ava
            jump anger_fr2_ava

        #OPTION 2 
        "Darius Wrecker" if fr1_anger_choice != "Darius":

            vivi neutral "Darius seems like good competition."
            # JUMP TO: Free Roam 2 / Darius 
            jump anger_fr2_darius

        # OPTION 3 
        "Susu'Rha Balrinn" if fr1_anger_choice != "Susu'Rha":

            vivi neutral "I'm sure Susu'Rha would be down for a little competition."
            # JUMP TO: Free Roam 2 / Susurha
            jump anger_fr2_susurha