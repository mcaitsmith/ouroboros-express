# The scene starts here.

label epi_friend_ava:

    #Epilogue/Friendship/Avatar of Asha
    #Naj's note: this should just be a brief description - about 100 words, if that. Kind of like the slides at the end of Fallout, but it'll be from Urshu's perspective and they'll be against a plain, bright background. 

    stop music fadeout 2.0
    pause 2.0
    play music goodendmusic volume 0.5

    # LOCATION: terminalofdreams
    scene white with dissolve

    show ava happy at center with dissolve

    urshu happy "While I had my occasional doubts about you two, I'm glad that you found each other. So many near misses, close connections, heated moments..."
    urshu "Our sun goddess brought the warm light of friendship into Vivi's empty heart; our reporter helped the Avatar to realize there was more to her than a voice, more than a goddess." 
    urshu "Their verbal sparring matches were an intricate, passionate tango of emotional darts. Their time together burned down their outer defenses until only honesty and friendship remained." 
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    urshu "It had always been there, though here, the All was the Two."
    $ _skipping = True

    return