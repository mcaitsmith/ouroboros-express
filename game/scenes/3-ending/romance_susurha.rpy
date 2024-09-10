# The scene starts here.

label romance_susurha:

    #Romance/Susu'Rha Balrinn
    # A heartfelt interaction as you both hold each other in the face of the end. Darkness, and then a bright light. You hear the train conductor's sigh. "I'm a romantic fool." A chance to begin again... together...

    #LOCATION: observatory
    scene observatory with fade

    show vivi neutral blush at center_left with dissolve:
        xzoom -1
    show susurha happy blush at center_right with dissolve

    vivi neutral blush  "Can you feel it? We're approaching our final stop."
    susurha "Come into my arms. There."
    # show vivi neutral blush:
    #     linear 1.0 xpos 480
    # show susurha happy blush:
    #     linear 1.0 xpos 1560
    show vivi neutral blush with dissolve:
        xpos 0.35
    show susurha happy blush with dissolve:
        xpos 0.65
    hide vivi
    hide susurha
    show susu_vivi hug at center
    with { "master" : Dissolve(1.0) }
    pause 2.0

    susurha "We can merge with each other as we merge with the cosmic weave."
    vivi neutral blush "It's getting brighter..."

    # VISUAL: the screen shakes
    show observatory with hpunch
    # VISUAL: the scene brightens
    show observatory at bright with dissolve

    show susu_vivi hug blush at center

    vivi happy blush "This is all so much. I may cry."
    vivi happy blush "It's awfully bright... I can hardly see."
    susurha "I'm here, Vivi. I've got you."
    vivi happy "I don't know where you end and I begin!"
    susurha happy "I don't either! And I don't know what awaits us, but if this is to be my final moment, I couldn't have asked for a better way to spend it than with you, Vivienne."
    vivi happy blush "Me, too."
    vivi happy blush "I want to be with you forever." 
    vivi happy blush "What if forever is only now?"
    vivi happy blush "Then I want to be with you forever, now."

    #EFFECT: fade to white
    scene white with Dissolve(3.0)

    # ROMANCE JOURNAL ENTRY
    $ message = "I can't believe I'm saying this, but\nI think I'm in love.\nMaybe it's the threat of swirling\ninto nothingness\nbut I've truly found someone special.\nThey're funny and positive. It's a breath\nof fresh air.\nI think the thing I love most is\nSusu'Rha's heart.\nThey're the kindest being I've ever met.\nIt feels like a warm hug\nwhenever they speak.\nI feel like I'm back in middle school, smiling\nas I write this, but I can't help it!"

    # Journal entry with degradation meter high
    call display_journal from _call_display_journal_10

    #To Epilogues according to attraction meters
    if att_meter_ava >= romance_threshold:
        call epi_friend_ava from _call_epi_friend_ava_1
    else:
        call epi_eldritch_ava from _call_epi_eldritch_ava_1
    # ??ATTRACTION
    if att_meter_darius >= romance_threshold:
        call epi_friend_darius from _call_epi_friend_darius_1
    else:
        call epi_eldritch_darius from _call_epi_eldritch_darius_1

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene black with Dissolve(3.0)
    window hide fade
    $ quick_menu = False # hide quick menu
    $ _game_menu_screen = None # disable menu
    play music goodendmusic volume 0.5
    call screen credits
    stop music fadeout 3.0
    pause 3.0

    # end game
    return