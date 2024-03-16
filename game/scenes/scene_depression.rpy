### EXAMPLE OF TEMPLATE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene_depression:

    #Briefing Depression

    #LOCATION: cabin
    scene cabin

    show vivi sad at left

    vivithinking "I'm...awake."
    "Alive."
    "Dying. But still goddamn alive."
    "I'm just a shell."
    "Empty, breaking."
    "I'm nothing."
    "Or..I will be soon."
    "Please, make it soon."

    # SOUND: knocking
    
    vivi "Go away."

    # SOUND: knocking

    # <CHOICE>
    vivithinking "Can I bring myself to talk to anyone?"

    menu:

        # <OPTION>
        "I guess so...":

            vivithinking "I guess so..."
            vivi "God, who is it?"
            urshu "Your worst enemy, I imagine."
            vivi angry "You...you fucker! You've done enough! Leave me here to die."
            urshu neutral "That will occur whether or not I deliver this breakfast to you or not."
            # JUMP TO: vivi angry "I don't care. Do what you want, like always. Little cretin."

        # <OPTION>
        "No. Let them knock till their knuckles bleed. Especially if it's Urshu.":

            vivithinking "No. Let them knock till their knuckles bleed. Especially if it's Urshu."
            urshu neutral "Miss Sanssouci, you will only die faster without a delicious breakfast."
            vivithinking angry "Oh, no. He doesn't get to bring me breakfast!"
            urshu "On second thought, you are dying anyway. Might as well let me in."
            # JUMP TO: vivi angry "I don't care. Do what you want, like always. Little cretin."

    vivi angry "I don't care. Do what you want, like always. Little cretin."

    show urshu neutral at right

    vivi "Know what? After seeing your smug face, I change my mind. Would you kindly jump off this train?"
    urshu "Espresso. Fresh croissant. Passionfruit juice. Warm congee with crispy garlic and cosmic ocean-caught catfish."
    vivithinking sad "Why does this feel like a gut punch?"
    urshu sad "This is the last meal you ate as a mortal. You might not recall it, but I do. I remember your whole life. All your lives; those who came before and those yet to jump aboard."
    "It is written on my heart and remains my burden: to remember everyone who travels with me."
    vivithinking "I can't face this. Whatever Ursh is doing...it hurts worse now."
    "When will it stop hurting?"
    "Why can't I just disappear?"
    urshu sad "Oh...don't turn away from me. I will not hurt you, my diamond."
    vivi angry "Don't call me that. Not anymore."
    urshu "Yes, of course, Miss Sanssouci."
    vivi "You don't deserve anything from me. Not my attention, nor my dwindling time!"
    urshu sad "..."
    vivi sad "We had a deal..."
    urshu sad "..."
    vivi sad "You made me think we did, anyway. Gave me hope. Then pulled the trapdoor from under me. No warning. I served you the food, then there was nothing beneath my feet."
    vivithinking "Now I'm falling and falling and I can't stop."
    urshu neutral "Miss Sanssouci..."
    vivi angry "Liar! Son of a bitch! Traitor! Crawl back to your hole you worm!"
    urshu sad "..."
    vivi sad "I...want to live."
    urshu neutral "I wish you could."
    vivi "I want to--God. There's no words for it."
    urshu "I understand. I wish to help you understand something about our locomotive existence."
    vivithinking "If this turns into another trite anecdote..."
    urshu "I have been on this journey countless times, will be on it for an eternity still. This is what I do. It is what I am."
    vivi angry "A torturer in a sharp suit who could bounce silver dollars off his ass?"
    urshu blush neutral "Well...how flattering."
    urshu neutral "I am a torturer, yes. A marauder of poor souls. The only currency I accept is the pleasure of conversation and high-stakes romantic drama. It is all I have here."
    vivi neutral "So what? You're immortal. That can't be your excuse to manipulate us."
    vivithinking "If he's keen on being honest..."
    "I can get him to admit more!"
    vivi neutral "And what about you and me? We had a moment yesterday. An incredible one, over some goddamn espresso."
    urshu "Yes..."
    vivi neutral "And the food I made you?"
    urshu sad "It was divine!"
    vivi neutral "And we've had weird, wonderful sparring matches!"
    urshu neutral "Yes! A thousand times, yes!"
    vivi angry "Then why did you fucking lie to me?"
    "Now, I have no hope."
    "I have nothing."
    "Can't you just...finish me off?" 
    vivithinking "I don't even have the juice for innuendo..."
    urshu angry "No! No, Miss Sanssouci. You have more to do and live for."
    urshu neutral "Moreso, it is not true that you have nothing. You have time, still. And it is not time to lie here, falling into yourself."
    "It is time to embrace the void with others."
    vivi neutral "That is the worst advice to give to someone in my state."
    urshu neutral "I urge you to embrace, not death, but the fleeting moments before. When nothing holds you back. When it does not matter that there is no tomorrow, because you have the present, and it is wholly yours."
    vivi angry "Shut up. I won't take this fluffy language. Make it make sense or leave."
    urshu angry "Don't you fucking get it? This is all on purpose and you only have so much time! You have to complete--"
    vivithinking "He just used a contraction. And said 'fucking'? What the hell?"
    vivi neutral "Complete what?" 
    urshu neutral blush "Nothing. I apologize, Miss Sanssouci, for losing my composure."
    urshu sad "And I am terribly sorry for lying to you."
    urshu neutral "I care for you. Please, give yourself a little more time. Just, be free with it."
    hide urshu
    vivithinking "God damn it, Urshu! Just when I got under your skin."
    "The breakfast, the honesty, the breakdown...I can't stay here. I need to get out of myself."

    # JUMP TO: character selector 1

    #Character Selector 1

    #LOCATION: cabin
    scene cabin

    show vivi neutral at left

    vivi angry "I really wish Urshu would get off my back. I don't need this."

    vivi sad "I am sick of running around chasing my tail with no end in sight. It's exhausting."

    #<CHOICE>
    vivi neutral "I'm gonna go get a drink. I'm sure I'm not the only one who'd want one."

    menu:

    #OPTION 1
        "Avatar of Asha":

            vivi neutral "Can a goddess get drunk? Let's find out."
            # JUMP TO: Free roam 1 / Avatar of Asha
            jump d_fr1_ava

    #OPTION 2
        "Inquisitor Darius Wrecker":

            vivi neutral "I wonder what Darius is like when they're drunk."
            #JUMP TO: Free roam 1 / Darius Wrecker
            jump d_fr1_darius

    #OPTION 3
        "Susu'Rha Balrinn":

            vivi neutral "Susu'Rha might like to get drunk with me."
            # JUMP TO: Free roam 1 / Susu'Rha Balrinn
            jump d_fr1_susurha

    label d_fr1_ava:
        #FREE ROAM 1 - Ava

        #LOCATION: Lounge
        scene lounge

        # SOUND: train

        show ava neutral at left
        show urshu neutral at center
        show vivi neutral at left

        "(if decay)"# ??DECAY
        ava neutral "Perhaps you would like a drink at the bar alone? We would."
        # END

        "(if attraction)"#??ATTRACTION
        ava happy "We could sit with you in the sunlight and silence and be content."
        # END

        vivithinking "She's a tall drink of fizzy water!"

        vivi "Hi! I see you're already ahead of me."
        ava "Hello, vivi. We are drinking...?"
        urshu "Tequila Sunrise."
        "(if attraction)"# ??ATTRACTION
        ava happy blush " Ah. Sunrise. Lovely, like you, vivi."
        vivithinking "Er, um...flirt alert!! Try not to be painfully awkward."
        # END
        urshu happy "Your cocktail, vivi. Aroma of marshmallows and Haribos? Ta ta, you two."
        vivithinking "Shoulda figured he'd know my drink, cagey bastard!"
        # SHOW urshu leaves
        hide urshu

        # <CHOICE>
        vivi neutral "So how about we..."
        "(decay route)"# DECAY ROUTE
        ava sad "We misspoke. We wish to drink alone."
        # JUMP TO: vivi saying "Well then, see ya, sunshine."

        menu: 
        # OPTION 1 +DECAY
            "...play a game?":
        
                vivi neutral "...play a game?"
                ava "We will be no more tomorrow and you want to play games."
                vivi "Might help. That and another swig."
                # JUMP TO: vivi saying "It's called Never Have I Ever."

            # OPTION 2 +ATTRACTION +DECAY
            "...drink our feelings away?":

                vivi neutral "...drink our feelings away?"
                ava "We accept. Our feelings weigh heavily on us."
                vivi "Then maybe we can play a fun game?"
                ava surprised "A game? Frivolity amidst such sorrow?"
                # JUMP TO: vivi saying "It's called Never Have I Ever."

            # OPTION 3 +ATTRACTION
            "...sneak behind the bar for two top shelf top offs?":

                vivi happy "...sneak behind the bar for two top shelf top offs?"
                ava happy "We were unaware you were this naughty, vivi."
                "(if attraction)"# ?? ATTRACTION
                ava happy blush "It pleases us. How does it feel? To disobey?"
                vivi happy "It feels exciting because it's wrong. Is that crazy?"
                ava neutral "No. We crave this...excitement."
                vivithinking "She's eating out of my palm...don't spook her now!"
                # END
                vivi happy "I've been called naughty before. So I propose a game of knowledge."
                # JUMP TO: vivi saying "It's called Never Have I Ever."

        vivi neutral "It's called Never Have I Ever."
        ava "How is it played?"
        vivi "If you haven't done something I have, you drink. I'll go first."

        # <CHOICE>
        vivi neutral "Never have I ever..."
        "(decay route)"# DECAY ROUTE
        ava sad "We misspoke. We wish to drink alone."
        vivithinking "Up yours, snooty patootie."
        # JUMP TO: vivi saying "See ya, sunshine."

        menu: 
            # OPTION 1 +DECAY
            "...had a pet.":

                vivi sad "...had a pet."
                ava "Do we drink if we have?"
                vivi "Exactly."
                vivithinking "Daaang! She pounded that one."
                vivi sad "Want to talk about it?"
                ava sad "We do not."
                "(if decay)"# ??DECAY
                ava "Never have we ever..."
                vivi surprised "It's called Never Have I Ever."
                ava sad "This game displeases us."
                vivi angry "Don't blame the game."
                ava angry "Surprisingly, you are correct. You displease us."
                vivi angry "We know where we are not wanted."
                # END
                # JUMP TO: vivi saying "Well then, see ya, sunshine."

            # OPTION 2 +ATTRACTION
            "...flirted with a goddess. Or the avatar, or whatever.":

                vivi happy "...flirted with a goddess. Or the avatar, or whatever."
                "(if attraction)"# ??ATTRACTION
                vivithinking "She's not drinking...hmmm?"
                ava sad "We are no longer an avatar. Or a goddess. We are...no one."
                vivi neutral "Not true. Maybe no one is just a starting point?"
                # END
                ava sad blush "Your flirtation pleases us. Never have we ever spat."
                vivithinking "Well, chug-a-lug, vivi!"
                vivi happy "Any reason why not?"
                ava surprised "We represent the goddess, vivi. We must not profane."
                vivi "Well, since we're dead and all, don't you think you can? Taboo's over, no?"
                ava "You have given me much to consider. Many thanks."
                vivi "You know where to find me."
                vivithinking "Oh shitballs!! Did I really say that out loud just now!?! Cornier than all of Iowa and Kansas combined."
                ava happy "We do. Good-bye, vivi."
                #JUMP TO: vivi saying "See ya, Asha!"
                
                
            # OPTION 3 <<ATTRACTION +ATTRACTION
            "...made a commitment to someone. Like a relationship.":

                vivi sad "...made a commitment to someone. Like a relationship."
                ava sad "We do not drink then." 
                "(if attraction)"# ??ATTRACTION
                ava sad blush "We understand this pain, vivi. We feel as you."
                vivithinking "Goddamn she dug deep. It's in her eyes."
                vivi happy "Wow. Thank you, Asha. I know it's hard to share your pain."
                ava sad "At times...we feel we are drowning in it. Our mind whirls."
                vivi neutral "Close your eyes and breathe. It's helped me before."
                # END
                ava "Ours was taboo. Why did you not find a love-mate?"
                vivi sad "Never had the time."
                "(if attraction)"# ?? ATTRACTION
                ava neutral blush "Had or made?"
                vivi surprised "Good question, Asha!"
                ava neutral "Our choices pave our paths forward. Is it not so?"
                # END
                vivi happy "It sure is. Good talk. I really... it felt awkward but I'm glad I shared."
                ava happy "We felt as you. Good-bye, vivi."
                #JUMP TO: vivi saying "See ya, Asha!"
                
        vivi "Well then, see ya, sunshine."
        vivi "See ya, Asha."
        vivithinking "What are the others doing, I wonder?"
        jump d_cs2

    label d_fr1_darius:
        #FREE ROAM 1 - Darius
        #LOCATION: Lounge
        scene lounge

        show darius sad at right
        show vivi happy at left

        "Perfect. They're here."

        vivi happy "Just the sad cephalopod I wanted to see-"
        vivi sad "Oh. Sorry. Is... this a bad time?"
        darius sad "It's nothing."
        vivi angry "It's clearly something, you clod."

        # <CHOICE>
        menu:

        #OPTION 1 +ATTRACTION
            "Darius. I could really use someone to talk with right now.":

                vivi neutral "Darius. I could really use someone to talk with right now."
                darius sad "I'm not sure that's such a good idea."
                vivi neutral "I do. I'd like your company."
                darius surprised blush "No one likes my company. It's my specialty."
                vivi happy blush "Well, consider me the first."

                # JUMP TO: "So. What are we drinking?"

        #OPTION 2 +DECAY 
            "You just push everyone away don't you? Fine. We can wait for whatever's coming in silence.":

                vivi angry "You just push everyone away don't you? Fine. We can wait for whatever's coming in silence."
                darius surprised "I didn't mean to offend."
                vivi angry blush "You never do. So cold. You're practically an icicle."
                "That flare of rage again. Good. Burn me."
                darius angry "Sitting alone is hardly me choosing to be cold to you."
                vivi angry blush "Well, you're not alone now. Deal with it."
            
        # JUMP TO: "So. What are we drinking?"

        #OPTION 3 NEUTRAL
            "Is it really nothing? Like nothing, nothing? Because it feels like something.":

                vivi neutral "Is it really nothing? Like nothing, nothing? Because it feels like something."
                darius neutral "I promise you. Nothing that concerns you."
                vivi neutral "Just because it doesn't concern me directly doesn't me I don't want to know what it is"
                darius surprised "It's just... I don't usually have a lot of back-and-forth conversations."
                vivi happy "Good news, Darius. You're having one."

                # JUMP TO: "So. What are we drinking?"

        # consider adding ATTRACTION ROUTE and DECAY ROUTE options

        vivi happy "So. What are we drinking?"
        darius neutral "... you can't laugh."
        vivi surprised "Why would I?"
        darius neutral blush "My drink of choice. It's a bit unexpected."
        vivi surprised blush "Oh no- should I prepare to be horrified? The tears of the damned? The blood of the innocent?"
        darius surprised blush "N-no! Nothing like that. What you all must think of me..."
        "That's the pinkest drink I've ever seen!"
        darius happy blush "It's called a... Singapore Sling."
        vivi surprised "A... what? It looks like a tall glass of juice!"
        darius happy blush "I'll have you know it's much more than that Ms. Sanssouci. It's actually a sophisticated gin cocktail with hints of bitters and Cointreau..."
        "...layered with cherry brandy and Bénédictine..."
        "...lime juice, pineapple juice, and grenadine, naturally..."
        vivi happy "Monsieur Wrecker, I can say with all honesty this is the happiest I've ever seen you."
        "Umph. There it is again- rage, but this time it's tempered by- pain? Sadness?"
        darius sad "Don't get used to it."
        darius neutral "I suppose I should ask you: what's your poison?"
        darius sad "I'd rather not drink alone."

        #<CHOICE>

        menu:

        #OPTION 1 +ATTRACTION
            "I'll have what you're having, handsome.":

                vivi happy blush "I'll have what you're having, handsome."
                "I could use a little fruity delight."
                darius surprised "I assure you, this drink is enough to knock you off your feet."
                vivi happy blush "Trust me, it'll take more than a juicebox to get me sauced."
                "Oh, my. Cripes. That's strong."
                vivi neutral blush "Delicious!"
                darius surprised "You like it? I worried it might go right to your head."

                # JUMP TO: "Never mind all that. How about a little 'Never Have I Ever'? A distraction to keep our spirits up!"
            
        #OPTION 2 +DECAY
            "I thought you wanted to be alone. Pick a lane, won't you?":
                vivi neutral "I thought you wanted to be alone. Pick a lane, won't you?"
                darius angry "Which is it? Do you want to drink with me and wallow in our mutual misery or do you want to needle me?"
                "Agh. The flash. There's definitely pain here."
                vivi angry "Don't be so sensitive. We're all in the same... train."
                darius sad "Hmph. Just... here. What do you want to drink?"

        # JUMP TO: "Never mind all that. How about a little 'Never Have I Ever'? A distraction to keep our spirits up!"

        #OPTION 3 NEUTRAL
            "Truthfully? I'm not much of a drinker. Hasn't been great for my family, historically.":

                vivi neutral "Truthfully? I'm not much of a drinker. Hasn't been great for my family, historically."
                darius surprised "Ah. I'm... sorry to hear."
                vivi neutral "Quite alright. How could you possibly have known?"
                "I feel their doubt. They didn't want to trigger me."

        # JUMP TO: "Never mind all that. How about a little 'Never Have I Ever'? A distraction to keep our spirits up!"

        vivi happy "Never mind all that. How about a little 'Never Have I Ever'? A distraction to keep our spirits up!"
        darius sad "Why not. Nothing else to do."
        vivi neutral "I'll start. Never have I ever... been in love."
        darius surprised blush "I... neither have I."
        "What happens now?"
        vivi neutral blush "I think that means we both drink."
        darius neutral "Let's see..."
        darius neutral "Never have I ever..."
        darius sad "Apologized."
        vivi surprised "For what?"
        darius sad "For anything."
        "Radiating off of them- that uncomfortable heat."
        darius neutral "Well? Surely you must drink to that. I know your kind... is always saying that."
        "Whether it's warranted or not."
        vivi neutral "You're not wrong. You know- if you'd rather talk instead of just playing a game-"
        darius sad "I wouldn't."
        "In fact- perhaps it's time we leave. This lounge is feeling a bit small."
        jump d_cs2

        # this scene could probably benefit from a couple more back and forth exchanges and possibly another choice- but I'm bumping up against the character limits

    label d_fr1_susurha:
        #FREE ROAM 1 - Susu'Rha (DEPRESSION)

        #LOCATION: Dining Car
        scene diningcar

        show vivi neutral at left

        vivithinking "If anyone knows how to drink on this train, it's gotta be Susu'Rha."

        show susurha neutral at right

        susurha "Well, if it isn't little ol' you."

        "(if attraction)"#ATTRACTION ROUTE
        susurha happy blush "Come to torment me some more?"

        "(if decay)"#DECAY ROUTE
        susurha "Come to torment me some more?"

        vivi "To be honest, I'm ready to just get nice and drunk."
        susurha neutral "Although to be honest with you..."
        susurha sad "I share your thoughts."
        susurha neutral "Come come. Take a seat and let me treat you to something special."

        vivithinking "Wow. They seem at home behind the bar."

        vivi surprised "When someone's really good at mixing drinks, we call them a mixologist."
        susurha happy "In the Viridian Wood, the mixture and ingestion of intoxicating potions was almost a nightly occurrence."
        vivi "Ah... to sit in the moonlight, reading a collection of poetry with a glass of red wine in hand."
        vivi "It sounds like you've lived a full life."
        susurha sad "In the Wood, we lived joyously, following the path of self-expression."
        vivithinking "I could have used more of that."
        susurha happy "A delectable pina colada for me and a sloe gin fizz for you."

        "(if attraction)"#ATTRACTION ROUTE
        susurha blush "Made with love."

        vivithinking "Hmmm..."

        vivi "This is incredible."

        susurha "Good."

        susurha "During my time at the druid camp, they had this special ritual they participated in that required the unique properties of liquor."

        vivithinking "Curious..."

        vivi "What was it?"

        susurha "It is where we playfully say something about ourselves that we have never done and the others would take a drink if they have done the deed."

        susurha "Allowing us to tear away at the veils that encase us to those we know."

        "(decay route)"#DECAY ROUTE
        vivi "Oh, I don't know about this."
        susurha "Even now as we near the end of the tracks?"
        susurha sad "Can we just try..."
        susurha sad "Try to pull back the mask?"

        susurha neutral "I'll even let you ask the first question."

        vivithinking "Are we sure about this?"
        vivithinking "..."
        vivithinking "Screw it!"

        vivi "Alright."

        #<CHOICE>
        vivi "Never have I ever..."
        menu:

            #OPTION +Attraction
            "Been engaged.":

                vivi "Been engaged."
                susurha "Hmmm..."
                susurha "You got me there."
                vivithinking "Wow! They've been engaged?"
                vivithinking "Looking at them, not hard to believe."
                vivi "Who was it to?"
                susurha "You know, I never learned their name."
                susurha "It was arranged."
                vivi "Oh..."
                susurha "I learned about it the night before I ran away."
                susurha "I didn't want to be tied down and now I'm here."
                susurha "Dead and alone."
                "(if attraction)"#ATTRACTION ROUTE
                vivi "You're not alone."
                show susurha happy
                #JUMP TO: susurha saying "My turn."

            #OPTION +Decay
            "Led a kingdom.":

                vivi "Led a kingdom."
                susurha "Hmm... got me there I suppose."
                susurha "Bottoms up."
                susurha "That was quite the easy one. Are you trying to make me drunk?"
                vivi "Maybe."
                vivi "Why didn't you stay? The power alone..."
                susurha sad "Was a lie. There is no power that lays upon the throne."
                susurha sad "Just chains that bind and a muzzle that seals your mouth."
                susurha sad "An avatar of those around you."
                vivithinking "They surely can't be serious."
                susurha sad "I suppose we can't escape the chains that bind us."
                susurha sad "We all end on the same track."
                #JUMP TO: susurha saying "My turn."

            #OPTION >>Decay +Attraction
            "I don't know.":
                
                vivi "I don't know."
                susurha "Boooo..."
                vivi "I'm sorry. I'm not sure what to say."
                susurha "Really?"
                vivi sad "Yeah, I truly don't know what to say."
                vivi sad "I'm sorry."
                susurha "It's okay. Don't stress. Just..."
                susurha "Be...."
                vivi "Okay."
                show susurha happy 
                susurha "You got it."
                #JUMP TO: susurha saying "My turn."

            #OPTION >>Decay +Decay
            "Can we just sit and drink?":

                vivi "Can we just sit and drink?"
                vivithinking "I don't know if I have anymore games left in me."
                susurha "Hmmm..."
                susurha angry "Fine."
                #JUMP TO: susurha saying "My turn."

        susurha happy "My turn."

        vivithinking "Oh boy."

        # <CHOICE>
        susurha neutral "Never have I ever been in love."

        menu:

            #OPTION +Attraction
            "No.":

                vivi "No."
                susurha surprised "Really?"
                vivi sad "Yeah, I've... never really gotten that far before."
                vivi sad "I've had plenty of partners, but none of them... felt..."
                vivi sad "You know."
                vivi sad "I'm sorry. I'm killing the buzz."
                susurha neutral "Stop. You've nothing to apologize for."
                susurha "This is the whole point of the ritual. To remove our masks."
                susurha sad "I share your same experience. Many held me in their gaze, but none could hold mine."
                vivi "Alone together."
                #SOUND: susurha scoffs.
                susurha "I can drink to that."
                #JUMP TO: susurha saying "I wonder if love lasts beyond death."

            #OPTION >>Attraction +Attraction
            "Possibly, recently.":

                vivi blush "Possibly, recently."
                susurha surprised "Oh... do tell me more, madam."
                vivithinking "Do I tell them? Do I not?"
                vivithinking "No."
                vivithinking "Let's be fun."
                vivi happy blush "You should have been more specific."
                susurha happy blush "Your face tells it all."
                #JUMP TO: susurha saying "I wonder if love lasts beyond death."

            #OPTION +Decay
            "I've had plenty of lovers.":

                vivi "I've had plenty of lovers."
                susurha "I'm sure. A woman such as yourself, but..."
                susurha "Have YOU ever been in love?"
                vivi "Everyone has been in love in their life."
                vivi "It isn't anything special."
                "..."
                susurha sad "vivienne..."
                susurha sad "I'd want to believe you're wrong."
                #JUMP TO: susurha saying "I wonder if love lasts beyond death."

        susurha neutral "I wonder if love lasts beyond."

        "(if attraction)"#ATTRACTION ROUTE
        susurha "Thank you for spending these moments with me."

        "(if decay)"#DECAY ROUTE
        susurha "I wish I could have made these moments more special for you."

        susurha "The train is speeding up. Have you noticed?"

        hide susurha

        vivithinking "I think I got enough out of this drink."

        vivithinking "My head is already spinning."

        vivithinking "I should take a moment to collect myself."

        #JUMP TO: Free Roam 2 - Character Selector
        jump d_cs2


    label d_cs2:
        #Character Selector 2

        #LOCATION: cabin
        scene cabin

        show vivi neutral at left

        vivithinking sad "Ugh... I think I might've had a little too much."

        vivithinking neutral "Then again, there's nothing to look toward. Might as well take advantage of the open bar."

        # SOUND: Knocking on the door

        show urshu neutral at right

        urshu neutral "Ms. Sanssouci, I see you've found the liquor cabinet."

        vivi neutral "Top shelf stuff, Urshu."

        vivithinking neutral "What does he want now?"

        vivi neutral "So, has the conductor of this fine train come to reprimand me?"

        urshu neutral "Not at all. The way you spend your time is entirely up to you."

        vivithinking angry "This guy is impossible!"

        vivi angry "You got a problem with the way I'm spending my time? I'm sick of you looking down at all of us. You may ferry people to the next life but you don't know how it feels."

        vivi sad "We're just trying to have a moment of peace." 

        vivi sad "We don't want to think about this train falling apart, or the horrible things outside..."

        vivi angry "Or you."

        vivi sad "I don't want to think anymore. I just want rest."

        vivi sad "I'm tired of being so tired. And scared and angry and..."

        vivi angry "...Argh!"

        show vivi sad

        urshu sad "I'm sorry you feel that way. Truly, I am."

        urshu neutral "Countless have boarded my train. Some have sung its praise. Many more have cursed it out. But this place, whether you see it or not, is a gift."

        urshu neutral "You have been granted a second chance. A place to right your deepest regrets. There's a reason it's not a solo voyage."

        vivi sad "What does it matter? It ends all the same."

        urshu neutral "Heed my advice, or don't. Only one thing is certain:"

        urshu happy "Your story, my dear? It's not finished. Yes, the finale draws near, but the last act is yours to write. Make it a good one."

        vivi neutral "And how do you figure I do that?"

        "(if attraction)"#??ATTRACTION
        urshu neutral "Believe it or not, you have had a profound effect on the other passengers. I'm sure one of them would love to spend time with you as we approach our destination."

        "(if decay)"#??DECAY
        urshu neutral "That is for you to discover. We approach our destination. Now would be a good time for final goodbyes."

        hide urshu

        vivithinking neutral "I suppose there might be something to what he said."

        # <CHOICE>
        "(if attraction)"#??ATTRACTION
        vivithinking happy "Let's find someone to hold one last time before this thing ends."

        "(if decay)"#??DECAY
        vivithinking neutral "Time to finally leave this purgatory. I reckon goodbyes are in order."

        menu:
        # OPTION 1
            "Avatar of Asha":

                vivi neutral "The goddess. I want to spend my last moments with her."
                # JUMP TO: Free roam 2 / Avatar of Asha
                jump d_fr2_ava

        # # OPTION 2
        #     "Inquisitor Darius Wrecker"

        #     vivi neutral "Darius. I want to spend my last moments with them."
        #     # JUMP TO: Free roam 2 / Darius Wrecker

        # OPTION 3
            "Susu'Rha Balrinn":

                vivi neutral "Susu'Rha. I want to spend my last moments with them."
                # JUMP TO: Free roam 2 / Susu'Rha Balrinn
                jump d_fr2_susurha

    label d_fr2_ava:
        #FREE ROAM 2 - Ava
        #Location: Observatory
        scene observatory

        show vivi neutral at right

        show ava neutral at left

        vivithinking "Oh, the Sun Goddess, herself. Somehow looking radiant as usual after being on this damned train for who knows how long."

        "(if decay)"#??DECAY
        vivi sad "She's too good for me..."
        #END

        "(if attraction)"#??ATTRACTION
        vivi happy "I need her in my life, no matter what."
        #END

        vivithinking "Okay, vivi, deep breath, and-"

        vivi happy blush "Asha, darling, how are you?"

        ava neutral "..."

        vivi surprised "Asha?"

        ava surprised "Oh, sunshine, we are so sorry. We couldn't detach from our memories. They are painful, you must understand. Our life has not been a happy one."

        # <CHOICE>
        menu:
            #OPTION 1 + ATTRACTION
            "Really?":

                vivi surprised "Really? Even though the royals treated you poorly you had everything you could have ever wanted. I don't understand."

                ava sad "Of course you do not understand. How could you?"

                vivi sad "I want to...understand. How can I share your pain if you don't talk about it with me?"

                # JUMP TO: ava saying "vivi..."

        #OPTION 2 + DECAY
            "You're pretty ungrateful, huh?":

                vivi angry "You're pretty ungrateful, huh? It sounds like you had everything you could have ever wanted."

                ava sad "How could you ever understand..."

                vivi angry "You're right, Asha. I can't and I won't. How could a puny little human peasant like me ever understand what it's like to be a princess in a castle?!"

                # JUMP TO: ava saying "vivi..."

        #OPTION 3>>+ATTRACTION
            "I wish I could have been there for you.":

                vivi sad "I wish I could have been there for you. Our relationship has been the one thing keeping me sane on this journey...I wish we could have spent some time together while we were alive."

                ava happy "Really? We feel the same way."

                # JUMP TO:


        ava sad "vivi..."

        ava sad "We never had a friend."

        vivi angry blush "What about me?! I thought we were friends!"

        ava surprised "That may be true, but we will soon be separated by fate. There is no heaven awaiting for Asha."

        vivi surprised blush "Oh? And why's that?"

        ava neutral "*sigh* You are aware that I am not the first Avatar of Asha. Every twenty and five years, a new avatar is chosen."

        ava sad "Soleos was not always the peaceful society it is today. The planet was once split in two, marred by war and terror...until the Avatar arrived."

        ava sad "She was born from the seed of a Solarian man and the egg of a Lunolian woman. The mixing of cultures was considered taboo, said to bring about the end of the world."

        vivi sad "Oh, my goodness. I had no idea."

        ava sad "The woman who gave birth to Asha was my ancestor, far removed. My bloodline is the only one that can act as a vessel for the Avatar."

        # <CHOICE>
        menu:
            #OPTION 1 + ATTRACTION
            "But why do you need her to begin with?":

                vivi surprised "But why do you need her to begin with? I wish you could have had a normal life on Earth."

                ava sad "Without the Avatar, our world would be doomed. These hands have seen much bloodshed."

                vivi surprised "I didn't realize that your life wasn't all sunshine and rainbows."

                ava sad "It is not your fault, my sunshine. For we did not share with you. It is not an easy thing to broach lightly."

                # JUMP TO: vivi saying "I'm sorry, Asha."


            #OPTION 2
            "Why are you telling me all this now?":

                vivi surprised "Why are you telling me all this now?"

                ava sad "What better time to share our lore than at the end of the world?"

                vivi happy "I guess you make a good point."

                #JUMP TO vivi saying "I'm sorry, Asha."


            #OPTION 3>>+ATTRACTION
            "If only I had known you in life.":

                vivi sad "If only I had known you in life, things could have been different."

                ava neutral blush "A little bit of love would have gone a long way."

                vivi happy blush "Well I'm glad we can spend this time together now."

                # JUMP TO: vivi saying "I'm sorry, Asha."

        vivi neutral blush "I'm sorry, Asha."

        "(if attraction)"#??ATTRACTION
        ava neutral blush "No need. Just be here now."

        #pause

        # SOUND heartbeat

        #END


        ava neutral blush "I want to know more about your life on Earth. What can you tell us?"

        # <CHOICE>
        menu:

            #OPTION 1>>+ATTRACTION
            "There was this one time...":

                vivi happy blush "There was this one time I won a writing competition in school for this shitty poem I wrote. The prize was a trip to the continent of South America, and I got to bring a friend with me." 

                ava surprised "Merit based reward...interesting."

                vivi happy "I didn't have any friends to bring so I posted online about the extra ticket and got a bunch of responses. Random people from all over reached out to me."

                vivi happy "Most of them just wanted to go to a new country of course, but there were a few people who reached out wanting to make new friends."

                vivi happy "That vacation ended up changing my life. I met tons of amazing people, saw new cultures, and got to try some crazy foods. It's a precious memory for me. Something that keeps me going."

                ava happy blush "That sounds remarkable. A change in perspective really can make a big difference, huh."

                # JUMP TO: vivi saying "Like you wouldn't believe!"


            #OPTION 2>>+DECAY
            "I wrote this haiku in school once.":

                vivi happy "I wrote this haiku in school once. Wanna hear it?"

                ava surprised blush "Go on, then."

                vivi happy blush "Tasty soup tasty. Tasty soup tasty soup mmm. Tasty tasty soup."

                ava surprised blush "Wow. You really have a way with words, huh?"

                # JUMP TO: vivi saying "Like you wouldn't believe!"

            #OPTION 3 NEUTRAL
            "Earth is beautiful.":

                vivi happy blush "Earth is beautiful. In its own way. There are thousands of unique cultures and ways of life that thrive in different ecosystems, from deserts and mountains to swamps and snow."

                ava happy "We cannot imagine..."

                vivi happy "If I could spend the rest of my life traveling the world, I would do it in a heartbeat. Being locked up at work is no fun."

                ava surprised blush "Can a change in perspective truly make that much of a difference?"

            # JUMP TO: vivi saying "Like you wouldn't believe!"


        vivi happy "Like you wouldn't believe!"

        ava neutral blush "Well our conversations have certainly helped me feel better. We enjoy your...perspective."

        vivi happy blush "Come to Earth sometime! I'll show you around!"

        "(if decay)"#??DECAY
        ava sad "If only we could have..."
        #END

        "(if attraction)"#??ATTRACTION
        ava blush "It's a date. We're looking forward to it."
        #END


        vivi sad blush "I should go...See you soon, Asha."

        ava blush "Remember, The All is the One."

        vivi blush "The All is the One..."

        # JUMP TO: DEBRIEF DEPRESSION
        jump debrief_depression

    label d_fr2_susurha:

        #FREE ROAM 2 - Susu'Rha (DEPRESSION)

        #LOCATION: Observatory
        scene observatory

        show susurha neutral at right
        show vivi neutral at left

        susurha "The stars are out tonight. As beautiful and endless as the night I left home."

        vivithinking "It seems Susu'Rha is holding up as well as me."

        susurha "Ah, vivi."

        "(if attraction)"#ATTRACTION ROUTE
        susurha "I needed to see a friendly face."

        "(if decay)"#DECAY ROUTE
        susurha "What brings you to me in these final moments?"

        # <CHOICE 1>
    #XXX decay + decay choice, something like, "you're not as bad as the others."
        vivi "I wanted to see you."
        menu:

            #OPTION +Attraction
            "I didn't want to be alone.":

                vivi "I didn't want to be alone."
                susurha "I feel you. Oh so very much."
                vivi "Is it okay if I stay here?"
                susurha "Please... sit with me."
                #JUMP TO: vivi thinking "It feels so warm being next to them."

            #OPTION >>Attraction +Attraction
            "I also needed a friendly face.":
                
                vivi "I also needed a friendly face."
                show susurha happy blush
                "..."
                susurha neutral "Please... sit with me."
                # JUMP TO: vivi thinking "It feels so warm being next to them."

            #OPTION >>Decay +Attraction
            "I don't know why.":

                vivi "I don't know why."
                susurha "Why do we do a lot of things when nearing the end?"
                susurha "Thank you for your honesty."
                vivi "Is it okay if I stay here?"
                susurha "It's okay. Come, sit with me."
                # JUMP TO: vivi thinking "It feels so warm being next to them."

        vivithinking "It feels so warm being next to them."

        vivithinking "I could almost fall asleep right here with them."

        "(decay route)"#DECAY ROUTE
        vivithinking "Why do I feel this way?"

        susurha "Even with all the druid teachings in my life..."
        susurha "The space out there seems so peaceful in all its chaos."
        susurha "It feels so welcoming..."
        susurha "Yet I can't trust it."
        susurha "Do you think it will hurt..."
        susurha "...when we become one with the cosmic weave?"

        #<CHOICE 2>
        susurha "Will we know when we're gone?"

        menu:

            #OPTION 
            "We'll never know until it happens.":

                vivi "We'll never know until it happens."
                susurha "That's what I'm afraid of."
                # JUMP TO: susurha saying "Are you afraid?"

            #OPTION +Attraction
            "I don't want to go.":

                vivi "I don't want to go."
                susurha sad "Yeah..."
                # JUMP TO: susurha saying "Are you afraid?"

        # <CHOICE>
        susurha "Are you afraid?"

        menu:

            #OPTION +Attraction
            "Yes.":

                vivi "Yes."
                vivi "I'm very afraid."
                vivi "Who wouldn't be?"
                # JUMP TO: susurha saying "Well, I know I am."

            #OPTION +Decay
            "No.":

                vivi "No."
                vivi "What's the point in being afraid?"
                vivi "We can take it on. Deal with it as it comes."
                susurha "Your enthusiasm feels as if it is made of glass."
                # JUMP TO: susurha saying "Well, I know I am."

            #OPTION
            "...":

                vivi "..."
                # JUMP TO: susurha saying "Well, I know I am."

        susurha "Well, I know I am."

        susurha sad "..."

        susurha sad "I used to pride myself in knowing people with ease."

        susurha neutral "But that thing that stalks me..."

        susurha "I've tried to talk to it. Understand it."

        susurha "I thought it chose to not speak to me when I begged for it to free me, but I realize now that it never had a voice to begin with."

        susurha "Its body is chained at the wrists and ankles, making it unable to move."

        susurha "Its eyes were blinded so that it couldn't see a path ahead."

        susurha "Its mouth is muzzled so that it can never express its thoughts."

        susurha sad "..."

        susurha sad "I ran away from home because I was afraid that I would never get to be who I felt I was. Live the life I want to live."

        susurha sad "Now I'm afraid that thing, void of personality, will be the fate in the cosmic weave."

        susurha sad "I don't want to cease to exist."

        susurha sad "I want to be ME."

        vivithinking "What if they are correct?"

        # <CHOICE 3>
        vivithinking "I want to be me."

        menu:

            #OPTION +Attraction
            "I want to be ME as well.":

                vivi "I want to be ME as well."
                vivi "My whole life... I felt I was living someone else's life."
                vivi "Think like someone else. Act like someone else."
                vivi "I'm afraid I've missed my chance to be me."
                susurha "Right here, right now, you are you."
                # JUMP TO: susurha saying "Thank you for staying with me, if even for a moment."
                

            #OPTION >>Decay +Attraction
            "I get what you mean.":

                vivi "I get what you mean."
                susurha "You do?"
                vivi "I've always wanted to be me. Feel like I am actually me."
                vivi "It's just that...I don't know if I can say I ever have."
                susurha "Right here, right now, you are you."
                # JUMP TO: susurha saying "Thank you for staying with me, if even for a moment."

            #OPTION >>Attraction +Attraction
            "Nothing can take away who you are.":

                vivi "Nothing can take away who you are."
                vivi "You're one of the most unique people I have ever met."
                vivi "There aren't many poet-musicians druids that were once heir to a throne, but chose to not take that power so that they could be THEMSELVES."
                vivi happy blush "You are truly one of a kind."
                susurha happy blush "STOP... You flatter me so much, vivienne"
                susurha neutral blush "I can say the same thing about you."
                susurha neutral blush "Nothing can take away who you are."
                # JUMP TO: susurha saying "Thank you for staying with me, if even for a moment."

            #OPTION >>Decay +Decay
            "I know who I am.":

                vivi "I know who I am."
                susurha "Are you sure about that?"
                vivi "What are you trying to say?"
                susurha "This whole time that I've interacted with you, it has always felt like I was talking to a mirror that bends and flows with the wind."
                vivithinking "This son of a..."
                susurha "I told you the thing that stalks me. Tell me, what does the thing that haunts you appear as?"
                vivithinking "It's..."
                vivithinking "Oh."
                #JUMP TO: susurha saying "Thank you for staying with me, if even for a moment."

        susurha "Thank you for staying with me, if even for a moment."

        "(if decay)"#DECAY ROUTE
        susurha "I hope I brought some worth to you."

        susurha "The only thing worse than being alone is never being at all."

        "(if attraction)"#ATTRACTION ROUTE
        vivi "We can sit here for a little while longer."
        vivi "And just watch the cosmic weave fly by."
        susurha neutral blush "I'd love that."
        vivithinking "In its own strange way, the view sure is beautiful from here."

        "(decay route)"#DECAY ROUTE
        vivi "Everything will turn out for the best."
        susurha "You lie to yourself so easily."
        susurha "I hope there is someone behind that mask."
        susurha "Even if you don't show me them."
        vivithinking "I..."
        vivithinking "I think I have had enough of this."
        vivi "Good night."
        susurha "Sleep easy, vivi."

        jump debrief_depression

    label debrief_depression:
        #Debrief Depression

        #LOCATION: cabin
        scene cabin

        "(if attraction)"#??ATTRACTION

        show vivi neutral at left

        # SOUND Knocking on door

        show urshu neutral at right

        urshu neutral "I trust you had a good evening?"

        vivi happy "Yeah, it was nice."

        vivi neutral "About what you said before. Writing my own story... I think I get it."

        urshu happy "I live to serve, Miss. Sanssouci."

        vivi neutral "You know you're a cosmic entity, right? No need to be so formal with me."

        urshu happy "As you wish."

        vivi neutral "Hey Urshu, before you go, can I ask you something?"

        vivi neutral "Why'd you put us four together?"

        urshu happy "Maybe it was preordained. Maybe it was random. Or maybe, I think you four just fit together. I do love puzzles after all."

        vivi neutral "You've been quite the conductor, Urshu."
        urshu neutral "And you have been quite the puzzle."

        urshu neutral "Enjoy your final night here."

        vivi sad "It's really ending, huh?"

        urshu happy "All may not be as lost as you think."

        vivi happy "Goodnight, Urshu."

        urshu happy "Goodnight, vivienne."

        vivithinking neutral "My mind is buzzing. I need to write."

        "(journal entry)"#Journal entry with attraction meter high
        "Wow. At the beginning of all this, I would've never thought I'd get to know some of the other passengers this well. We're all more similar than I thought. Even Urshu, believe it or not. Time is weird here. I feel like I've been riding this train for ages, but I think I finally understand this place. It's a lot to process, but I'm so glad I didn't have to do it alone."


        "(if decay)"#??DECAY

        show vivi neutral at left

        # SOUND Knocking on door

        show urshu neutral at right

        urshu neutral "I trust you had a good evening?"

        vivi neutral "It was fine. I am glad this is ending though."

        urshu surprised "Oh? Do tell."

        vivi neutral "I was scared at first. Of changing, of the unknown, of leaving my past behind..."

        vivi neutral "I'm not anymore."

        urshu neutral "And what changed?"
        vivi neutral "Nothing. I guess I realized wherever I'm going can't be worse than here."

        vivi angry "The more I talk to the people on this train the more I realize how much I hate it here. I'm not myself anymore. You took that from me. I've withered away just like this train."

        vivi angry "I don't even recognize myself in the mirror. I can't tell if I've physically changed or if my perception of self has warped. My thoughts... they're not entirely my own anymore. The only thing I had were my thoughts!"

        urshu sad "I'm sorry you feel that way."

        vivi angry "And I'm sorry I wasn't your perfect little plaything to be experimented on!"

        vivi neutral "I will thank you for one thing: You've pushed me beyond all knowable limits. Now I can guarantee I'll be ready for anything in the next life."

        urshu neutral "Thank you for the feedback. Goodnight, Ms. Sanssouci."

        hide urshu

        vivithinking neutral "I should write whatever thoughts I have left. By tomorrow, I'm not sure they'll be mine."

        "(journal entry)"# Journal entry with degradation meter high

        "I can't take this anymore. There's something growing inside me. A hunger I, we can't explain. What is happening to us? This is the conductor's fault. He's behind everything. The other passengers too. They must be working with him. None of them feel the way we do. They're all out to get us. We won't go. Not like this. They'll see."

        return
