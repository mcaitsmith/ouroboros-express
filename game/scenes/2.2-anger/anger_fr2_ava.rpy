﻿# The scene starts here.

label anger_fr2_ava:

    #FREE ROAM 2 - AVA

    # LOCATION: dining car
    # call check_overlay from _call_check_overlay_6
    scene diningcar with fade
    play ambience amb_bar if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    # SOUND: dart hitting the board
    play sound darts
    pause 2.0

    vivithinking neutral "I hear darts. Is that...Asha? Here already?"

    show ava neutral at right with dissolve

    ava neutral "Ah, bullseye. Game of darts, Vivienne? We hear your watering holes often host such competitions." 
    vivi neutral "Watering holes? You mean a pub?"

    # SOUND: dart hitting the board 
    play sound darts
    pause 2.0

    ava neutral "Good throw, Vivienne. But no such term exists on Soleos."
    vivi happy blush "Well, technically you could call it a watering hole. But we call it a pub...or a bar if they don't have Guinness."
    vivi sad blush "I miss my pub back home, but that's all. What was your home like?"
    ava happy "Though servants catered to us, people worshipped us...it was but an ornate patina, we were forbidden friendship and family. We lived in solitude."

    # <CHOICE>
    vivi surprised "My God, that sounds..."

    menu:
        # OPTION 1 +DECAY
        "Amazing.":

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
        
            vivi happy "Amazing. Peace and quiet? Now that's luxury."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava sad "No, Vivienne, perpetual loneliness. We would not wish that even upon our monarchy."
            # SOUND: dart hitting the board
            play sound darts
            pause 1.0
            # JUMP TO: ava happy "Another bullseye. Your turn, little one."

        # OPTION 2 +ATTRACTION
        "Awful.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_anger_fr2 / att_num_list_ava[1])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi sad "Awful. I'm so sorry. I can't even begin to imagine."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            show ava sad blush
            ava "Thank you...that means more to us than you know."
            # SOUND: dart hitting the board
            play sound darts
            pause 1.0
            show ava happy -blush
            # JUMP TO: ava happy "Another bullseye. Your turn, little one."

        #OPTION 3
        "Crazy.":
            vivi neutral "Crazy. Your life is like a rollercoaster!"
            ava neutral "A...rollercoaster?... We do not quite understand the meaning of this word."
            vivi happy "It's something that moves quickly with lots of ups and downs."
            ava neutral "We...still struggle to grasp why you have this torture device, but your meaning is clear."
            # SOUND: dart hitting the board
            play sound darts
            pause 1.0
            # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    show darts_asha with dissolve
    $ renpy.pause()
    hide darts_asha with dissolve
    ava happy "Another bullseye. Your turn, little one."
    vivi angry "I thought I asked you to stop calling me that."
    ava sad "Oh, do not take offense at our term of endearment. We are warming up to you."
    vivithinking angry "I'm feeling warm too. Hot blood's creeping up into my face. Ughhh. I gotta let this out...And THROW!"
    # SOUND: dart hitting the board
    play sound darts
    pause 2.0

    # <CHOICE>
    vivi angry blush "Well...it's still demeaning. I don't like it."

    menu:
        #OPTION 1 +DECAY (removing meter effect for balance)
        "But if you like it...":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi happy blush "But if you like it...I guess I could get used to it."
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            show ava happy blush
            ava "No. We never wish to offend you."
            vivithinking happy "I'll do anything she wants to spend some more time with her...!"
            show ava happy -blush
            # JUMP TO: vivi neutral "Sure. Anyways..."

        #OPTION 2 +ATTRACTION (removing meter effect for balance)
        "Don't ever call me that again.":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_ava += int(att_max_anger_fr2 / att_num_list_ava[1])

            vivi angry "Don't ever call me that again. I don't like it. I'm not your pet."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            show ava sad blush
            ava "By Asha, we beg forgiveness. We never intended harm."
            vivi  "..." 
            vivi sad blush "It's...just...old memories. Sorry, I snapped."
            vivithinking angry "An ex-boyfriend called me 'little one' à la Yoda. Ugh!"
            show ava sad -blush
            ava "There is no need to explain. We understand...Vivienne."
            # JUMP TO: vivi neutral "Sure. Anyways..."

        #OPTION 3 
        "My old roommates called me dildo.":

            vivi blush "My old roommates called me dildo. It's a...personal massage device. For...relaxation?"
            ava happy "Oh! Those. The orgies after were most pleasureable!"
            vivi happy blush "Oh! I didn't know Soleos did...that."
            show ava happy blush
            ava "Perhaps our other customs might tempt you?"
            vivithinking surprised "Write this down. WRITE THIS DOWN!"
            # SOUND: dart hitting the board
            play sound darts
            pause 2.0
            show ava happy -blush
            # JUMP TO: vivi neutral "Sure. Anyways..."

    vivi neutral "Sure. Anyways..."
    
    # <CHOICE>
    vivi neutral blush "I've been meaning to ask you:"

    menu:
        # OPTION 1 +DECAY (removing meter effect for balance)
        "What are your thoughts on our conductor?":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "What are your thoughts on the conductor?"
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            ava surprised "Ah, Urshu. A mystery."
            vivi "Personally...I think he's undead."
            ava surprised "A zombie?"
            vivithinking surprised "Wow, she almost sounded human for a sec."
            ava neutral "Why do you smile so?"
            vivi neutral "..."
            vivi happy blush "No reason!"
            ava neutral "I suppose humans do rank in the highest percentile for creatures who smile without cause." 
            # JUMP TO: vivi neutral "How...interesting."    

        # OPTION 2 +ATTRACTION (removing meter effect for balance)
        "What do you want to do with your time left?":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_ava += int(att_max_anger_fr2 / att_num_list_ava[1])

            vivi neutral "What do you want to do with your time left?"
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            ava sad "..."
            ava neutral "Enjoy the view. We seldom saw nighttime. It is strange. Nice."
            vivi happy "It is pretty nice, huh." 
            show ava happy blush
            ava "We would enjoy spending more time talking with you."
            vivithinking surprised blush "BRRRRT BRRRTT! Flirt alert!!"
            show ava happy -blush
            # JUMP TO: vivi neutral "How...interesting."    
    
    vivi neutral "How...interesting."
    # SOUND: dart hitting the board and dropping to the floor
    play sound darts
    pause 2.0
    vivi angry "Aw shit. Dumbass dart."
    ava angry "We wish you would refrain from such vulgarity."
    vivi angry "If you really want to get to know me better, then deal! Like I do with your ego."
    
    # <CHOICE>
    ava angry "Hmph. And to think we ever considered you special..."

    menu:
        #OPTION 1 +ATTRACTION +DECAY
        "Don't play games with me.":

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
            $ att_meter_ava += int(att_max_anger_fr2 / att_num_list_ava[1])
            $ dec_meter += int(dec_max_anger / dec_num_anger)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi angry "Don't play games with me."
            hide attraction_icon
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava neutral "Ah. Because you lack skill at darts?" 
            vivi angry "Look, you may have been some kind of big deal deity on Soleos, but we're all equals here on death row, you silly moose!"
            # JUMP TO: ava blush angry "You dare speak to us with such impudence! Refer to us as Asha or not at all!"

        #OPTION 2 +DECAY
        "I don't need you to think I'm special.":

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

            vivi angry "I don't need you to think I'm special. Just because your crazy cult revered you doesn't mean that I'm going to, ass hat!"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            # JUMP TO: ava blush angry "You dare speak to us with such impudence! Refer to us as Asha or not at all!"

    ava angry "You dare speak to us with such impudence! Refer to us as Asha or not at all!"
    
    # <CHOICE>
    vivithinking "..."
    
    menu:
        # OPTION 1
        "(Nice one, Vivi. Handled that with all the grace of an ornery bull.)":
            
            vivithinking neutral "Nice one, Vivi. Handled that with all the grace of an ornery bull."

            # JUMP TO vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."

        # OPTION 2
        "(Like I have time to worry about manners. Still...)":

            vivithinking neutral "Like I have time to worry about manners. Still, maybe I should say..."

            # JUMP TO vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."
    
    vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."
    ava sad "Please...go."
    vivithinking sad "Ugh! I messed up. Maybe they'll accept my apology tomorrow..."

    # JUMP TO: Urshu Darius scene
    stop ambience fadeout 1.0
    jump anger_urshu_darius