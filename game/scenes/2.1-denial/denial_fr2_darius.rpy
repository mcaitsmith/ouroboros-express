# The scene starts here.

label denial_fr2_darius:

    #FREE ROAM 2 - Inquisitor Darius

    #LOCATION: dining car
    scene diningcar with fade
    play ambience amb_bar fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    show darius neutral at right with dissolve

    vivithinking "Darius is... drinking? Guess impeccably-dressed cephalopods need a break every now and then."

    vivi "Enjoying a drink?"
    play music dariusmusic

    # <CHOICE>

    darius surprised "Hmm? Oh, yes. Would you like one? I'm a bit of a lightweight."

    menu:
        
    #OPTION 1 
        "Sure.":

            vivi "Sure."
            # SOUND: glassclink
            play sound glassclink01
            darius neutral "There you are."

            vivi "Thank you."

            vivithinking "Is this... piña colada?"

            vivi happy "Didn't think you had a sweet tooth."

            darius happy "It's actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."

            darius sad "Mindflayers and hard alcohol... don't mix."

            vivithinking "They shuddered at those last words. It still ripples through their sleek frame like a gentle breeze. Gotta be a story there."

            vivi neutral "Mindflayer? Is that what you are?"

            darius neutral "I suppose there's no point in hiding it anymore, but yes. Are you familiar with them?"

            vivi neutral "I've heard some things. Mainly that your people eat brains."

            show darius neutral blush

            darius "We don't {i}only{/i} eat brains. I've been known to enjoy a treat now and again."

            vivi happy "Right. Hence the drink."

            show darius happy -blush

            darius happy "Exactly."

            # JUMP TO: vivithinking "Why is the air here so... heavy?"


    #OPTION 2
        "I'm okay, thank you.":

            vivi "I'm okay, thank you."
            darius neutral "Not a fan? That's fine. I can make you a non-alcoholic version."

            # SOUND: glassclink
            play sound glassclink02

            vivi surprised "Fruits? I didn't think you had a sweet tooth."

            darius happy "It's actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."

            darius sad "Mindflayers and hard alcohol... don't mix."

            vivithinking "They shudder at those last words. It still ripples through their sleek frame like a gentle breeze. Gotta be a story there."

            vivi neutral "Mindflayer? Is that what you are?"

            darius neutral "I suppose there's no point in hiding it anymore, but yes. Are you familiar with them?"

            vivi neutral "I've heard some things. Mainly that your people eat brains."

            show darius neutral blush

            darius "We don't {i}only{/i} eat brains. I've been known to enjoy a treat now and again."

            vivi happy "Right. Hence the drink."

            show darius happy -blush

            darius happy "Exactly."

            #JUMP TO: vivithinking "Why is the air here so... heavy?"


    vivithinking "Why is the air here so... heavy?"

    darius neutral "Are you ok, Ms. Sanssouci? You look a little... sickly."

    darius surprised "Ah! My apologies. Give me a moment."

    #SOUND (if possible): Darius sighs/tries to calm themself
    $ renpy.music.set_volume(0.00, delay=2.60, channel='music')
    play sound orex_char_telepathy volume 1.0
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=2.6)
    pause 2.0
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5)
    $ renpy.music.set_volume(1.00, delay=5.00, channel='music')

    darius neutral "There. Feeling better?"

    vivithinking  "A quick flick of the wrist... wish {i}I{/i} could be so graceful. Did they do something..? Things feel a lot lighter."

    darius neutral "A mindflayer's brain is a powerful thing. Sometimes our emotions and thoughts can leak out. I believe you may have been feeling my... malaise, so to speak."

    darius neutral "I don't speak with humans often, so I've developed a bit of a bad habit of letting my emotions wander."

    vivi neutral "It's alright, I figured you didn't get to speak with humans much. You can just call me Vivi by the way, no need for formalities."

    darius neutral "Very well."

    vivi neutral "What had you so bothered?"

    darius sad "Aside from some unpleasant memories... I've been thinking."

    darius sad "I have many questions about this place that need answers. But I don't believe asking will get me any of them..."

    darius neutral "I've let myself fall into passivity too often, simply allowing the current to wash over me. This time, I'll act."

    vivithinking "They want to act, huh? Looks like we're on the same page."

    vivi neutral  "Listen, I was thinking about looking for a way off of this damnable train. What do you think?"

    darius neutral "Hmm. I'm not interested in leaving just yet, but I think there is a way our needs could both be met."

    darius neutral "I am going to trail the conductor. Should you wish to join me, you may search for an exit."

    vivi surprised "Trail? Are you some sort of detective?"

    darius surprised "What? Ahem, I'm— something like that, yes. I have the skills needed for the job, don't you worry."

    vivithinking "What a weirdo. They seem pretty confident though, so I'll take their lead on this. Nice to be able to rely on someone for once."

    vivi happy "Sounds good to me. When did you want to start?"

    darius neutral "Well... now is as good a time as any, don't you think?"

    vivi surprised "Straight to business then? Lead on."

    stop ambience fadeout 1.0
    stop music fadeout 1.0

    #LOCATION: lounge
    scene lounge with fade
    play ambience amb_lounge fadein 1.0
    play music spymusic fadein 1.0 loop

    show darius neutral at right with dissolve

    show vivi neutral at left with dissolve:
        xzoom -1

    darius neutral "Stay behind me and follow my motions."

    vivithinking "Where is he?"

    hide darius with dissolve

    hide vivi with dissolve

    show urshu happy at left with dissolve

    show vivi angry at right with dissolve:
        xzoom 1

    # SOUND: whistling
    play sound char_whistle loop
    $ renpy.music.set_volume(0.20, delay=5.0, channel='sound')

    vivithinking "Is he... whistling? This asshole has us captive here and he's whistling?"

    hide urshu with dissolve

    hide vivi with dissolve

    show darius neutral at right with dissolve

    show vivi angry at left with dissolve :
        xzoom -1

    stop sound fadeout 10

    darius neutral "Calm yourself."

    vivi angry "Can't you just ask your questions now and I'll go off to look for an exit while he's distracted?"

    darius angry "That isn't what we agreed on. Besides, you've spoken to him. Do you really think he'd just give up his secrets so easily?"
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=5)
    play sound [ "<silence 3.0>", "audio/sfx/orex_char_telepathy.ogg" ]
    darius neutral "This is the best way to find out more. So please: it may be human nature to be quick to anger, but {i}calm yourself{/i}."
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5)

    vivithinking "Those last words held an undercurrent to them. Like the rumble of an oncoming storm."

    vivithinking "Where the hell did that come from? Darius was pretty agreeable up until now."

    darius neutral "Vivi, look."

    hide darius with dissolve

    hide vivi with dissolve
    show urshu happy at left with dissolve

    urshu happy "Suppose it's time to retire for the evening. Should do the rounds, ensure nothing is out of order."

    # SOUND: teleport
    $ renpy.music.set_audio_filter("music", audio_filter.Lowpass(500), replace=True, duration=0.5)
    $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
    play sound teleport_enter volume 1.0
    $ renpy.music.set_audio_filter("music", None, replace=True, duration=1.5)
    $ renpy.music.set_volume(1.0, delay=1.5, channel='music')
    hide urshu with pixellate

    show darius surprised at right with dissolve

    show vivi surprised at left with dissolve:
        xzoom -1

    darius surprised "Is that..."

    vivi surprised "Magic. Yeah I think so."

    # <CHOICE>
    darius happy "This is exactly what I wanted to see. Come, let's pursue him."
    stop music fadeout 15

    menu: 

    # OPTION 1
        "(Aww, their little mouth tentacles curl up when they're happy.)":

            show vivi happy blush 
            vivithinking "Aww, their little mouth tentacles curl up when they're happy."
            show vivi angry blush 
            vivithinking "What am I thinking? This isn't the time Vivi!"
            stop ambience fadeout 1.0

            # JUMP TO scene observatory with fade

    # OPTION 2
        "(Wow, they're really on this. Good call teaming up with them, Vivi.)":

            vivithinking neutral "Wow, they're really on this. Good call teaming up with them, Vivi."
            stop ambience fadeout 1.0

            # JUMP TO scene observatory with fade

    #LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0

    show darius surprised at right with dissolve

    show vivi surprised at left with dissolve:
        xzoom -1 

    darius surprised "Been a while since I had to track a mage. Hopefully my senses are somewhat intact here."

    # <CHOICE>

    vivithinking "They're a natural at this. I'm kinda curious to know more. Should I ask them?"

    menu:

    # OPTION 1 
        "Hey, how did you develop these skills anyways?":

            vivi neutral "Hey, how did you develop these skills anyways?"

            darius neutral "Oh, I was trained in observation since I was young. Making myself scarce, learning my target's habits and routines. As for reading people, that comes rather naturally to mindflayers."

            vivi neutral "Cause of the whole mind reading thing?"

            darius neutral "Yes, there's always that to fall back on. But we're also very good at sensing emotional shifts, lapses in thought... lies."

            vivithinking "!"

            vivi neutral "Must come in handy as a detective."

            show darius surprised blush

            darius "Yes, it's uhh...very useful."

            show darius neutral -blush

    # OPTION 2
        "Never mind.":

            vivithinking "Never mind."
            darius neutral "You seem rather quiet back there."

            vivi neutral "Just looking out for any sign of an escape route."

            #JUMP TO: darius neutral "Found anything yet?"


    darius neutral "Found any sign of an escape yet?"

    vivi angry "No. It's like nothing makes sense on this train, the doors just lead to more doors. There's no final car either. It's almost like it just... keeps going."

    darius neutral "Hmm. If my hunch is correct, then there's a good chance there is no escape from this train."

    vivi angry "What? So you think that Urshu is telling the truth?"

    darius neutral "Maybe part of it. There are things he's keeping from us, of that I'm sure."

    vivi neutral "Hold on."

    vivithinking "Speaking of hunches, I've got one of my own."
    play sound twinkle volume 0.1

    #I'd like Vivi to move to the right here and Darius to move to the left. Is that possible without making them disappear and reappear?
    # PROGRAMMING NOTE: not gonna implement this for now since we don't have a Vivi sprite


    show vivi at right with move
    show darius at center with move
    show darius at center:
        xzoom -1

    darius surprised "Ms. Sanssouci, I didn't take you to be one for stargazing, but this hardly seems the time for it."
    stop sound fadeout 3.0
    vivi neutral "Shut up."

    # SOUND: crash
    play sound crash #are we sure here?
    pause 5.0
    play music mysterymusic

    vivithinking "What... what the fuck is that through the window?"

    darius surprised "Vivi? You look like you've seen a ghost."

    vivi surprised "Just... just take a look for me will you? Do you see it? The weird... figure out there?"

    darius neutral "Very well. What kind of figure?"
    $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=2), audio_filter.Lowpass(500)], replace=True, duration=2.0)
    $ renpy.music.set_volume(0.50, delay=1.00, channel='ambience')

    vivi angry "Just look! It's in a dress but it's like it has no torso or anything! It has some sort of mirror thing for a head!"
    play sound char_mirror
    pause 8.0

    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=10.0)
    show darius at right with move
    show vivi at left with move

    darius surprised "I don't see this figure you're speaking of, but... oh my."

    vivi surprised "What? What do you see?"

    darius surprised "I... I knew it. This place... it is his."

    vivithinking "There's awe in those words but also something else. Fear?"

    show urshu neutral at left with dissolve:
        xzoom -1.0
    show vivi surprised at left:
        xzoom 1
        linear 0.1 ypos 1000
        linear 0.1 ypos 1080
    play sound teleport_exit
    stop music fadeout 3.0
    urshu neutral "Interesting! What do you see out there?"

    vivi surprised "What the? Get out of the way!"
    
    show darius at right:
        xzoom 1
    show vivi surprised:
        linear 0.5 xpos 700
    $ renpy.pause(0.7)
    show vivi surprised at center with dissolve:
        xzoom 1
    vivi surprised "Where the hell did you come from?"

    show urshu neutral blush

    urshu "Apologies, Ms. Sanssouci. Sometimes the teleportation spell can be a bit... wonky."

    show urshu neutral -blush

    urshu neutral "However, I appear when I am needed, my dear! Now, Mr. Wrecker, I believe from your tailing of me tonight that you have something you desire. May it be related to what you see out there, I wonder?"
    play music dariusmusic loop

    show darius surprised at right
    darius surprised "You... Are you not an ambassador of the Eternal Rest?"

    urshu surprised "Oh? And what would make you think that?"

    darius surprised "Out there... I could've sworn I saw its tendrils grasping out for me."

    urshu neutral "Ahh, now I see. I'm afraid to disappoint you, Mr. Wrecker, but unfortunately that is not the case."

    urshu neutral "The cosmos holds many things, not all of them friendly. Some may draw themselves to you, while others may find another passenger more appealing. What you saw is simply one of those entities."

    show vivi angry at center :
        xzoom 1

    # <CHOICE>

    vivithinking "Are they really gonna act like I'm not here? I have questions too, you know!"

    menu:

    # OPTION 1 
        "Excuse me? You're going to answer my questions now.":

            vivi angry "Excuse me? You're going to answer my questions now."

            urshu neutral "I know asking questions is in a reporter's nature, but is decorum not? Mr. Wrecker is clearly \"going through something\" as it were, so I'd appreciate your silence."

            vivi angry blush "I—"

            vivithinking "Scolded like a schoolgirl. I hate that he's right."

            #JUMP TO: darius neutral "I've been having... visions."

    # OPTION 2
        "Darius, compose yourself. Didn't you have questions for him?":
        
            vivi neutral "Darius, compose yourself. Didn't you have questions for him?"

            darius surprised "You're right, Vivi. Thank you."

            #JUMP TO: darius neutral "I've been having... visions."

    darius neutral "I've been having... visions."

    darius sad "A loving couple, screams, confusion... I can't make sense of it all."

    show urshu neutral at left:
        xzoom -1
    urshu neutral "I see. Tell me, how much of your... end, do you remember?"

    darius sad "My end?"

    urshu sad "I wasn't lying to you. Any of you. All of you here have well and truly passed on from the world of the living."

    vivithinking "That sounded... honest. He can't be serious, right? He can't be..."

    urshu sad "As for you, Mr. Wrecker, hmm. I promised I wouldn't get involved in any of your journeys, but I believe showing you this will help."
    play sound twinkle volume 0.5

    vivithinking "He stretches out his hand. Darius takes it."
    stop music fadeout 3.0

    #SOUND: twinkle
    pause 2.0
    stop sound fadeout 10

    #SOUND: horror
    play music horrormusic

    darius surprised "What... what is {i}this{/i}?"

    urshu sad "I understand this must be hard. But nothing I've shown you is an illusion. These were your choices, your actions."

    stop sound fadeout 1.0

    show vivi sad at center

    vivithinking "I've never seen Darius like this before."

    urshu sad "And as for you, Ms. Sanssouci, I know this must've been hard for you as well. You may not believe it, but I am here to help you, you know."

    vivi sad "So it's true then? We're really gone?"

    vivithinking "He simply nods."

    vivithinking "... I don't know what to say."

    show darius angry at right
    darius angry "Urshu. What was it all for them? Who am I anymore?"

    urshu sad "Unfortunately, I can't answer that for you, my friend. I'm sure you'll learn the answer yourself, in time."

    urshu neutral "Ms. Sanssouci, if you don't mind, could you meet me at your cabin shortly? We have some matters to discuss."

    show vivi neutral at  center
    vivithinking "We have things to discuss?"

    vivithinking "The tension hangs in the air. It's like a miasma, cutting the oxygen and making my heart race."

    urshu happy "...On a lighter note, we will be serving brunch tomorrow! Do come... well I'd say \"early\" but time has no meaning here anyways. Ta-ta!" 

    hide urshu with dissolve
    show vivi at left with move

    show darius surprised at right
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=2.6)
    play sound char_telepathy 
    stop music fadeout 2.6
    pause 2.6
    darius surprised "What?"
    play music confrontationmusic
    show vivi sad blush at left with dissolve:
        xzoom -1

    vivithinking sad "The air is getting thin, heated even. It's just like before in the dining car. Darius is..."

    darius angry "Don't toy with me! COME BACK!"

    #VISUAL: screen shake
    show observatory with hpunch
    play sound cineboom

    darius angry "I AM AN INQUISITOR OF THE LORD—"

    vivi sad "Darius... your emotions are—"

    #VISUAL: screen shake
    show observatory with hpunch
    play sound cineboom

    # pause
    pause 1.0

    vivithinking "They stopped."

    show darius sad blush

    darius "I... I suppose I'm not anymore."

    darius "I'm sorry, Vivi; I lost my temper. Thank you for joining me, and I hope you can forgive that little outburst."

    vivithinking "Are they muttering to themselves?"

    show darius sad -blush:
        xzoom -1

    darius "It was all pointless..."

    hide darius with dissolve

    vivi sad "This is all too much... I need to sleep."

    # JUMP TO: Debrief Denial.
    jump denial_debrief