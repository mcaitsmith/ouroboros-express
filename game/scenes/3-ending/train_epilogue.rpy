# The scene starts here.

label train_epilogue:

    # EFFECT: fade to white
    scene white with Dissolve(3.0)

    # ROMANCE JOURNAL ENTRY
    $ message = "Here we are: the final stop. And I'm still here. I'm staying with Urshu. He's easily the most frustrating, maddening, cryptic excuse for a cosmic entity I've ever met... and yet I can't get enough of him. He sees me. Sees the real me in a way that no one ever has, and when I look at him I see a soul so much deeper than the flippant remarks he likes to come out with. Sure, we're probably going to argue our way through eternity, but I love a challenge. And... I love Urshu. I hate to say goodbye to the others. But Urshu told me he has a trick up his sleeve when it comes to that... lets go find out."
    
    
    
    #LOCATION: observatory
    scene observatory with fade
    play ambience amb_observatory fadein 1.0
    play music finalemusic

    show romancemotes
    
    #SERA NOTE - Both Vivi and Urshu should be in train conductor outfits from here.

    show vivi_conductor neutral at center_left with dissolve:
        xzoom -1
    show urshu happy at center_right with dissolve
    
    vivi_conductor surprised "I can feel it... something in the cosmic weave shifting. This was meant to be my final stop."
    urshu neutral "You're weaving your own future now, in the brightest of thread. As long as you haven't changed your mind?"
    vivi_conductor happy "Don't even think about it. You can't get rid of somebody who's won your heart."
    urshu happy "Truly, my love, I wouldn't dream of trying."
    vivi_conductor neutral "But what happens to the others, now? I never imagined I'd meet anyone like them: a sun goddess, a dragon prince, and squid Poirot, much less care about their eternal fates. But..."
    urshu neutral "Perhaps you'll find you've changed their fates, too."
    vivi_conductor surprised "What? How is that possible?"
    urshu neutral "Our Sun Goddess burns with a new light now she's come to realise she is more than a mouthpiece. She is whole, and wholly Ava."
    urshu neutral "Darius Wrecker, former inquisitor, soldier of the Lord of Eternal Rest, turns away from his dark past and towards the possibility of a new journey of atonement."
    urshu neutral "And Susu'Rha, who once broke the chains of expectation and eschewed their royal burden, only to find themselves burdened by regret, now leaves their past where it belongs."
    urshu happy "But what should fate bring them now? Perhaps... to new beginnings!"
    vivi_conductor surprised "New beginnings? You mean..."
    stop ambience fadeout 5.0
    
    #SERA NOTE - ideally it would be lovely to fade out here, and fade up an image of 
    # the three NPCs at the terminal. Vivi's next line could be shown over this image, 
    # before returning to them in the obervatory.
    show white with Dissolve(2.0)
    show terminalofdreams with Dissolve(2.0)
    play ambience amb_terminal fadein 1.0
    play sound trainwhistle
    pause 3.0
    show ava neutral at left with dissolve:
        xzoom -1.0
    show darius neutral at center with dissolve
    show susurha neutral at right with dissolve
    hide white
    
    vivi_conductor surprised "They're together on the platform! Urshu, you little peach! Wherever they're going, you made sure they wouldn't be alone."
    show white with dissolve
    hide ava
    hide darius
    hide susurha
    stop ambience fadeout 0.5
    hide terminalofdreams
    play ambience amb_observatory fadein 0.5
    hide white with dissolve
    
    urshu happy "Ahem... yes, well. Someone recently did something similar for me. You could say I found myself inspired."
    vivi_conductor neutral "Remember that first day, when I thought everyone was wearing masks? I was right, wasn't I. We all were. Especially you."
    urshu neutral "You do have quite the gift for seeing straight through them."
    vivi_conductor happy "And for finding something beautiful underneath."
    urshu neutral blush "And yet, none quite so beautiful as you. Won't you take my hand, Vivi? At any moment we will leave them to their new beginning, as our journey begins its spiral of theatrics and redemption once again."
    vivi_conductor happy "It's been a long time since you had a fresh start of your own, huh, Urshu?"
    urshu neutral "An eternity, one might say."
    stop music fadeout 3.0
    show vivi_conductor at center with moveoutleft:
        xoffset -100
    show urshu at center with moveoutright:
        xoffset 100
    $ renpy.choice_for_skipping() # stop skipping
    $ _skipping = False
    vivi_conductor happy "Then hold me close. Don't let go. Our new beginning starts now."
    
    stop ambience fadeout 3.0
    scene white with Dissolve(3.0)
    

    scene black with Dissolve(3.0)
    window hide fade
    $ quick_menu = False # hide quick menu
    $ _game_menu_screen = None # disable menu
    play music creditsmusicgood loop
    call screen credits
    stop music fadeout 3.0
    pause 3.0

    # end game
    return
    