label anger_susurha_urshu:

    # call check_overlay from _call_check_overlay_9
    scene lounge with fade
    play ambience amb_lounge if_changed fadein 1.0
    play music mainmusic loop
    show vivi neutral at right with dissolve:
        xzoom 1

    $ urshu_fullbody = True
    $ susurha_fullbody = True
    vivithinking "This is getting to be too much. This train, these games, Urshu..."


    vivithinking "I’m sick of it!"


    vivithinking "Oh, speaking of the devil."


    vivithinking "It seems Urshu is getting feisty with Susu’Rha."





    show urshu neutral at center with dissolve:
        xoffset -300 xzoom -1
    show susurha neutral at center with dissolve:
        xoffset 30


    urshu "Lounging about again, I see. Kicking the feet up and enjoying the ride, hmm?"


    susurha happy "You know it, Mr. Conductor. Envious?"


    urshu "Envious? Ah, do you spot a green-eyed monster, perhaps? I don’t have nearly enough time in the day for such feelings."
    stop music fadeout 2.0


    susurha "Mhm."

    play music spymusic loop
    urshu "How do you do it?"


    susurha neutral "Do what?"


    urshu "Present yourself as so relaxed."


    susurha "Present?"


    susurha happy "Look at you. So confident that I’m playing pretend."


    susurha neutral "What about yourself? Coming here to criticize me. Acting like you’re better than I."


    urshu sad "..."


    urshu sad "I come to you, honestly."


    susurha neutral "Sure you do, dragging me here to this contraption really invokes such ideas."


    urshu sad "What are you afraid of? What makes you wear this mask of relaxation?"


    susurha angry "I wear no mask! So don’t even try to project your own lies onto me!"


    susurha angry "Your dashing physique and alluring voice may convince the others to play your little game, but I see you for the creature you are."


    urshu sad "I merely wish to help, Susu’Rha."


    urshu sad "Not everyone is scheming."


    vivithinking "I can feel the heat burn as Susu’Rha snarls."


    susurha sad "..."


    susurha sad "Just remove yourself from my sight."


    susurha sad "You know nothing of me."


    urshu sad "It is a great shame that no one does."
    stop music fadeout 2.0

    hide susurha
    hide urshu

    show vivi neutral with dissolve 

    vivithinking  "Time to go."

    #JUMP TO: Character Selector 2
    stop ambience fadeout 1.0
    jump anger_cs2
