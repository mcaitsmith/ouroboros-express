# The scene starts here.

label denial_cs2:

    #Character Selector 2

    #LOCATION: cabin
    scene cabin with fade
    play ambience amb_bedroom if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    vivi neutral "That was... interesting. Looks like I wasn't the only one blindsided by this train. I need some time to gather my thoughts."
    $ ava_fullbody = False
    $ darius_fullbody = False
    # Fade to blur if possible.
    show cabin blur with dissolve

    vivithinking "This car has big windows..."
    vivithinking "What I see behind those windows makes...zero sense though."
    vivithinking "Surreal landscapes—blending into a swirl of colors. The train's breathtaking speed blurs everything into cosmic spaghetti. It gets darker. Darker."

    # Fade back in.
    show cabin -blur with dissolve

    vivi sad "This can't be happening."
    #$ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(400), replace=True, duration=1.0)
    #play sound heartbeat
    #pause 5.0
    #$ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5.0)
    vivi angry "It can't end like this."

    # <CHOICE>
    vivi neutral "I should go talk to someone else. I can't be the only one who wants off this ride."
    stop music fadeout 5.0

    # Note that whoever you talked to in free roam 1 should be unavailable as an option.

    menu:

    # OPTION 1
        "Avatar of Asha" if fr1_denial_choice != "Ava":

            vivi happy "I should try the goddess. I think she's in the observatory."
            stop ambience fadeout 1.0
            #JUMP TO: Free Roam 2 / Avatar of Asha
            jump denial_fr2_ava

    #OPTION 2
        "Darius Wrecker" if fr1_denial_choice != "Darius":

            vivi neutral "I have a feeling Darius knows more than he's letting on. I believe he's in the dining car."
            stop ambience fadeout 1.0
            #JUMP TO: Free Roam 2 / Inquisitor Darius Wrecker
            jump denial_fr2_darius

    #OPTION 3
        "Susu'Rha Balrinn" if fr1_denial_choice != "Susu'Rha":

            vivi neutral "I feel like the druid wants out too. Maybe they can help me figure this all out. I think they're in the lounge."
            stop ambience fadeout 1.0
            #JUMP TO: Free Roam 2 / Susu'Rha Balrinn
            jump denial_fr2_susurha