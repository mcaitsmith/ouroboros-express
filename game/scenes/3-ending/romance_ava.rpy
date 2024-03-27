# The scene starts here.

label romance_ava:

    # Romance/Avatar of Asha
    #A heartfelt interaction as you both hold each other in the face of the end. Darkness, and then a bright light. You hear the train conductor's sigh. "I'm a romantic fool." A chance to begin again... together...

    # LOCATION: observatory
    scene observatory with fade

    show vivi neutral at left with dissolve
    show ava neutral at right with dissolve

    show ava sad blush with dissolve
    ava "Now, take my hand, Vivi." 
    ava "Hold me close for our last dance."
    vivi neutral blush "Aren't you afraid?"
    show ava happy blush
    ava "Not anymore."
    vivi surprised "Oh, Ava! Are you crying?"
    ava "Yes, but with joy. Hold me close. Close your eyes. We will be in this moment forever."
    vivi "Yes. Forever. Praise Ava."

    # EFFECT: fade to white
    scene white with Dissolve(3.0)
    # To Epilogues according to attraction meters
    # ??ATTRACTION
    call epi_friend_darius
    # ELSE
    call epi_eldritch_darius
    # ??ATTRACTION
    call epi_friend_susurha
    # ELSE
    call epi_eldritch_susurha

    scene black with Dissolve(3.0)
    window hide fade
    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 3.0

    # end game
    return