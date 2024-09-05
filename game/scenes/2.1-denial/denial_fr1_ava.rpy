# The scene starts here.

label denial_fr1_ava:

    #FREE ROAM 1 - Ava

    #LOCATION: Observatory
    scene observatory with fade

    show ava sad at right with dissolve
    show vivi neutral at left with dissolve:
        xzoom -1
    vivithinking "On to the observatory. Who do I see staring out the window into darkness but the sun goddess herself?"

    show ava surprised at right

    # SOUND: ava gasps.
    play sound gasp
    pause 1.0
    
    show ava happy at right
    vivithinking "Oh, she's noticed me. So imposing~"

    show ava happy blush with dissolve

    # <CHOICE>
    ava "Hello, little one. Has our radiance tempted you today? Come, sit with us for a moment."

    menu:

    # OPTION 1
        "(Well, when she says it like that, how's a girl supposed to say no?)":

            vivithinking "Well, when she says it like that, how's a girl supposed to say no?"

            # JUMP TO show ava neutral -blush

    # OPTION 2
        "(Well, it can't hurt. I guess.)":

            vivithinking neutral "Well, it can't hurt. I guess."

            # JUMP TO show ava neutral -blush

    show ava neutral -blush

    # <CHOICE>
    ava neutral "Your sandal has a pebble, little one?"

    menu:

    # OPTION 1
        "She'd know where we're headed and how to escape.":

            vivithinking "She'd know where we're headed and how to escape."
            vivi surprised "Where do you think we're really headed? Or how does one escape?"
            ava happy "Where are we going? A destination. The train will stop, we will leave..."
            vivi neutral "Not very specific."
            ava happy "Correct. For how can we tell you what we do not yet know?"
            vivithinking "What is wrong with her?"
            #JUMP to vivi saying "Beats me!"

    # OPTION 2 +ATTRACTION
        "I wonder what she saw in the window.":

            play sound attchoice

            vivithinking "I wonder what she saw in the window."
            vivi happy "I'm a little overwhelmed by everything going on. What are you looking at?"
            show ava happy blush with dissolve
            ava "We exist to spread the light of knowledge. We have looked into the darkness. Above us."
            vivi surprised "What'd you see?"
            show ava surprised -blush
            ava "A cold void stares back at us. A sun, black as night. Inescapable emptiness."
            vivi surprised "How terrifying!" 
            ava neutral "Perhaps it was just our imagination, hm?"
            #JUMP to vivi saying "Beats me!"

    vivi neutral "Beats me!"

    # <CHOICE>
    ava sad "The pebble remains. Speak your mind."

    menu:

    # OPTION 1 +ATTRACTION
        "I should share my worries with her.":

            play sound attchoice

            vivithinking "I should share my worries with her."
            vivi surprised "I don't even know what to think anymore...this whole journey has thrown me for a loop. I mean, if the conductor was telling the truth, then are we all really dead...?"
            ava neutral "We can understand why you feel that way, but the Avatar shall not perish before twenty and five years! It is as obvious as the sunrise. We can still feel the Goddess' power surging through us."
            vivi surprised "But maybe we really are gone. You'd think I'd remember dying!" 
            vivi "Maybe that's why we're here...to come to terms with...with this."
            ava angry "Silly mortal... But... we know how you feel. We scarcely recall boarding this train; home one moment, here the next. Why has our memory forsaken us?...ugh! Let us speak of other things."

            # JUMP TO: vivi "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."

    # OPTION 2 
        "I should interview her for more info.":

            vivithinking "I should interview her for more info."
            vivi neutral "How has this luxury liner been for you?"
            ava neutral "Let us bring Light to your darkness. Besides last night, the journey, like so many, has been pleasant."
            # JUMP TO: vivi "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."

    vivi neutral "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."
    ava neutral "Ridiculous. Of course we are alive. Look around you. Breathe. Have a drink and calm those nerves of yours."

    # <CHOICE>
    show ava happy blush with dissolve
    ava "What say you, little one?"

    menu:

    # OPTION 1 +ATTRACTION
        "Drink, yes? Little one? No!":

            play sound attchoice

            vivithinking "Drink, yes? Little one? No!"
            vivi happy blush "Another time! But please stop calling me \"little one.\" I'm thirty."
            show ava sad blush
            ava "Ah. Our words have offended. A thousand pardons." 
            show ava happy blush
            ava "We admire you standing up for yourself. It is...appealing."
            show ava happy -blush
            ava "May the Goddess guide your travels. The All is the One."
            vivi happy "Thanks, Asha! May the Goddess guide your journey too."
            #JUMP TO: vivi: "That was interesting. Wonder what's next..."

    # OPTION 2
        "More of the cat chasing its tail.":

            vivithinking "More of the cat chasing its tail."
            vivi neutral "Maybe later. Thank you for listening, Asha. I'll keep you updated with my investigation as it progresses."
            show ava neutral -blush
            ava "May the Goddess guide your travels. The All is the One."
            vivi neutral "Sure thing, sunshine. See ya."
            #JUMP to vivi saying, "That was interesting. Wonder what's next..."

    hide ava with dissolve
    vivithinking "That was interesting. Wonder what's next..."
    
    # JUMP TO: 2.1 Denial NPC scene Ava and Darius
    jump denial_fr1_ava_darius