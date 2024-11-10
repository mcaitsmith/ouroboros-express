# The scene starts here.

label epi_friend_darius:

    # Epilogue/Friendship/Darius Wrecker
    # LOCATION: terminalofdreams

    stop music fadeout 2.0
    pause 2.0
    scene white with fade
    play music goodendmusic volume 0.5

    scene terminalofdreams with Dissolve(3.0)
    pause 1.0
    show darius happy at center with dissolve
    pause 2.0

    urshu happy "Darius Wrecker, former Inquisitor, soldier of the Lord of Eternal Rest, was a being who looked in the mirror and hated what they saw."
    urshu happy "He regretted his past actions, but could not accept that he deserved anything but guilt and shame." 
    urshu happy "With Vivi's help, he came to accept the possibility of a new journey: atonement." 
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    urshu happy "Forgiveness was a long way down the road. But for the first time, Darius thought, there could perhaps be a future for him after all."
    $ _skipping = True

    return