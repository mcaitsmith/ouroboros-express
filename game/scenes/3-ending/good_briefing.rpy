# The scene starts here.

label good_briefing:

    # Good Ending/Briefing

    play music goodendmusic volume 0.5
    
    # fade in

    # LOCATION: cabin
    scene cabin with fade

    show vivi happy at left with dissolve:
        xzoom -1

    vivithinking neutral "Something seems different today."
    vivithinking neutral "The decay... It's...slowed? The train is looking back to its gaudy self."
    vivithinking happy "Hmm. Coincidentally, I feel the same."

    # SOUND: knocking on the door
    play sound knock
    pause 1.0

    show urshu happy at right with dissolve

    urshu happy "Hello, Vivienne! I hope you are well."
    vivi happy "Hey, Urshu. Yeah, I surprisingly feel okay."
    vivi sad "Don't get me wrong, though, I'm still {i}really{/i} afraid of...well, everything that awaits."
    urshu neutral "What is it exactly that scares you?"
    vivi neutral "...Well, um. That's it right there."
    vivi neutral "The unknown..."
    vivi sad "And...feeling that I could've done more with my time."
    vivi sad "And ending up...alone."
    urshu happy "My darling Vivienne, you needn't worry. This train has a habit of taking folks exactly where they need to go. The unknown is scary, yes, but it's less scary with company. I have a feeling it will all work out."
    vivi neutral "How do you know?"
    urshu happy "I trust you."
    vivithinking neutral "He trusts me? With what?"
    vivi neutral "Oh, well...Thanks, Urshu."
    vivi happy "You're in a really good mood today!"
    urshu happy "I'm not the only one. Come see who's waiting for you in the lounge."

    # JUMP TO: Romance/Confession/Character Selector
    jump romance_cs