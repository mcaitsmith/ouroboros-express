# The scene starts here.

label romance_ava:

    # Romance/Avatar of Asha
    #A heartfelt interaction as you both hold each other in the face of the end. Darkness, and then a bright light. You hear the train conductor's sigh. "I'm a romantic fool." A chance to begin again... together...

    # LOCATION: observatory
    scene observatory with fade

    show vivi neutral at left with dissolve:
        xzoom -1
    show ava neutral at right with dissolve

    show ava sad blush with dissolve
    ava "Now, take my hand, Vivi." 
    ava "Hold me close for our last dance."
    vivi neutral blush "Aren't you afraid?"
    show ava happy blush
    ava "Not anymore."
    vivi surprised "Oh, Ava! Are you crying?"
    ava "Yes, but with joy. Hold me close. Close your eyes. We will be in this moment forever."
    vivi "Yes. Forever. Praise Ava."

    # EFFECT: fade to white
    scene white with Dissolve(3.0)

    # ROMANCE JOURNAL ENTRY
    $ message = "I can't believe I'm saying this, but\nI think I'm in love.\nMaybe it's the threat of swirling into nothingness\nbut I've truly found someone special.\nShe's regal and majestic and... She opened up to me.\nNot in the way people talk when I'm reporting.\nIt's different. More intimate.\nI feel I truly know her fears and dreams.\nI can open up to her and she sees me.\nShe sees me!\nI feel like I'm back in middle school, smiling\nas I write this, but I can't help it!"

    # Journal entry with degradation meter high
    call display_journal from _call_display_journal_8

    # To Epilogues according to attraction meters
    # ??ATTRACTION
    if att_meter_darius >= romance_threshold:
        call epi_friend_darius from _call_epi_friend_darius
    elif att_meter_darius > 0:
        call epi_eldritch_darius from _call_epi_eldritch_darius
    # ??ATTRACTION
    if att_meter_susurha >= romance_threshold:
        call epi_friend_susurha from _call_epi_friend_susurha
    elif att_meter_susurha > 0:
        call epi_eldritch_susurha from _call_epi_eldritch_susurha

    scene black with Dissolve(3.0)
    window hide fade
    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 3.0

    # end game
    return