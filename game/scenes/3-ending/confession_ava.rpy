# The scene starts here.

label confession_ava:

    # Romance/Confession/Avatar of Asha
    # Asha takes ownership of her identity, Ava, for the first time in her life. She thanks Vivi for helping her come to this realization. She asks whether Vivi would like to take this last dance until the end as lovers. Vivi can either say yes, say no but stay friends, or ask her to wait before she makes a decision. 

    #LOCATION: lounge
    # scene lounge with fade

    # show ava happy at right with dissolve
    # show vivi neutral at left with dissolve:
    #     xzoom -1

    vivithinking neutral "There she is. Radiant as always."
    play sound sparkle
    vivithinking surprised blush "But damn! Today she {i}really{/i} is glowing! Like even more than normal..." 
    vivithinking neutral "I wonder what's going on..."
    vivi happy "Asha! Hi!"
    play music ashamusic loop
    ava happy "Vivi! Hello! What a delight to see you!" 
    vivi happy blush "Haha...I think \"delight\" is a bit strong, don't you think?"
    show ava happy blush
    ava "Nonsense. You have always brought us joy, even when we were unable to see it at first..."
    show ava neutral -blush
    ava neutral "Listen. We shall make this short as time is of the essence. There is something we have to tell you." 
    show ava neutral blush
    ava "Something we should have told you long ago."
    vivi neutral blush "Uh, sure! Yeah! Go ahead."
    show ava happy blush
    ava "Vivienne, our time together, our feelings, our heart...We feel a change."
    show ava happy -blush
    ava happy "You have shown us that we are worthy of your time and your trust. You have shown us kindness."
    ava happy "And you have given us the courage so that we..."
    ava neutral "We..."
    ava happy "No. No, so that {i}I{/i} can ask you this."
    vivithinking surprised "I! She can't be..."
    vivi surprised blush "Asha...Do you mean—?"
    show ava happy blush
    ava "From now on we are Asha no more. {i}I{/i} am Ava." 
    ava "And I would like to dance with you, Vivienne, until you and I are no more."

    # <CHOICE>
    ava "Will you accept my love?"
    show ava happy -blush

    menu:
        # OPTION 1
        # Accept Romance
        "Yes!":

            vivi happy "Yes! Yes! A thousand times yes!"
            ava happy "Oh, my heart! I have never felt in my entire existence such..."
            ava happy "Such love!"

            # JUMP TO: Romance/Avatar of Asha
            jump romance_ava
        
        # OPTION 2
        # Reject Romance
        "I can't.":

            $ ava_friend = True

            vivi surprised "Oh...Oh, God. Ava..."
            vivi neutral "Thank you! And...and I'm so happy for you too!" 
            vivi sad "But I just don't think I can do that. I'm sorry."

            show ava sad blush
            stop music fadeout 5.0

            ava "Ah. This is sad news. Would you still allow me to be your friend, regardless?"
            vivi happy "Of course! I would be honored to be your friend."
            vivi happy "Ava."
            show ava sad -blush
            # Note: Ava is locked as friend. Can no longer be chosen as romance partner.
            # JUMP TO: Character Selector
            jump show_chars

        # OPTION 3
        # Delay Decision
        "Could you give me a moment?":

            vivi surprised blush "Could you give me a moment? I just need to...clear my head for a sec."

            stop music fadeout 5.0
            show ava neutral blush

            ava "We have precious few, but for you? Anything."
            show ava neutral -blush

            # JUMP TO: Character Selector
            jump show_chars