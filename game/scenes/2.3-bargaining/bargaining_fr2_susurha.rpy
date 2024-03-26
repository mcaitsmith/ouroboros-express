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
    jump bargaining_meal_reveal