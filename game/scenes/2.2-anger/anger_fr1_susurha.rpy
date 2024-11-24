# The scene starts here.

label anger_fr1_susurha:

    #FREE ROAM 1 - SUSU'RHA

    # LOCATION: dining car
    # call check_overlay from _call_check_overlay_5
    scene diningcar with fade
    play ambience amb_bar fadein 1.0

    # VISUAL: screen shakes
    show diningcar with hpunch
    # SOUND: the dining car's door slams shut
    play sound doorslam
    pause 1.0

    show susurha neutral at right with dissolve

    show vivi neutral at left with dissolve:
        xzoom -1

    # SOUND: card shuffle
    play sound shuffle
    pause 2.0
    play music susumusic loop

    susurha surprised "Vivienne! What brings you here?"
    vivithinking surprised "Are they shuffling cards? Doesn't look like a deck I've ever seen."
    vivi blush surprised "Uh... nothing. Never mind. It's stupid."
    vivi neutral "...Well, actually...Do you want to...play a game with me?"
    susurha happy "Certainly! There's a wonderful game here from my childhood that I'd be honored to share with you!"
    vivi neutral "What's the game?"
    susurha neutral "Truth or Lies."
    vivi neutral "What's at stake?"
    susurha neutral "Everything. After all, we're riding a slowly decaying train headed inexorably toward the cosmic weave."
    vivi neutral "I'm not sure..."
    susurha neutral "Don't be coy. It doesn't suit you."
    vivi angry "I'm not coy."
    susurha happy "Alright then."
    susurha neutral "Time is of the essence. Sit with me, and with this deck of cards, we'll find out what's true, and what isn't."

    # <CHOICE>
    vivithinking neutral "Provocative. This one's certainly not boring." 

    menu:
        # OPTION 1 +ATTRACTION (removing meter effect for balance)
        "I'll play.":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_susurha += int(att_max_anger_fr1 / att_num_list_susurha[0])
        
            vivi neutral "I'll play."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            susurha happy "Indeed you will. There's nothing quite like an intimate question to enliven the mood." 
            # JUMP TO: susurha neutral "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."

        # OPTION 2 +DECAY (removing meter effect for balance)
        "I'd be revealing too much.":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "I'd be revealing too much."
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            susurha neutral "You don't even know the contents of the game yet, and you're already scared I may pierce your carefully crafted veneer."
            vivi angry "I'm a reporter. I don't do masks. I expose the masks of others."

            # <CHOICE>
            susurha neutral "Either you're suffering from an acute lack of self-awareness, or you're simply a bad liar."
            
            menu:
                # OPTION 2A
                "(The nerve of this creature!)":

                    vivithinking angry "The nerve of this creature!"

                    # JUMP TO: susurha neutral "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."

                # OPTION 2B
                "(Ugh. Jerk. Not far wrong, though.)":

                    vivithinking neutral "Ugh. Jerk. Not far wrong, though."

                    # JUMP TO: susurha neutral "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."

    susurha neutral "I'm going to draw cards from this deck with questions."
    play sound orex_fol_shuffle
    pause 2.0
    susurha happy "You will answer, and I will try to ascertain whether or not you are lying."
    vivi surprised "That's it?"
    vivi neutral "Hit me." 

    # <CHOICE>
    susurha neutral "The card reads, \"You are hiding something.\""


    menu:
        # OPTION 1 +ATTRACTION
        "Everyone hides something. I'm no exception.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_anger_fr1 / att_num_list_susurha[0])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral blush "Everyone hides something. I'm no exception."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "I'm the exception. All of my pretense has been burned away."
            susurha surprised "..."
            vivithinking "Why are they looking at me like that?"
            susurha neutral "The fire."  
            vivi surprised "The what?"
            susurha neutral "You're hiding fire."                         
            vivithinking "I know what they're going to say..."
            # JUMP TO: susurha surprised "You're... angry."
                    

            # OPTION 2 +DECAY
        "Me? Hiding? What about you?!":

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

            vivi angry "Me? Hiding? What about you?! What exactly are YOU hiding behind those beady eyes?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha surprised "Deflection!"
            susurha surprised "A keen observer of everything but yourself."                            
            susurha neutral "Do you know what I see when I look into your eyes?"
            susurha surprised "A boiling ocean of fury!"
            vivithinking surprised "How could they tell?"
            vivi angry "Of course I'm furious. I didn't expect to die."
            susurha neutral "This goes deeper. And it's been going on for a long time."
            # JUMP TO: susurha surprised "You're... angry."

    susurha surprised "You're...angry. And you've been angry far before your demise."

    # <CHOICE>
    vivithinking "What if they're right?"


    menu:
        #OPTION 1 +ATTRACTION
        "I am angry.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_anger_fr1 / att_num_list_susurha[0])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi angry "I am angry."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivithinking angry "And the cocky bastard leans back in their chair with a smile too. Right on cue..."
            susurha happy "You know what? For all of my years of frolicking, I believe I am too."    
            vivi neutral "Who are you angry at?"
            susurha sad "..."
            vivithinking neutral "That wiped their smile away."
            susurha angry "My... parents, the judgemental cretins."
            vivithinking surprised "Their exhale is literally so hot. Wow."
            vivi sad  "I'm sorry..."
            vivi angry "I'm angry at my ex-boyfriend. He tried to own my wins."
            susurha angry "Sounds like.. the courtiers I grew up around! Those leering, grasping snobs, interminable features of my childhood!"
            susurha neutral "What else? Don't spare the sssavory details."
            vivi angry "My ex-girlfriend stole my Datsun and got it towed in another state!"
            vivi angry  "And...and...my teacher, Mizz Costello. She told me I was pugnacious. And she meant it as an insult!"
            vivi angry  "The entire school system sucks! All systems do! Society at large!"
            susurha angry "Society! Oh, how I hate society! I fled all the way to the Viridian Wood to escape it!"           
            vivi happy "The EXPECTATIONS of people who, at the end of the day, JUST DON'T MATTER!"
            susurha happy "YES!"
            vivi angry "But most of all, my agent, Chloe. It was she who told me to get the scoop on this cursed death train." 
            susurha neutral "And here we all are."
            # JUMP TO: vivithinking neutral "To see them like that. Vulnerable. Staring back at me. It's been a while, hasn't it?"


        #OPTION 2 +DECAY
        "You're the one who's angry.":

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
        
            vivi angry "You're the one who's angry."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha happy "Again, you're deflecting."
            susurha angry "But you are right. I'm furious."
            # SOUND: sigh
            play sound char_sigh_susu
            pause 1.0
            vivithinking surprised "That exhale's like, 150 degrees. Hate to see them truly mad."
            susurha angry "The bloodsuckers. The leeches. Those with souls impervious to art and music. All of them infuriate me to no end!"
            vivithinking surprised "My face is literally burning."
            susurha neutral "..."
            susurha happy "It feels good to let it out. You should try it."
            susurha neutral "That mask you wear, it extracts a toll, you see. I know because I have been before the way you are now."
            vivi angry "..."
            vivithinking angry "What do they mean, \"That mask you wear\"? I don't have a mask!"
            vivithinking neutral "Calm down, Vivienne. Just look at them."
            # JUMP TO: vivithinking neutral "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"

    vivithinking neutral "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"
    susurha happy "I think we got what we needed from this. I imagine whoever runs this place did too."
    susurha happy "See you around, dear Vivienne."
    stop music fadeout 2.0

    # susurha exits
    hide susurha with dissolve

    vivithinking neutral "That was a lot. I'm going back to my room."

    # JUMP TO: Anger Susurha Urshu
    jump anger_susurha_urshu