# The scene starts here.

label epi_friend_ava:

    #Epilogue/Friendship/Avatar of Asha
    #Naj's note: this should just be a brief description - about 100 words, if that. Kind of like the slides at the end of Fallout, but it'll be from Urshu's perspective and they'll be against a plain, bright background. 

    pause 2.0
    scene white with fade
    play music finalemusic if_changed loop

    # LOCATION: terminalofdreams
    scene terminalofdreams with Dissolve(3.0)
    play ambience amb_terminal fadein 1.0
    pause 1.0
    show ava happy at center with dissolve
    pause 2.0

    urshu happy "While I had my occasional doubts about you two, I'm glad that you found each other. So many near misses, close connections, heated moments..."
    urshu "Our sun goddess brought the warm light of friendship into Vivi's empty heart; our reporter helped the Avatar to realize there was more to her than a voice, more than a goddess." 
    urshu "Their verbal sparring matches were an intricate, passionate tango of emotional darts. Their time together burned down their outer defenses until only honesty and friendship remained." 
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    play sound sparkle
    urshu "It had always been there, though here, the All was the Two."
    stop ambience fadeout 1.0
    $ _skipping = True

    return