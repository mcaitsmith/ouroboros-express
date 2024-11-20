# The scene starts here.

label anger_fr2_susurha:

    #FREE ROAM 2 - SUSU'RHA

    # LOCATION: dining car
    # call check_overlay from _call_check_overlay_8
    scene diningcar with fade

    show vivi neutral at left with dissolve : 
        xzoom -1 
    show susurha neutral at right with dissolve
        
    vivi neutral "Susu'Rha! My favorite reptilian! Care to play some darts?"
    susurha neutral "I'm flattered, but what exactly is this...\"darts?\""
    vivi neutral "You toss pointed sticks at that round board over there. You score points based on how well you hit the target, and if you score enough points, you win."
    
    # <CHOICE>
    susurha happy "In the Viridian Wood, we played a game similar to this. Instead of a round board, we used the carcasses of Burrowers."
    
    menu:
    # OPTION 1
        "(And that's what happens when you don't have a TV.)":
    
            vivithinking neutral "And that's what happens when you don't have a TV." 
    
            # JUMP TO susurha neutral "And we used magic to increase our accuracy."

    # OPTION 2
        "(Note to self: don't die in the Viridian Wood.)":

            vivithinking neutral "Note to self: don't die in the Viridian Wood."
            vivithinking neutral "The funeral will not be pretty."

            # JUMP TO susurha neutral "And we used magic to increase our accuracy."
    
    susurha neutral "And we used magic to increase our accuracy."
    vivithinking neutral "Well then, nice of you to be born in a magical world."

    # <CHOICE>
    susurha neutral "Doubtful you could best me in a contest of accuracy." 

    menu:
    # OPTION 1 +ATTRACTION
        "The arrogance on this one. I'd sure love to shut them up.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_anger_fr2 / att_num_list_susurha[1])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivithinking "The arrogance on this one. I'd sure love to shut them up."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi neutral "Magic or not, I'm gonna beat you."
            susurha neutral "I will give you the grace of going first."

            # SOUND: dart hits the board
            play sound darts
            pause 2.0

            vivi happy "Bullseye!"
            susurha angry "Bullseye?!"
            vivi happy "A bullseye is when you hit the dartboard dead center."

            # SOUND: dart hits the board
            play sound darts
            pause 1.0
            show darts_susu_1 with dissolve
            $ renpy.pause()
            hide darts_susu_1 with dissolve

            susurha happy "Mine hit close, does that count for something?"
            vivi happy "Not as much as a bullseye!"
            susurha surprised "Hmm... seems my magic doesn't work here."
            vivi happy "Either that, or I'm better at darts than you."
            susurha neutral "In that case, thank you for not patronizing me by pretending to be something you're not — in this case, inadequate at this darts game."
            vivi neutral "You're...welcome." 
            #JUMP TO: susurha neutral "..."



    # OPTION 2 +DECAY
        "Clearly, they're insecure. I'm gonna let them win.":

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

            vivithinking "Clearly, they're insecure. I'm gonna let them win."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            vivi neutral "You go first."
            
            # SOUND: dart hits the board
            play sound darts
            pause 2.0

            susurha happy "Bullseye! Oh, how simple!"
            susurha happy "No wonder you humans enjoy this."
            
            # SOUND: dart hits the board and then the floor
            play sound darts
            pause 1.0
            show darts_susu_2 with dissolve
            $ renpy.pause()
            hide darts_susu_2 with dissolve

            vivi angry "Urghhh. Stupid dart."
            susurha happy "Am I supposed to believe that you can't hit the board from this distance?"
            vivi neutral blush "..."
            vivi neutral "Sorry. It seemed like you could use a win. After being banished from your kingdom, and well, dying."
            susurha neutral "Actually, I banished myself." 
            # JUMP TO: susurha neutral "..."

    susurha neutral "..."

    # SOUND: dart hits the board
    play sound darts
    pause 2.0
 
    susurha surprised "Vivienne. You seem almost relaxed."
    vivi happy "I am. For a moment I almost forgot how I got here."
    susurha neutral "How did you get here?"

    # <CHOICE>

    menu:
    # OPTION 1 +ATTRACTION (removing meter effect for balance)
        "It was an assignment given to me by my agent.":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_susurha += int(att_max_anger_fr2 / att_num_list_susurha[1])

            vivi neutral "It was an assignment given to me by my agent, Chloe. She told me to write an exposé about a mysterious train line with an enigmatic conductor."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            vivi happy "I said yes because it reminded me of those internet horror stories I grew up with."
            vivi neutral "Seems like the stories swirling around the Ouroboros Express were more than just stories."
            vivi sad "Now I'm dead..."
            show susurha sad
            vivi sad "I'm going to miss living."
            susurha sad "Vivienne. I'm so sorry, my dear. But you cannot blame yourself for this travesty."
            # JUMP TO: susurha neutral "The fault lies with your "agent.""

    # OPTION 2 +DECAY (removing meter effect for balance)
        "I didn't have a choice.":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi angry "I didn't have a choice."
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            susurha neutral "Do tell."
            vivi angry "I'm a reporter. I go where the story is. Wherever Chloe tells me to go."
            vivi sad "What a silly reason to die."
            susurha sad "Oh, Vivienne. I'm sorry. "
            susurha neutral "But you must remember that you did not come here on your own. Someone told you to come."
            # JUMP TO: susurha neutral "The fault lies with your \"agent.\""

    susurha neutral "The fault lies with your \"agent.\" This Chloe individual."
    vivi neutral "Yeah. It does."

    # SOUND: dart hits the board
    play sound darts
    pause 2.0

    susurha neutral "Why don't you envision your \"agent\" being at the target's center?"
    vivi happy "Okay!"
    susurha neutral "Now, hold that dart firmly in your hand."
    susurha neutral "Concentrate on the board. And see \"Chloe\"..."
    susurha neutral "...Now, let go."

    # <CHOICE>
    vivithinking "Chloe..."
    menu:
    #OPTION 1 +DECAY
        "(Pierce Chloe!)":

    # mica, I believe the above is an action rather than something vivi says. Same w/ option 2

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

            vivithinking "Pierce Chloe!"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            vivi angry "It's all her fault!"
            vivi angry "HER!"
            vivi angry "SHE had to discover this \"exclusive story.\""
            vivi angry "SHE had to get me to come here!"
            vivi angry "SHE killed me!"
            vivi angry "It's HER FAULT!"
            # VISUAL: the screen shakes
            susurha happy "You got a bullseye!"
            vivithinking neutral "God, I'm out of breath!"
            susurha neutral "Thank you, Vivienne. I hope you feel a bit better now."
            susurha neutral "Would you like to know what brought me here?"
            vivi neutral "*GASPS* Sure. *HEAVES* Why not."
            # JUMP TO: susurha sad "It was fear that brought me here."

    #OPTION +ATTRACTION
        "(Pierce the idea that it was her fault.)":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_anger_fr2 / att_num_list_susurha[1])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivithinking sad "No. . . this isn't right.'"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            # SOUND: dart hits the board
            play sound darts
            pause 2.0
            susurha happy "Bullseye!"
            vivi sad "It's not her fault. It's mine."
            vivi angry "I was the master of my fate, and I chose to come here!"
            vivi sad "How galactically stupid."
            susurha neutral "Would you like to know what's even more galactically stupid?"
            # JUMP TO: susurha sad "It was fear that brought me here."

    susurha sad "It was fear that brought me here."
    susurha neutral "It was a night like any other. The stars were out in their most intense configurations, lighting the sky as the gods had always intended. All was quiet."
    susurha neutral "But then we heard rumbling in the distance."
    susurha neutral "Then there was smoke. So much of it. Everyone ran as fast as they could."
    susurha sad "That's when I saw it."
    susurha sad "My city, where my family had lived for hundreds of generations, besieged by Tellethor's great army."
    vivithinking surprised "Oh wow."
    vivi sad "What did you do?"
    susurha sad "I ran home."
    susurha angry "I thought that if I could just GET THERE, I could save them."
    susurha sad "But the smoke was too much. None of us could see. I couldn't breathe."
    susurha sad "Then...a sharp pain and...darkness."
    susurha sad "I woke up here."
    susurha angry "I have no idea whether my family--that I abandoned--is okay. My fear is I'll see them walk into this dining car, like me, wondering what happened."    
    susurha angry "If only I had been there to protect them."
    susurha sad "They died because I abandoned them."

    # <CHOICE>

    menu:
    #OPTION 1 +ATTRACTION (removing meter effect for balance)
        "You did what you could. It isn't your fault.":

            # play sound attchoice
            # show attraction_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -850
            # $ att_meter_susurha += int(att_max_anger_fr2 / att_num_list_susurha[1])

            vivi sad "You did what you could. It isn't your fault."
            # hide attraction_icon
            # with { "master" : Dissolve(0.5) }
            susurha sad "Thank you. That means something."
            
            # SOUND: dart smacks the board
            play sound darts
            pause 2.0
        
            vivithinking neutral "At least there's darts."
            vivi sad  "I'm going to miss taking pictures."
            susurha sad "I'm going to miss playing my lute under the stars."
            vivi sad "I'm going to miss internet forums. Seeing just the craziest, most nonsensical things that people would ever think to share with others."
            susurha happy "Sounds delightful."
            susurha happy "I'll miss sharing my singing voice with those who would listen."
            vivi happy "I'd love to hear your singing voice."
            susurha happy "I would happily sing for you."
            susurha sad "Quiet moments. I will miss them the most."
            vivi sad "I can't tell you the last time I was alone with my thoughts. I was always busy."
            susurha sad "Perhaps now is a good time."
            vivi sad "..."
            # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    #OPTION +DECAY (removing meter effect for balance)
        "We got a raw deal. Life is unfair.":

            # play sound decchoice
            # show decay_icon at right with Dissolve(2.0):
            #     xoffset -500
            #     # xoffset -30
            #     yoffset -750
            # $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi angry "We got a raw deal. Life is unfair."
            # hide decay_icon
            # with { "master" : Dissolve(0.5) }
            susurha angry "Certainly nothing about our present situation is fair."
            vivi angry "I HATE this train!"
            vivi angry "And the conductor. It's his fault we're here."
            susurha angry "He runs this place."
            vivi angry "He could let us off if he wanted."
            susurha angry "Instead, he toys with us for his own enjoyment. Only a devil behaves this way!"
            susurha sad "But there's nothing we can do."
            vivi angry "No. Perhaps that's the lesson."
            susurha "..."
            vivi "..."
            # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    #VISUAL: susurha exits
    hide susurha with dissolve

    vivithinking "It's not a bad idea. I could use this time to reflect."
    vivithinking "I may not get many more chances."

    # JUMP TO: Urshu Darius scene
    jump anger_urshu_darius