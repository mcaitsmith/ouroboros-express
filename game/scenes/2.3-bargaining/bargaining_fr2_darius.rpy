# The scene starts here.

label bargaining_fr2_darius:

    #FREE ROAM 2 - Darius

    # LOCATION: diningcar
    scene diningcar with fade

    # SOUND: cooking, dining sounds
    play sound cooking
    pause 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    show darius neutral at right with dissolve

    darius neutral "Well? We're here. What is it you wanted?"
    vivi neutral "Okay, promise to hear me out?"

    stop sound fadeout 1.0

    # <CHOICE>
    darius neutral "Always."

    menu:
        # OPTION 1 +ATTRACTION
        "Could I interest you in dinner?":

            play sound attchoice
            $ att_meter_darius += int(att_max_bargaining_fr2 / att_num_list_darius[3])

            vivi neutral "Could I interest you in dinner?"
            show darius neutral blush with dissolve
            darius "Pardon me?"
            vivi neutral "I'm making a meal today for Urshu, and I thought this would be a great chance to work together."
            darius "Ah, I see. I'm not the greatest chef, but I suppose I can help you prepare what you need."
            vivi happy "Thank you, Darius!"
            show darius neutral -blush

            # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

        # OPTION 2 +DECAY
        "Can you help me with something for Urshu?":

            play sound decchoice
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "Can you help me with something for Urshu? He asked me to make dinner for the group and I'd appreciate the extra hands."
            darius neutral "Urshu asked you?"
            vivi neutral "Yeah, why do you ask?"
            darius neutral "Nothing it just seems...strange. Urshu has never asked us to do anything for him. Besides, he's a god."
            vivi neutral "Yeah, well, first time for everything I suppose!"
            vivithinking "I may have given him the idea, but Darius doesn't have to know that."

            # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

        # OPTION 3 >>DECAY +DECAY
        "You want out of this place?" if dec_meter > 20:

            play sound decchoice
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            vivi neutral "You want out of this place? I may have your ticket, if you just help me out."
            darius angry "No."
            vivi neutral "No, what?"
            darius neutral "No, I do not \"want out of this place\" because it isn't possible."
            vivi neutral "Yeah, that's what I thought too. But it turns out old Urshu's love language is favors. Who would've thought?"
            vivi neutral "He said if I could make a meal he could truly enjoy, then he'd send me back to my life, no strings attached."
            darius angry "And you took him at his word? Perhaps, I overestimated your intelligence."
            darius angry "Truly, Vivi, how long are you going to ignore the obvious? We are here for a reason. It's up to us to figure out what that is."
            vivi angry "Bullshit. If the god says he has a way out for me, I'll take his word over yours."
            darius neutral "Ugh. Very well. I'll help you, if only because it will give me some time to think."
            vivi neutral "Alright, okay. Great!"
            vivithinking "Well, I got what I wanted, right?"

            # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

    vivi neutral "So, my sous chef, what shall we prepare?"
    darius sad "I'm...not sure. I don't think typical illithid cuisine fits the palate of our guests."

    show vivi angry at left

    vivithinking "Right, they're a mindflayer. Why did I ask the guy whose people eat brains to make food with me?"
    darius neutral "Human cuisine is rather approachable, is it not? Do you have any ideas?"

    show vivi neutral blush at left

    vivithinking "Hmm? What do I think?"
    vivithinking "I could go all out, give these people something to really drool over. But maybe Urshu doesn't like that? Maybe something simple is better?"

    # <CHOICE>
    vivithinking "Then there's my specialty...but I haven't made that in a long time. Besides, do I really want to make something so personal for these...beings?"

    menu:
        # OPTION 1 +DECAY
        "Better not leave my comfort zone.":

            play sound decchoice
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)

            show vivi neutral at left
            vivithinking "Let's just make something simple. Urshu doesn't strike me as the extravagant type."
            vivi neutral "Let's make some chicken stir fry. I know a pretty easy recipe."
            darius neutral "Ah, seems simple enough. Let me prepare the meat."

            # JUMP TO: # SOUND: cooking

        # OPTION 2 +ATTRACTION
        "Screw it, let's go all out!":

            play sound attchoice
            $ att_meter_darius += int(att_max_bargaining_fr2 / att_num_list_darius[3])

            show vivi neutral at left

            vivithinking "Screw it, let's go all out! Really need to wow Urshu if I want my ticket out of here."
            vivi neutral "It's a bit of a challenging recipe, but I know a beef wellington that's sure to make his jaw drop."
            darius neutral "That's a rather sophisticated recipe. Do you have a culinary background, Vivi?" 
            vivi neutral "Not exactly. I just pick up a lot of things on this job. Everyone loves food, and they all have an opinion on it. It's pretty easy to get good recipes if you just ask."
            darius happy "Fascinating. You'll have to tell me more afterwards."
            vivi happy "Sure! I'd be happy to... Oh."

            show vivi sad at left
    
            vivithinking "I guess I wouldn't be able to if this plan goes through."
            vivithinking "What's this lump in my chest? The idea of leaving these people is having this much of an effect?"

            # JUMP TO: # SOUND: cooking

        # OPTION 3 >>ATTRACTION
        "Desperate times call for desperate measures." if att_meter_darius >= 40:

            show vivi neutral at left

            vivithinking "Desperate times call for desperate measures."
            vivi neutral blush "I have one recipe that I know is a hit. But...it's a bit personal."
            darius neutral "You don't have to show me if you don't want to."
            vivi neutral blush "No, I...I think I do."
            vivi neutral "My Nana is the one who first taught me to cook anything. A really simple dish, spaghetti and meatballs with a carbonara sauce."
            vivi happy blush "It was awful. I burnt half the beef, the pasta was soggy, and the sauce came out all lumpy. But Nana didn't care. She praised it like it was a five star meal."
            vivi happy blush "I made it for her every time I visited, and every time she made me feel like a master chef."
            vivi sad blush "Until... I couldn't visit anymore."
            vivi sad blush "When she died, that recipe went with her. Those were perfect memories, and I didn't want to associate it with anything else."
            darius neutral "And now you want to make that again."
            vivi neutral blush "Yes."
            show darius happy blush with dissolve
            darius "I think if anything were to truly impress Urshu, it would be something like that. Something with heart behind it, as you humans say."
            vivi neutral blush "I guess you're right. It's cheesy, but it does make a difference."
            show darius happy -blush
            darius happy "Indeed. Let me get the pasta."

            # JUMP TO: # SOUND: cooking

    # SOUND: cooking
    play sound cooking
    pause 3.0
    stop sound fadeout 1.0

    vivithinking neutral "Wow. Darius is really good with their hands."
    vivi neutral "You're rather dextrous, Mr. Wrecker."
    darius neutral "Part of the trade. Sleight of hand can be rather useful when trying to slip something past an unsuspecting fool."
    vivi happy "I'm sure they could be useful for...other things as well."
    show darius neutral blush with dissolve
    darius "Ms. Sanssouci, I have no idea what you could possibly be referring to."
    
    # <CHOICE>
    vivi happy blush "Oh, I'm sure."
    
    menu:
        # OPTION 1
        "(They're cute when they try to act clueless.)":
        
            vivithinking "They're cute when they try to act clueless."

            # JUMP TO # SOUND: glassware clinking (dining, clatter of silverware and plating)

        # OPTION 2
        "(Heh. They know.)":

            vivithinking "Heh. They know."

            # JUMP TO # SOUND: glassware clinking (dining, clatter of silverware and plating)

    # SOUND: glassware clinking (dining, clatter of silverware and plating)
    play sound glassclink
    pause 2.5
    stop sound fadeout 1.0

    vivi neutral "Well, that's about as good as it's going to get. What do you think?"
    show darius neutral -blush
    darius neutral "I'm no expert, but it looks appetizing to me."
    vivi sad "Really? That's all you can offer?"
    show darius neutral blush with dissolve
    darius "Erm, I mean wow! Such a brilliantly composed plate! Each ingredient implemented fantastically, contributing to something greater than the sum of its parts. Splendid."
    vivi neutral "Alright, cool your jets. You get any more worked up, and we might be able to serve you next."
    show darius neutral -blush
    darius neutral "Please. You couldn't handle all of me."
    vivi neutral blush "Oh? Are you so sure?"
    show darius neutral blush with dissolve
    darius "Not like that! I... Damn you."
    vivi happy blush "Haha, so flustered, Mr. Wrecker!"
    vivi neutral "..."
    vivi neutral "Actually, Darius, before we go..."
    show darius neutral -blush
    darius neutral "Yes?"
    vivi neutral "I should be honest with you... This dinner isn't as altruistic as I made it seem."
    vivi sad "The reason I'm cooking is because of a deal I made with Urshu. If I make him a fantastic meal, he'll get us off this train."
    vivi sad "Well, I mean... I...could get off this train."
    darius neutral "..."
    darius surprised "You...you..."
    darius sad "...I see."
    vivi neutral "I'm sorry! I--"
    darius sad "You don't need to say anything else."
    vivi neutral "Wait, Darius! You don't understand!"
    darius angry "What is there to not understand? You kept this a secret from me! I respected you enough to not read you, and this is how you repay me?" 
    vivi neutral "Darius! I--"
    darius angry "Did you ever stop to think about how the rest of us would feel?"
    darius sad "How I'd feel being trapped here...without you?"

    # ??ATTRACTION (and if not DECAY below)
    if att_meter_darius >= 50:
        vivi neutral blush "But I'm not getting off this train if you can't come with me!"
        vivi neutral blush "That's why I'm telling you this now."
        vivi sad "I'm sorry I kept this a secret from you. I wasn't thinking straight when I made the deal, and I...I just didn't want anyone to get hurt."
        vivi neutral blush "But now, all I know is that you... You guys really mean a lot to me."
        vivi neutral blush "And home won't be home if you're not a part of it in some way."
        darius neutral "...You know I would never ask you to do that, right?"
        vivi neutral "Yeah, but..."
        vivi neutral blush "It's something I want. I don't care about the consequences anymore."
        show darius neutral blush with dissolve
        darius "Vivi... I..."
        darius "Ahem. Well,"
        darius "I think that's...something I...also want."

        show vivi neutral blush at left

        vivithinking "What I wouldn't give for a hug..."
        vivithinking "When was the last time I hugged someone?"
        show darius neutral -blush
        darius neutral "...Let's focus on one thing at a time though. Urshu first."
        vivi neutral "Right."
    # END

    # ??DECAY (and if not ATTRACTION above)
    else:
        vivi sad "But Darius! I--"
        darius angry "I already told you! You don't need to say anything else."

        show vivi sad at left

        vivithinking "...Damn it. What have I done?" 
        vivithinking "I should've just kept my mouth shut."
        vivi sad "You're right."

    #END

    vivi neutral "...Let's go before the food gets cold."

    # JUMP TO: URSHU MEAL REVEAL
    jump bargaining_meal_reveal