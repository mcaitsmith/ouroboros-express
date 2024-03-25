# The scene starts here.

label bargaining_fr2_susurha:

    #FREE ROAM 2 - Susu'Rha

    # LOCATION: diningcar
    scene diningcar with fade

    show vivi neutral at left with dissolve

    show susurha neutral at right with dissolve

    vivi neutral "Thanks for coming on such short notice, Susu'rha. I really need your help."
    susurha neutral "Of course, Vivienne. What is it that you need?"
    vivi neutral "Okay, so... Listen to me."
    vivi neutral "I know how we're gonna get off this train."
    vivi neutral "I made a deal with Urshu, and if we make the best-tasting meal he's ever had, we can get outta here!"
    vivithinking "Well... I can get outta here. I'm not sure I specified more than one person getting off this train..."
    vivi neutral "All we gotta do is make a meal that knocks the sock suspenders off of Ursh!     What do you say? You in?"
    susurha neutral "..."
    susurha neutral "If you would have told me that the fate of my soul rested on my ability to cook..."
    susurha neutral "...I would have said, \"WHY DIDN'T YOU TELL ME SOONER?!\""
    vivi surprised "Sorry! I just made the deal today!"

    show vivi neutral at left

    vivithinking "Ah, man. Now they're pissed. What am I supposed to do now?"
    vivithinking "I wish my Nana was here."
    vivi neutral "..."
    susurha neutral "...Is something on your mind?"
    vivi neutral "Oh, I was thinking about my Grandmother. My mother's mother. She was from the far side of my world. An excellent chef. And an all-around brilliant human." 

    # <CHOICE>   
    susurha neutral "What made her so brilliant?"

    menu:
        #OPTION 1 +ATTRACTION
        "She could see down to the essence of a person.":

            vivi neutral "She could see down to the essence of a person."
            susurha neutral "I sense that power in you too, milady."
            vivi neutral "I guess I have it..."
            vivi neutral "...When my agenda doesn't get in the way."
            susurha neutral "Well, you're not alone in that. Where I'm from, everyone is power-mad, agenda-driven."
            susurha neutral "Which leads to war."
            vivi neutral "Yeah. It's like that where I'm from too."
            susurha neutral "Yet you're dying to go back there."
            vivi neutral "There are things I miss, I'm not gonna lie. And a lot of them are food-related."
            susurha neutral "Which reminds me..."

            # JUMP TO: susurha neutral "We have a meal to cook."

        #OPTION 2 +DECAY
        "Whatever it was, it skipped over me.":

            vivi neutral "Whatever it was, it skipped over me."
            susurha neutral "Whatever do you mean?"
            vivi neutral "Nana could read people. She could bargain. She had grit. Tenacity." 
            susurha neutral "Those are good qualities."
            vivi neutral "She lived a long life and everyone loved her."
            vivi neutral "Somehow I don't think she's ever set foot on this train."
            susurha neutral "Winding up on this train is evidence that you did something wrong?"
            vivi angry "It sure isn't evidence that I did something {i}right{/i}!"
            susurha neutral "Maybe we have a chance to turn it all around if we let the food speak for us. Keep your head up, Vivienne."
        
            # JUMP TO: susurha neutral "We have a meal to cook."


        #OPTION 3 >>ATTRACTION +ATTRACTION
        "She was a hustler. She knew how to get what she wanted.":

            vivi neutral "She was a hustler. She knew how to get what she wanted."
            susurha neutral "Well, you have that quality as well, Vivienne. It's why you're such an excellent reporter!"
            vivi blush neutral "Oh. Thank you! No one's ever said that to me before..."
            vivi neutral "I guess I do have a little \"girlboss\" energy in me..."
            susurha happy "Indeed you do! Now, let's use that to get us off this train!"
            vivi neutral "You're right..."
            vivi neutral "If we work together, maybe we can pull this thing off."
            show susurha neutral blush with dissolve
            susurha "I dare say, working in close quarters with you, I hope I don't get too distracted...by your \"girlboss\" energy."
            vivi surprised blush "Susu'rha, I'm not sure that's the complement you think it is..."
            susurha "No, sorry! What I meant to say was... Well, I just think... I think you're quite... radiant. I mean that. Earnestly."
            vivithinking "No one's ever said anything so nice to me in my entire life...I...I'm not falling in love, am I? No! No, that's silly. I just love being called radiant. Yeah! That's all... Right?"
            vivi neutral "Ahem. Well, thank you..."
            show susurha neutral -blush
            susurha neutral "Apologies. I'm the one who's being distracting."

            #JUMP TO: susurha neutral "We have a meal to cook."
        
    susurha neutral "We have a meal to cook."
    vivi neutral "Really? You'll do it?"
    susurha neutral "Sure, why not! I have nothing on my agenda."
    susurha neutral "And as for getting off of this racing death express, it's better to try and fail than never to try at all."

    # <CHOICE>
    susurha neutral "So what should we cook?"
    # DECAY ROUTE

    vivi neutral "I can't...seem to make up my mind...."
    vivithinking "What's outside the window?"
    vivithinking "Wow. Look at those cosmic spirals, twisting violently like tornados."

    hide susurha with pixellate

    vivithinking "Drawing me in..."
    vivithinking "Like someone is calling me."
    vivithinking "Oh crap! I...I can't breathe."

    # EFFECT: Distort screen
    show diningcar blur with pixellate

    show vivi surprised at left with dissolve

    vivithinking "It's the thing. The damn monster in the silver dress."
    vivithinking "How can it be so big? I can't take my eyes off it"
    vivithinking "It doesn't have eyes. Why do I feel it's staring at me?"
    vivithinking "Why is there no body inside that dress?"
    vivithinking "Why is it so empty?"
    vivithinking "Why is it stealing all the light—and reflecting it everywhere?"
    vivithinking "I don't get it!"

    show diningcar with dissolve

    show susurha neutral at right with dissolve

    susurha neutral "Vivi! Vivienne! Collect yourself!"
    vivi neutral "Sorry! Sorry. I don't know what that was..."
    susurha neutral "You looked like a ghost for a moment! You are sure you wish to go through with this?"

    # JUMP TO: vivi happy "Yeah! Let's make some magic happen." 

    menu:
        # OPTION 1 +DECAY
        "Let's try to appeal to Urshu's taste.":
        
            vivi neutral "Let's try to appeal to Urshu's taste."
            susurha neutral "We would only be guessing."
            vivi neutral "Let's guess then."
            vivi neutral "If I were that penguin-dressed, double-talking astral weirdo, I'd eat... Meatloaf."
            susurha neutral "Which is?"
            vivi neutral "A loaf. Of meat."
            vivi neutral "Thickened with breadcrumbs."
            susurha surprised "That sounds like prison food."
            vivi neutral "Do you have a better idea?" 
            susurha neutral "Ughhhh. Could we at least top it with a glaze? Or add some nice caramelized onions?"
            vivi happy "Ooh... You know I'm a sucker for carmelized onions! Sure!"
            susurha neutral "Alright then."
            susurha neutral "Shall we begin?"

            # JUMP TO: vivi happy "Yeah! Let's make some magic happen." 

        # OPTION 2 +ATTRACTION
        "We'll just try to cook the best dish we possibly can!":
        
            vivi neutral "We'll just try to cook the best dish we possibly can!"    
            susurha neutral "Unluckily for you, I eat nothing but grubs and Burrowers."
            vivi angry "Susu'rha..."
            susurha neutral "I'm joking, of course! I grew up crafting my own cuisine from the family larder."
            vivi neutral "Oh, great! I too, am a bit of a master chef."
            vivithinking "AKA, I fall asleep watching \"{i}Diners, Drive-Ins and Dives.{/i}\""
            susurha happy "Well, then. Sounds like I have some friendly competition!"
            vivi happy blush "Sounds like you sure do."
            susurha happy "We'll have to taste each other's creations then to see who comes out on top." 
            vivi surprised blush "We...sure will!"
            vivithinking blush "...EEEEEEEEE."
            show susurha neutral blush with dissolve
            susurha "Ahem... Right... Anyways."
            susurha "Shall we begin?"
            show susurha neutral -blush
        
            # JUMP TO: vivi happy "Yeah! Let's make some magic happen." 

        # OPTION 3 >>ATTRACTION +ATTRACTION
        "I don't know. I'll let my Nana's spirit guide me.":
        
            vivi neutral "I don't know. I'll let my Nana's spirit guide me."
            susurha neutral "The spirit of your ancestors... Yes! Great idea!"
            susurha sad "It's...really wonderful that you try to connect with your family in times of hardship." 
            susurha sad "Even now, as I plunge towards imminent death, I still run from mine." 
            vivi sad "Oh... Susu'rha..."
            vivi sad "Look... I don't wanna tell you the same old cliche of \"You can't blame yourself\" for what happened to your family because, in a way...I did the same thing as you." 
            susurha neutral "What do you mean? You're actions resulted in the death of your loved ones?!"
            vivi neutral "Well, okay. Let me clarify. Where I'm from, running away doesn't necessarily mean physically running away. It can mean a lot of things, like burrowing yourself in some much work you don't face, just...how terrifying it all is..."
            vivi sad "I think by working so much on this reporting gig that I never saw my family did...kill the bond between us in a way..."
            vivi neutral "Anyways. What I'm trying to say is... Both of us ran from what we thought would hurt us, which is natural... I think."
            vivi angry "And we both regret it. We {i}reallllyyyy{/i} fucking regret it, and we would do anything to take it back."
            vivi neutral "But we can't. Well... Not yet at least." 
            vivi neutral "All we can do is take the next best step to make it right."
            vivi neutral "Which means getting the hell out of here!"
            susurha neutral "...You're right. The hole in my heart... {i}Our{/i}...hearts..."

            show vivi surprised blush at left

            vivithinking "EEEEEEP!" 
            susurha angry "Still burn with rage." 
            susurha neutral "But the first step towards quelling that rage is leaving this iniquitous purgatory and going home."
            susurha neutral "Which means..."
            vivi happy "It's time to start cookin', good lookin'!"

            show vivi surprised blush at left

            vivithinking "VIVIENNE SANSSOUCI, YOU GODDESS OF CRINGE!"
            susurha happy "Oh, you humans and your sense of humor."
            susurha happy "Anyways. Shall we begin then?"

            # JUMP TO: "Yeah! Let's make some magic happen." 

    vivi happy "Yeah! Let's make some magic happen."

    show vivi neutral at left

    vivithinking "Alright. Let's see what we got here..."
    vivithinking "Spices, check. Wow, the beef is quite succulent for...wherever we are. I wonder if they have cows here. Ghost cows." 

    # SOUND: kitchen noises, cooking noises

    vivithinking "That's...wonky. But edible!"
    vivi neutral "And voila!"
    vivi neutral "Okay, Susu'Rha, try a bite! What do you think?"
    show susurha happy blush with dissolve
    susurha "It's, uh...exquisite!"
    vivi angry "Really? Good enough to get us off this train?"
    show susurha neutral -blush
    susurha neutral "...Well."
    show susurha neutral blush with dissolve
    susurha "I don't want to hurt your feelings..."   
    show susurha neutral -blush
    susurha neutral "And I can't put my claw on it, but..."

    # <CHOICE>
    susurha neutral "It needs... something."

    # DECAY ROUTE

    vivi angry "Well, if you don't know what it is, keep your opinion to yourself!"
    susurha neutral "If you'd just let me help you--"
    vivi angry "I've got this under control!"
    susurha angry "Enough with the rude commentary!"
    susurha angry "You act as though you WISH to displease Urshu!"
    susurha angry "Don't you even want to go home?"

    show vivi neutral at left

    vivithinking "Maybe I don't."
    vivithinking "Maybe I know it's all pointless."
    vivi neutral "Let's just get this over with, then."
    vivi neutral "I'm too tired to care."
    susurha neutral "Are you sure you don't--"

    # JUMP TO: vivi neutral "Let's serve this up!"

    menu:
        # OPTION 1 +ATTRACTION
        "It needs more spice.":

            susurha neutral "It needs more spice."
            vivi neutral "Okay...I can work with that!"
            vivi neutral "Nana would want things spicy."
            vivi neutral "I'll add...more cardamom."
            vivi neutral "More cinnamon."
            vivi neutral "More cumin."
            vivi happy "More everything!"
            vivi happy "More! More! More! More!"
            susurha neutral "I admire how you do that."
            vivi neutral "What?"
            susurha neutral "Inject life into everything you do. Even..."
            vivi neutral "...Beyond death?"
            susurha neutral "I didn't want to say it, but... Yes." 
            vivi neutral blush "Well...it's easy to do when you've got someone with you who...makes life worth living..."
            show susurha neutral blush with dissolve
            susurha "The feeling is mutual...Vivi."
            vivithinking "God, I'm as red as a beet. Shoulda put {i}me{/i} in the meal!"
            show susurha neutral -blush
            susurha neutral "Ahem, well. We should go, before our creation cools!"
            vivi neutral "Yeah, totally!"

            # JUMP TO: vivi neutral "Let's serve this up!" 

        #OPTION 2 +DECAY
        "I think it's fine the way it is.":
        
            vivi neutral "I think it's fine the way it is."
            susurha neutral "There's no part of you that believes that."
            vivi neutral "So what. We're being scammed anyway."
            susurha neutral "\"So what?\" Vivi!"
            susurha neutral "If you truly don't believe our food can win over the conductor, then why are we even cooking in the first place?"
            vivithinking "Hmmm. He's got a good point..."

            show vivi angry at left

            vivithinking "Gah! I hate being wrong."
            vivi neutral "Fine, whatever."
        
            # JUMP TO: vivi neutral "Let's serve this up!" 

        #OPTION 3 >>DECAY +DECAY
        "Something?!":
        
            vivi angry "Something?!"
            vivi angry "We get ONE SHOT to impress Urshu or we're stuck on this train forever, and you the only thing you can think of is that's it's missing \"something?!\""
            vivi angry "You know what? Forget it. The food is all yours, lizard brain! And you can add all the unspecific \"somethings\" your little reptilian heart desires!"
            susurha surprised "Vivienne, enough!"
            susurha neutral "I'm trying to help you, but it should be a collaboration."
            vivi sad "What's the use? I tried my best, and I failed! What more do you want from me?"
            susurha angry "Maybe for you not to give up so easily, seeing as my fate is tied to yours!"
            vivi angry "I DIDN'T EVEN TELL URSHU ABOUT YOU! THE BARGAIN WAS FOR ME AND ME ONLY!"
            susurha surprised "..."
            vivi surprised "..."
            susurha neutral "The \"something\" missing..."
            susurha sad "It needs...love."
            vivi angry "...That's a tall order right now."
            susurha neutral "I can see that."
            vivi neutral "..."
            vivi neutral "Whatever." 

            # JUMP TO: vivi neutral "Let's serve this up!" 
        
    vivi neutral "Let's serve this up!"

    # JUMP TO: URSHU MEAL REVEAL

    # FREE ROAM 2 - Darius

    # # LOCATION: diningcar

    # # SOUND: cooking, dining sounds

    # show vivi neutral at left

    # show darius neutral at right

    # darius neutral "Well? We're here. What is it you wanted?"
    # vivi neutral "Okay, promise to hear me out?"

    # # <CHOICE>
    # darius neutral "Always."

    # menu:
    #     # OPTION 1 +ATTRACTION
    #     "Could I interest you in dinner?":

    #         vivi neutral "Could I interest you in dinner?"
    # show darius neutral blush with dissolve
    #         darius "Pardon me?"
    #         vivi neutral "I'm making a meal for everyone today, and I thought this would be a great chance to work together."
    #         darius "Ah, I see. I'm not the greatest chef, but I suppose I can help you prepare what you need."
    #         vivi happy "Thank you, Darius!"
    # show darius neutral -blush

    #         # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

    #     # OPTION 2 + DECAY
    #     "Can you help me with something for Urshu?":

    #         vivi neutral "Can you help me with something for Urshu? He asked me to make dinner for the group and I'd appreciate the extra hands."
    #         darius neutral "Urshu asked you?"
    #         vivi neutral "Yeah, why do you ask?"
    #         darius neutral "Nothing it just seems...strange. Urshu has never asked us to do anything for him. Besides, he's a god."
    #         vivi neutral "Yeah, well, first time for everything I suppose!"
    #         vivithinking "I may have given him the idea, but Darius doesn't have to know that."

    #         # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

    #     # OPTION 3 >>DECAY +DECAY
    #     "You want out of this place?"

    #         vivi neutral "You want out of this place? I may have your ticket, if you just help me out."
    #         darius angry "No."
    #         vivi neutral "No, what?"
    #         darius neutral "No, I do not "want out of this place" because it isn't possible."
    #         vivi neutral "Yeah, that's what I thought too. But it turns out old Urshu's love language is favors. Who would've thought?"
    #         vivi neutral "He said if I could make a meal he could truly enjoy, then he'd send me back to my life, no strings attached."
    #         darius angry "And you took him at his word? Perhaps, I overestimated your intelligence."
    #         darius angry "Truly, Vivi, how long are you going to ignore the obvious? We are here for a reason. It's up to us to figure out what that is."
    #         vivi angry "Bullshit. If the god says he has a way out for me, I'll take his word over yours."
    #         darius neutral "Ugh. Very well. I'll help you, if only because it will give me some time to think."
    #         vivi neutral "Alright, okay. Great!"
    #         vivithinking "Well, I got what I wanted, right?"

    #     # JUMP TO: vivi neutral "So, my sous chef, what shall we prepare?"

    # vivi neutral "So, my sous chef, what shall we prepare?"
    # darius sad "I'm...not sure. I don't think typical mindflayer cuisine fits the palate of our guests."

    # show vivi angry at left

    # vivithinking "Right, they're a mindflayer. Why did I ask the guy whose people eat brains to make food with me?"
    # darius neutral "Human cuisine is rather approachable, is it not? Do you have any ideas?"

    # show vivi neutral blush at left

    # vivithinking "Hmm? What do I think?"
    # vivithinking "I could go all out, give these people something to really drool over. But maybe Urshu doesn't like that? Maybe something simple is better?"

    # # <CHOICE>
    # vivithinking "Then there's my specialty...but I haven't made that in a long time. Besides, do I really want to make something so personal for these...beings?"

    # menu:
    #     # OPTION 1 +DECAY
    #     "Better not leave my comfort zone.":

    #         show vivi neutral at left
    #         vivithinking "Let's just make something simple. Urshu doesn't strike me as the extravagant type. "
    #         vivi neutral "Let's make some chicken stir fry. I know a pretty easy recipe."
    #         darius neutral "Ah, seems simple enough. Let me prepare the meat."

    #         # JUMP TO: # SOUND: cooking

    #     # OPTION 2 +ATTRACTION
    #     "Screw it, let's go all out!":

    #         show vivi neutral at left

    #         vivithinking "Screw it, let's go all out! Really need to wow Urshu if I want my ticket out of here."
    #         vivi neutral "It's a bit of a challenging recipe, but I know a beef wellington that's sure to make his jaw drop."
    #         darius neutral "That's a rather sophisticated recipe. Do you have a culinary background, Vivi?" 
    #         vivi neutral "Not exactly. I just pick up a lot of things on this job. Everyone loves food, and they all have an opinion on it. It's pretty easy to get good recipes if you just ask."
    #         darius happy "Fascinating. You'll have to tell me more afterwards."
    #         vivi happy "Sure! I'd be happy to... Oh."

    #         show vivi sad at left
    
    #         vivithinking "I guess I wouldn't be able to if this plan goes through."
    #         vivithinking "What's this lump in my chest? The idea of leaving these people is having this much of an effect?"

    #         # JUMP TO: # SOUND: cooking

    #     # OPTION 3 >>ATTRACTION
    #     "Desperate times call for desperate measures.":

    #         show vivi neutral at left

    #         vivithinking "Desperate times call for desperate measures."
    #         vivi neutral blush "I have one recipe that I know is a hit. But...it's a bit personal."
    #         darius neutral "You don't have to show me if you don't want to."
    #         vivi neutral blush "No, I...I think I do."
    #         vivi neutral "My Nana is the one who first taught me to cook anything. A really simple dish, spaghetti and meatballs with a carbonara sauce."
    #         vivi happy blush "It was awful. I burnt half the beef, the pasta was soggy, and the sauce came out all lumpy. But Nana didn't care. She praised it like it was a five star meal."
    #         vivi happy blush "I made it for her every time I visited, and every time she made me feel like a master chef."
    #         vivi sad blush "Until... I couldn't visit anymore."
    #         vivi sad blush "When she died, that recipe went with her. Those were perfect memories, and I didn't want to associate it with anything else."
    #         darius neutral "And now you want to make that again."
    #         vivi neutral blush "Yes."
    # show darius happy blush with dissolve
    #         darius "I think if anything were to truly wow Urshu, it would be something like that. Something with heart behind it, as you humans say."
    #         vivi neutral blush "I guess you're right. It's cheesy, but it does make a difference."
    # show darius happy -blush
    #         darius happy "Indeed. Let me get the pasta."

    #         # JUMP TO: # SOUND: cooking

    # # SOUND: cooking

    # vivithinking neutral "Wow. Darius is really good with their hands."
    # vivi neutral "You're rather dextrous, Mr. Wrecker."
    # darius neutral "Part of the trade. Sleight of hand can be rather useful when trying to slip     something past an unsuspecting fool."
    # vivi happy "I'm sure they could be useful for...other things as well."
    # show darius neutral blush with dissolve
    # darius "Ms. Sanssouci, I have no idea what you could possibly be referring to."
    # vivi happy blush "Oh, I'm sure."
    # vivithinking "They're cute when they try to act clueless."

    # # SOUND: glassware clinking (dining, clatter of silverware and plating)

    # vivi neutral "Well, that's about as good as it's going to get. What do you think?"
    # show darius neutral -blush
    # darius neutral "I'm no expert, but it looks appetizing to me."
    # vivi sad "Really? That's all you can offer?"
    # show darius neutral blush with dissolve
    # darius "Erm, I mean wow! Such a brilliantly composed plate! Each ingredient     implemented fantastically, contributing to something greater than the sum of its parts. Splendid."
    # vivi neutral "Alright, cool your jets. You get any more worked up, and we might be able to serve you next."
    # show darius neutral -blush
    # darius neutral "Please. You couldn't handle all of me."
    # vivi neutral blush "Oh? Are you so sure?"
    # show darius neutral blush with dissolve
    # darius "Not like that! I... Damn you."
    # vivi happy blush "Hahahaha."
    # vivi neutral "..."
    # vivi neutral "Actually, Darius, before we go..."
    # show darius neutral -blush
    # darius neutral "Yes?"
    # vivi neutral "You...know that if Urshu likes this food, we might be able to get off this train..."
    # vivi sad "Well, I mean... I...could get off this train."
    # darius neutral "..."
    # darius surprised "You...you..."
    # darius sad "...I see."
    # vivi neutral "I'm sorry! I--"
    # darius sad "You don't need to say anything else."
    # vivi neutral "Wait, Darius! You don't understand!"
    # darius angry "What is there to not understand? You kept this a secret from me! I respected you enough to not read you, and this is how you repay me?" 
    # vivi neutral "Darius! I--"
    # darius angry "Did you ever stop to think about whether or not I'd want to get off this train too?"
    # darius sad "How I'd feel being trapped here...without you?"


    # # ??ATTRACTION
    # vivi neutral blush "But I'm not getting off this train if you can't come with me!"
    # vivi neutral blush "That's why I'm telling you this now."
    # vivi sad "I'm sorry I kept this a secret from you. I wasn't thinking straight when I made the deal, and I...I just didn't want anyone to get hurt."
    # vivi neutral blush "But now, all I know is that you... You guys really mean a lot to me."
    # vivi neutral blush "And home won't be home if you're not a part of it in some way."
    # darius neutral "...You know I would never ask you to do that, right?"
    # vivi neutral "Yeah, but..."
    # vivi neutral blush "It's something I want. I don't care about the consequences anymore."
    # show darius neutral blush with dissolve
    # darius "Vivi... I..."
    # darius "Ahem. Well,"
    # darius "I think that's...something I...also want."

    # show vivi neutral blush at left

    # vivithinking "What I wouldn't give for a hug..."
    # vivithinking "When was the last time I hugged someone?"
    # show darius neutral -blush
    # darius neutral "...Let's focus on one thing at a time though. Urshu first."
    # vivi neutral "Right."

    # # END

    # # ??DECAY (IF BAR IS LOW)
    # vivi sad "But Darius! I--"
    # darius angry "I already told you! You don't need to say anything else."

    # show vivi sad at left

    # vivithinking "...Shit. What have I done?" 
    # vivithinking "I should've just kept my mouth shut."
    # vivi sad "You're right."

    # #END

    # vivi neutral "...Let's go before the food gets cold."


    # # JUMP TO: URSHU MEAL REVEAL
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
