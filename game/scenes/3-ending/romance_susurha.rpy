# The scene starts here.

label romance_susurha:

    #Romance/Susu'Rha Balrinn
    # A heartfelt interaction as you both hold each other in the face of the end. Darkness, and then a bright light. You hear the train conductor's sigh. "I'm a romantic fool." A chance to begin again... together...

    #LOCATION: observatory
    scene observatory with fade

    show vivi neutral blush at left with dissolve
    show susurha happy blush at right with dissolve

    vivi neutral blush  "Can you feel it? We're approaching our final stop."
    susurha "Come into my arms. There."
    susurha "We can merge with each other as we merge with the cosmic weave."
    vivi neutral blush "It's getting brighter..."

    # VISUAL: the screen shakes
    show observatory with hpunch
    # VISUAL: the scene brightens
    show observatory at bright with dissolve

    vivi happy blush "This is all so much. I may cry."
    vivi happy blush "It's awfully bright... I can hardly see."
    susurha "I'm here, Vivi. I've got you."
    vivi happy "I don't know where you end and I begin!"
    show susurha happy -blush
    susurha happy "I don't either! And I don't know what awaits us, but if this is to be my final moment, I couldn't have asked for a better way to spend it than with you, Vivienne."
    vivi happy blush "Me, too."
    vivi happy blush "I want to be with you forever." 
    vivi happy blush "What if forever is only now?"
    vivi happy blush "Then I want to be with you forever, now."

    #EFFECT: fade to white
    scene white with Dissolve(3.0)
    #To Epilogues according to attraction meters
    jump epi_friend_ava
    # ELSE
    jump epi_eldritch_ava
    # ??ATTRACTION
    jump epi_friend_darius
    # ELSE
    jump epi_eldritch_darius