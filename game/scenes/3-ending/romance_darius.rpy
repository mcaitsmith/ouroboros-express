﻿# The scene starts here.

label romance_darius:

    #Romance/Darius Wrecker
    #LOCATION: observatory
    scene observatory with fade

    show darius surprised at right with dissolve
    show vivi happy at left with dissolve 

    show darius surprised blush with dissolve
    darius "Yes?"
    vivi happy blush "Yes."
    vivithinking happy blush "Their hands... Those claws. He holds me so delicately."
    vivithinking happy blush "Like they'll never hurt anyone ever again."
    vivi neutral blush "I believe in you, Darius."
    vivi sad "I just wish we'd had a bit more time... Seems like our final stop is approaching."
    show darius happy -blush
    darius happy "I'd take these brief moments with you over millennia of the sorry existence I had before."

    # VISUAL: the screen shakes, flickering
    show observatory with hpunch
    show observatory with flash
    show observatory with flash

    vivithinking sad "The end... It's here... But I feel at peace." 
    vivithinking happy "Wherever you are, Urshu--thank you."

    # VISUAL: screen fades to black  
    scene black with fade

    show urshu happy at center with dissolve

    urshu happy "Goodness me, that went much better than I expected for Mr. Wrecker and Miss Sanssouci."
    urshu neutral "I must admit, there were a few close misses. Ah, love. It seems such a shame for their story to end here..."
    urshu neutral "..."
    urshu happy "But now, what kind of conductor would I be if I couldn't arrange an alternate journey for my passengers? Oh dear, I've become quite the romantic fool in my old age..."

    # VISUAL: screen fades to white
    scene white with Dissolve(3.0)
    # LOCATION: terminalofdreams

    vivi surprised "What-- Where are we? Darius?"
    darius surprised "Vivi... I-I don't believe it. Haha!"
    vivithinking surprised "He's laughing?"
    vivi surprised "What is this place?"
    darius happy "You know, I think Urshu had a few cards up his sleeve. We're somewhere {i}new{i}."
    vivi happy "Wait... Are you saying we have a second chance? A fresh start?"
    darius neutral "You know better than to ask a silly question, Miss Sanssouci." 
    darius happy "Don't wait about, my love; let's go explore. I don't intend to make a mess of it this time."
    vivi happy "I'm with you."


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

    scene black with Dissolve(3.0)
    window hide fade
    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 3.0

    # end game
    return