# The scene starts here.

label depression_fr2_ava:

    # FREE ROAM 2 - Ava
    # LOCATION: observatory
    # call check_overlay from _call_check_overlay_31
    scene observatory with fade
    play ambience amb_observatory fadein 1.0
    play music mainmusic loop

    show vivi neutral at left with dissolve:
        xzoom -1

    show ava neutral at right with dissolve

    vivithinking "Oh, the Sun Goddess, herself. Somehow looking radiant as usual."

    # ??DECAY
    if dec_meter >= 40:
        vivi sad "She's too good for me..."
    #END

    # ??ATTRACTION
    elif att_meter_ava >= 50:
        vivi happy "I need her in my life, no matter what."
    #END

    vivithinking "Okay, Vivi, deep breath, and-"
    vivi happy blush "Asha, darling, how are you?"
    ava neutral "..."
    vivi surprised "Asha?"
    ava surprised "Oh, sunshine, we are so sorry. We couldn't detach from our memories. They are painful, you must understand. Our life has not been a happy one."

    # <CHOICE>
    menu:
        #OPTION 1 +ATTRACTION (removing meter effect for balance)
        "Really?":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_ava += int(att_max_depression_fr2 / att_num_list_ava[5])

            vivi surprised "Really? Even though the royals treated you poorly you had everything you could have ever wanted. I don't understand."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            ava sad "Of course you do not understand. How could you?"
            vivi sad "I want to...understand. How can I share your pain if you don't talk about it with me?"
            # JUMP TO: ava sad "Vivi..."

        #OPTION 2 +DECAY
        "You're pretty ungrateful, huh?":

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

            vivi angry "You're pretty ungrateful, huh? It sounds like you had everything you could have ever wanted."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava sad "How could you ever understand..."
            vivi angry "You're right, Asha. I can't and I won't. How could a puny little human peasant like me ever understand what it's like to be a princess in a castle?!"
            # JUMP TO: ava sad "Vivi..."

        #OPTION 3 >>ATTRACTION +ATTRACTION (removing meter effect for balance)
        "I wish I could have been there for you." if att_meter_ava >= 50:

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_ava += int(att_max_depression_fr2 / att_num_list_ava[5])

            vivi sad "I wish I could have been there for you. Our relationship has been the one thing keeping me sane on this journey... I wish we could have spent some time together while we were alive."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            ava happy "Really? We feel the same way." 
            # JUMP TO: ava sad "Vivi..."


    ava sad "Vivi..."
    stop music fadeout 5.0
    ava sad "We have never had a friend."
    vivi angry blush "What about me?! I thought we were friends!"
    ava surprised "That may be true, but we will soon be separated by fate. There is no heaven awaiting for Asha."
    vivi surprised blush "Oh? And why's that?"
    play cd_ambience twinkle fadein 5.0 volume 0.2
    play music ashamusic fadein 5.0 loop
    ava neutral "{i}*sigh*{/i} You are aware that I am not the first Avatar of Asha. Every twenty and five years, a new avatar is chosen."
    ava sad "Soleos was not always the peaceful society it is today. The planet was once split in two, marred by war and terror...until the Avatar arrived."
    ava sad "She was born from the seed of a Solarian man and the egg of a Lunolian woman. The mixing of cultures was considered taboo, said to bring about the end of the world."
    vivi sad "Oh, my goodness. I had no idea."
    ava sad "The woman who gave birth to Asha was my ancestor, far removed. My bloodline is the only one that can act as a vessel for the Avatar."

    # <CHOICE>
    menu:
        #OPTION 1 +ATTRACTION
        "But why do you need her to begin with?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr2 / att_num_list_ava[5])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi surprised "But why do you need her to begin with? I wish you could have had a normal life on Earth."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            ava sad "Without the Avatar, our world would be doomed. These hands have seen much bloodshed."
            vivi surprised "I didn't realize that your life wasn't all sunshine and rainbows."
            ava sad "It is not your fault, for we did not share with you. It is not an easy thing to broach lightly."
            stop cd_ambience fadeout 5.0

            # JUMP TO: vivi neutral blush "I'm sorry, Asha."


        #OPTION 2
        "Why are you telling me all this now?":

            vivi surprised "Why are you telling me all this now?"
            stop cd_ambience fadeout 5.0
            ava sad "What better time to share our ways than at the end of the world?"
            vivi happy "I guess you make a good point."

            #JUMP TO: vivi neutral blush "I'm sorry, Asha."


        #OPTION 3 >>ATTRACTION (+ATTRACTION?)
        "If only I had known you in life." if att_meter_ava >= 55:

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr2 / att_num_list_ava[5])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi sad "If only I had known you in life, things could have been different."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            show ava neutral blush
            ava "A little bit of love would have gone a long way."
            vivi happy blush "Well I'm glad we can spend this time together now."
            stop cd_ambience fadeout 5.0
            show ava neutral -blush

            # JUMP TO: vivi neutral blush "I'm sorry, Asha."

    vivi neutral blush "I'm sorry, Asha."
    stop music fadeout 5.0

    show ava neutral blush

    # ??ATTRACTION
    if att_meter_ava >= 55:
        ava "No need. Just be here now."

        #pause

        # SOUND: heartbeat
        play sound heartbeat
        pause 3.0
        stop sound fadeout 1.0

    #END

    ava "We want to know more about your life on Earth. What can you tell us?"
    show ava neutral -blush

    # <CHOICE>
    menu:

        #OPTION 1 >>ATTRACTION (+ATTRACTION) - updating to be non-conditional
        # "My family moved around a lot..." if att_meter_ava >= 60:
        "My family moved around a lot...":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_ava += int(att_max_depression_fr2 / att_num_list_ava[5])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "My family moved around a lot, from country to country."
            play music peacefulmusic loop
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi neutral "I'm luckier than most - seen and experienced so many amazing cultures."
            vivi sad "But it's lonely for a kid, you know? As soon as I made friends, started feeling comfortable... We'd uproot again."
            ava neutral "Ah, you were a lonely child. We understand this."
            vivi sad "Over time, I just felt like it was easier to not make friends... And even when my family stopped moving, I just kept going."
            ava neutral "Did you find solace in other things?"
            vivi happy "Yes - there were always books... and I guess I retreated into those pages."
            vivi happy "I think that's why I wanted to become a writer, you see. When people disappointed me, books were always there."
            vivi sad "Unfortunately, needing money meant that I became a reporter instead of a novelist. It's one of my regrets." 
            vivi sad "I wish I'd pursued my passions more."
            vivi surprised "I'm sorry, I forgot myself. I'm trauma dumping."
            ava sad "Please do not apologize. We, too found shelter in the palace library."
            ava neutral "Your imagination, it must have grown, no?"

            # JUMP TO: vivi happy "Like you wouldn't believe!"



        #OPTION 2 >>DECAY (+DECAY?)
        "I wrote this haiku in school once." if dec_meter >= 50:

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

            vivi happy "I wrote this haiku in school once. Wanna hear it?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            ava surprised "Go on."
            vivi happy blush "Tasty soup tasty. Tasty soup tasty soup mmm. Tasty tasty soup."
            ava surprised "Wow. You do have a way with words."
            # JUMP TO: vivi happy "Like you wouldn't believe!"


        #OPTION 3 NEUTRAL
        "Earth is beautiful.":

            play music peacefulmusic loop
            vivi happy blush "Earth is beautiful. In its own way. There are thousands of unique cultures and ways of life that thrive in different ecosystems, from deserts and mountains to swamps and snow."
            ava happy "We cannot imagine..."
            vivi happy "And the people! I've reported on so many stories, interviewed so many strange characters."
            vivi neutral "I just wish I could have taken my time in the places I traveled to. Really got to know some people - or someone."
            show ava surprised blush
            ava "Is there really so much diversity on your Earth?"
            show ava surprised -blush
        # JUMP TO: vivi happy "Like you wouldn't believe!"


    vivi happy "Like you wouldn't believe!"
    show ava neutral blush
    ava "Well our conversations have certainly helped us feel better. We enjoy your...perspective."
    vivi happy blush "Come to Earth sometime! I'll show you around!"

    # ??DECAY
    if dec_meter >= 50:
        stop music fadeout 1.0
        show ava sad -blush
        ava sad "If only we could have..."
    #END

    # ??ATTRACTION
    elif att_meter_ava >= 60:
        stop music fadeout 5.0
        show ava happy blush
        ava "It's a date. We look forward to it."
    #END

    vivi sad blush "I should go... See you soon, Asha."
    show ava neutral blush
    ava "Remember, The All is the One."
    vivi blush "The All is the One..."

    # JUMP TO: Depression NPC Group Scene
    jump depression_npc_group_scene