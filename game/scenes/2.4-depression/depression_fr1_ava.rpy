﻿# The scene starts here.

label depression_fr1_ava:

    # FREE ROAM 1 - Ava

    # LOCATION: lounge
    # call check_overlay from _call_check_overlay_28
    scene diningcar with fade
    play ambience amb_bar fadein 1.0

    
    play sound trainwhistle

    show ava neutral at right with dissolve
    show vivi neutral at center with dissolve
    show urshu neutral at left with dissolve:
        xzoom -1.0

    # ??DECAY
    if dec_meter >= 40:
        ava neutral "Perhaps you would like a drink at the bar alone? We would."
    # END

    #??ATTRACTION
    elif att_meter_ava >= 50:
        ava happy "We could sit with you in the sunlight and silence and be content."
    # END

    vivithinking "She's an oasis in the desert!"
    vivi "Hi! I see you're already ahead of me."
    ava "Hello, Vivi. We are drinking...?"
    play sound drinkstir
    pause 3.0
    urshu "Tequila Sunrise."

    # ??ATTRACTION
    if att_meter_ava >= 55:
        show ava happy blush
        ava "Ah. Sunrise. Lovely, like you, Vivi."
        vivithinking "Er, um... Flirt alert!! Try not to be painfully awkward."
        show ava happy -blush
    # END

    urshu happy "Your cocktail, Vivi. Aroma of marshmallows and Haribos? Ta ta, you two."
    play music peacefulmusic loop
    vivithinking "Shoulda figured he'd know my drink, the cagey bastard!"
        
    hide urshu with dissolve
    show vivi neutral at left with dissolve:
        xzoom -1
    stop sound fadeout 1.0

    # <CHOICE>
    vivi neutral "So how about we..."

    # DECAY ROUTE
    if dec_meter >= 40:
        # play sound decchoice
        ava sad "We misspoke. We wish to drink alone."
        vivi "Well then. See ya, sunshine."
        play sound glassclink03
        # JUMP TO: vivithinking "What are the others doing, I wonder?"
        jump dep_fr1_ava_end

    menu: 
        # OPTION 1 +DECAY
        "...play a game?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

        
            vivi neutral "...play a game?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava "We will be no more tomorrow and you want to play games."
            vivi "Might help. That and another swig."
            # JUMP TO: vivi neutral "It's called {i}Never Have I Ever{/i}."

        # OPTION 2 +ATTRACTION +DECAY
        "...drink our feelings away?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attdecchoice
            show attraction_icon at right:
                xoffset -500
                # xoffset -30
                yoffset -850
            show decay_icon at right:
                xoffset -500
                # xoffset -30
                yoffset -750
            with { "master" : Dissolve(2.0) }
            $ att_meter_ava += int(att_max_depression_fr1 / att_num_list_ava[4])
            $ dec_meter += int(dec_max_depression / dec_num_depression)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi neutral "...drink our feelings away?"
            hide attraction_icon
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava "We accept. Our feelings weigh heavily on us."
            vivi "Then maybe we can play a fun game?"
            ava surprised "A game? Frivolity amidst such sorrow?"
            # JUMP TO: vivi neutral "It's called {i}Never Have I Ever{/i}."
        
        # OPTION 3 +ATTRACTION
        "...sneak behind the bar for two top-shelf top-offs?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr1 / att_num_list_ava[4])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi happy "...sneak behind the bar for two top shelf top offs?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            ava happy "We were unaware you were this naughty, Vivi."
            # ??ATTRACTION
            if att_meter_ava >= 55:
                show ava happy blush
                ava "It pleases us. How does it feel? To disobey?"
                vivi happy "It feels exciting because it's wrong. Is that crazy?"
                show ava neutral -blush
                ava neutral "No. We crave this...excitement."
                vivithinking "She's eating out of my palm... Don't spook her now!"
            # END
            vivi happy "I've been called naughty before. So I propose a game of knowledge."
            # JUMP TO: vivi neutral "It's called {i}Never Have I Ever{/i}."

    vivi neutral "It's called {i}Never Have I Ever{/i}."
    ava "How is it played?"
    vivi "I'll tell you something I haven’t done. If you have, you take a drink. I'll go first."

    # <CHOICE>
    vivi neutral "Never have I ever..."

    # DECAY ROUTE
    if dec_meter >= 40:
        # play sound decchoice
        ava sad "We misspoke. We wish to drink alone."
        vivithinking "Up yours, snooty patootie."
        vivi "Well then. See ya, sunshine."
        # JUMP TO: vivithinking "What are the others doing, I wonder?"
        jump dep_fr1_ava_end

    menu: 
        # OPTION 1 +DECAY
        "...had a pet.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi sad "...had a pet."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava "Do we drink if we have?"
            vivi "Exactly."
            vivithinking "Daaang! She pounded that one."
            vivi sad "Want to talk about it?"
            ava sad "We do not."
            # ??DECAY
            if dec_meter >= 40:
                ava "Never have we ever..."
                vivi surprised "It's called {i}Never Have{/i} I {i}Ever{/i}."
                ava sad "This game displeases us."
                vivi angry "Don't blame the game."
                ava angry "Surprisingly, you are correct. {i}You{/i} displease us."
                vivi angry "We know where we are not wanted."
            # END
            vivi "Well then. See ya, sunshine."
            # JUMP TO: vivithinking "What are the others doing, I wonder?"

        # OPTION 2 +ATTRACTION
        "...flirted with a goddess. Or the avatar, or whatever.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr1 / att_num_list_ava[4])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi happy "...flirted with a goddess. Or the avatar, or whatever."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            # ??ATTRACTION
            if att_meter_ava >= 55:
                vivithinking "She's not drinking...hmmm?"
                ava sad "We are no longer an avatar. Or a goddess. We are...no one."
                vivi neutral "Not true. Maybe no one is just a starting point?"
            # END
            show ava sad blush
            ava "Your flirtation pleases us. Never have we ever spat."
            vivithinking "Well, chug-a-lug, Vivi!"
            vivi happy "Any reason why not?"
            show ava surprised -blush
            ava surprised "We represent the goddess, Vivi. We must not profane."
            vivi "Well, since we're dead and all, don't you think you can? Taboo's over, no?"
            ava "You have given us much to consider. Many thanks."
            vivi "You know where to find me."
            vivithinking "Oh shitballs!! Did I really say that out loud just now?! Cornier than a dad joke!"
            ava happy "We do. Good-bye, Vivi."
            vivi "See ya, Asha."
            #JUMP TO: vivithinking "What are the others doing, I wonder?"
            
            
        # OPTION 3 >>ATTRACTION +ATTRACTION
        "...made a commitment to someone." if att_meter_ava >= 50:

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr1 / att_num_list_ava[4])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi sad "...made a commitment to someone."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            ava sad "We do not drink then." 
            # ??ATTRACTION
            if att_meter_ava >= 60:
                show ava sad blush
                ava "We understand this pain, Vivi. We feel as you."
                vivithinking "Goddamn she dug deep. It's in her eyes."
                vivi happy "Wow. Thank you, Asha. I know it's hard to share your pain."
                show ava sad -blush
                ava sad "At times...we feel we are drowning in it. Our mind whirls."
                vivi neutral "Close your eyes and breathe. It's helped me before."
            # END
            ava "Ours was taboo. Why did you not find a love-mate?"
            vivi sad "Never had the time."
            # ??ATTRACTION
            if att_meter_ava >= 65:
                show ava neutral blush
                ava "Had or made?"
                vivi surprised "Good question, Asha!"
                show ava neutral -blush
                ava neutral "Our choices pave our paths forward. Is it not so?"
            # END
            vivi happy "It sure is. Good talk. I really... It felt awkward but I'm glad I shared."
            ava happy "We felt as you. Good-bye, Vivi."
            vivi "See ya, Asha."
            #JUMP TO: vivithinking "What are the others doing, I wonder?"

    label dep_fr1_ava_end:

        vivithinking "What are the others doing, I wonder?"

        # JUMP TO: Asha Susurha convo
        jump depression_asha_susurha