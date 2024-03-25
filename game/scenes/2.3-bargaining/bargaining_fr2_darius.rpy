# The scene starts here.

label bargaining_fr2_darius:

    #FREE ROAM 2 - Darius

    # LOCATION: diningcar
    scene diningcar with fade

    # SOUND: cooking, dining sounds

    show vivi neutral at left with dissolve

    show darius neutral at right with dissolve

    darius neutral "Well? We're here. What is it you wanted?"
    vivi neutral "Okay, promise to hear me out?"

    # <CHOICE>
    darius neutral "Always."

    menu:
        # OPTION 1 +ATTRACTION
        "Could I interest you in dinner?":

            vivi neutral "Could I interest you in dinner?"
            show darius neutral blush with dissolve
            darius "Pardon me?"
            vivi neutral "I'm making a meal for everyone today, and I thought this would be a great chance to work together."
            darius "Ah, I see. I'm not the greatest chef, but I suppose I can help you prepare what you need."
            vivi happy "Thank you, Darius!"
            show darius neutral -blush

            # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

        # OPTION 2 +DECAY
        "Can you help me with something for Urshu?":

            vivi neutral "Can you help me with something for Urshu? He asked me to make dinner for the group and I'd appreciate the extra hands."
            darius neutral "Urshu asked you?"
            vivi neutral "Yeah, why do you ask?"
            darius neutral "Nothing it just seems...strange. Urshu has never asked us to do anything for him. Besides, he's a god."
            vivi neutral "Yeah, well, first time for everything I suppose!"
            vivithinking "I may have given him the idea, but Darius doesn't have to know that."

            # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

        # OPTION 3 >>DECAY +DECAY
        "You want out of this place?":

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
    darius sad "I'm...not sure. I don't think typical mindflayer cuisine fits the palate of our guests."

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

            show vivi neutral at left
            vivithinking "Let's just make something simple. Urshu doesn't strike me as the extravagant type."
            vivi neutral "Let's make some chicken stir fry. I know a pretty easy recipe."
            darius neutral "Ah, seems simple enough. Let me prepare the meat."

            # JUMP TO: # SOUND: cooking

        # OPTION 2 +ATTRACTION
        "Screw it, let's go all out!":

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
        "Desperate times call for desperate measures.":

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
            darius "I think if anything were to truly wow Urshu, it would be something like that. Something with heart behind it, as you humans say."
            vivi neutral blush "I guess you're right. It's cheesy, but it does make a difference."
            show darius happy -blush
            darius happy "Indeed. Let me get the pasta."

            # JUMP TO: # SOUND: cooking

    # SOUND: cooking

    vivithinking neutral "Wow. Darius is really good with their hands."
    vivi neutral "You're rather dextrous, Mr. Wrecker."
    darius neutral "Part of the trade. Sleight of hand can be rather useful when trying to slip something past an unsuspecting fool."
    vivi happy "I'm sure they could be useful for...other things as well."
    show darius neutral blush with dissolve
    darius "Ms. Sanssouci, I have no idea what you could possibly be referring to."
    vivi happy blush "Oh, I'm sure."
    vivithinking "They're cute when they try to act clueless."

    # SOUND: glassware clinking (dining, clatter of silverware and plating)

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
    vivi happy blush "Hahahaha."
    vivi neutral "..."
    vivi neutral "Actually, Darius, before we go..."
    show darius neutral -blush
    darius neutral "Yes?"
    vivi neutral "You...know that if Urshu likes this food, we might be able to get off this train..."
    vivi sad "Well, I mean... I...could get off this train."
    darius neutral "..."
    darius surprised "You...you..."
    darius sad "...I see."
    vivi neutral "I'm sorry! I--"
    darius sad "You don't need to say anything else."
    vivi neutral "Wait, Darius! You don't understand!"
    darius angry "What is there to not understand? You kept this a secret from me! I respected you enough to not read you, and this is how you repay me?" 
    vivi neutral "Darius! I--"
    darius angry "Did you ever stop to think about whether or not I'd want to get off this train too?"
    darius sad "How I'd feel being trapped here...without you?"

    # ??ATTRACTION (and if not DECAY below)
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
    vivi sad "But Darius! I--"
    darius angry "I already told you! You don't need to say anything else."

    show vivi sad at left

    vivithinking "...Shit. What have I done?" 
    vivithinking "I should've just kept my mouth shut."
    vivi sad "You're right."

    #END

    vivi neutral "...Let's go before the food gets cold."

    # JUMP TO: URSHU MEAL REVEAL

    # URSHU MEAL REVEAL

    # # LOCATION: lounge 

    # show vivi neutral at right

    # # show [INSERT NPC] happy at left
    # #Sal's note: INSERT NPC means: The NPC chosen in Character Selector 2

    # vivithinking "Okay, this is it. Time to show Urshu what we got."  
    # vivithinking "But, hold on... None of this would've been possible without   
    # [INSERT NPC]'s help. I need to say something." 
    # vivi blush neutral "Hey. I just... I wanna say... I can't thank you enough."

    # # AVA ROUTE
    # ava happy "It is our honor and joy to be of aid, my radiant sun."
    # ava neutral "Now, hurry we must! Our creation is cooling!"
    # vivi neutral "Right. Urshu is waiting for us. Let's go."
    # # END AVA ROUTE

    # # DARIUS ROUTE
    # vivi neutral "You didn't have to do this, but you still did, and I just..."
    # vivi neutral "I really appreciate it."
    # darius neutral "You're welcome, Vivi. I'm glad I could help."
    # darius neutral "...Anyways."
    # vivi neutral "Yeah. We should go."
    # # END DARIUS ROUTE

    # # SUSU'RHA ROUTE
    # vivi neutral "You didn't have to do this, but you still did, and on such short notice too."
    # susurha neutral "It was my pleasure, Vivienne. Really, it was."
    # susurha neutral "Now, let's go show this conductor what world class meatloaf is made of!"
    # vivi neutral "Haha, yeah!"
    # # END SUSU'RHA ROUTE


    # # LOCATION: observatory

    # show vivi happy at center

    # show [INSERT NPC] happy at left

    # show urshu neutral at right

    # vivithinking neutral "Table, chairs, white linen, candles... Where did he get those?
    # vivithinking neutral "He looks so smug. A bit creepy. His hands steepled like a movie villain." 
    # vivithinking neutral "Nah, it's just the lighting. Ursh has such a flair for drama."
    # urshu happy "I am famished, dear ones. What have you prepared for me?"
    # vivi happy "Something to blow your mind and tastebuds!" 
    # vivi neutral "[INSERT NPC] and I made a meal that's gonna knock your god socks off!"
    # urshu happy "You two have worked together? Ah, what joyous collaboration! All the more to be excited about!" 
    # urshu neutral "Let's try a bite, shall we?"
    # vivithinking neutral "Alright, let's set this down. Careful... Okay. Nothing spilled." 
    # vivithinking neutral "God, I'm hovering. Step away, V. It smells {i}soooo good{/i}, though. Maybe he'll leave us a bite?" 
    # vivithinking neutral "Oh, shit, he's going for it!"

    # # <CHOICE>
    # "I need to hold on to something!"

    # menu:
    #     # OPTION 1 +ATTRACTION
    #     "Grab [INSERT NPC'S] Hand"

    #         vivithinking neutral "I need to hold on to something!"
    #         vivithinking neutral "But no, what if [INSERT NPC] doesn't want to?" 
    #         vivithinking neutral "Fuck it!"
    #         show [INSERT NPC] surprise blush at left
    #         vivithinking surprised "Oh, God. What am I doing? What are they thinking? Do they hate me?"

    #         # JUMP TO: vivithinking neutral "He's taking another bite!"    

    #     # OPTION 2
    #     "Grab the guard rail."
            
    #         vivithinking neutral "Oh, God. I'm lightheaded."
    #         vivithinking neutral "I can't believe this is happening. What if he hates it? What if he...?"

    #         # JUMP TO: vivithinking neutral "He's taking another bite!"    

    # vivithinking neutral "He's taking another bite! And another! He's...he's crying."
    # show urshu sad blush with dissolve
    # urshu "My, my. I have never... My mouth dances with joy! The texture, the temperature, the sensation of it all. You have truly gone A and B the C of D."
    # vivi and [INSERT NPC] surprised "What?"
    # show urshu happy -blush
    # urshu happy "You have gone above and beyond the call of duty."
    # vivi happy "That...that's amazing! Urshu, that's the best news we could have possibly heard!"
    # vivithinking neutral "Hell yeah! We are getting OUTTA HERE!"
    # urshu neutral "I am certain with every ounce of my being that this tastes absolutely wondrous."
    # vivi happy "Oh, my God Urshu! Thank you! Thank you! Thank you! I am so--"
    # vivi neutral "..."
    # vivi neutral "Wait, what do you mean by...certain?"
    # vivithinking neutral "Holy moly. He's crying again!
    # vivithinking neutral "Crying? No, sobbing." 
    # vivithinking neutral "That's not a happy cry. He's covering his mouth."
    # vivi neutral "Urshu, what's going on? Why are you crying?"
    # urshu sad "Miss Sanssoucci, my dear."
    # urshu sad "I underestimated you, as I so often do with humans."
    # vivi neutral "Ursh..."
    # urshu sad "I did not think you would complete the task at hand, let alone with a companion."
    # urshu sad "So I have led you into another ruse, I fear."
    # vivi neutral "...No."
    # urshu sad "I do not possess what you call "taste buds." I do not know what this actually tastes like."
    # vivi neutral "Nonononono."
    # urshu sad "And I therefore cannot call this the best tasting meal I have ever had."
    # vivi angry "YOU. DRINK. NARUBIAN. CITRUS. INFUSED. ESPRESSO. EVERY. FUCKING. MORNING. WHAT. DO. YOU. MEAN. YOU. DON'T. HAVE. TASTE. BUDS?"
    # # Sal's note !!!!: Here the chosen NPC talks. If this is effort, it's not worth the pain to implement. It's only one line.
    # [INSERT NPC] surprised "Vivienne..." 
    # urshu neutral "You don't understand! Coffee is different. Coffee is a metaphysical experience."
    # urshu neutral "The concept of coffee! Hypothetical productivity with a hint of idealism, mmm! That I can taste. Not the lowly physical aspect."
    # vivi angry "No! No! NO! I can't take any more of this. I'm done."
    # vivi sad "You know, I actually trusted you. You looked me in the eyes and shook my hand, and I trusted you."
    # urshu sad "Dear Vivienne, I did not mean to obscure the truth. I tried to tell you numerous times that I do not possess the power to take you off this train, yet you only hear what you want to hear."

    # #SOUND: Prime moment for sad music
    
    # urshu neutral "As my way of apologizing, let me elucidate for you something you cannot seem to accept..."
    # urshu neutral "While living, you received innumerable second chances to make things right in your own life."
    # urshu neutral "But the Ouroboros Express is not a second chance. It is your last chance to 
    # make peace with yourself and the other travelers with you."
    # urshu neutral "I told you that I am a conductor, nothing more. I am sorry for this ruse. It was wrong of me to play with your heart in such a careless manner." 
    # urshu neutral "But when you shook my hand, there was a certain hope in your soul, Miss Sanssouci, that I was too weak to crush at its onset." 
    # urshu neutral "Only now are you ready to accept the reality of—"
    # vivi sad "I can't hear another word. I can't—"

    # # fade out

    # vivithinking neutral "It's falling apart again. It's all..."

    # # JUMP TO: Debrief Bargaining


    # Debrief Bargaining

    # # LOCATION: cabin
    # # ATTRACTION ROUTE

    # show vivi sad at left

    # vivithinking sad "I should've known better than to think there was an {i}actual{/i} way 
    # out. What the hell was the point in even trying?"

    # vivithinking sad "I really shouldn't have shared my plan with anyone else. I didn't just get my hopes up. Now I've let down friends."
    # vivithinking happy "Never thought I'd call the folks on this train friends."
    # vivithinking sad "And I managed to fuck that up too. What's wrong with me?"

    # vivithinking neutral "I need to write."

    # # Journal entry with attraction meter high

    # If cooking for him didn't work, what would? I'm beginning to think that this is it. The end of the line. Everything I worked for... gone. Maybe [INSERT NPC] will join me at the bar. I definitely owe them a drink. Good a place as any to forget everything.


    # # DECAY ROUTE

    # show vivi angry at left

    # vivithinking angry "He knew. He knew from the very start and just led me along! Why give any of us hope?"
    # vivithinking sad "There is no hope. All of my time here was pointless."
    # vivithinking sad "I am pointless."
    # vivithinking neutral "I can't even recognize myself. I feel like I'm trying to swim to shore but the current keeps me from ever making it."
    # vivithinking surprised "This place is changing me. I'm withering away into     something dark and no amount of clawing back can save me."
    # vivithinking sad "I'm doomed."
    # vivithinking neutral "Maybe I should write out my thoughts."

    # # Journal entry with degradation meter high

    # Urshu...that stupid, cruel son of a... This is all hopeless! I can see changes in all of us. I don't feel fully human anymore. Those creatures outside the windows... Will we end like them? At least the bar is stocked. Tomorrow's plan is to drink the place dry. Hopefully, if I'm lucky, it'll piss the conductor off.
