# The scene starts here.

label introduction:

    # Introduction
    # We meet Vivi as she is writing her notes. We know that she has been invited to review the Ouroboros Express for her job. Urshu knocks on her cabin door, inviting her to dine.

    # SOUND: bedroom ambience
    play ambience amb_bedroom fadein 3.0

    # fade in

    # LOCATION: cabin
    scene cabin with Fade(3.0,1.0,3.0)

    # show cabin at train_shake

    show vivi neutral at left with dissolve:
        xzoom -1


    vivithinking surprised "Notepad, check. Pen, check. Laptop... ugh, I swear I charged it. Phone... dead too? Typical... hundreds of interviews and still I make amateur mistakes. This is an important story!"
    # $ message = "Hello there"
    # call display_journal
    vivi neutral "..."

    vivithinking neutral "At least, I think it is."

    vivithinking neutral "It's funny, I don't quite remember what I'm on this train for..."

    vivithinking neutral "Chloe always sends me to the weirdest places for the Halloween issue of the magazine, but normally I can recall the story I'm supposed to follow."

    # NOTE: all options should be explored before moving on

    $ option1 = False
    $ option2 = False
    $ option3 = False

    label lookaround:

        # <CHOICE>
        if option1 == False and option2 == False and option3 == False:
            vivithinking neutral "I must be here for a reason. Might as well look around."
        else:
            vivithinking neutral "Hmm..."

        menu:
            # OPTION 1 
            "Inspect the walls" if option1 == False:

                $ option1 = True

                pause 0.5
                show vivi neutral at left:
                    xzoom 1
                pause 1.0
                show vivi neutral at left:
                    xzoom -1
                pause 1.0
                vivithinking neutral "This place definitely comes off more tacky than spooky. The decor is way over the top, and that's coming from me." 
                vivithinking neutral "Huh... A plaque with my name on the door. I'm definitely meant to be here."
                vivithinking "Let's keep looking."
                jump lookaround

            # OPTION 2
            "Inspect the desk" if option2 == False:

                $ option2 = True

                hide vivi with dissolve

                $ vivi_fullbody = True

                show vivi neutral at left with dissolve:
                    xzoom 1

                vivithinking neutral "It looks like an early 20th-century desk. Actually, everything in here looks like it came from 100 years ago, although it's all in pristine condition."

                vivithinking "Maybe something else will jog my memory."

                hide vivi with dissolve
                $ vivi_fullbody = False
                show vivi neutral at left with dissolve:
                    xzoom -1

                jump lookaround

            # OPTION 3
            "Inspect the mirror" if option3 == False:

                $ option3 = True

                hide vivi with dissolve

                $ vivi_fullbody = True

                show vivi neutral at left with dissolve:
                    xzoom -1

                vivithinking surprised "I'm a little paler than usual. Need to get out in the sun more. I'm absolutely asking Chloe for a vacation when this job is finished."

                vivithinking "There must be something more."

                hide vivi with dissolve
                $ vivi_fullbody = False
                show vivi neutral at left with dissolve:
                    xzoom -1
                jump lookaround

            # NOTE after all three options are explored, OPTION 4 should appear

            # OPTION 4
            "Look out the window" if option1 == True and option2 == True and option3 == True:

                vivithinking neutral "Hmm. The view from the window is really hard to make out. It's all dark and misty. I think we're in a forest?"
                play cd_ambience amb_cosmicdecay fadein 1.0 volume 1.0
                $ renpy.music.set_audio_filter("cd_ambience", audio_filter.Lowpass(8000), replace=True, duration=1.0)
                $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(400), replace=True, duration=1.0)
                $ renpy.music.set_volume(0.25, delay=1.0, channel='music')
                show black with fade
                show vivi_window with Dissolve(3.0)
                pause 1.0
                vivithinking surprised "Huh, weird. The condensation on the window is flowing up as if the train is falling. That can't be right."
                hide vivi_window with dissolve
                hide black with dissolve
                stop cd_ambience fadeout 1.0
                $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.0)
                $ renpy.music.set_volume(1.0, delay=5.0, channel='music')
                vivithinking surprised "What's going on?"

    pause 0.5
    # SOUND: knocking on the door
    play sound2 knock
    pause 2.0
    show urshu neutral at right with dissolve

    urshu neutral "Ah, Miss Sanssouci, I'm glad you are awake. Welcome aboard the Ouroboros Express. We've been expecting you."
    urshu neutral "My name is Urshunabi, but you may call me Urshu. I am the conductor here, so if you need anything during your stay, please don't hesitate to call."
    vivi neutral "Outside... How is that..."
    urshu happy "Oh, don't you mind that. There will be plenty of time later to get acquainted with this place."
    vivi neutral "Sorry, this is all just a lot. I must be really tired."
    urshu happy "I could whip up an espresso if you'd like. They are to die for. I personally have one every morning."
    vivi neutral "I think I'm okay for now, but thank you."
    urshu neutral "Well, in any case, I've actually stopped by to invite you to dinner. The other guests have gathered in the dining car. I'm sure they're quite eager to meet you."

    # <CHOICE>
    vivi neutral "Um..."

    menu:
        # OPTION 1
        "Lead the way.":

            vivi neutral "Lead the way. It'll be nice to talk to others."

            stop sound fadeout 2.0

            # JUMP TO: The Welcome Meal
            jump welcome_meal

        # OPTION 2
        "Can I have a second?":

            vivi surprised "Can I have a second? I'm a bit off balance at the moment." 
            urshu neutral "Quite understandable, my dear, but a hot meal and some conversation might be just what you need."
            vivithinking neutral "How can I argue with that?"
            vivi neutral "I guess you're right. Okay. Lead the way."

            stop sound fadeout 2.0

            # JUMP TO: The Welcome Meal
            jump welcome_meal