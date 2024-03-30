# The scene starts here.

label epi_friendship_all:

    # Epilogue/Friendship/All
    # It's a friendship bonanza! Our passengers alight from the train and have a big cheesy moment. Urshu waves at them with a white handkerchief from the train.
    #"What is this place?"
    # "The Terminal of Dreams. You've made it. Come on! Everyone is waiting for you."

    # LOCATION: terminalofdreams
    scene white with dissolve

    show vivi happy at center_left with dissolve:
        xzoom -1
    show urshu happy at center_right with dissolve

    vivithinking surprised "I can hear brakes..." 
    vivithinking happy "I'm in the open!"
    vivithinking happy "I think Urshu's being serious."
    urshu happy "It is time to disembark, now. Please, watch your step."
    show susurha happy at right with dissolve

    susurha happy "Yeah, get off the train already!"
    vivithinking neutral "Wow! Solid ground! Not that slightly-canted, bouncy train floor!"
    vivi surprised "What is this place?"

    show urshu neutral

    urshu neutral "The station."
    urshu neutral "We have already said our goodbyes. Shoo, shoo!"
    vivithinking surprised "I'm stepping off, I'm stepping off, I'm off!"
    vivi happy "Woah. This place... And you're all here!"

    show susurha happy

    susurha "Despite everything... We are."
    susurha happy "Does that mean there's no end to the Vivienne antics?"

    show ava happy at left with dissolve:
        xzoom -1.0

    ava happy "And we are together, too, us strangers."

    show darius happy at center with dissolve

    darius happy "Strangers to ourselves, perhaps, but not among each other."
    vivi happy "That's a cute way of saying we're friends."
    show darius angry blush with dissolve
    darius "Vivienne Sanssouci."
    vivi neutral "But now what..? Like, there's no signs!"
    show darius angry -blush

    show urshu neutral 

    urshu neutral "In case it was not clear, you will need each other to find the way!"
    vivi neutral "So, we passed your test? Can you tell us how we did it?"
    vivithinking sad "So many probably never did..."
    urshu happy "You all honored each other, I will say."
    urshu "But you, Miss Sanssouci, you offered something powerful, more so than simple love."
    vivi happy "A pretty smile and nice hips?"
    urshu neutral "Come now, no need for deflecting or verbal jousts."
    urshu "Besides, you never did beat me..."
    urshu "You created camaraderie, companionship, {i}connection{/i}."
    vivi neutral blush "I did no such things..."
    urshu "You did! And it's something the Miss Sanssouci who boarded the train may never have achieved." 
    urshu happy "You have finally changed! Do us a favor and be more silly and moody! Enough of that pedantic reporter mask, okay?"
    vivi angry blush "Silly and moody? I'm going to rip that smugness out of your face!"
    urshu neutral "It is by being yourself that you saved everyone here."
    urshu "Your new bonds are North Stars in dark places. They will lead you back to the light, when you next are lost."

    # SOUND: Train whistle
    play sound trainwhistle
    pause 3.0

    show urshu happy blush with dissolve
    urshu "Au revoir, my diamonds!"
    vivi happy blush "Give us one more look!"
    show urshu neutral -blush
    urshu neutral "At what?"
    vivi happy "AT DAT ASS!"

    show darius happy

    darius happy "There, Vivienne. He's turning."
    darius neutral "The atrocity. Barely fits through the doorway..."

    show susurha happy blush with dissolve

    susurha "If only all the peoples in the worlds were blessed as he!"
    show susurha neutral -blush
    susurha neutral "But if everyone's rear was so, would it be special?"
    vivi happy "I hate to see him go..."

    show ava happy

    ava happy "Come now, otherworldly companions, wherever we shall go, we will find behinds plump as Lomulan berries."
    vivithinking "But will we, though?"
    vivi happy "Enough about berries and rear ends..."
    vivi "We're free. Wherever we are."

    show darius neutral

    darius happy "This has to be the Terminal of Dreams, a place oft-referred to in heretical texts."
    darius "I can't believe they were right. It is also known as the Waypoint of the Worthy..."

    show susurha neutral

    susurha neutral "Worthy of what, I wonder?"
    vivi happy "Let's not stick around and think about it."
    vivi "Let's go and figure it out."
    vivi happy blush "Together."

    # The End

    scene black with Dissolve(3.0)
    window hide fade
    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 3.0

    # end game
    return