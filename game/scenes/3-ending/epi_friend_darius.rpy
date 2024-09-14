# The scene starts here.

label epi_friend_darius:

    # Epilogue/Friendship/Darius Wrecker
    # LOCATION: terminalofdreams

    stop music fadeout 1.0
    pause 1.0
    play music goodendmusic volume 0.5

    scene white with dissolve

    show darius happy at center with dissolve

    urshu happy "Darius Wrecker, former Inquisitor, soldier of the Lord of Eternal Rest, was a being who looked in the mirror and hated what they saw."
    urshu happy "He regretted his past actions, but could not accept that he deserved anything but guilt and shame." 
    urshu happy "With Vivi's help, he came to accept the possibility of a new journey: atonement." 
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    urshu happy "Forgiveness was a long way down the road. But for the first time, Darius thought, there could perhaps be a future for him after all."
    $ _skipping = True

    return