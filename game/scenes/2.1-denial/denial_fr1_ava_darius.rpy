# The scene starts here.

label denial_fr1_ava_darius:

    #2.1 DENIAL NPC scene - Ava and Darius

    #LOCATION: observatory

    #SOUND: train
    play sound train

    scene observatory with fade

    show vivi angry at left with dissolve:
        xzoom -1       



    vivithinking "My brain is turning faster than the wheels of this accursed train. I'm going in circles. I'm back at the observatory. may as well make a few wishes."

    hide vivi

    show darius angry at right with dissolve
    show ava angry at left with dissolve:
        xzoom -1

    vivithinking "Oh! The Goddess and the detective are in the middle of something. Time to be a fly on the wall, Vivi."

    ava angry "You mock us? Your shapeless, nameless god sends his Illithid scourge to commit murder; nay, rather, genocide. Your sacrifices brought you nothing but here."

    darius neutral "I’m not mocking you or anyone else here. Merely mentioning that you’re just as alone as I."

    ava angry "More mockery, skull shredder? We are nothing alike; I bring mercy where you are merciless, life for your death. Mother Asha, the All is the One, but for your god, The One is the All."

    darius angry "You think you know of love? The love of the One is so all-encompassing that you quite literally cannot comprehend it." 

    ava neutral "The One of which you speak? Does the One feed the poor with death? Great goddess. We have fed the poor and felt their love. What does your One know of kindness?"

    darius happy "This is what those who do not understand the beauty of oblivion could never imagine. Relief. Release." 

    ava happy "Death brought you to this cage, Illithid. Your One cannot free you, yet you talk of relief and release."  

    darius angry "I am more free than you could ever possibly be."

    ava neutral "We never knew freedom until now, minion. Hunger has sweetened the beans."

    darius surprised "Minion? Beans? Explain." 

    ava happy "We serve the goddess as her Avatar, you as the One’s minion. And have you not so hungered for your forbidden fruit that delay makes the mundane magnificent?"

    darius neutral "I am satiated. In ways you could never be. My One is All, and I am satisfied. Unlike you, despite your staunch repudiations." 

    ava neutral "Satisfied? Do we not see regret in those dark eyes? If your One had lifted you from all doubt, you would not be here with us."

    darius neutral "Enough."

    show ava angry blush at left
    show darius angry blush at right

    vivithinking "Wowzers. That was heavy. Sounds like they’re both right on some things. Both had and lost faith."

    #TURN ava away from Darius.

    show ava angry at left:
        xzoom 1

    vivithinking "I should get outta here. Their silence is making me uncomfortable!"

    # JUMP TO: Character Selector 2
    jump denial_cs2