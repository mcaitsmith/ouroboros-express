# The scene starts here.

label denial_fr2_ava:

    #FREE ROAM 2 - Avatar of Asha
    #LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0


    show vivi neutral at left with dissolve :
        xzoom -1

    vivithinking "Many thoughts... Head full."
    vivithinking "Oh. I ended up in the observatory."
    vivithinking "Well, the goddess is here, staring into the darkness."

    show ava neutral at right with dissolve
    play music ashamusic fadein 1.0
    vivi happy "Hey Ash, I think I found us a way out of this bi-"
   
    # <CHOICE>
    ava angry "You may refer to us as Asha or Avatar of the Eternal Light... but your proposition has intrigued us. Proceed."
    
    menu:

    # OPTION 1
        "(Bruh. Stick up your ass, much?!)":

            vivithinking angry "Bruh. Stick up your ass much?!"

            # JUMP TO vivi neutral "Well then, if your Eternal Shininess agrees, I'll go grab the others."

    # OPTION 2
        "('Proceed'? Very well, {i}m'lady{/i}. I shall proceed forthwith.)":

            vivithinking neutral "'Proceed'? Very well, {i}m'lady{/i}. I shall proceed forthwith."

            # JUMP TO vivi neutral "Well then, if your Eternal Shininess agrees, I'll go grab the others."
   
    vivi neutral "Well then, if your Eternal Shininess agrees, I'll go grab the others."
    ava surprised "Those poor creatures? Pay them no mind. Their only worry is their own insignificance."
    vivithinking "What a self-important prickle this Avatar of ASSha is!" 
    ava sad "Like sand in the wind."

    # <CHOICE>
    vivithinking "Who does she think she is?"

    menu:

    # OPTION 1 
        "Asha! Or Avatar! Whatever! How dare you!":

            vivi angry "Asha! Or Avatar! Whatever! How dare you!" 
            vivi angry "If you feel that way, why are we even speaking? I'm one of them, you know!"
            show ava sad blush
            ava "Our humblest apologies, Vivi. We never intended to offend you. We have led vastly different lives, you see."
            vivi neutral "Well you've managed to offend me regardless." 
            show ava neutral -blush
            ava "Let us talk about something else... you were saying earlier?"
            #JUMP to vivi saying "Yeah, so about that exit I mentioned..." 

    # OPTION 2 +ATTRACTION
        "Maybe we all matter, Asha.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "Maybe we all matter, Asha."
            vivi sad "Maybe we're all just specks of sand on a cosmic beach."
            vivi sad "Our lives only have the value we give it. Yours. Mine. Theirs."
            ava sad "There are times we wished for a simpler life. Family. Friends. Love, perhaps? All forbidden. Even tears."
            vivithinking surprised "Whoa. Even tears? Here I thought I was a hot mess."
            vivi sad "That must've been awful. Well, I'm here now, so dry those eyes."
            show ava sad blush
            ava "Your heart speaks strangely, but with truth. Tears do not come easily to us. Thank you, Vivi."
            show ava sad -blush
            # JUMP TO: vivi saying "Yeah, so about that exit I mentioned..." 


    # OPTION 3 +ATTRACTION
        "Asha, respectfully, I disagree with you.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "Asha, respectfully, I disagree with you."
            vivi neutral "Humans have identities, lives, and belief systems. Like you. We're complex. Like you. And you're no goddess. You're just a woman calling herself one."
            ava happy "Really? In our world, humans are simple creatures incapable of conscious thought." 
            vivithinking "Hold my bujo, I'm about to destroy this woman."
            vivi happy blush "Well you're speaking with me right now, are you not? I'm human. Would you say I'm incapable of conscious thought?"
            show ava surprised blush
            ava "Well, when you put it as such... who are we to argue? We apologize."
            vivithinking "About time! Still, I can't forget why I came here."
            show ava neutral -blush
            #JUMP TO: vivi saying "Yeah, so about that exit I mentioned..." 

    vivi happy "Yeah, so about that exit I mentioned..."
    vivi neutral "I spotted an emergency hatch in the glass above you. We can pop it open and escape. Look here at the win-"
    $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=8), audio_filter.Lowpass(2000)], replace=True, duration=2.0)
    play cd_ambience amb_cosmicdecay fadein 2.0
    stop music fadeout 2.0
    play sound char_mirror
    pause 5.0
    play music horrormusic
    vivi surprised "...dow"
    vivithinking "What the heck am I seeing?"
    ava surprised "Radiance protect me! What-"
    vivi surprised "IT'S LIKE THE MORTON'S SALT GIRL COVERED IN TINFOIL AND ROASTED UNDER A JET ENGINE?!"
    vivithinking "Dammit. I've seen this thing in nightmares." 
    vivithinking "I can't move, I can't breathe."
    ava neutral "Do you... jest? We see a cold abyss, pulsing with hunger and emptiness."
    stop music fadeout 3.0
    stop cd_ambience fadeout 3.0
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5.0)
    pause 2.0

    play sound teleport_exit
    show urshu happy at left with dissolve:
        xzoom -1.0
    show vivi surprised at left with hpunch:
        linear 0.1 ypos 1000
        linear 0.1 ypos 1080
    $ renpy.pause(0.3)
    urshu happy "You are both correct!"

    vivi surprised "What the? Get out of the way!"

    show vivi surprised:
        linear 1 xpos 700
    $ renpy.pause(1)
    show vivi surprised at center with dissolve:
        xzoom 1
    $ renpy.pause(1)
    vivi surprised "Where the hell did you come from?"
    show urshu neutral blush
    urshu "Apologies Ms. Sanssouci, sometimes the teleportation spell can be a bit... faulty."
    show urshu neutral -blush

    urshu "Those are the spirits of passengers lost to the fabric of space-time. Or perhaps how you see them.. hard to say sometimes."

    vivi sad "Those poor souls... is there no help for them?" 
    ava sad "Is there no help for us?"
    show urshu sad at left
    urshu sad "None for them, I fear."
    play music mysterymusicpiano
    show vivi neutral at center

    # <CHOICE>

    menu:

    #OPTION 1 
        "Nightmarish. That's the only word for it.":

            vivi surprised "Nightmarish. That's the only word for it."
            vivi angry "And I want nothing to do with whatever that is."
            ava surprised "Were you not lamenting those same souls?"
            vivi angry "Since when do you care? There's no point to all of this."
            show urshu happy at left
            urshu happy "Ah, but there is. That could be you one day."
            urshu neutral "So..."
            #JUMP TO: urshu "Do you..have any questions?"


    #OPTION 2 +ATTRACTION
        "Terrifying. I can't imagine how it feels.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi sad "Terrifying. I can't imagine how it feels."
            ava sad "A circular void haunts our every thought. We fear it."
            show urshu happy at left
            urshu happy "Best not to think too hard about it."
            urshu neutral "So instead..."
            # JUMP TO: urshu "Do you... have any questions?"

    urshu neutral "Do you... have any questions?"
    urshu happy " Anything about the Ouroboros Express you want to know..?"
    ava surprised "So are we truly dead? Our service to the Goddess has ended?"
    urshu neutral "All quite true. All of it. I wish I could offer better news, but on the Ouroboros Express your soul is bound for the afterlife."
    ava sad "But..this cannot be!"

    show vivi sad 
    vivi "Oh, Asha! I'm so sorry. I would say I couldn't imagine, but given the circumstances..."
    vivithinking "Oh my God, c'mon, Vivi, shut up, summon your inner reporter, and ask the Conductor something clever!"

    # <CHOICE>
    menu:
        #OPTION 1 +ATTRACTION
        "Can we get out of here?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi surprised "Can we get out of here?"
            show urshu neutral at left
            urshu "No, Miss Sanssouci. Your lives belong to the cosmic fabric now. Tomorrow you will see, should any lingering doubt remain."
            vivi surprised "But how did I...?"
            urshu "Not important. The destination is."
            vivithinking "Maybe it's not important to you, but why can't I remember how I died?"
            vivi angry "Mind divulging our destination then?"
            urshu "The destination? Why, that is up to you, is it not?"
            vivithinking "Like getting blood from a turnip, this guy!"
            urshu neutral "Vivi, Asha, the universe does not decide your fate here; fate has placed the compass in your hands. Here and now."
            # JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"

    #OPTION 2 
        "So am I going to Hell, then?":

            vivi surprised "So am I going to Hell then?"
            show urshu neutral at left
            urshu neutral "Depends. Were you good, deserving of reward, or a villain, destined to rot eternally in Hell? Hell! A silly tale to frighten ill-mannered children, at best."
            vivi surprised "So... Heaven?"
            urshu surprised "Heaven - what a noble concept. The word boring also comes to mind..."
            vivi angry "Fine, it's not either one."
            vivithinking "Just like pulling teeth..."
            #JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"
        
    #OPTION 3
        "Why do you do this job?":

            vivi sad "Why do you do this job?"
            show urshu surprised at left
            show urshu surprised blush
            urshu "That is the first time anybody has asked me that! Well to be honest, the tale is long, so perhaps another time?"
            vivi sad "Oh..."
            show urshu happy -blush
            urshu "In short, my destiny is to be on this train, one way or another."
            #JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"

    vivi sad "We all die, one way or another, so what's the point of all this?"
    show ava happy at right
    ava happy "The answer to that lies within you, Vivi."
    vivi neutral "Well, I cannot thank you both enough for this wonderful chat. Time to head back to my room, now."
    ava happy "See you soon, Vivi. The All is the One."
    ava sad "We have much to ponder. May your dreams be peaceful and warm."
    vivi neutral "Yeah yeah... you too, Asha."
    vivithinking "Ugh, I think I need to go lie down. That was a lot to take in."

    # JUMP TO: Debrief Denial
    jump denial_debrief