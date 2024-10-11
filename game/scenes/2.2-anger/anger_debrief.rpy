# The scene starts here.

label anger_debrief:

    #Debrief Anger

    # LOCATION: cabin
    # call check_overlay from _call_check_overlay_2
    scene cabin with fade
    
    # ??DECAY
    if dec_meter >= 10:

        show vivi angry at left with dissolve:
            xzoom -1

        vivithinking angry "I feel like the only one trying to get off this train. How are people content with playing silly card games when their lives are at stake? And the conductor! He knows he's messing with me and gets off on it."

        vivithinking surprised "What? Did my face just..."
        
        vivithinking neutral "...no, it couldn't have. That's impossible. Take a deep breath, V. This isn't getting me anywhere."

        vivithinking neutral "Fighting with everybody is obviously not gonna work. Maybe I can get what I want another way. Urshu is the key. He must want something."

        vivithinking neutral "I should write."

        play sound writing

        $ message = "This whole thing is pointless!\nThat conductor... URG!\nI wanna strangle him and wipe that\nstupid smirk off his face.\nTalking to him is like solving a riddle.\nIt's infuriating!\nGotta find something on him.\nMaybe the others know a thing or two.\n\nThere's gotta be some way to make\nUrshu help me.\nHe seems like one who'd appreciate an\nexchange for his aid."

        call display_journal from _call_display_journal_1
        $ cycle = 3

        stop sound

        # Journal entry with degradation meter high

    # ELSE
    else:

        show vivi neutral at left with dissolve:
            xzoom -1

        vivithinking neutral "Well, that was...interesting. Didn't expect to get that deep with anyone on this train. I can't remember the last time I've been that open with anyone before."

        vivithinking happy "It was kinda refreshing! I'm glad I'm not alone here. It's nice to be seen. Nobody wanting or expecting anything from me. Just two beings trying to understand each other."

        vivithinking neutral "I should journal my thoughts."

        play sound writing

        $ message = "Talking to the other passengers has helped\nput things into perspective.\nThey're not so bad after all.\nI won't get off this train by fighting.\n\nI still need more info on the conductor.\nHe's my ticket off this ride.\nHe seems like one who'd appreciate\nan exchange for his aid.\nMaybe some of the other passengers\ncan help me?\nWe can maybe figure out together\nwhat Urshu would want from us..."

        call display_journal from _call_display_journal_2
        $ cycle = 3

        stop sound

        # Journal entry

    # END

    stop music fadeout 1.0

    scene clockbargaining with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    play music mainmusic volume 0.5 # start main track

    # JUMP to Briefing Bargaining
    jump bargaining_briefing