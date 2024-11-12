# The scene starts here.

label bargaining_fr2_ava:

    #FREE ROAM 2 - Ava

    # LOCATION: diningcar
    # call check_overlay from _call_check_overlay_20
    scene diningcar with fade

    # SOUND: cooking, kitchen sounds
    play sound cooking

    show vivi neutral at left with dissolve:
        xzoom -1

    show ava neutral at right with dissolve

    vivi neutral "Thanks for coming on such short notice, Asha. I really need your help."
    ava happy "Of course, my radiant companion."
    ava neutral "What services of ours do you require so urgently?"

    stop sound fadeout 1.0

    # <CHOICE>
    vivi neutral blush "Asha, to be entirely honest...well..."

    menu:
        # OPTION 1 +ATTRACTION
        "I want to cook together...with you.":

            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_bargaining_fr2 / att_num_list_ava[3])

            vivi neutral blush "I want to cook together... With you."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi neutral blush "I bet we can whip up something really incredible."
            show ava happy blush
            
            # <CHOICE>
            ava "We would be honored to cook with you. It has been over a decade since we've set foot in a kitchen. This should prove to be...interesting."
            
            menu:
                # OPTION 1A
                "(Interesting indeed...)":
                    
                    vivithinking blush "Interesting indeed..."

                    # JUMP TO vivi happy blush "Thank you! You have no idea what this means to me!"


                # OPTION 1B
                "(Oh man, not {i}too{/i} interesting, I hope! Edible would be good.)":

                    vivithinking -blush "Oh man, not {i}too{/i} interesting, I hope! Edible would be good."

                    # JUMP TO vivi happy blush "Thank you! You have no idea what this means to me!"
           
            vivi happy blush "Thank you! You have no idea what this means to me!" 
            vivi happy "I can't wait! Let's get cooking."
            show ava happy -blush
            ava happy "Excellent."

            # JUMP TO: ava neutral "So what shall we make, then?"

        # OPTION 2 +DECAY (removing meter effect for balance)
        "Urshu asked me...":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi sad blush "Urshu asked me to cook something for everyone, so I figured we could do it together. What do you think?"
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            ava neutral "We wish you would have asked us sooner. The sun is nearly gone today."
            vivi neutral "So...is that a yes?"
            ava neutral "We suppose..."

            # JUMP TO: ava neutral "So what shall we make, then?"

        # OPTION 3 >>ATTRACTION +ATTRACTION
        "Be my sous chef! Together, we'll rule this train." if att_meter_ava >= 40:

            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_bargaining_fr2 / att_num_list_ava[3])

            vivi neutral blush "Be my sous chef! Together, we'll rule this train."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            show ava surprised blush
            ava "We're not sure exactly what you mean."
            vivi neutral "A sous chef is the right-hand to the main chef! We're gonna be making something in the kitchen today!" 
            show ava surprised -blush
            ava surprised "Right...hand?"
            ava happy "We don't know with confidence what you speak of, but your passion is coming through."
            vivi surprised blush "Did you just...use a contraction?"
            show ava surprised blush
            ava "A what?"
            vivi neutral blush "Errr...Nevermind!"

            show vivi angry at left

            vivithinking "Stupid journalism major! Always messing up my game!"
            show ava neutral -blush

            # JUMP TO: vivi neutral "So what shall we make, then?"

    ava neutral "So what shall we make, then?"
    vivi neutral "Good question! What meal feels like home for you?"
    show ava surprised blush
    ava "Well, whenever I was feeling unhappy, the servants would bring me a cornucopia of croquembouche."
    vivithinking "That sounds like a nightmare to make..."
    show ava happy -blush
    ava happy "Do you enjoy cooking at home? Allegedly the food culture on Earth has few rivals."
    vivi happy blush "You heard right! I've taken a few cooking classes back home. They even taught me how to make soufflé!"
    show ava happy blush
    ava "That sounds lovely, but it couldn't compare to the delight of croquembouche."

    show vivi neutral at left

    vivithinking "I swear she's speaking differently today."

    show ava happy -blush
        
    #<CHOICE>
    vivi happy "I think we should make..."

    menu:
        # OPTION 1 +DECAY
        "Croquembouche.":

            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi happy "Let's make the croquembouche you used to have at home. I'm sure it'll put us in a good mood."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava happy "Delightful. We shall gather the 74 ingredients required to make the dish."
            vivi surprised "74 ingredients? What is this, Masterchef?"
            ava happy "Do not worry, my radiance. We shall take the lead on this request."

            show vivi neutral at left

            vivithinking "Well, then that'd make me the sous chef, not you."
            vivithinking "It's fine. Whatever gets me off this train."

            # JUMP TO: vivi happy blush "Let's get cooking!"

        # OPTION 2 +ATTRACTION (removing meter effect for balance)
        "Something simple.":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_ava += int(att_max_bargaining_fr2 / att_num_list_ava[3])

            vivi happy "Something simple. A good old American breakfast!"
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }

            ava surprised "We are not familiar with...American..."
            vivi happy "Well, then I'll tell ya, Asha! Americans love to eat, and they wake up most days with a massive meal."
            vivi happy blush "You can never be sad eating breakfast back home! Hot pancakes with eggs and crispy bacon could make a grown man cry."
            ava surprised "We don't wish to cry today, please."
            vivi happy blush "Don't worry, love, it's just an expression."

            show vivi surprised blush at left

            vivithinking "Did I just call her...love?"

            # JUMP TO: vivi happy blush "Let's get cooking!"

        # OPTION 3 +DECAY 
        "Soufflé.":

            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "Soufflé. I think I can remember the recipe from my class."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava happy "The last soufflé we ate was made with the highest quality eggs and milk on all of Soleos. We wonder how this will compare."
            vivi surprised "Uh...well. Since we're on a death train, I wouldn't get your hopes up too high."
            ava neutral "Oh. Well, then..."
            vivi neutral "...Anyways."

            # JUMP TO: "Let's get cooking!"

    vivi happy blush "Let's get cooking!"
    show ava happy blush
    ava "We shall wash our hands, just in case."

    hide ava with dissolve

    vivithinking "The Goddess? Washing her dirty hands? Wonder what she's been up to..."

    show ava neutral at right with dissolve

    show ava neutral blush

    ava "Apologies..."
    vivi neutral "For what, Asha? You worry too much."
    ava "We just know how much this means to you."
    vivi happy blush "Oh, Asha..."
    vivithinking "I haven't even told her why this meal is so special and she just...knows."
    show ava neutral -blush
        
    # <CHOICE>
    vivi neutral "Do you mind..."

    menu:
        # OPTION 1 +ATTRACTION
        "If we work together?": 

            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_bargaining_fr2 / att_num_list_ava[3])

            vivi neutral blush "Do you mind if we work together? I'm not the most comfortable in the kitchen."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivithinking "That's a lie. But I want her...near." 
            show ava happy blush
            ava "Of course, Vivienne. Let's do this together."
            vivi neutral blush "I like this new Asha. Where has she been?"
            show ava neutral blush
            ava "Whatever do you mean?"
            show ava neutral -blush

            # JUMP TO: vivi neutral blush "Nothing at all..."

        # OPTION 2 +DECAY
        "Beating the eggs and sifting the flour for me?":

            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "Do you mind beating the eggs and sifting the flour for me? I'll take care of the other stuff, and we can combine ingredients."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava neutral "We'll get right to it!"
            vivi happy "Thank you!"
            vivi neutral "Wait a minute...have you done this before?"
            ava neutral "Certainly! We learned from the finest chefs on Soleos, so that we bring peace and food as diplomats."
            vivi surprised "Oh! Good to know..."
            ava surprised "What's wrong?"

            # JUMP TO: vivi neutral blush "Nothing at all..."

    vivi neutral blush "Nothing at all..."

    # SOUND: cooking sounds
    play sound cooking

    # PAUSE
    pause 3.0

    stop sound fadeout 1.0

    vivi surprised "Wow! I can't believe we actually did it. It tastes so good too!"
    show ava happy blush
    ava "Shall we present our creation to the conductor?"
    vivi happy "Let's do it!"

    # ??ATTRACTION
    if att_meter_ava >= 50:
        vivi neutral "Actually, Asha. Before we go, I should tell you something."
        vivi neutral "The reason this meal is so important to me is because...Urshu and I made a deal."
        vivi neutral "He said that if I made him the best-tasting meal he's ever had, then he'd let me off this train."
        vivi neutral "I'm sorry I didn't tell you earlier, but..."
        vivi neutral "Now I realize..."
        vivithinking "Please, don't be cringey. Please, don't be cringey."
        vivi neutral blush "I don't want to leave this train if you're not with me."
        vivi neutral "I want this meal to be the exit ticket for both of us."
        show ava neutral blush
        ava "We see..."
        ava "We are in agreement with you, and we thank you for your honesty. Life with you outside of this place sounds... idyllic."

        show vivi surprised blush at left

        vivithinking "Idyllic! Not even my mother has ever described life with me that way! Not that I'd expect her to."

        show vivi neutral blush at left

        vivithinking "And I'm not crazy, either. Asha really is changing her speech pattern around me. I think... No, I shouldn't read into it too much."
    #END
    show ava neutral -blush

    #JUMP TO: URSHU MEAL REVEAL
    jump bargaining_meal_reveal