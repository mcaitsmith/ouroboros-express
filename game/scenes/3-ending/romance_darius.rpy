# The scene starts here.

label romance_darius:

    #Romance/Darius Wrecker
    #LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0

    show darius surprised at center_right with dissolve:
        xpos 0.65
    show vivi happy at center_left with dissolve :
        xzoom -1
        xpos 0.35
    hide vivi
    hide darius
    show darius_vivi hug at center
    with { "master" : Dissolve(1.0) }
    pause 2.0

    # show darius surprised blush with dissolve
    show darius_vivi hug blush at center
    play music dariusmusic loop
    darius "Yes?"
    vivi happy blush "Yes."
    vivithinking happy blush "Their hands... those claws. He holds me so delicately."
    vivithinking happy blush "Like they'll never hurt anyone ever again."
    vivi neutral blush "I believe in you, Darius."
    vivi sad "I just wish we'd had a bit more time... seems like our final stop is approaching."
    # show darius happy -blush
    show darius_vivi hug at center
    darius happy "I'd take these brief moments with you over millennia of the sorry existence I had before."

    # VISUAL: the screen shakes, flickering
    play sound cineboom
    show observatory with hpunch
    show observatory with flash
    show observatory with flash

    vivithinking sad "The end... It's here... But I feel at peace." 
    vivithinking happy "Wherever you are, Urshu — thank you."
    stop music fadeout 5.0

    # VISUAL: screen fades to black  
    stop ambience fadeout 1.0
    scene black with fade

    show urshu happy at center with dissolve

    urshu happy "Goodness me, that went much better than I expected for Mr. Wrecker and Miss Sanssouci."
    urshu neutral "I must admit, there were a few close misses. Ah, love. It seems such a shame for their story to end here..."
    urshu neutral "..."
    urshu happy "But now, what kind of conductor would I be if I couldn't arrange an alternate journey for my passengers? Oh dear, I've become quite the romantic fool in my old age..."
    play music finalemusic loop

    # VISUAL: screen fades to white
    scene white with Dissolve(3.0)
    # LOCATION: terminalofdreams
    scene terminalofdreams with Dissolve(2.0)
    play ambience amb_terminal fadein 2.0
    pause 1.0
    show darius happy at center_right with dissolve:
        xpos 0.65
    show vivi happy at center_left with dissolve :
        xzoom -1
        xpos 0.35

    vivi surprised "What— Where are we? Darius?"
    darius surprised "Vivi... I-I don't believe it. Haha!"
    vivithinking surprised "He's laughing?"
    vivi surprised "What is this place?"
    darius happy "You know, I think Urshu had a few cards up his sleeve. We're somewhere {i}new{i}."
    vivi happy "Wait... Are you saying we have a second chance? A fresh start?"
    darius neutral "You know better than to ask such a silly question, Miss Sanssouci." 
    darius happy "Don't wait about, my love; let's go explore. I don't intend to make a mess of it this time."
    vivi happy "I'm with you."

    stop ambience fadeout 3.0
    scene white with Dissolve(3.0)

    # ROMANCE JOURNAL ENTRY
    $ message = "I can't believe I'm saying this, but\nI think I'm in love.\nMaybe it's the threat of swirling\ninto nothingness,\nbut I've truly found someone special.\nThey're smart and charming but\nmost of all, kind.\nIt takes a strong person to defy their god\nand risk eternal damnation to do\nwhat's right.\nAcceptance is a hard thing to find but\nwe've found it in each other.\nI feel like I'm back in middle school, smiling\nas I write this, but I can't help it!"

    # Journal entry with degradation meter high
    call display_journal from _call_display_journal_9

    #To Epilogues according to attraction meters
    # ??ATTRACTION
    if att_meter_ava >= romance_threshold:
        call epi_friend_ava from _call_epi_friend_ava
    else:
        call epi_eldritch_ava from _call_epi_eldritch_ava
    # ??ATTRACTION
    if att_meter_susurha >= romance_threshold:
        call epi_friend_susurha from _call_epi_friend_susurha_1
    else:
        call epi_eldritch_susurha from _call_epi_eldritch_susurha_1

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