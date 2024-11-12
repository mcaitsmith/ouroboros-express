# The scene starts here.

label confession_darius:

    #Romance/Confession/Darius Wrecker
    #LOCATION: lounge
    # scene lounge with fade
    # show darius neutral at right with dissolve
    show vivi neutral at left with dissolve:
        xzoom -1

    play music mainmusic loop
    vivithinking neutral "There he is. He's standing tall."
    darius neutral "I'm glad to see you. I wasn't sure if we'd have the chance to talk again."
    vivi neutral "Where else would I go?"
    show darius neutral blush with dissolve
    darius "Fair enough."
    darius "There's... something about you, Vivi." 
    darius "That fierce intelligence, the dogged questioning."
    darius "You have a spark that I can't help but want to fan into an inferno."
    vivi surprised blush "Are you calling me hot?"
    show darius surprised blush
    darius "What? Yes! I mean, no! I mean, what?"
    show darius happy blush
    darius "I'm trying to bare my soul to you, you wretched human!"
    darius "I know I'm... worthless. A murderer. Degraded beyond belief."
    show darius sad blush
    darius "But I can... I must... be better. These sins. I carry them with me— I can't pretend they don't mean anything, anymore."
    darius "I own them. But whatever happens, I want someone by my side. Not to share my burden, but as a witness. Someone to remind me of the Ouroboros Express."
    show darius neutral blush
    darius "Someone who knows I'm not hiding any longer."
    show darius happy blush
    darius "Someone to love."

    #<CHOICE>
    darius "What do you think? It could be the assignment of a lifetime. One you chose yourself."
    show darius happy -blush

    menu:
        #OPTION 1
        #Accept Romance
        "Yes!":
            vivithinking happy "The way their mouth tentacles curl..."
            vivi happy blush "Darius... Yes."
            stop music fadeout 5.0
            stop ambience fadeout 1.0
            #JUMP TO: Romance/Darius Wrecker
            jump romance_darius

        #OPTION 2
        #Reject Romance
        "I can't.":

            $ darius_friend = True

            vivi neutral blush "Darius, I believe that you've accepted your past. But your future—you have a lot to figure out on your own."
            vivi happy "I'd love to come with you on your journey. As a friend."
            show darius neutral blush with dissolve
            darius "I understand. And I appreciate the confidence. And your honesty."
            darius "Safe travels... friend."
            show darius neutral -blush
            stop music fadeout 5.0
            # Note: Darius is locked as friend. Can no longer be chosen as romance partner.
            # JUMP TO: Character Selector
            jump show_chars

        #OPTION 3
        #Delay Decision
        "Could you give me a moment?":

            vivi surprised blush "Could you give me a moment? I want to give this, um, assignment the consideration it's due."
            show darius neutral blush with dissolve
            darius "Noted. And...thank you."
            show darius neutral -blush
            stop music fadeout 5.0
            #JUMP TO: Character selector
            jump show_chars