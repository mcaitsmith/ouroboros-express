# The scene starts here.

label bargaining_meal_reveal:

    #URSHU MEAL REVEAL

    # LOCATION: lounge 
    scene lounge with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    # show [INSERT NPC] happy at left
    #Sal's note: INSERT NPC means: The NPC chosen in Character Selector 2
    if fr2_bargaining_choice == "Asha":
        call show_ava from _call_show_ava
    elif fr2_bargaining_choice == "Darius":
        call show_darius from _call_show_darius
    elif fr2_bargaining_choice == "Susu'Rha":
        call show_susurha from _call_show_susurha

    vivithinking "Okay, this is it. Time to show Urshu what we got."  
    vivithinking "But, hold on... None of this would've been possible without [fr2_bargaining_choice]'s help. I need to say something." 
    vivi neutral blush "Hey. I just... I wanna say... I can't thank you enough."

    if fr2_bargaining_choice == "Asha":
        call ava_route from _call_ava_route
    elif fr2_bargaining_choice == "Darius":
        call darius_route from _call_darius_route
    elif fr2_bargaining_choice == "Susu'Rha":
        call susurha_route from _call_susurha_route


    # LOCATION: observatory
    scene observatory with fade

    show vivi happy at center with dissolve

    #show [INSERT NPC] happy at left
    if fr2_bargaining_choice == "Asha":
        $ npc_meal = ava
        call show_ava from _call_show_ava_1
    elif fr2_bargaining_choice == "Darius":
        $ npc_meal = darius
        call show_darius from _call_show_darius_1
    elif fr2_bargaining_choice == "Susu'Rha":
        $ npc_meal = susurha
        call show_susurha from _call_show_susurha_1

    show urshu neutral at left with dissolve:
        xzoom -1.0

    vivithinking neutral "Table, chairs, white linen, candles... Where did he get those?"
    vivithinking neutral "He looks so smug. A bit creepy. His hands steepled like a movie villain." 
    vivithinking neutral "Nah, it's just the lighting. Ursh has such a flair for drama."
    urshu happy "I am famished, dear ones. What have you prepared for me?"
    vivi happy "Something to blow your mind and tastebuds!" 
    vivi neutral "[fr2_bargaining_choice] and I made a meal that's gonna knock your god socks off!"
    urshu happy "You two have worked together? Ah, what joyous collaboration! All the more to be excited about!" 
    urshu neutral "Let's try a bite, shall we?"
    vivithinking neutral "Alright, let's set this down. Careful... Okay. Nothing spilled." 
    vivithinking neutral "God, I'm hovering. Step away, V. It smells {i}soooo good{/i}, though. Maybe he'll leave us a bite?" 
    vivithinking neutral "Oh oh oh! He's going for it!"

    # <CHOICE>
    "I need to hold on to something!"

    menu:
        # OPTION 1 +ATTRACTION
        "Grab [fr2_bargaining_choice]'s Hand":

            vivithinking neutral "I need to hold on to something!"
            vivithinking neutral "But no, what if [fr2_bargaining_choice] doesn't want to?" 
            vivithinking neutral "Fuck it!"
            show vivi neutral blush with dissolve:
                xpos 0.5
                linear 0.5 xpos 0.7
            #show [INSERT NPC] surprise blush at left
            play sound attchoice
            if fr2_bargaining_choice == "Asha":
                $ att_meter_ava += int(att_max_bargaining_fr2 / att_num_list_ava[3])
                call show_ava_blush from _call_show_ava_blush
            elif fr2_bargaining_choice == "Darius":
                $ att_meter_darius += int(att_max_bargaining_fr2 / att_num_list_darius[3])
                call show_darius_blush from _call_show_darius_blush
            elif fr2_bargaining_choice == "Susu'Rha":
                $ att_meter_susurha += int(att_max_bargaining_fr2 / att_num_list_susurha[3])
                call show_susurha_blush from _call_show_susurha_blush
            vivithinking surprised "Oh, God. What am I doing? What are they thinking? Do they hate me?"

            # JUMP TO: vivithinking neutral "He's taking another bite!"    

        # OPTION 2
        "Grab the guard rail.":
            
            vivithinking neutral "Oh, God. I'm lightheaded."
            vivithinking neutral "I can't believe this is happening. What if he hates it? What if he...?"

            # JUMP TO: vivithinking neutral "He's taking another bite!"    

    vivithinking neutral "He's taking another bite! And another! He's...he's crying."
    show urshu sad blush with dissolve
    urshu "My, my. I have never... My mouth dances with joy! The texture, the temperature, the sensation of it all. You have truly gone A and B the C of D."
    if fr2_bargaining_choice == "Asha":
        call show_ava_surprised from _call_show_ava_surprised
    elif fr2_bargaining_choice == "Darius":
        call show_darius_surprised from _call_show_darius_surprised
    elif fr2_bargaining_choice == "Susu'Rha":
        call show_susurha_surprised from _call_show_susurha_surprised
    vivi surprised "What?"
    show urshu happy -blush
    urshu happy "You have gone above and beyond the call of duty."
    vivi happy "That...that's amazing! Urshu, that's the best news we could have possibly heard!"
    vivithinking neutral "Hell yeah! We are getting OUTTA HERE!"
    urshu neutral "I am certain with every ounce of my being that this tastes absolutely wondrous."
    vivi happy "Oh, my God Urshu! Thank you! Thank you! Thank you! I am so--"
    vivi neutral "..."
    vivi neutral "Wait, what do you mean by...certain?"
    vivithinking neutral "Holy moly. He's crying again!"
    vivithinking neutral "Crying? No, sobbing." 
    vivithinking neutral "That's not a happy cry. He's covering his mouth."
    vivi neutral "Urshu, what's going on? Why are you crying?"
    urshu sad "Miss Sanssoucci, my dear."

    # THE BELOW TEXT (UP UNTIL LINE 129 INCLUSIVE) ONLY APPEARS IF VIVI CHOSE TO HEAR/TELL 
    # ALL THREE STORIES WITH URSHU (SELECTED OPTION 1 "Go on, already. A story might lift 
    # my crow's feet." IN 2.1 DENIAL_BRIEFING + SELECTED OPTION 2 "Look, just tell me the 
    # story. If we have time." IN 2.2 ANGER_BRIEFING + SELECTED OPTION 1 "Urgh, ok. You win. 
    # What do you want to hear?" IN 2.3 BARGAINING BRIEFING). OTHERWISE, NEEDS TO JUMP TO 
    # urshu sad "I underestimated you, as I so often do with humans." BELOW

    if urshu_story_1 == True and urshu_story_2 == True and urshu_story_3 == True:

        urshu sad "Miss Sanssoucci, my dear."
        vivi neutral "You can just call me Vivi, Ursh."
        urshu surprised blush "I would like that, Miss Sa- I mean, my dear Vivi."
        urshu sad -blush "But I must confess..."

        # JUMP TO: urshu sad "I underestimated you, as I so often do with humans."
    
  
    urshu sad "I underestimated you, as I so often do with humans."
    vivi neutral "Ursh..."
    urshu sad "I did not think you would complete the task at hand, let alone with a companion."
    urshu sad "So I have led you into another ruse, I fear."
    vivi neutral "...No."
    urshu sad "I do not possess what you call \"taste buds.\" I do not know what this actually tastes like."
    vivi neutral "Nonononono."
    urshu sad "And I therefore cannot call this the best tasting meal I have ever had."
    vivi angry "YOU. DRINK. NARUBIAN. CITRUS. INFUSED. ESPRESSO. EVERY. FUCKING. MORNING. WHAT. DO. YOU. MEAN. YOU. DON'T. HAVE. TASTE. BUDS?"
    # Sal's note !!!!: Here the chosen NPC talks. If this is effort, it's not worth the pain to implement. It's only one line.
    npc_meal "Vivienne..." 
    urshu neutral "You don't understand! Coffee is different. Coffee is a metaphysical experience."
    urshu neutral "The concept of coffee! Hypothetical productivity with a hint of idealism, mmm! That I can taste. Not the lowly physical aspect."
    vivi angry "No! No! NO! I can't take any more of this. I'm done."

    # Carrie's note - VERSION 1: THE BELOW TEXT (UNTIL LINE 159 INCLUSIVE) ONLY APPEARS IF 
    # VIVI CHOSE TO HEAR ALL THREE OF URSHU'S STORIES (SELECTED OPTION 1 "Go on, already. 
    # A story might lift my crow's feet." IN 2.1 DENIAL_BRIEFING + SELECTED OPTION 2 
    # "Look, just tell me the story. If we have time." IN 2.2 ANGER_BRIEFING + SELECTED 
    # OPTION 1 "Urgh, ok. You win. What do you want to hear?" IN 2.3 BARGAINING BRIEFING). 
    # OTHERWISE, NEEDS TO JUMP TO # VERSION 2 BELOW 

    if urshu_story_1 == True and urshu_story_2 == True and urshu_story_3 == True:
    
        vivi sad "I cannot believe you, Urshu. That you did this. {i}You.{/i}" 
        vivi sad "You know, I actually trusted you, more than most. I don't have much time left, but I gave you plenty of it. I heard you out. I listened to you, and all your ferryman stuff."
        vivi sad "And I opened up to you. I haven't spoken to anyone - {i}anyone{/i} - like that in a long time. You looked me in the eye and said that we understood each other perfectly."
        vivi sad "I got to feel... I felt like we were..."
        urshu sad "My dear Vivi?"
        vivi sad "No. It doesn't matter. Because you clearly don't, and we're clearly not. I thought I was seeing my time here wisely, differently, like you said I should. But maybe I don't have the investigative chops I thought I did." 
        urshu sad "Dear Vivi, I did not mean to obscure the truth. I tried to tell you numerous times that I do not possess the power to take you off this train, yet you only hear what you want to hear."

        # JUMP TO: stop music fadeout 5.0
    
    # Carrie's note - VERSION 2: BASE GAME VERSION (NO URSHU ROMANCE PATH)
    else:
    
        vivi sad "You know, I actually trusted you. You looked me in the eyes and shook my hand, and I trusted you."
        urshu sad "Dear Vivienne, I did not mean to obscure the truth. I tried to tell you numerous times that I do not possess the power to take you off this train, yet you only hear what you want to hear."

    #SOUND: Prime moment for sad music
    stop music fadeout 5.0 # gonna stop the music here for effect
    
    urshu neutral "As my way of apologizing, let me elucidate for you something you cannot seem to accept..."
    urshu neutral "While living, you received innumerable second chances to make things right in your own life."
    urshu neutral "But the Ouroboros Express is not a second chance. It is your last chance to make peace with yourself and the other travelers with you."
    urshu neutral "I told you that I am a conductor, nothing more. I am sorry for this ruse. It was wrong of me to play with your heart in such a careless manner." 
    urshu neutral "But when you shook my hand, there was a certain hope in your soul, Miss Sanssouci, that I was too weak to crush at its onset." 
    urshu neutral "Only now are you ready to accept the reality of—-"
    vivi sad "I can't hear another word. I can't—-"

    # fade out
    scene black with fade

    vivithinking neutral "It's falling apart again. It's all..."

    # JUMP TO: Debrief Bargaining
    jump bargaining_debrief

    label show_ava:
        show ava happy at right with dissolve
        return
    label show_darius:
        show darius happy at right with dissolve
        return
    label show_susurha:
        show susurha happy at right with dissolve
        return

    label ava_route:
        ava happy "It is our honor and joy to be of aid, my radiant sun."
        ava neutral "Now, hurry we must! Our creation is cooling!"
        vivi neutral "Right. Urshu is waiting for us. Let's go."
        return
    label darius_route:
        vivi neutral "You didn't have to do this, but you still did, and I just..."
        vivi neutral "I really appreciate it."
        darius neutral "You're welcome, Vivi. I'm glad I could help."
        show darius neutral blush with dissolve
        darius "...Anyways."
        vivi neutral "Yeah. We should go."
        show darius neutral -blush
        return
    label susurha_route:
        vivi neutral "You didn't have to do this, but you still did, and on such short notice too."
        susurha neutral "It was my pleasure, Vivienne. Really, it was."
        susurha neutral "Now, let's go show this conductor what world class meatloaf is made of!"
        vivi neutral "Haha, yeah!"
        return

    label show_ava_blush:
        show ava surprised blush with dissolve
        return
    label show_darius_blush:
        show darius surprised blush with dissolve
        return
    label show_susurha_blush:
        show susurha surprised blush with dissolve
        return

    label show_ava_surprised:
        show ava surprised -blush
        return
    label show_darius_surprised:
        show darius surprised -blush
        return
    label show_susurha_surprised:
        show susurha surprised -blush
        return