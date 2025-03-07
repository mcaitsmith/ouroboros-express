﻿# The scene starts here.

label denial_fr1_susurha:

    #FREE ROAM 1 - Susu'Rha

    #LOCATION: Dining Car
    scene diningcar with fade
    play ambience amb_bar fadein 1.0

    # SOUND: Footsteps storm into the room.
    #play sound footsteps
    #pause 2.0

    show susurha happy at right with dissolve
    #stop sound fadeout 1.0

    vivithinking "Wait. Susu'Rha just stormed into the room."
    vivithinking "What are they doing?"
    #stop sound fadeout 1.0
    vivithinking "Are they literally feasting on a slice of cake?"
    play sound dinnerware
    vivithinking "Okay, that's cute."

    # SOUND: The train car door slams shut.
    play sound doorslam
    # VISUAL: The screen shakes.
    show diningcar with hpunch

    show susurha surprised at right

    # SOUND: Susu'Rha drops their fork against the table.
    # skipping this one

    susurha neutral "Oh my... are you as hungry as I? I too get flustered when I haven't eaten all day."

    show vivi neutral at left :
        xzoom -1

    # SOUND: Vivi sighs.
    # skipping this one

    # <CHOICE> 
    vivi neutral "I'm not hungry. I'm..."

    menu:

    # OPTION 1 
        "I'm fine.":
        
            vivi "I'm fine."
            susurha "Are you positive?"
            vivi "Yes, I'm positive. There is just a lot on my mind at the moment."
            susurha "Mmmhmm... That much I can glean."
            # JUMP TO: susurha "Here. Join me and enjoy a slice."

    # OPTION 2 +ATTRACTION
        "Honestly, I don't know.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi "Honestly, I don't know."
            show susurha sad
            susurha sad "Yeah, I get that too. I'm..."
            show susurha happy
            susurha happy "Well, I'm here doing what I know can lift the spirits."
            # JUMP TO: susurha "Here. Join me and enjoy a slice."

    #OPTION 3 
        "Are you eating cake right now?":
            vivi "Are you eating cake right now?"
            susurha "Ah yes. This angel food cake is quite delectable. I wonder if that angel beauty had anything to do with this being here."
            susurha "..."
            susurha "I do hope that you aren't judging me."
            vivi "I'm not."
            susurha "Good."
            #JUMP to susurha "Here. Join me and enjoy a slice." 

    susurha happy "Here. Join me and enjoy a slice."

    vivithinking "Deep breaths."

    # SOUND: Vivi inhales and exhales.
    # skipping this one

    vivithinking "Alright, let's just sit down and chill."

    vivithinking "What's the worst that can happen?"

    # SOUND: Vivi takes a seat at the table.
    play sound swoosh
    # skipping this one

    vivithinking "They carve a slice of cake and nudge it my way."
    play sound dinnerware
    vivithinking "Fine. I take the fork and take a bite."

    vivi happy "Oh my goodness, this is amazing."

    susurha happy "I told you. The Archdruids back in the living forest can't even dream of conjuring such savory delights. This angel food cake is to die for."
    play sound sparkle

    show susurha neutral
    show vivi neutral

    susurha "..."

    vivi "..."

    vivithinking "Oh no..."
    vivithinking "Awkward silence alert..."

    # <CHOICE> 
    susurha "Alas... Please tell me you weren't paying attention to that Urshu fellow the other day when he was spouting off about..."

    menu:

    # OPTION 1 
        "Urshu has no idea what he was rambling about.":

            vivi "Urshu has no idea what he was rambling about."
            susurha happy "Ah... music to my ears. So clearly I haven't found myself entirely surrounded by those more insane than I."
            vivi "No, I am very much sane, but this place is testing that."
            susurha happy "I couldn't agree any more."
            susurha happy "Hehe."
            susurha happy "Dead..."
            susurha happy "My father could have told better crafted jokes than that back home."
            susurha sad "Hmm."
            show vivi sad
            #JUMP TO: susurha saying "I'm sorry..."
        
    # OPTION 2 +ATTRACTION
        "How could I not? I can't stop thinking about it.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')
            

            vivi "How could I not? I can't stop thinking about it."
            susurha angry "Uh.... Wrong answer. Not quite what I was looking to hear. Thank you very much. Now please tell me that the next thing that you utter isn't just echoing..."
            vivi "I don't know. What if we are truly dead?"
            susurha neutral "That."
            susurha "Great, everyone has gone mad and I'm soon to join them."
            vivi "Are you telling me that you haven't thought about the possibility?"
            susurha "No ma'am, I haven't. I would very much be aware if I was dead. I'd either be roasting in an abyss of flames with like-minded individuals or be experiencing the sweet void of nothingness."
            susurha "NOT some poorly designed metallic tube flying to who knows where."
            susurha sad "I... I don't know."
            vivithinking "Oh wow. They're breaking."
            show susurha neutral
            # JUMP TO: susurha saying "I'm sorry..."

    susurha sad "I'm sorry..."

    susurha sad "I really know how to go and spoil a mood, don't I?"
    play sound dinnerware
    vivithinking "Whoa! They just slid the entire cake dish to my side."

    susurha sad "I've lost my appetite."

    susurha neutral "Please do enjoy what you can of it. I'd hate to see it waste away."

    # <CHOICE>
    susurha "...I think I'm going to go lay my head down and not think."

    menu:

    # OPTION 1 +ATTRACTION
        "Are you okay?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi "Are you okay?"
            show susurha happy
            #JUMP TO: hide susurha.

    # OPTION 2 
        "Alright.":
        
            vivi "Alright."
            show susurha sad
            #JUMP TO: hide susurha.
        
    pause 1.0
    hide susurha with dissolve

    vivithinking "Hey! Oh no, they're leaving!"
    vivithinking "Well..."

    # SOUND: Door closes.
    play sound doorslam
    pause 3.0
    stop sound

    # SOUND: A headache inducing ringing echoes.
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(400), replace=True, duration=1.0)
    vivithinking "Ugh... my head feels like something is crawling at the walls of my skull."

    

    vivithinking "I think that was enough for me too."
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.0)

    vivithinking "I better head back to my cabin and collect myself."

    # JUMP TO: Character Selector 2
    jump denial_fr1_ava_darius