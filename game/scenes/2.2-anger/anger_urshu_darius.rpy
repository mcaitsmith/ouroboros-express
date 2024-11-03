# i’m not sure of where this should take place so i’m putting it as the observatory

label anger_urshu_darius:

    # call check_overlay from _call_check_overlay_10
    scene observatory with fade
    stop music fadeout 2.0
    play ambience amb_observatory fadein 1.0
    

    show vivi neutral at left with dissolve :
        xzoom -1
        

    vivithinking neutral "Something drew me here. It’s late, but I couldn’t resist the pull."

    # can we fade in on a character portrait? might be a good place to do that here with urshu

    show urshu neutral at right with dissolve

    vivithinking surprised "Is that– the conductor? I thought he was in the lounge."

    # another character portrait fade-in, of darius

    show darius neutral at center with dissolve

    vivithinking surprised "Looks like that cosmic detective guy is here too. He seems pissed. I shouldn’t interrupt them."

    vivithinking neutral "But I’ll still listen in."
    play music spymusic loop

    hide vivi

    show darius angry at left :
        xzoom -1
    show urshu neutral at right

    darius angry "I know what it is like to toy with your prey. I don’t appreciate it."

    urshu happy "My sincerest apologies. We want everyone’s experience aboard the Ouroboros Express to be as pleasant as possible."

    darius angry "Pleasant? Really? You call {i}this{/i} pleasant?"

    urshu happy "Pardon?"

    darius neutral "All this. It’s a facade. And you’re acting like a damn clown. There is a gravity to all this."

    darius angry "One that you are either entirely unaware of or cannot begin to understand."

    urshu surprised "Explain it to me."

    darius neutral "This train. These people. It’s all some game to you. I was responsible for the fates of thousands. Maybe millions."

    darius angry "This is not what was meant for me. Maybe the others. Not me."

    urshu neutral "Go on."

    darius neutral "I wanted... more. There must be more. Something to give some kind of context."

    darius surprised "This can’t be all there is. What about my service? All I’ve done? Does that not count for anything here?"

    darius angry "I need it to mean something."

    urshu neutral "It does. In fact, I’d say everything is coming together better than I’d hoped."

    urshu happy "Wouldn’t you agree, Miss Sanssouci?"

    stop music fadeout 1.0
    show vivi surprised at center with dissolve

    vivithinking surprised "Crap on a cracker, they must have heard me. Sensed me? Who can say."

    vivithinking sad "Ugh– my tummy just flipped. Like when I walked in on my editor and her secretary kissing."

    vivithinking neutral "Only this time the embarrassment is from being caught by a walking squid and a little shit."

    vivi surprised "Um...hello. I didn’t hear anything."

    darius neutral "I'm sure. Well. Goodnight, Vivi." 

    darius angry "Urshu, don't think I'm finished with you."
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=2.6)
    play sound char_telepathy
    pause 1.0
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5)
    

    hide darius

    # sound of darius leaving/ steps/ door closing
    #play sound footsteps
    #pause 2.0
    play sound doorslam
    pause 1.0

    vivithinking sad "A wave of something like sadness just crashed over me."
    vivi surprised "What was that about?"

    urshu neutral "Dear Darius is simply adjusting. They will be fine. Do excuse me."

    jump anger_debrief