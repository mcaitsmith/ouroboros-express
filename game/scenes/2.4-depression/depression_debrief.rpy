# The scene starts here.

label depression_debrief:

    # Debrief Depression

    # LOCATION: cabin
    scene cabin with fade

    # ??ATTRACTION
    if att_meter_ava >= romance_threshold or att_meter_darius >= romance_threshold or att_meter_susurha >= romance_threshold:

        show vivi neutral at left with dissolve

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

        #Journal entry with attraction meter high
        "Wow. At the beginning of all this, I would've never thought I'd get to know some of the other passengers this well. We're all more similar than I thought. Even Urshu, believe it or not. Time is weird here. I feel like I've been riding this train for ages, but I think I finally understand this place. It's a lot to process, but I'm glad I didn't have to do it alone."

        call showclock

        # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH
        jump good_briefing

    # NOTE: SCENE VARIATION IF DECAY IS HIGH
    # ??DECAY
    else:
        show vivi neutral at left with dissolve

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

        # Journal entry with degradation meter high
        "I can't take this anymore. There's something growing inside me. A hunger I, we can't explain. What is happening to us? This is the conductor's fault. He's behind everything. The other passengers too. They must be working with him. None of them feel the way we do. They're all out to get us. We won't go. Not like this. They'll see."

        call showclock

        # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH
        jump bad_waking_up

label showclock:

    stop music fadeout 1.0

    scene clockacceptance with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    return