label bargaining_asha_urshu :

    #LOCATION: observatory
    # call check_overlay from _call_check_overlay_11
    scene observatory with fade
    play ambience amb_observatory fadein 1.0
    $ ava_fullbody = True
    $ urshu_fullbody = True

    #SOUND: train
    #play sound train

    show vivi angry at left :
        xzoom -1

    vivithinking "Ah, insomnia, my old friend. Let us gaze on the stars again. Better than tossing and turning like a fish flopping around to death."

    show vivi sad at left :
        xzoom -1

    vivithinking "Death. It seems inescapable. I came here to forget for a while. Maybe focus on the literally stellar display in front of you, Vivi, hm?"

    show vivi surprised at left :
        xzoom -1

    vivithinking "Maybe I’m not the only one who can’t sleep. Is that Urshu and the Goddess? Dare I eavesdrop? Not like anyone’s gonna sue."

    show ava angry at center with dissolve :
        xzoom -1
    show urshu neutral at right with dissolve

    vivithinking "Well, hot damn! They look deep in conversation."

    # hide vivi with dissolve

    show ava angry at center with dissolve :
        xzoom -1
    with move

    
    play music spymusic loop
    ava angry "Sleep eludes us, conductor. So many thoughts. So many regrets."

    urshu neutral "Regrets, you say? To live without regret is to believe you have nothing to learn, no amends to make, and no opportunity to be braver with your life."

    ava sad "Braver? How much braver must we be, slippery one?"

    urshu sad "The only thing worse than giving up is wishing that you hadn't."

    ava sad "Give up? We gave everything to our goddess. And now...what was the point of our sacrifices?"

    urshu neutral "What is the point of anything, O Enlightened One?"

    ava angry blush "Do not distract us with juvenile hypotheticals, conductor."

    urshu sad blush "Apologies, O Radiant One. But answer truly: how did you feel about your service to your goddess?"

    ava surprised "Feel? We went where Mother Asha needed us to go. We did so willingly."

    show urshu neutral -blush
    urshu neutral "Curious answer. Tell me this then: How did you feel about your upbringing alongside the decaying royal family?"

    ava angry "Alongside indeed. We dwelt in the same place, yet could not have been more distant."

    urshu sad "Ah, the distance that separated you was a bottomless chasm, to be sure!"

    ava sad "Custom demanded habitation alongside the aristocrats. Distance softened their contempt and disdain."

    ava neutral "And yet, we have seen this bottomless dark void outside through the windows. Is it...?"

    urshu neutral "Mayhaps, O Enlightened One. Mayhaps the emptiness you see is what you fear most."

    ava angry "Mother Asha! Mocking us again, Dark Ferryman?"

    urshu sad blush "Mocking, no; prodding, yes. At what point did your service end and did you begin?"

    ava sad "You speak in circuitous riddles, conductor. We were Mother Asha, born to serve, no more, no less."

    show urshu neutral -blush

    urshu sad "Yes, goddess. But what of the heart that beats in your chest and craves more?"

    ava sad "Buried away long ago, conductor. A silly dream of a naïve child. No more."

    stop music fadeout 10.0
    urshu neutral "Sometimes children have the simple answers that elude us. Ah, speaking of elusive, I see a visitor. I’ll leave you two. Ta ta!"

    hide urshu with dissolve
    hide ava with dissolve

    $ ava_fullbody = False
    $ urshu_fullbody = False

    show ava neutral at right with dissolve

    show vivi neutral at left with dissolve:
        xzoom -1

    show ava neutral at right:
        xzoom 1

    vivi neutral "Glad I found you here, Asha."

    ava happy "As are we, my radiant companion, but we are weary of speech. Would you agree to a quiet moment with us, gazing at the cosmos strewn with stars?"

    vivithinking "Hard to say no to that!"

    vivi happy blush "Yes. Let’s."

    #JUMP TO Depression briefing

    stop music fadeout 1.0

    scene clockdepression with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 5.0

    #play music mainmusic volume 0.5 # start main track

    jump depression_briefing
