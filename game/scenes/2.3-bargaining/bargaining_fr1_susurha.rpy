# The scene starts here.

label bargaining_fr1_susurha:

    #FREE ROAM 1 - Susu'Rha

    # LOCATION: diningcar
    call check_overlay
    scene diningcar with fade

    # SOUND: window click - opening
    play sound windowopen
    pause 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    show susurha neutral at right with dissolve

    vivithinking "There they are. Wait, what are they--"
    vivi neutral "Susu'Rha? Why are you just staring out that dirty window?"
    vivi neutral "Is something wrong?"
    susurha neutral "..."
    susurha neutral "When we made our way around the last turn I was able to see the entire length of the train for a brief moment."
    vivi neutral "And?"
    susurha neutral "It's decaying. Parts of the train that were visible during the start of our voyage are now impossible to see."
    susurha neutral "Shrouded in mist."
    vivi neutral "That's not good."
    susurha neutral "The phenomenon is becoming more pronounced as time goes on."
    vivi neutral "..."
    susurha neutral "I can see your wheels turning. What is it?"
    vivithinking "How much do I reveal about the plan?"
    vivi neutral "Tell me...what do you know about Urshu?"

    # <CHOICE>
    susurha neutral "Our oh-so articulate, impeccably-dressed conductor? Why do you want to know?"

    menu:
        # OPTION 1 +DECAY
        "You're such an observant lizard. I just want to know what you pick up on.":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "You're such an observant lizard. I just want to know what you pick up on."  
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha angry "The one so seemingly dedicated to self-deception has the temerity to call me a lizard."
            vivi angry "Alright, then. Fine! Keep your assiduous observations to yourself."
    
            # JUMP TO: vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."
    
        # OPTION 2 >>DECAY +DECAY
        "He just seems like such an enigmatic character." if dec_meter >= 10:

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "He just seems like such an enigmatic character..."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha angry "...and after that statement I'm supposed to fill in the blanks about what I know?"
            susurha angry "Even if I did know anything useful about Urshu, what makes you think I'd tell you?"
            vivi surprised "Damn. I thought we had a good rapport. I guess not."
            susurha angry "I thought you were a good reporter. I guess not."
            vivi surprised "Ouch!"
            vivithinking "I must have really ticked them off."
            vivithinking "I should come at this from a different angle."
        
            # JUMP TO: vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."


        # OPTION 3 +ATTRACTION
        "I struck a bargain with Urshu. I'm going to make him a meal.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_bargaining_fr1 / att_num_list_susurha[2])
        
            vivi neutral "I struck a bargain with Urshu. I'm going to make him a meal and I need your help."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "A meal...to die for?"
            vivi angry "Witty."
            susurha happy "I'm listening."
            vivi neutral "But I don't know if it's a trap or not. It could be a test of some kind."
            susurha neutral "So you'd like me to help answer the question of whether or not we can trust him."
            vivi neutral "Exactly."
            vivithinking "Well, that and..."

            # JUMP TO: vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."


        # OPTION 4 +ATTRACTION +DECAY
        "Well, I may have a plan...":

            play sound attdecchoice
            show attraction_icon at right:
                xoffset -500
                # xoffset -30
                yoffset -850
            show decay_icon at right:
                xoffset -500
                # xoffset -30
                yoffset -750
            with { "master" : Dissolve(0.5) }
            $ att_meter_susurha += int(att_max_bargaining_fr1 / att_num_list_susurha[2])
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)
        
            vivi neutral "Well, I may have a plan, but I need to know everything I can about that conductor to get it to come off properly." 
            hide attraction_icon
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "..." 
            vivi neutral "You want me to tell you about my plan."
            susurha neutral "Or you could keep me in suspense, and while we stand here awkwardly, more and more of this train is reclaimed by whomever or whatever entity rules this cursed liminality."
            vivi happy "We need to make him a meal. If he enjoys it, we get our lives back."
            susurha neutral "He told you that?"
            vivi neutral "Not in so many words."
            susurha neutral "..."
            susurha neutral "That man or...thing, or whatever he is—what makes you think we can trust him?"

            show vivi neutral at left

            vivithinking "Because we don't have a CHOICE."
        
            # JUMP TO: vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."

    vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."
    susurha neutral "He's not human, that much I know."
    vivi surprised "How do you know?"
    susurha neutral "When I stand next to him, there's a low, resonant hum. Typical of phantasms. Humans don't have it."
    vivi neutral "Then what is he exactly?"
    susurha neutral "When I was three years old, my family stole an ancient tomb from a village they burned to the ground. Inside the tomb was not a body but a book. "
    susurha neutral "Late at night, I would sneak downstairs to read the stories it told."
    susurha neutral "One story in particular haunted my nightmares for years."
    vivi neutral "What was it?"
    susurha neutral "Boskala Nah, a sentient mass of ooze that floods the very fabric of reality."
    susurha neutral "The stories claimed that when someone dies they return to all that is. Become one with everything... existence, if you will."
    susurha neutral "To do this, Boskala Nah drowns you as a test, watching to see if you sink or swim."
    susurha neutral "This Urshu I believe, holds a similar function."
            
    # <CHOICE>
    susurha neutral "And all I know is that bargaining with Boskala Nah was useless." 
    
    # DECAY ROUTE
    if dec_meter >= 10:
        play sound decchoice
        susurha neutral "Try not to burn yourself, Vivienne."
        # JUMP TO: Character Selector 2
        jump bargaining_cs2

    menu:
        # OPTION 1 +ATTRACTION
        "So you're calling Urshu a slimy freak?":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_bargaining_fr1 / att_num_list_susurha[2])

            vivi neutral "So you're calling Urshu a slimy freak?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "...Yes."
            susurha angry "In fact, he is the slimiest of them all."
            susurha neutral "I know you feel as I do about him."
            vivi neutral "Yeah." 
            vivi neutral "He's so slimy, I bet he takes a bath every hour."
            susurha neutral "He's so slimy, I bet he could glide through the eye of a needle."
            vivi happy "He's so slimy, I bet he watches TLC unironically."
            susurha happy "He's so slimy, I bet he reads those terrible romance novels."
            vivi happy "Like Colleen Hoover?!"
            susurha happy "Who?"
            vivi neutral "...Nevermind! Ignorance is bliss!"
            susurha happy "Ahaha."
            susurha happy "I imagine him lounging around, laughing at all the poorly executed twists and betrayals."
            susurha happy "Wishing he were the one thing slimier than himself, a human!"
            vivi angry "HEY!"
            susurha happy "Hahahaha." 

            show vivi neutral at left

            vivithinking "They're laughing."

            show vivi happy at left

            vivithinking "Seeing them like this makes me feel...warm."
        
            # JUMP TO: vivi neutral "I still need to try at least."

        # OPTION 2 +ATTRACTION
        "I don't think Urshu is that bad.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_bargaining_fr1 / att_num_list_susurha[2])

            vivi neutral "I don't think Urshu is that bad."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha angry "Oh, come on now. I know a woman as skilled as yourself can sniff out fakery from miles away."
            susurha angry "The man, or whatever he is, has been painting himself this whole time as a well-dressed, well-meaning human conductor while we hurtle towards our deaths on a train for the dead!"
            show susurha neutral blush with dissolve
            susurha "I love your ability to think positively of others, but..."
            show susurha neutral -blush
            susurha neutral "When we can't even trust that the mask they wear is their own face..."
            susurha neutral "There's room for doubt."
            vivithinking "Perhaps they have a point, but I still need to try something."

            # JUMP TO: vivi neutral "I still need to try at least."

        # OPTION 3 +DECAY
        "Are you absolutely sure we can't bargain with Urshu?":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "Are you absolutely sure we can't bargain with Urshu?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "I wouldn't trust him if my life depended on it."
            susurha neutral "Heh...I suppose our lives do depend on him, don't they?"
            vivi neutral "This isn't a joke."
            susurha neutral "You don't see me laughing about it, do you?"
            susurha angry "That conductor evokes the same sensations as a slimy worm crawling up your spine on a blistering summer day."
            susurha neutral "I'd imagine he has always been flexible with what he reveals and to whom."
            susurha neutral "I don't doubt that the boredom of leading this train dulls his mind."
        
            # JUMP TO: vivi neutral "I still need to try at least."

        # OPTION 4 >>ATTRACTION +ATTRACTION
        "Urshu is quite the slimy freak." if att_meter_susurha >= 30:

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_susurha += int(att_max_bargaining_fr1 / att_num_list_susurha[2])

            vivi neutral "Urshu is quite the slimy freak."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "The slimiest of them all."
            vivi neutral "I bet he thinks he looks good in that garb he has on every day."
            susurha neutral "I imagine him lounging around, reading romance novels nightly."
            vivi happy "And sipping the most expensive of red wines."
            susurha happy "And laughing at all twists and betrayals."
            vivi happy "Snooping on all of our drama."
            susurha happy "Wishing he was human."
            vivi happy "HAH! Yes."
            vivithinking "This is nice."
            vivithinking "I really do love talking to Susu'Rha."

            show vivi neutral at left

            vivithinking "But I won't be able to talk with them anymore if I die..."

            # JUMP TO: vivi neutral "I still need to try at least."

        # OPTION 5 >>DECAY +DECAY
        "I NEED his help if I'm gonna get off this train." if dec_meter >= 15:

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "I NEED his help if I'm gonna get off this train."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            susurha neutral "Do the prisoners trust their escape with the jailors?"
            susurha neutral "I've had my fair share of desperation, but this..."
            susurha neutral "You can do better."
            vivithinking "This is getting me nowhere."
            # JUMP TO: vivi neutral "I still need to try at least."

    vivi neutral "I still need to try at least."
    susurha neutral "I know how you feel."
    susurha neutral "Your choice is your own."
    susurha neutral "Take care, and see you later, Vivienne."


    # JUMP TO: Darius Susu'Rha intermission scene'
    jump bargaining_darius_susurha