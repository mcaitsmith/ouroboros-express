# The scene starts here.

label anger_debrief:

    #Debrief Anger

    # LOCATION: cabin
    scene cabin with fade

    # ??DECAY
    if dec_meter >= 10:

        show vivi angry at left with dissolve

        vivithinking angry "I feel like the only one trying to get off this train. How are people content with playing silly card games when their lives are at stake? And the conductor! He knows he's messing with me and gets off on it."

        vivithinking neutral "Take a deep breath, V. This isn't getting me anywhere."

        vivithinking neutral "Fighting with everybody is obviously not gonna work. Maybe I can get what I want another way. Urshu is the key. He must want something."

        vivithinking neutral "I should write."

        call display_journal
        $ cycle += 1

        # Journal entry with degradation meter high

        "This whole thing is pointless! That conductor... URG! I wanna strangle him and wipe that stupid smirk off his face. Talking to him is like solving a riddle. It's infuriating! Gotta find something on him. Maybe the others know a thing or two. There's gotta be some way to make Urshu help me. He seems like one who'd appreciate an exchange for his aid."

    # ELSE
    else:

        show vivi neutral at left with dissolve

        vivithinking neutral "Well, that was...interesting. Didn't expect to get that deep with anyone on this train. I can't remember the last time I've been that open with anyone before."

        vivithinking happy "It was kinda refreshing! I'm glad I'm not alone here. It's nice to be seen. Nobody wanting or expecting anything from me. Just two beings trying to understand each other."

        vivithinking neutral "I should journal my thoughts."

        call display_journal
        $ cycle += 1

        # Journal entry

        "Talking to the other passengers has helped put things into perspective. They're not so bad after all. I won't get off this train by fighting. I still need more info on the conductor. He's my ticket off this ride. He seems like one who'd appreciate an exchange for his aid. Maybe some of the other passengers can help me? We can maybe figure out together what Urshu would want from us..."

    # END

    stop music fadeout 1.0

    scene clockbargaining with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    play music mainmusic volume 0.5 # start main track

    # JUMP to Briefing Bargaining
    jump bargaining_briefing