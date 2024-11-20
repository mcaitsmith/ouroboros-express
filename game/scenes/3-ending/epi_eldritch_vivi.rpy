# The scene starts here.

label epi_eldritch_vivi:

    #3.2 Epilogue
    #Epilogue/Eldritch/Vivi
    # A snapshot of Vivi as her new form.
    # Vivi monster gets its way back to Earth...for a little revenge. Aahaha. (She's insane)

    #LOCATION: eldritchlandscape
    scene eldritch_vivi with Fade(2,2,2)
    play sound char_terror
    pause 6.0
    play music badendmusic loop
    show urshu sad at left with dissolve:
        xzoom -1.0
    urshu sad "Anyone can change for the better, but they have to want to change."
    urshu "Unfortunately, Miss Sanssouci was stuck in her ways. She was too stubborn and too angry to open up. Her repressed self gave birth to emptiness. From the emptiness came the hunger, too strong for her decaying body."
    urshu sad "I should have realized sooner that she was meant for a different purpose." 
    urshu neutral "You can't have light without dark and you can't have absolution without punishment. Vivienne Sanssouci's body was altered to match her mind."
    urshu neutral "A flowing dress and shards of a broken mirror flowing through eternity—an attractive facade concealing a devouring maw." 
    urshu "She finally got the life she pursued. She would no longer be censored and repressed by others."
    stop music fadeout 5.0
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    urshu happy "The new Vivi managed to make her way back to Earth...for a little revenge."
    window hide fade
    hide urshu with dissolve
    $ quick_menu = False # hide quick menu
    $ _game_menu_screen = None # disable menu
    scene black with Dissolve(3.0)
    pause 1.0
    play music creditsmusicbad loop
    call screen credits
    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 3.0
    #SOUND: Vivi's evil laughter
    # skipping
    
    # end game
    return