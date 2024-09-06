# The scene starts here.

label depression_debrief:

    # Debrief Depression

    # LOCATION: cabin
    scene cabin with fade

    # ??ATTRACTION
    if att_meter_ava >= romance_threshold or att_meter_darius >= romance_threshold or att_meter_susurha >= romance_threshold:

        show vivi neutral at left with dissolve:
            xzoom -1

        # SOUND: knocking
        play sound knock
        pause 1.0

        show urshu neutral at right with dissolve

        urshu neutral "I trust you had a good evening?"

        vivi happy "Yeah, it was nice."
        vivi neutral "About what you said before. Writing my own story... I think I'm starting to understand."
        urshu happy "I live to serve, Miss Sanssouci."
        vivi neutral "You know you're a cosmic entity, right? No need to be so formal with me."
        urshu happy "As you wish."
        vivi neutral "Hey Urshu, before you go, can I ask you something?"
        vivi neutral "Why'd you put us four together?"
        urshu happy "Maybe it was preordained. Maybe it was random. Or maybe, I think you four just fit together. I do love puzzles after all."
        vivi neutral "You've been quite the conductor, Urshu."
        urshu neutral "And you have been quite the puzzle."
        urshu neutral "Enjoy your final night here."
        vivi sad "It's really ending, huh?"
        urshu happy "All may not be as lost as you think."
        vivi happy "Goodnight, Urshu."
        urshu happy "Goodnight, Vivienne."

        hide urshu with dissolve
        
        vivithinking neutral "My mind is buzzing. I need to write."

        play sound writing

        $ message = "Wow.\nAt the beginning of all this, I would've\nnever thought I'd get to know some of\nthe other passengers this well.\nWe're all more similar than I thought.\nEven Urshu, believe it or not.\n\nTime is weird here.\nI feel like I've been riding this train\nfor ages,\nbut I think I finally understand this place.\n\nIt's a lot to process,\nbut I'm glad I didn't have to do it alone."

        $ day = 5 # good ending
        #Journal entry with attraction meter high
        call display_journal from _call_display_journal_5

        $ cycle = 4

        stop sound

        call showclock from _call_showclock

        # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH
        jump good_briefing

    # NOTE: SCENE VARIATION IF DECAY IS HIGH
    # ??DECAY
    else:
        show vivi neutral at left with dissolve:
            xzoom -1

        # SOUND: Knocking on door
        play sound knock
        pause 1.0

        show urshu neutral at right with dissolve

        urshu neutral "I trust you had a good evening?"
        vivi neutral "It was fine. I am glad this is ending though."
        urshu surprised "Oh? Do tell."
        vivi neutral "I was scared at first. Of changing, of the unknown, of leaving my past behind..."
        vivi neutral "I'm not anymore."
        urshu neutral "And what changed?"
        vivi neutral "Nothing. I guess I realized wherever I'm going can't be worse than here."
        vivi angry "The more I talk to the people on this train the more I realize how much I hate it here. I'm not myself anymore. You took that from me. I've withered away just like this train."
        vivi angry "I don't even recognize myself in the mirror. I can't tell if I've physically changed or if my perception of self has warped. My thoughts... they're not entirely my own anymore."
        vivi angry "The only thing I had were my thoughts!"
        urshu sad "I'm sorry you feel that way."
        vivi angry "And I'm sorry I wasn't your perfect little plaything to be experimented on!"
        vivi neutral "I will thank you for one thing: You've pushed me beyond all knowable limits. Now I can guarantee I'll be ready for anything in the next life."
        urshu neutral "Thank you for the feedback. Goodnight, Miss Sanssouci."

        hide urshu with dissolve

        vivithinking neutral "I should write whatever thoughts I have left. By tomorrow, I'm not sure they'll be mine."

        play sound writing

        $ message = "I can't take this anymore.\n\nThere's something growing inside me.\nA hunger I, {i}we{/i} can't explain.\nWhat is happening to us?\n\nThis is the conductor's fault.\nHe's behind everything.\nThe other passengers too.\nThey must be working with him.\nNone of them feel the way we do.\nThey're all out to get us.\nWe won't go. Not like this.\nThey'll see."

        $ day = 6 # bad ending
        # Journal entry with degradation meter high
        call display_journal from _call_display_journal_6

        $ cycle = 4

        stop sound

        call showclock from _call_showclock_1

        # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH
        jump bad_waking_up

label showclock:

    stop music fadeout 1.0

    scene clockacceptance with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    return