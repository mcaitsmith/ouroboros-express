label epi_imperfect_friendship:
    # Scene unlocked when the player rejects 1 or 2 romance attempts.
    # Vivi has rejected 1 or 2 lovers. Urshu shows Vivi to the observatory. She has 30 seconds to say goodbye, before she departs to the next place.
    
    # LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1
    show urshu neutral at right with dissolve
    
    vivithinking neutral "This place always feels so fuzzy."
    urshu "Well, the time has come to clock out. Another spiral of theatrics and redemption closed."
    vivi sad "You must be exhausted going through this again and again, for all eternity?"
    urshu "I like you when you're caring, Miss Sansoucci. But enough about me. How does it feel?"
    vivi "Feel to what?"
    urshu "Finding that light at the end of the tunnel. At times, I was not sure you would make it! You've drifted and messed around a couple of times! Delicious!"
    urshu "So, how does it feel?"
    vivi "I feel...fresh. But I'm also tired. How long is left?"
    urshu happy "Thirty seconds."
    play music finalemusic loop
    vivi surprised "Are you kidding me?"
    
    # VISUAL: screen starts flashing white
    show white:
        alpha 0.0
        linear 1 alpha 0.3
        linear 1 alpha 0.6
        linear 1 alpha 0.8
        linear 0.2 alpha 0.4
        linear 0.2 alpha 0.8
        flicker_opacity
        linear 0.6 alpha 0.5
    urshu "Any time now! Look at you, you're starting to float! See?"
    with hpunch
    vivi "What? No! What, what, what?"
    # show vivi surprised blush with disRsolve:
    show vivi floating_happy with dissolve:
        linear 4 ypos 1100 xpos 700
        linear 4 ypos 1000 xpos 200
        linear 4 ypos 1200 xpos 500
        repeat 2
        linear 4  ypos 1380 xpos 200
    # vivithinking surprised blush "I'm drifting like an astronaut!"
    vivi "I'm drifting like an astronaut!"
    show white:
        linear 0.6 alpha 0.55
    vivi "..."
    show white:
        linear 0.6 alpha 0.6
    # vivithinking happy "It's warm. I feel like curling up like a cat and purring myself to infinity..."
    vivi "It's warm. I feel like curling up like a cat and purring myself to infinity..."
    urshu "Hey! Any last words to your conductor?"
    show white:
        linear 0.6 alpha 0.65
    vivi "..."
    urshu sad "Come on, Vivi. For posterity!"
    vivi "..."
    # vivi happy "I hate you, ahaha!!"
    vivi "I hate you, ahaha!!"
    vivi "So long, DUMBASS!"
    
    hide vivi with dissolve
    
    urshu neutral "What a beautiful laugh."
    scene white with Dissolve(3.0)
    
    # VISUAL: Fade to white
    
    #To Epilogues according to attraction meters
    # ??ATTRACTION
    if att_meter_ava >= romance_threshold:
        call epi_friend_ava from _call_epi_friend_ava_2
    else:
        call epi_eldritch_ava from _call_epi_eldritch_ava_2
    # ??ATTRACTION
    if att_meter_darius >= romance_threshold:
        call epi_friend_darius from _call_epi_friend_darius_2
    else:
        call epi_eldritch_darius from _call_epi_eldritch_darius_2
    # ??ATTRACTION
    if att_meter_susurha >= romance_threshold:
        call epi_friend_susurha from _call_epi_friend_susurha_2
    else:
        call epi_eldritch_susurha from _call_epi_eldritch_susurha_2

    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with Dissolve(3.0)
    window hide fade
    $ quick_menu = False # hide quick menu
    $ _game_menu_screen = None # disable menu
    play music creditsmusicgood loop
    call screen credits
    stop music fadeout 3.0
    pause 3.0

    # end game
    return