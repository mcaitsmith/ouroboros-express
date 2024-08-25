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

    ava "Hello, little one. Has our radiance tempted you today? Come, sit with us for a moment."

    vivithinking "When she says it like this. It's not like I can say no."

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

    #NPC Scene with Darius and Asha
    #LOCATION: observatory
    scene observatory with fade

    #SOUND: train

    show vivi angry at left with dissolve:
        xzoom-1       #LOCATION: observatory

    vivithinking “My brain is turning faster than the wheels of this accursed train. I'm going in circles. I'm back at the observatory. may as well make a few wishes.”

    show darius angry at right with dissolve
    show ava angry at right with dissolve

    vivithinking “Oh! The Goddess and the Inspector are in the middle of something. Time to be a fly on the wall, Vivi.”

    hide vivi

    ava angry “You mock us? Your shapeless, nameless god sends his Illithid scourge to commit murder; nay, rather, genocide. Your sacrifices brought you nothing but here.”

    darius neutral “I’m not mocking you or anyone else here. Merely mentioning that you’re just as alone as I.”

    ava angry “More mockery, skull shredder? We are nothing alike; I bring mercy where you are merciless, life for your death. Mother Asha, the All is the One, but for your god, The One is the All.”

    darius angry “You think you know of love? The love of the One is so all-encompassing that you quite literally cannot comprehend it.” 

    ava neutral “The One of which you speak? Does the One feed the poor with death? Great goddess. We have fed the poor and felt their love. What does your One know of kindness?”

    darius happy “This is what those who do not understand the beauty of oblivion could never imagine. Relief. Release.” 

    ava happy “Death brought you to this cage, Illithid. Your One cannot free you, yet you talk of relief and release.”  

    darius angry “I am more free than you ever possibly be.”

    ava neutral “We never knew freedom until now, minion. Hunger has sweetened the beans.”

    darius surprised “Minion? Beans? Explain.” 

    ava happy “We serve the goddess as her Avatar, you as the One’s minion. And have you not so hungered for your forbidden fruit that delay makes the mundane magnificent?”

    darius neutral “I am satiated. In ways you could never be. My One is All, and I am satisfied. Unlike you, despite your staunch repudiations.” 

    ava neutral “Satisfied? Do we not see regret in those dark eyes? If your One had lifted you from all doubt, you would not be here with us.”

    darius neutral “Enough.”

    show ava angry blush at left
    show darius angry blush at right

    vivithinking “Wowzers. That was heavy. Sounds like they’re both right on some things. Both had and lost faith.”

    #TURN ava away from Darius.

    vivithinking “I should get outta here. Their silence is making me uncomfortable!”

    # JUMP TO: 2.1 Denial NPC scene Ava and Darius
    jump denial_NPC_ava_darius