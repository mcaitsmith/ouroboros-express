# The scene starts here.

label denial_debrief:

    #Debrief Denial

    #LOCATION: cabin
    scene cabin with fade

    show vivi angry at left with dissolve

    show urshu neutral at right with dissolve

    vivi neutral "Outside this train... the void... it's too much. I thought I was living a nightmare before, but that outside...  That was chilling to my core."

    vivi angry "Do you get off in seeing all of us in pain? Giving us all an existential dread that we can't fix?"

    urshu neutral "Seeing the outside is sobering for many. I'm glad you're no longer denying the gravity of the situation. I understand that this is a lot to process." 

    urshu happy "We've left a journal for you. I thought a reporter such as yourself would like the ability to write down her thoughts."

    urshu neutral "I hope you utilize it. Please know that nobody else, including myself, can ever read what's inside. Everyone deserves a private place to think."

    hide urshu with dissolve

    vivi angry "He's so infuriating! I don't know why I even bother asking him anything."

    vivi neutral "But, he might be right. Might as well use the journal."

    #Journal entry
    call display_journal
    $ cycle = 1

    "This is real. It doesn't make sense but it's all really happening. There was no way off the train. How the hell did I die? I thought I'd leave a mark on the world before I left. Or at least someone special. It's all so frustrating. The conductor is the worst, acting like this is a game. THIS IS OUR LIVES! At least I'm not the only one going through this."

    stop music fadeout 1.0

    scene clockanger with fade
    play sound clock loop

    pause 5.0
    stop sound fadeout 2.0

    play music mainmusic volume 0.5 # start main track

    # JUMP TO: Briefing Anger
    jump anger_briefing