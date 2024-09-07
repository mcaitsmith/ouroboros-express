# The scene starts here.

label bargaining_fr1_ava:

    #FREE ROAM 1 - Ava

    # LOCATION: observatory
    call check_overlay
    scene observatory with fade

    # SOUND: the train on its tracks
    play sound train

    show vivi neutral at left with dissolve:
        xzoom -1

    show ava neutral at right with dissolve

    vivithinking "Oh, she's here. I thought she'd be in her room still." 
    vivi neutral "Hey, Asha."
    ava neutral "Yes, little— I mean, Vivienne."

    stop sound fadeout 2.0

    # <CHOICE>
    vivi neutral "I have a question for you..."

    menu: 
        # OPTION 1 +DECAY
        "Who or what is our mysterious train conductor?":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "Who or what is our mysterious train conductor?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava neutral "He is known by many names, the conveyor of souls. Charon? Urshu? Anubis? The trickster Hermes seems fitting, no?"
            vivi neutral "Think we can convince him to let us off this death train?"
            ava sad "We know the will of the gods, Vivienne."

            # ??DECAY
            if dec_meter > 10:
                vivi sad "Well, I guess you would, huh? So in layman's terms for me?" 
                ava sad "We are like a dog chasing its tail, round and round. Catch the tail, and you shall know their will."
                vivi sad "So no? The answer is no?"
                ava sad "Correct." 
                ava sad "The stars would all burn out first."
            # END

            # JUMP TO: vivi neutral blush "It's always memorable talking with you, Asha."

        # OPTION 2 >>ATTRACTION +ATTRACTION
        "If you could redo a past event, what would it be?" if att_meter_ava >= 20:

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_bargaining_fr1 / att_num_list_ava[2])

            vivi neutral "If you could redo a past event, what would it be?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
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

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_bargaining_fr1 / att_num_list_ava[2])

            vivi neutral "That was a big sigh. Pebble in your sandal, Asha?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            ava sad "Regrets, Vivienne. Many. No Avatar is allowed a family, a name, men...even tears."
            show vivi surprised at left:
                xzoom -1

            # <CHOICE>
            vivithinking "Damn! Which one's the worst?!"

            # DECAY ROUTE
            if dec_meter >= 10:
                play sound decchoice
                vivi surprised "Which one—?"
                ava angry "We have no answer."
                jump barg_fr1_ava_end

            menu:
                # OPTION 1 +DECAY
                "No family?":

                    play sound decchoice
                    show decay_icon at right with dissolve:
                        xoffset -500
                        # xoffset -30
                        yoffset -750
                    $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

                    vivi surprised "No family?"
                    hide decay_icon
                    with { "master" : Dissolve(0.5) }
                    ava sad "Our mother gave us to Asha at birth, then sent us back."
                    vivi surprised "Sent you back?"
                    ava sad "We are sacrificed. We are grateful we do not remember our mother or our death. Praise Asha."
                    vivithinking surprised "Damn. That's the saddest thing I've ever heard. What do I even say?"
                
                    # JUMP TO: vivi happy "I'm glad you made the most of it."
                
                #OPTION 2 +ATTRACTION
                "No name?":

                    play sound attchoice
                    show attraction_icon at right with dissolve:
                        xoffset -500
                        # xoffset -30
                        yoffset -850
                    $ att_meter_ava += int(att_max_bargaining_fr1 / att_num_list_ava[2])

                    vivi surprised "No name?"
                    hide attraction_icon
                    with { "master" : Dissolve(0.5) }
                    ava sad "We speak for our people, so we are all, and we are one."

                    show vivi neutral at left:
                        xzoom -1

                    vivithinking "That puts a lot into perspective."
                    ava neutral "Better us than the Royals. We care."
                    vivi happy "Since your service is over, why not name yourself?"
                    ava surprised "..."
                    ava happy "Your idea has interested us."
                    vivi happy "Good! Maybe it'll help you forget your time on Soleos."
                    ava sad "No, I do not wish that entirely." 
                    ava neutral "The Royals were cruel, yes, but it was an honor to serve our people."
                    show vivi neutral blush at left:
                        xzoom -1
                    vivithinking "Wow. She really is radiant. Inside and out."
                
                    # JUMP TO: vivi happy "I'm glad you made the most of it."

                # OPTION 3 +ATTRACTION
                "No tears?":

                    play sound attchoice
                    show attraction_icon at right with dissolve:
                        xoffset -500
                        # xoffset -30
                        yoffset -850
                    $ att_meter_ava += int(att_max_bargaining_fr1 / att_num_list_ava[2])

                    vivi surprised "No tears?"
                    hide attraction_icon
                    with { "master" : Dissolve(0.5) }
                    ava sad "We have felt the onset once, but no. We have never cried."
                    vivithinking "That explains a lot!"

                    # ??ATTRACTION
                    if att_meter_ava >= 15:
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

                    play sound attchoice
                    show attraction_icon at right with dissolve:
                        xoffset -500
                        # xoffset -30
                        yoffset -850
                    $ att_meter_ava += int(att_max_bargaining_fr1 / att_num_list_ava[2])

                    vivi surprised "No men?"
                    hide attraction_icon
                    with { "master" : Dissolve(0.5) }
                    ava happy "We never had one, but we knew many women."
                    vivithinking "Whoa! Did I underestimate Her Radiance?"
                    ava happy "When we went to lands run by women, our diplomacy always prevailed, no matter the tongue."

                    # ??ATTRACTION
                    if att_meter_ava >= 25:
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
            if att_meter_ava >= 40:
                show ava happy blush with dissolve
                ava "We sighed differently then. And we sigh looking at you now."
                show ava neutral -blush
            # END

            # JUMP TO: vivi neutral blush "It's always memorable talking with you, Asha."

    label barg_fr1_ava_end:

        vivi neutral blush "It's always memorable talking with you, Asha."
        ava neutral "And with you. Goodbye, Vivienne. The All is the One."
        vivithinking "That sure was...something."

        # JUMP TO: Darius/Susu'Rha intermission scene'
        jump bargaining_darius_susurha