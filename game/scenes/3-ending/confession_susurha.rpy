# The scene starts here.

label confession_susurha:

    #Romance/Confession/Susu'Rha Balrinn
    # Susu'Rha takes responsibility for his actions and is able to move on. He asks Vivi whether she will make the most of their present and accept his love.

    # Vivi can either say yes, say no but stay friends, or ask them to wait before she makes a decision

    #LOCATION: Lounge
    # scene lounge with fade
    #show susurha neutral at right with dissolve
    #show vivi neutral at left with dissolve

    play music susumusic fadein 1.0 loop
    vivithinking neutral "There they are, gazing out the window..."
    vivithinking neutral "The glow... It's haunting, yet..."
    susurha "Wondrous, isn't it?"
    vivi neutral blush "It sure is."
    susurha happy "I'm thrilled you could be here to enjoy it with me."
    susurha happy "Our brief time together these past few—I'm not sure if I can even call them days—has been..."
    show susurha happy blush with dissolve
    susurha "Intoxicating..."
    vivithinking happy "Quite."
    show susurha happy -blush
    susurha happy "And cathartic."
    vivi happy "Oh, for me too. As I'm sure you know, given your part in it."
    susurha neutral "..."
    susurha neutral "All my life, all I ever wanted was to be myself, to live life on my own terms. But I didn't understand how much {i}responsibility{/i} was bound up in that."
    show susurha happy blush with dissolve
    susurha "I didn't see..."
    vivi neutral "What?"
    vivithinking neutral "They look so nervous."
    vivithinking neutral blush "Wait..."
    susurha "I didn't see that until I met you."
    susurha "Here, in this place, you helped me understand that my decisions are mine alone. And while there may be consequences for those decisions, there is no reason to punish myself."
    show susurha happy -blush
    susurha happy "Now nothing binds me anymore. The past stays where it belongs."
    vivi neutral "What about the present? The future?"
    susurha happy "The future remains unwritten. All I know is that, whatever's in store..."
    show susurha happy blush with dissolve
    susurha "...I want you by my side."
    susurha "Before everything fades away, I have to know..."
    #<CHOICE 1>
    susurha "Will you stay with me, whatever may come?"
    show susurha happy -blush

    menu:
        #OPTION 1
        # Accept Romance
        "Yes!":

            play peacefulmusic loop
            vivi happy blush "I'd love nothing more than that."
            show susurha happy blush with dissolve
            susurha "That makes me happier than you can possibly imagine."
            vivi happy blush "Oh, but I {i}can{/i} imagine...because I feel the same way."
            show susurha happy -blush
            stop ambience fadeout 1.0
            # JUMP TO: Romance/Susu'Rha Balrinn
            jump romance_susurha

        #OPTION 2
        # Reject Romance
        "I can't.":

            $ susurha_friend = True

            vivi neutral blush "I...I'm sorry. I like you, I do. But I can't like you in the way that you want me to."
            susurha sad "I would be remiss if I didn't tell you how disappointed I am. But I understand. I am a lizard with a troubled past, after all."  
            susurha sad "Nevertheless, I'm glad to have met you, Vivienne Sanssouci." 
            susurha neutral "And to call you my friend."
            vivi happy "Me too, Susu'Rha. A friend till the end."
            susurha happy "See, you are a poet."
            # Note: Susu'Rha is locked as friend. Can no longer be chosen as romance partner.
            #JUMP to: character selector 
            jump show_chars

        #OPTION 3
        #Delay Decision
        "Could you give me a moment?":

            vivi neutral blush "Could you give me a moment to think about it?"
            show susurha neutral blush with dissolve
            susurha "Of course."
            susurha "But don't take too long, please."
            susurha "I would say the suspense would kill me, but..."
            show susurha neutral -blush
            #JUMP TO: Character Selector
            jump show_chars