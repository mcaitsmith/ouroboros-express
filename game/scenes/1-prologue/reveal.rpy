# The scene starts here.

label reveal:

    # Reveal
    # LOCATION: diningcar
    # pixellate transition since teleport!
    scene diningcar with pixellate

    show vivi surprised at center_left:
        xzoom -1
    with dissolve
    vivi "{i}*cough* *cough*{/i}"

    show darius surprised at right with dissolve
    darius surprised "Huh."

    show ava neutral at center with dissolve
    ava neutral "Another trick?"

    show susurha angry at left behind vivi with dissolve:
        xzoom -1.0
    susurha angry "Teleportation? That's rude."

    vivithinking surprised "We're in the dining car? How?"

    # SOUND: heartbeat
    play sound heartbeat

    vivithinking surprised "I can't focus."
    vivithinking surprised "There's stuff at the edges of my view. Like, shards?"
    vivithinking sad "Can't think straight..."

    stop sound fadeout 1.0

    show urshu happy at center_right with dissolve
    urshu happy "How delightful. Attention over here, please! Lovely! Now, it's finally time—for the welcoming party!"
    urshu happy "I know, I know. Apologies for the ruse, my dear passengers."
    vivi sad "What ruse?"
    urshu neutral "Perhaps the swiftest explanation is a reintroduction. My good people, I am known by many names, but you may call me Urshunabi, ferryman of the dead."
    urshu happy "Or conductor of the dead, I should say."

    show susurha happy
    susurha happy "Ha! A joke! How droll!"

    show darius neutral
    darius neutral "Hmph."

    show ava angry
    ava angry "What trickery is this? We've had enough of this game. Release us this instant."
    urshu neutral "This is neither game nor jest, Illuminated One. Your flicker is extinguished—what a shame—and now you spiral into the elder dark." 
    urshu happy "For you are all dead! Haha!"

    # SOUND: heartbeat
    play sound heartbeat

    show vivi surprised
    vivithinking surprised "No, no, no... This isn't real."

    stop sound fadeout 1.0

    show susurha happy
    susurha "Haha! A funny conductor! Say it again!"

    show ava angry
    ava angry "Retract. Mocking death is a grave sin and a banner of poor judgment."

    urshu happy "Do not be afeared, dear ones, for you have some time yet. I have made every care to ensure this final journey is a productive one."
        
    show susurha neutral
    susurha "Oh, come on, Lady Bright. Don't tell me you believe him."

    show ava angry
    ava angry "We, in fact, believe we have been captured."
    susurha surprised "Oh, well, then that's funny, see? It'll take more than a fool in uniform to keep me captive."

    show darius neutral
    darius "Hmph."
    ava "What is the matter, master of thralls? Care to elaborate?"
    darius "I-I'm a mere observer."

    show urshu happy
    urshu happy "And observe, you shall—the greatest theater of all, after curtain call, in the liminal wings on your way to center stage to take your final bow."
    urshu neutral "But even in this cosmic plane, the light wanes and there is time but for one encore. Will you play as you were, broken characters of your respective tragedies? Or flip the script?"

    show ava angry
    ava angry "Tragedies. You dare?"

    urshu happy "Well, the reviews don't write themselves. A reporter would surely have sat to the end of a play or two. Well, dear Miss Sanssouci, have you any thoughts?"

    show vivi sad
        
    # SOUND: heartbeat
    play sound heartbeat

    vivithinking sad "This is too much. Everyone's looking at me."
    vivithinking sad "What am I supposed to do? I can't help them. I can't even stand straight."

    stop sound fadeout 1.0

    show ava angry
    ava "Ignore the pawn. {i}We{/i} will ask the ques--"

    # EFFECT: Brighten or distort the display
    show diningcar at bright with dissolve
    # SOUND: heartbeat
    play sound heartbeat

    show vivi sad
    vivithinking sad "I see them shouting, but... I can't hear them."
    vivithinking sad "Why's everything...so bright?"

    show urshu surprised
    urshu surprised "Miss Sanssouci?"


    # EFFECT: Fade out
    scene black with fade

    stop sound fadeout 1.0

    vivithinking sad "Bright...like a mirror..."

    # SOUND: crash
    play sound crash
    pause 6.0

    stop music fadeout 1.0

    scene clockdenial with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    play music mainmusic volume 0.5 # start main track

    # JUMP TO: Briefing Denial
    jump denial_briefing
