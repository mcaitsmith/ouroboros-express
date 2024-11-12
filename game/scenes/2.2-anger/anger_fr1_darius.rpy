# The scene starts here.

label anger_fr1_darius:

    #FREE ROAM 1 - DARIUS 

    # LOCATION: lounge
    # call check_overlay from _call_check_overlay_4
    scene lounge with fade
    play ambience amb_lounge if_changed fadein 1.0

    show darius angry at right with dissolve

    vivithinking angry "I can feel them. Seething."

    show darius neutral at right

    show vivi neutral at left with dissolve:
        xzoom -1

    darius neutral "Well. Cards, then?"
    vivi surprised "Of course you read my mind already. Do you actually want to play?"
    darius angry "Why not? Seems as though we can't do anything else at the moment."
    vivi neutral "I don't know a lot of card games."
    darius surprised "I thought that's all you humans did. Play games. Fritter away your time."
    darius neutral "We'll play a game I know called Hearts. No need to explain. You'll catch on quickly, even as a human. And we'll learn about each other. About this place. About Urshu."
    vivithinking neutral "Mon dieu, his hands. Dextrous fingers. Manicured claws."
    
    # <CHOICE>
    darius neutral "..."
    stop music fadeout 5.0
    
    menu:
    # OPTION 1
        "(Wait, what is this feeling?)":

            vivithinking blush "Wait, what is this feeling?"
            vivithinking blush "Displeasure? Embarrassment? Satisfaction?"
            vivithinking -blush "Ughhh I got so distracted."

            # JUMP TO darius neutral "You start."

    # OPTION 2
        "(Damn, caught staring in the act!)":

            vivithinking neutral "Quick, eyes somewhere else. Literally anywhere else, Vivi."

            # JUMP TO darius neutral "You start."

    # <CHOICE>
    darius neutral "You start."

    menu:
    # OPTION 1 +ATTRACTION
        "Can you even play this with two people?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_anger_fr1 / att_num_list_darius[0])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi surprised "Can you even play this with two people?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            darius happy "Of course you can. Watch me."
            # SOUND: cards shuffling
            play sound shuffle
            pause 2.0
            vivi neutral "You deal so swiftly."
            show darius happy blush
            darius "That's kind."
            vivi neutral "I'm surprised, given your history."
            show darius angry -blush
            vivithinking surprised "Definitely should not have said that."
            darius "What could you possibly understand about my history?"
            vivi surprised "..."
            # JUMP TO: darius angry "You still haven't played a card. Take your turn already."

    # OPTION 2 +DECAY
        "You mentioned Urshu. Why bring him up?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_anger / dec_num_anger)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "You mentioned Urshu. Why bring him up?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius angry "That little twerp knows more than he lets on."
            play sound shuffle
            vivi surprised "You're getting angry."
            darius angry "Yes. You should be, too."
            vivi surprised "What makes you think I'm not?"
            darius neutral "This place. I know it. We shouldn't be here."
            vivithinking "Now, what does that mean?"
            # JUMP TO: darius angry "You still haven't played a card. Take your turn already."

    darius angry "You still haven't played a card. Take your turn already."
    vivi angry "Don't tell me what to do."
    darius neutral "There's no reason to get snippy with me. I'm not the one who trapped us all here."
    vivi angry "Who are you calling 'snippy'? You're being aggressive. No way to talk to a lady."
    # SOUND: telepathy
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=1.5)
    $ renpy.music.set_volume(0.25, delay=1.5, channel='music')
    play sound char_telepathy
    pause 3.0
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5)
    $ renpy.music.set_volume(1.0, delay=5.0, channel='music')
    vivithinking surprised "That flare of rage again. So bright, it's almost painful."
    darius surprised "Well. That's... interesting."
    vivi surprised "What is?"
    darius neutral "You're unreadable. That is... unusual."
    vivi neutral "I'm happy to answer any questions you might have about me."
    darius neutral "Why waste energy on words when I can simply read what's in front of me without them?"
    vivi happy "Ah, but you can't, can you? And you find that frustrating. Tell me about it."
    darius angry "You're needling me. Play a card, damn you."
    vivi happy "Not without knowing what's making you so testy."
    darius angry "I have never once been 'testy' in a millennia of existence."
    vivi happy "And yet... here I am, not playing a card."
    vivithinking surprised "That rage. Pure. So hot that it makes my cheeks flush."
    darius angry "Fine. Vivi. Normally, I can read the beings around me. It's what makes me such an excellent judge of... character. But since arriving here, that's changed. I feel...cut off. Disarmed."
    vivi neutral "Darius, you shouldn't be reading my mind without asking first anyway. Bit rude."
    stop music fadeout 5.0
    show darius surprised blush
    darius "I...I'm not trying to—"
    vivi happy "Please don't do it again. Your turn!"


    # <CHOICE>
    show darius neutral blush
    play music dariusmusic fadein 5.0
    darius "Forgive me. All of this is new. As I said: unusual." 

    menu:
    # OPTION 1 
        "Qualify that. 'Unusual'.":

            vivi neutral "Qualify that. 'Unusual'."
            show darius neutral -blush
            darius "I don't know how else to explain it. Things were one way. Now, they're not. I'm... adjusting."
            vivi neutral "I guess we should do our best to adjust together."
            darius happy "We can try that."
            vivi neutral "..."
        # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."

    # OPTION 2 +ATTRACTION
        "That sounds difficult. Like being unmoored.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_anger_fr1 / att_num_list_darius[0])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi sad "That sounds difficult. Like being unmoored."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            show darius surprised -blush
            darius "Yes, exactly. 'Unmoored.' You have a way with... words."
            vivi happy "Aw, you're just saying that. You think so?"
            darius angry "You're mocking me."
            vivi surprised "I'm not! Trust me. When I'm mocking you, you'll know."
            darius happy "Well then. I look forward to it."
            vivi happy "..."
            # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."


    # OPTION 3 +DECAY
        "Well, you don't hear me crying about it.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_anger / dec_num_anger)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')
        
            vivi neutral "Well you don't hear me crying about it."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            show darius surprised -blush
            darius "I'm sorry?"
            vivi neutral "You heard me. Things may be different, but they aren't dire."
            darius angry "Not yet, anyway. Give it time, Vivienne. You're just like the rest of your kind."
            vivi angry "You don't know me, Darius."
            darius neutral "I never claimed to."
            vivi angry "..." 
            darius angry "..."
            # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."


    vivi neutral "You're doing a terrible job at playing this game. And you didn't even explain it."
    darius neutral "It would seem so. And it was my suggestion. Apologies. Perhaps another time when I'm less... distracted."

    # darius exits
    hide darius with dissolve

    # vivi exits
    hide vivi with dissolve

    # JUMP TO: Anger Susurha Urshu
    jump anger_susurha_urshu