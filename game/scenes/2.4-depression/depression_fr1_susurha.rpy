# The scene starts here.

label depression_fr1_susurha:

    # FREE ROAM 1 - Susu'Rha (DEPRESSION)

    # LOCATION: diningcar
    # call check_overlay from _call_check_overlay_30
    scene diningcar with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking "If anyone knows how to drink on this train, it's gotta be Susu'Rha."

    show susurha neutral at right with dissolve

    susurha happy "Well, if it isn't our resident reporter!"
    susurha neutral "What brings you here?"

    #??DECAY
    if dec_meter >= 40:
        susurha "Come to torment me some more?"
    #END

    vivi "To be honest, I'm ready to just get nice and drunk."
    susurha sad "I share your thoughts."
    susurha neutral "Come, come. Take a seat and let me treat you to something special."
    vivithinking "Wow. They seem at home behind the bar."
    vivi surprised "When someone's really good at mixing drinks, we call them a mixologist."
    susurha happy "In the Viridian Wood, the mixture and ingestion of intoxicating potions was almost a nightly occurrence."
    susurha happy "Ah...to sit on my balcony, reading a collection of poetry with a glass of red wine in hand."
    vivi "It sounds like you've lived a full life."
    
    # <CHOICE>
    susurha sad "In the Wood, we lived joyously, following the path of self-expression."
    
    menu:
        # OPTION 1
        "(I could have used more of that.)":

            vivithinking sad "I could have used more of that."
            # JUMP TO susurha happy "A delectable pina colada for me and a sloe gin fizz for you."

        # OPTION 2
        "(Self-expression, huh. Yeah, right.)":

            vivithinking neutral "Self-expression, huh. Yeah, right."
            vivithinking neutral "I feel like constantly chasing a way to express myself in the next day's paper sometimes got in the way of the whole living joyously part..."
            # JUMP TO susurha happy "A delectable pina colada for me and a sloe gin fizz for you."

    susurha happy "A delectable pina colada for me and a sloe gin fizz for you."
    vivithinking neutral "Hmmm..."
    vivi "This is incredible."
    susurha "Good."
    susurha "During my time at the druid camp, they had a special ritual that required the unique properties of liquor."
    vivithinking "Curious..."
    vivi "What was it?"
    susurha "It is where we playfully say something about ourselves that we have never done and the others would take a drink if they have done the deed." 
    susurha "Allowing us to tear away at the veils that encase us to those we know."

    # ??DECAY
    if dec_meter >= 40:
        vivi "Oh, I don't know about this."
        susurha "Even now as we near the end of the tracks?"
        susurha sad "Can we just try..."
        susurha sad "Try to pull back the mask?"
        susurha neutral "I'll even let you ask the first question."
        vivithinking "Are we sure about this?"
        vivithinking "..."
        vivithinking "Screw it!"
        vivi "Alright."
    #END

    #<CHOICE>
    vivi "Never have I ever..."

    menu:

        #OPTION 1 +ATTRACTION
        "Been engaged.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_depression_fr1 / att_num_list_susurha[4])

            vivi "Been engaged."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha "Hmmm..."
            susurha "I believe this is called 'Beginner's luck.' You've got me there."
            vivithinking "Wow! They've been engaged?"
            vivithinking "Looking at them, not hard to believe."
            vivi "Who was it to?"
            susurha "My second cousin. Gal'Rha. It was arranged."
            vivi "Oh boy."
            susurha "I learned about it the night before I ran away."
            susurha "I didn't want to be tied down and now I'm here."
            susurha "Alone."
            vivi "Hardly alone."
            susurha happy "Of course. My mistake."
            #JUMP TO: susurha happy "My turn."

        #OPTION 2 +DECAY
        "Led a kingdom.":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi "Led a kingdom."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha "Hmm... Got me there I suppose."
            susurha "Bottoms up."
            susurha "That was quite the easy one. Are you trying to make me drunk?"
            vivi "Maybe."
            vivi "Why didn't you stay? The power alone..."
            susurha sad "Was a lie. There is no power that lays upon the throne."
            susurha sad "Just chains that bind and a muzzle that seals your mouth."
            susurha sad "A mere avatar for those around you."
            vivithinking "They surely can't be serious."
            susurha sad "I suppose we can't escape the chains that bind us."
            susurha sad "We all end on the same track."
            #JUMP TO: susurha happy "My turn."

        #OPTION 3 >>DECAY +ATTRACTION
        "I don't know." if dec_meter >= 35:

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_depression_fr1 / att_num_list_susurha[4])
                
            vivi "I don't know."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha "Boooo..."
            vivi "I'm sorry. I'm not sure what to say."
            susurha "Really?"
            vivi sad "Yeah, I truly don't know what to say."
            vivi sad "I'm sorry."
            susurha "It's okay. Don't stress. Just..."
            susurha "Be..."
            vivi "Okay."
        
            show susurha happy 

            susurha "You got it."
            #JUMP TO: susurha happy "My turn."

        #OPTION 4 >>DECAY +DECAY
        "Can we just sit and drink?" if dec_meter >= 40:

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi "Can we just sit and drink?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            vivithinking "I don't know if I have any more games left in me."
            susurha angry "Hmmm..."
            #JUMP TO: susurha happy "My turn."

    susurha happy "My turn."
    vivithinking "Oh boy."
    # <CHOICE>
    susurha neutral "Never have I ever been in love."

    menu:

        #OPTION 1 +ATTRACTION
        "No.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_depression_fr1 / att_num_list_susurha[4])

            vivi "No."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha surprised "Really?"
            vivi sad "Yeah, I've... never really gotten that far before."
            vivi sad "I've had plenty of partners, but none of them... felt..."
            vivi sad "You know."
            vivi sad "I'm sorry. I'm killing the buzz."
            susurha neutral "Stop. You've nothing to apologize for."
            susurha "This is the whole point of the ritual. To remove our masks."
            susurha sad "I share your same experience. Many held me in their gaze, but none could hold mine."
            vivi "Alone together."
            # SOUND: susurha scoffs.
            # skipping
            susurha "I can drink to that."
            #JUMP TO: susurha neutral "I wonder if love lasts beyond death..."

        #OPTION 2 >>ATTRACTION +ATTRACTION
        "Possibly, recently." if att_meter_susurha >= 60:

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_depression_fr1 / att_num_list_susurha[4])

            vivi blush "Possibly, recently."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha surprised "Oh... Do tell me more, madam."
            vivithinking "Do I tell them? Do I not?"
            vivithinking "No."
            vivithinking "Let's be fun."
            vivi happy blush "You should have been more specific."
            show susurha happy blush with dissolve
            susurha "Your face tells it all."
            show susurha neutral -blush
            #JUMP TO: susurha neutral "I wonder if love lasts beyond death..."

        #OPTION 3 +DECAY
        "I've had plenty of lovers.":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi "I've had plenty of lovers."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha "I'm sure. A woman such as yourself, but..."
            susurha "Have YOU ever been in love?"
            vivi "Everyone has been in love in their life."
            vivi "It isn't anything special."
            vivi "..."
            susurha sad "Vivienne..."
            susurha sad "I'd want to believe you're wrong."
            #JUMP TO: susurha neutral "I wonder if love lasts beyond death..."

    susurha neutral "I wonder if love lasts beyond death..."
    susurha "Thank you for spending these moments with me."

    #DECAY ROUTE (??DECAY?)
    if dec_meter >= 40:
        susurha "I wish I could have made these moments more special for you."
        susurha "The train is speeding up. Have you noticed?"
    # END

    hide susurha with dissolve

    vivithinking "I think I got enough out of this drink."
    vivithinking "My head is already spinning."
    vivithinking "I should take a moment to collect myself."

    #JUMP TO: Asha Susurha convo
    jump depression_asha_susurha