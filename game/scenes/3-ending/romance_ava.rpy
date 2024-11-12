# The scene starts here.

label romance_ava:

    # Romance/Avatar of Asha
    #A heartfelt interaction as you both hold each other in the face of the end. Darkness, and then a bright light. You hear the train conductor's sigh. "I'm a romantic fool." A chance to begin again... together...

    # LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0

    show vivi neutral at center_left with dissolve:
        xzoom -1
    show ava neutral at center_right with dissolve

    show ava sad blush with dissolve
    ava "Now, take my hand, Vivi." 
    play music ashamusic loop fadein 3.0
    stop ambience fadeout 1.0
    ava "Hold me close for our last dance."
    show vivi neutral with dissolve:
        # xpos 0.5
        # linear 0.5 xpos 0.35
        xpos 0.35
    show ava sad blush with dissolve:
        # xpos 0.5
        # linear 0.5 xpos 0.65
        xpos 0.65
    hide vivi
    hide ava
    show asha_vivi hug at center
    with { "master" : Dissolve(1.0) }
    pause 2.0

    vivi neutral blush "Aren't you afraid?"
    # show ava happy blush
    show asha_vivi hug blush at center
    ava "Not anymore."
    vivi surprised "Oh, Ava! Are you crying?"
    ava "Yes, but with joy. Hold me close. Close your eyes. We will be in this moment forever."
    vivi "Yes. Forever. Praise Ava."

    # EFFECT: fade to white
    scene white with Dissolve(3.0)

    # ROMANCE JOURNAL ENTRY
    $ message = "I can't believe I'm saying this, but\nI think I'm in love.\nMaybe it's the threat of swirling\ninto nothingness\nbut I've truly found someone special.\nShe's regal and majestic and...\nShe opened up to me.\nNot in the way people talk when I'm\nreporting. It's different. Intimate.\nI feel I truly know her fears and dreams.\nI can open up to her and she sees me.\nShe sees me!\nI feel like I'm back in middle school, smiling\nas I write this, but I can't help it!"

    # Journal entry with degradation meter high
    call display_journal from _call_display_journal_8

    # To Epilogues according to attraction meters
    # ??ATTRACTION
    if att_meter_darius >= romance_threshold:
        call epi_friend_darius from _call_epi_friend_darius
    else:
        call epi_eldritch_darius from _call_epi_eldritch_darius
    # ??ATTRACTION
    if att_meter_susurha >= romance_threshold:
        call epi_friend_susurha from _call_epi_friend_susurha
    else:
        call epi_eldritch_susurha from _call_epi_eldritch_susurha

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