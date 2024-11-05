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
    urshu happy "It is time to disembark now. Please watch your step."
    show susurha happy at right with dissolve

    susurha happy "Yes, hurry, let's get off this thing!"
    vivithinking surprised "Wow! Solid ground! Not that shaky-ass train floor!"
    vivi surprised "What is this place?"

    show urshu neutral

    urshu neutral "The station."
    urshu neutral "We have already said our goodbyes. Shoo, shoo!"
    vivithinking surprised "I'm stepping off, I'm stepping off, I'm off!"
    vivi happy "Woah. This place... And you're all here!"

    show susurha happy

    susurha "Despite everything... we are."
    susurha happy "Does that mean we're stuck with you and your antics forevermore?"

    show ava happy at left with dissolve:
        xzoom -1.0

    ava happy "I believe we're all intended to be together, now, no longer strangers."

    show darius happy at center with dissolve

    darius happy "Strangers to ourselves, perhaps, but not among each other."
    vivi happy "That's a cute way of saying we're friends."
    show darius angry blush with dissolve
    darius "Vivienne Sanssouci..."
    vivi neutral "But now what..? Where do we go? There are no signs!"
    show darius angry -blush

    show urshu neutral 

    urshu neutral "In case it was not clear, you will need each other to find the way!"
    vivi neutral "So, we passed your test? Can you tell us how we did it?"
    vivithinking sad "So many probably never did..."
    urshu happy "You all honored each other, that's all I can say."
    urshu "But you, Miss Sanssouci, you offered something powerful, more so than simple love."
    vivi happy "My pretty smile and devastating wit?"
    urshu neutral "Come now, no need for deflecting or verbal jousts."
    urshu "Besides, you never did beat me..."
    urshu "You created camaraderie, companionship, {i}connection{/i}."
    vivithinking surprised "I did? I guess I did."
    vivi surprised blush "Thanks Urshu... Though, it's not like I didn't have help."
    urshu "You did. And accepting help is something the Miss Sanssouci who boarded the train may never have achieved."
    urshu "In turn you have helped the others who stand with you now." 
    urshu happy "You've shown them who you really are. So don't put that reporter's mask back on and return to your prickly proclivites, my little cactus."
    vivi happy blush "'Little cactus?!' Don't make me get back on that train and show you my prickles!"
    urshu neutral "Ah, some things about you never change. But it is by being yourself that you saved everyone here."
    urshu "Your new friends are North Stars in dark places. They will lead you back to the light, when next you are lost."

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

    darius happy "I'll never get used to that human audacity."

    show ava happy
   
    ava "But I believe we have all come to appreciate it."

    show susurha happy blush with dissolve

    susurha "Look, Vivi, he's turning."
    show susurha neutral -blush
    vivi happy "I hate to see him go, but I love to watch him leave."

    ava neutral "There he goes, back into oblivion once more. It will be strange, I think, to no longer have him clutching the cards to the game of our lives."
    vivi neutral "It will be strange to have more to explore than a few rickety train carriages."
    ava neutral "Now we truly are alone, aren't we. We know not where."
    darius neutral "I might. This has to be the Terminal of Dreams, a place oft-referred to in heretical texts."
    darius "I can't believe they were right. It is also known as the Waypoint of the Worthy..."

    show susurha neutral

    susurha neutral "Worthy. Perhaps not a term I would have applied to myself."
    darius neutral "Nor I."
    ava neutral "Nor I."
    vivi neutral "Well, we can all be in the 'don't think we're worthy' club, but here we are. So maybe it means we're worth something to each other."
    vivi neutral "Worth everything to each other."
    vivi neutral "As far as {i}feeling{/i} worthy goes - I think that might be what Urshu wanted us to do with the time he's given us."
    susurha neutral "I hope we can prove ourselves up to the task."
    ava neutral "I have every faith in you, scaly one."
    darius neutral "I have faith in us."
    vivi happy "Then let's step into the Waypoint of the Worthy."
    susurha happy "Together."
    ava happy "Together."
    darius happy "Together."


    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    vivi happy blush "Together."

    # The End

    stop sound fadeout 3.0
    scene black with Dissolve(3.0)
    window hide fade
    $ quick_menu = False # hide quick menu
    $ _game_menu_screen = None # disable menu
    call screen credits
    stop music fadeout 3.0
    pause 3.0

    # end game
    return