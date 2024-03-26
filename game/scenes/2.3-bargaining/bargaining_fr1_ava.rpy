# The scene starts here.

label bargaining_fr1_ava:

    #FREE ROAM 1 - Ava

    # LOCATION: observatory
    scene observatory with fade

    # SOUND: the train on its tracks
    play sound train

    show vivi neutral at left with dissolve

    show ava neutral at right with dissolve

    vivithinking "Oh, she's here. I thought she'd be in her room still." 
    vivi neutral "Hey, Asha."
    ava neutral "Yes, little-- I mean, Vivienne."

    stop sound fadeout 2.0

    # <CHOICE>
    vivi neutral "I have a question for you..."

    menu: 
        # OPTION 1 +DECAY
        "Who or what is our mysterious train conductor?":

            vivi neutral "Who or what is our mysterious train conductor?"
            ava neutral "He is known by many names, the conveyor of souls. Charon? Urshu? Anubis? The trickster Hermes seems fitting, no?"
            vivi neutral "Think we can convince him to let us off this death train?"
            ava sad "We know the will of the gods, Vivienne."

            # ??DECAY
            vivi sad "Well, I guess you would, huh? So in layman's terms for me?" 
            ava sad "We are like a dog chasing its tail, round and round. Catch the tail, and you shall know their will."
            vivi sad "So no? The answer is no?"
            ava sad "Correct." 
            ava sad "The stars would all burn out first."
            # END

            # JUMP TO: vivi neutral blush "It's always memorable talking with you, Asha."

        # OPTION 2 >>ATTRACTION +ATTRACTION
        "If you could redo a past event, what would it be?":

            vivi neutral "If you could redo a past event, what would it be?"
            vivi neutral "Or I guess to be more specific, if you could change something that might have caused this, what would you do?"
            show ava sad blush with dissolve
            ava "Once, we broke a taboo. We found a bird, hurt and dying. We hid it, cared for it, grew attached to it."
            vivi neutral "What happened?"
            show ava sad -blush
            ava sad "We returned and found the prince and princess eating it. They had found it and decided to punish us."
            vivi angry "Those entitled little turds! How awful for you!"
            ava sad "Had we not taken the bird, we would not have lost it."
            vivi angry "Yeah, but if you hadn't taken the bird, it would've died alone and sooner!"
            ava neutral "This is true." 
            vivi neutral blush "At least you gave it some happiness before its end. That's gotta be worth something!"
            ava happy "We want to be happy at the end."

            #JUMP TO: vivi neutral blush "It's always memorable talking with you, Asha."

        # OPTION 3 +ATTRACTION
        "That was a big sigh. Pebble in your sandal, Asha?":

            vivi neutral "That was a big sigh. Pebble in your sandal, Asha?"
            ava sad "Regrets, Vivienne. Many. No Avatar is allowed a family, a name, men, even Tears."
            show vivi surprised at left

            # <CHOICE>
            vivithinking "Damn! Which one's the worst?!"

            # DECAY ROUTE
            vivi surprised "Which one—?"
            ava angry "We have no answer."

            menu:
                # OPTION 1 +DECAY
                "No family?":

                    vivi surprised "No family?"
                    ava sad "Our mother gave us to Asha at birth, then sent us back."
                    vivi surprised "Sent you back?"
                    ava sad "We are sacrificed. We are grateful we do not remember our mother or our death. Praise Asha."
                    vivithinking surprised "Damn. That's the saddest thing I've ever heard. What do I even say?"
                
                    # JUMP TO: vivi happy "I'm glad you made the most of it."
                
                #OPTION 2 +ATTRACTION
                "No name?":

                    vivi surprised "No name?"
                    ava sad "We speak for our people, so we are all, and we are one."

                    show vivi neutral at left

                    vivithinking "That puts a lot into perspective."
                    ava neutral "Better us than the Royals. We care."
                    vivi happy "Since your service is over, why not name yourself?"
                    ava surprised "..."
                    ava happy "Your idea has interested us."
                    vivi happy "Good! Maybe it'll help you forget your time on Soleos."
                    ava sad "No, I do not wish that entirely." 
                    ava neutral "The Royals were cruel, yes, but it was an honor to serve our people."
                    show vivi neutral blush at left
                    vivithinking "Wow. She really is radiant. Inside and out."
                
                    # JUMP TO: vivi happy "I'm glad you made the most of it."

                # OPTION 3 +ATTRACTION
                "No tears?":

                    vivi surprised "No tears?"
                    ava sad "We have felt the onset once, but no. We have never cried."
                    vivithinking "That explains a lot!"

                    # ??ATTRACTION
                    vivi neutral "What happened the time you almost cried?"
                    ava sad "A serving girl in the palace. We tried to befriend her."
                    vivi angry "Don't tell me something awful happened to you!"
                    show ava sad blush with dissolve
                    ava "No. Far worse. We never saw her again."
                    show ava sad -blush
                    # END

                    vivi sad "I'm so sorry, Asha. That really sucks."
                    ava surprised "Sucks?! What do you mean sucks? Like a calf does to its mother?"
                    vivi surprised "Uhhhhhhh... I guess?"
                    show ava sad blush with dissolve
                    ava "Strange you humans think sucking to be bad, but yes, we understand. Thank you for listening to us."
                    show ava neutral -blush
                    ava neutral "And while yes, we indeed faced much cruelty in our lives, it was an honor to serve our people. That we will never regret."

                    # JUMP TO: vivi happy "I'm glad you made the most of it."

                #OPTION 4 +ATTRACTION
                "No men?":

                    vivi surprised "No men?"
                    ava happy "We never had one, but we knew many women."
                    vivithinking "Whoa! Did I underestimate Her Radiance?"
                    ava happy "When we went to lands run by women, our diplomacy always prevailed, no matter the tongue."

                    # ?? ATTRACTION
                    # SOUND: heartbeat
                    play sound heartbeat
                    vivithinking "I think my pulse is pounding louder than the train. Wait! Is...she...flirting with me?"
                    stop sound fadeout 1.0
                    # END

                    vivi happy blush "Well, practice makes perfect, right?"
                    vivithinking "OMG AWKWARD, VIVI!!"
                    ava happy "Practice makes us better always."
                    vivi neutral blush "..."
                    vivi neutral blush "Well, anyways..."

                    # JUMP TO: vivi happy "I'm glad you made the most of it."

            vivi happy "I'm glad you made the most of it."

            # ??ATTRACTION
            show ava happy blush with dissolve
            ava "We sighed differently then. And we sigh looking at you now."
            show ava neutral -blush
            # END

            # JUMP TO: vivi neutral blush "It's always memorable talking with you, Asha."

    vivi neutral blush "It's always memorable talking with you, Asha."
    ava neutral "And with you. Goodbye, Vivienne. The All is the One."
    vivithinking "That sure was...something."

    # JUMP TO: Character Selector 2
    jump bargaining_cs2