# The scene starts here.

label epi_friend_susurha:

    #Epilogue/Friendship/Susu'Rha Balrinn
    #Naj's note: this should just be a brief description - about 100 words, if that. Kind of like the slides at the end of Fallout, but it'll be from Urshu's perspective  and they'll be against a plain, bright background.

    # LOCATION: terminalofdreams

    pause 2.0
    scene white with fade
    play music finalemusic if_changed loop

    scene terminalofdreams with Dissolve(3.0)
    pause 1.0
    show susurha happy at center with dissolve
    pause 2.0

    urshu happy "Susu'Rha, desirous of a life of their own design, broke the chains of expectation and eschewed their royal title, opting instead for a life of anarchic expression in the Viridian Wood."
    urshu happy "When the generational curse of war pulled them back, they found themself aboard the Ouroboros Express—and with you, Vivi."
    urshu happy "Just as they helped you shatter the artifice that kept you from embodying your true essence, you helped them leave their past...in the past."
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    urshu happy "Now they can again sing songs and imbibe of endless joy in the world beyond the Terminal."
    $ _skipping = True

    return