# The scene starts here.

label romance_cs:

    # Romance/Confession/Character Selector

    # LOCATION: lounge
    scene lounge with fade
    play ambience amb_lounge fadein 1.0

    $ ava_confess = False
    $ darius_confess = False
    $ susurha_confess = False
    $ ava_friend = False
    $ darius_friend = False
    $ susurha_friend = False
    define ava_asked = False
    define darius_asked = False
    define susurha_asked = False

    label show_chars:

        # show all characters happy that have a high attraction meter.
        # ??ATTRACTION
        if att_meter_ava >= romance_threshold:
            show ava happy at center_right with dissolve
        else:
            $ ava_confess = True
        # ??ATTRACTION
        if att_meter_darius >= romance_threshold:
            show darius happy at center with dissolve
        else:
            $ darius_confess = True
        # ??ATTRACTION
        if att_meter_susurha >= romance_threshold:
            show susurha happy at right with dissolve
        else:
            $ susurha_confess = True

        #hide all characters
        show vivi happy at center_left with dissolve:
                xzoom -1
        vivi happy "Hey..."
        
        vivithinking happy "Time to talk with someone."
        label end_choice:
            show vivi at center_left with dissolve:
                xzoom -1
            # <CHOICE>
            menu:
            # OPTION1 ??ATTRACTION
                "Avatar of Asha" if att_meter_ava >= romance_threshold and ava_confess == False:

                    $ ava_confess = True

                    vivithinking happy "Let's talk with the goddess."

                    hide darius with dissolve
                    hide susurha with dissolve

                    # JUMP to: Confession / Avatar of Asha
                    jump confession_ava

            # OPTION 7 ??ATTRACTION
                "I want to be with Ava" if att_meter_ava >= romance_threshold and ava_confess == True and ava_friend == False:

                    vivithinking happy "I think the answer is clear. I want to be with Ava." 
                    vivithinking happy blush "She is the one for me."

                    # JUMP to: Romance / Avatar of Asha
                    jump romance_ava

            # OPTION 2 ??ATTRACTION
                "Darius Wrecker" if att_meter_darius >= romance_threshold and darius_confess == False:

                    $ darius_confess = True

                    vivithinking happy "Let's see how Darius is doing."

                    hide ava with dissolve
                    hide susurha with dissolve

                    # JUMP to: Confession / Darius Wrecker
                    jump confession_darius

            # OPTION 8 ??ATTRACTION
                "I want to be with Darius" if att_meter_darius >= romance_threshold and darius_confess == True and darius_friend == False:

                    vivithinking happy "Darius. It's always been Darius. They are my other half."
                    vivithinking happy blush "They're the one for me."

                    # JUMP to: Romance / Darius Wrecker
                    jump romance_darius

            # OPTION 3 ??ATTRACTION
                "Susu'Rha Balrinn" if att_meter_susurha >= romance_threshold and susurha_confess == False:

                    $ susurha_confess = True

                    vivithinking happy "Let's check in on Susu'Rha."

                    hide ava with dissolve
                    hide darius with dissolve

                    # JUMP to: Confession / Susu'Rha Balrinn
                    jump confession_susurha

            # OPTION 9 ??ATTRACTION
                "I want to be with Susu'Rha" if att_meter_susurha >= romance_threshold and susurha_confess == True and susurha_friend == False:

                    vivithinking happy "I don't know why it's taken me so long to figure it out, but now I know for sure." 
                    vivithinking happy blush "Susu'Rha is the one I love."

                    # JUMP to Romance / Susu'Rha Balrinn
                    jump romance_susurha

            # NOTE options 4,5,6 are if a character is missing from the scene. It would replace the corresponding character option above.

            # OPTION 4 ??ATTRACTION (ELSE)
                "Where's the goddess?" if not att_meter_ava >= romance_threshold and not ava_asked:
                    $ ava_asked = True
                    vivi surprised "Wait, where's the goddess?"

                    show urshu sad at center_right with dissolve

                    urshu sad "Unfortunately, she had a hard time connecting to anyone on this train. This place became a little too much to bear. It's sad, but it does happen. I've made sure she found a place to belong."
                    vivi sad "Oh...okay."

                    hide urshu with dissolve

                    # JUMP to: the END CHOICE
                    jump end_choice

            # OPTION 5 ??ATTRACTION (ELSE)
                "Where's Darius?" if not att_meter_darius >= romance_threshold and not darius_asked:
                    $ darius_asked = True
                    vivi surprised "Wait, where's Darius?"

                    show urshu sad at center_right with dissolve

                    urshu sad "Darius was unable to see past his former self. The guilt he had from a millennia of inflicting pain tore away at his soul. This place became too much to bear. It's sad, but it does happen. I've made sure Darius ended up in a place that could accept him."
                    vivi sad "Oh..."

                    hide urshu with dissolve
                
                    # JUMP to: the END CHOICE
                    jump end_choice


            # OPTION 6 ??ATTRACTION (ELSE)
                "Where's Susu'Rha?" if not att_meter_susurha >= romance_threshold and not susurha_asked:
                    $ susurha_asked = True
                    vivi surprised "Wait, where's Susu'Rha?"

                    show urshu sad at center_right with dissolve

                    urshu sad "Susu'Rha was not able to move forward through past regrets. This train was not as helpful as I hoped it would be in helping them deal with their troubles. It's sad, but it does happen. I've made sure Susu'Rha ended up in a place that better suits them."
                    vivi sad "..."

                    hide urshu with dissolve

                    # JUMP to: the END CHOICE
                    jump end_choice

            # NOTE options 7,8,9 are if you have talked to a character, they confessed and you chose the "please hold while I make my decision" option. This would replace the corresponding character option from 1,2,3.

            # NOTE If you friendzone all characters, OPTION 10 will appear.
                # "Thank you for coming this far with me, Asha." if ava_friend == True and (susurha_asked and darius_asked):
                #     jump epi_friend_ava
                # "Thank you for coming this far with me, Darius." if darius_friend == True and (susurha_asked and ava_asked):
                #     jump epi_friend_darius
                # "Thank you for coming this far with me, Susu'Rha." if susurha_friend == True and (ava_asked and darius_asked):
                #     jump epi_friend_susurha
                "I think I've found closure now." if not (ava_friend == True and darius_friend == True and susurha_friend == True) and (ava_confess == True and darius_confess == True and susurha_confess == True):
                    vivi happy "I think I've found closure now."
                    vivi neutral "All is said and done."

                    hide ava with dissolve
                    hide darius with dissolve
                    hide susurha with dissolve
                
                    show urshu neutral at center_right with dissolve
                
                    urshu neutral "Then, would you accompany me to the observatory, Miss Sansoucci? One last look at the stars?"
                    vivi "You have something to say too? Fine. Let's hear it."

                    jump epi_imperfect_friendship

            # OPTION 10
                "I found friends." if ava_friend == True and darius_friend == True and susurha_friend == True:

                    vivi happy "I've truly found connection here. For the first time in a really long time, I'm not alone."

                    show urshu happy at center_right with dissolve

                    urshu happy "I'm glad the Ouroboros Express could be of service."
                    vivi sad "I wish I figured this all out sooner."
                    vivi neutral "Of course, I find fulfillment at the last second! I guess it was nice while it  lasted."
                    urshu happy "I really am a sucker for happy endings. I suppose you all have earned that."

                    # SOUND: Snap of fingers
                    play sound snap
                    pause 1.0

                    vivithinking surprised "What just happened? The decay of the train... It's completely reversed."
                    vivithinking surprised "And I feel warmth. I didn't realize how {i}cold{/i} this train was until now. How cold {i}I{/i} was." 
                    vivithinking neutral "What is that little bastard up to?"
                    vivi neutral "Ursh, what did you do?"
                    urshu happy "Like I said before. This train takes you to where you need to go. And the destination is finally clear." 

                    # VISUAL: screen starts flashing white
                    play sound trainshake fadein 1.0
                    show lounge with flash
                    show lounge with flash
                    show lounge with flash
                    show lounge at bright with dissolve
                    stop sound fadeout 1.0

                    vivi surprised "Wait, Urshu! What's going on?"
                    vivi surprised "Where am I going?" 
                    vivi sad "Will I ever see you again?"
                    urshu sad "I'm afraid not. This is goodbye, my dear."
                    vivi sad "Adieu, Urshu."
                    urshu happy "Enjoy your next journey, Vivienne Sanssouci."
                    urshu happy "It's been a pleasure having you aboard the Ouroboros Express." 

                    # VISUAL: screen flashes white and fades to epilogues
                    scene white with Dissolve(3.0)
                    # JUMP to: Epilogues
                    jump epi_friendship_all