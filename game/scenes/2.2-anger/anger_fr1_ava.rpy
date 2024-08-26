# The scene starts here.

label anger_fr1_ava:

    #FREE ROAM 1 - Ava

    # LOCATION: observatory
    scene observatory with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking sad "Looks like our friendly neighborhood sun goddess is here."

    show ava happy at right with dissolve

    vivithinking surprised "Oh, what's this? A sunny disposition?"

    show ava sad blush with dissolve
    ava "Hello, Vivi. Has our radiance tempted you today? Come, sit, and play a game. Let us see what future the cards hold."
    vivi neutral "Are those tarot cards? They look...off."
    show ava neutral -blush
    ava "We know not what a \"tarot\" is, but we have placed three cards in front of you."
    vivithinking surprised "A sun, a sea monster, and a huge snake?!"
    vivi neutral "Uh...okay?"

    # <CHOICE>
    ava neutral "Choose wisely."

    menu:
        # OPTION 1 +ATTRACTION
        "The sun card.":

            play sound attchoice
            $ att_meter_ava += int(att_max_anger_fr1 / att_num_list_ava[0])
        
            vivi neutral "The sun card."
            show ava sad blush with dissolve
            ava "The sun can represent light, truth, and love..."
            vivi surprised "Finally some good news!"
            show ava sad -blush
            ava "...we had not finished, Vivi. The sun is upside down, so it brings darkness, lies, indifference."
            # JUMP TO: vivi "This is silly! They're just cards. They can't tell us that!"

        # OPTION 2 +DECAY
        "The sea monster card.":

            play sound decchoice
            $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "The sea monster card."
            ava surprised "Ah. Leviathan. The eater of worlds. Scourge of the seas. Dominance. Aggression. We find this interesting."
            vivi neutral "Wait, was that a dig at...Darius?"
            ava angry "We know of his kind. You would be wise to stay away. His card brings darkness...and deceit."
            # JUMP TO: vivi "This is silly! They're just cards. They can't tell us that!"

        # OPTION 3 +DECAY
        "The big snake card.":

            play sound decchoice
            $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "The big snake card."
            ava surprised "Curious. We have not seen this card before. Curious, indeed. It resembles the snake biting its own tail, the Ouroboros."
            ava neutral "But of course, snakes, reptiles. They are of the same family. A warning... "
            vivi surprised "Oh?"
            vivi neutral "Is this a dig at Susu'rha?"
            ava surprised "I merely am the messenger. And the card could not be clearer. Avoid him, Vivienne."
            # JUMP TO: vivi angry "This is silly! They're just cards. They can't tell us that!"

    vivi angry "This is silly! They're just cards. They can't tell us that!"
    ava surprised "Perhaps, you're right. They are merely cards." 
    ava sad "..."
    ava sad "In the mirror this morning, fate stared back at us. And for you, Vivienne?"
    vivi sad "For me too, Asha."
    vivithinking neutral "We're fading even faster than we were yesterday. There's less of me and the train every second. Not totally unnerving at all!"
    # VISUAL: screen shakes, light flashes 
    show observatory with hpunch
    show observatory with flash
    # SOUND: ava says "ugh"
    # skipping
    ava angry "Why, Vivienne?" 
    ava angry "What was the point of it all?! All our sacrifices. For what?"
    vivithinking surprised "Damn! And I thought I was having trouble coping."

    # <CHOICE>
    vivi neutral "Look, Asha..."

    menu:
    # OPTION 1 +ATTRACTION +DECAY
        "...chin up, princess, or the crown slips.":

            play sound attdecchoice
            $ att_meter_ava += int(att_max_anger_fr1 / att_num_list_ava[0])
            $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "...chin up, princess, or the crown slips."
            ava angry "Princess? We were not royalty, those inbred lickspittles. We came from nothing."
            vivithinking neutral "With that stiff upper lip and all? Yeah, right." 
            ava angry "Why?! We are no more! Our mother sacrificed us. Gutted us like a butcher does a fatted calf."
            vivithinking surprised "Unnecessarily graphic and undeniably tragic!"
            vivi surprised "That's your people's tradition? Sacrifice?!"
            ava sad "We are sacrificed lest people love us too much. Once, an avatar nearly toppled the royals. But now, that is only but a distant fairytale ."
            vivi neutral blush "Well, then no offense, but you're better off here. If your whole purpose was to be sacrificed, then guess what?"
            show ava happy blush with dissolve
            ava "Then our service is at an end. We are free."
            vivi happy "Yes. I like that. Free."
            vivithinking happy "Not a great start, but a good ending, right?"
            show ava happy -blush
            # JUMP TO: vivi neutral blush "Thank you for sharing with me, Asha."

    # OPTION 2 +ATTRACTION
        "...I know what you mean about sacrifices.":

            play sound attchoice
            $ att_meter_ava += int(att_max_anger_fr1 / att_num_list_ava[0])

            vivi sad "...I know what you mean about sacrifices. You're not alone. My career always came first, over friends, family, love. Where'd it get me?" 
            vivi angry blush "Here!"
            ava sad "I'm aware of your tale, li-, ahem, Vivienne. And I am sorry for that."
            ava angry "We shall fade to darkness soon. Have you not seen it in your dreams?"
            vivi angry "You mean nightmares? Yeah..."
            vivi neutral "Well... at least we don't have to make any more sacrifices, right?"
            show ava happy blush with dissolve
            ava "That is true, yes. Our service is at an end. We are free."
            vivi happy "Yes. I like that. Free."
            show ava happy -blush
            ava "Thank you, Vivi. We hope you return."
            vivithinking happy "Not a great start, but a good ending, right?"
            # JUMP TO: vivi neutral blush "Thank you for sharing with me, Asha."

    # OPTION 3 +DECAY
        "Pull yourself up by your bootstraps, and deal with it, Asha.":

            play sound decchoice
            $ dec_meter += int(dec_max_anger / dec_num_anger)

            vivi neutral "...Wanna know what they say on earth where I'm from? Pull yourself up by your bootstraps, and deal with it, Asha."
            ava angry "Perhaps you should heed your own advice, Vivienne."
            vivithinking angry "Hmph. Well, someone's got their knickers in a twist!" 
            vivi angry "Perhaps I shall. Goodbye Asha."
            ava angry "Hmph. Very well. Have an... acceptable evening, Vivienne."

            # ava exits
            hide ava with dissolve

            # vivi exits
            hide vivi with dissolve
            jump anger_susurha_urshu

    vivi neutral blush "Thank you for sharing with me, Asha."
    vivithinking neutral "That went better than I thought. Maybe one of the others wants to play a game as well."
    vivithinking angry "Ugh. And I still gotta find out Urshu's riddle. How am I gonna get off this doomsday train?"

    # JUMP TO: Anger Susurha Urshu
    jump anger_susurha_urshu