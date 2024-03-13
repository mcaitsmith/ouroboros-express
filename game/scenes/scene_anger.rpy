### EXAMPLE OF TEMPLATE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene_anger:

    #LOCATION: cabin
    scene cabin

    show vivi neutral at left

    show urshu neutral at right
    urshu "Good cosmic morning, Miss Sanssouci!"
    vivi surprised "He's so light on his feet. Are all short kings also ninja-quiet? Are all short kings also ninjas?"
    "Urshu! You shouldn't sneak up on someone this early."
    "Especially when they haven't had their coffee yet..."
    urshu "The perfect way to start every morning, whether careening toward your death on the Ouroboros Express or not, is with Narubian citrus-infused espresso. There's some prepared in the lounge." 
    "Vivi narrows her eyes. She wonders, and not for the first time, if Urshu can read minds."
    vivi "The lounge. Where there's people, I'm guessing."
    "What scheme is he getting at today?"
    urshu happy "..."
    vivi "Urshu, are you being cute again?"
    urshu happy "I'm never not being cute. I have a surprise for you."
    vivi "His hands are behind his back. Shit."
    "Ursh...what is it?"
    urshu "Guess, Miss Sanssouci."
    vivi angry "I am not in the mood today!"
    "She really isn't in the mood today..."
    vivi angry "Is it espresso with fancy-ass lemon juice in it?"
    urshu happy "No, my dear. Guess again. I'll narrow it down for you...with a riddle."
    "Oh, spare me."
    "Today is NOT a good day for riddles."
    "There's never a good day for riddles, actually."

    # CHOICE
    urshu "I am something everyone needs, but so few use me. I am something that keeps you young, but adults deny me. I am at home among children, but taken away as they age. What am I?"

    menu:
        # OPTION 1
        "I don't have time or patience, patience or time!":

            "I don't have time or patience, patience or time! Get me, Urshu?!"
            # SOUND: urshu sighs
            urshu "Patience enough to repeat yourself."
            vivi angry "What was that?"
            "What is he on today?" 
            urshu "Nothing, Miss Sanssouci. Here is the answer to my riddle."
            "What are these...playing cards?" 
            urshu "Games, my dear. The answer is games. They bring unity and competition. They challenge you and change you. They--"
            vivi "Look, Ursh, I've got your number now. You think I should play games with the other passengers. Let me rephrase. You want me to shoot the breeze while this bullet train screams on down to our universal heat death?"
            urshu "Well, excuse me. You're already playing love games with the delicious denizens of death here, Miss Sanssouci. Why not something less challenging?"
            "Urshu reveals a set of playing cards. He is smiling. Vivi is not."
            vivi "Gah! This insufferable--yet so adorable--man! I swear..."
            "Are those...normal-ass playing cards?" 
            #JUMP to urshu saying "No matter when..." 

    # OPTION 2
        "Innocence.":

            "Innocence." 
            "That's a good guess, right? Don't even need to question it. I nailed it."
            urshu "Ah! Innocence is precious, is it not? A purity of existence where all emotions are in touch and rhythm. Doubt, fear, anger all have their freedom."
            vivi "So...?"
            urshu happy "I'm afraid not, my dear! The answer is not innocence. Good guess, though! In truth the answer is far less altruistic. Here, take a look."
            "I'd very much like to be free with MY feelings. Can I break something? Right now?"
            vivi "Cards. CARDS?! All this to get me to play poker? Let me tell you, I wanna be free with my feelings right now. I'll show Urshu my innocence..."
            "Give me a break, Ursh. I woke up today, still dead. Still hurtling toward THE end. And I haven't had coffee yet. Narubian or otherwise."
            #JUMP to urshu saying "No matter when..." 

    # OPTION 3
        "Baby teeth?":

            "Baby teeth?"
            urshu neutral "..."
            vivi "What?"
            "Why is he looking at me like I'm crazy?"
            urshu "That is the most logically nonsensical answer I've yet received."
            vivi "So, I'm right."
            urshu happy "Ha...no."
            urshu "It concerns me greatly to think that you believe baby teeth will keep you young. Do you consider baby teeth to be a source of eternal life? The philosopher's enamel, if you will."
            vivi surprised "I--what?"
            urshu "Are you in a cult? You must be, back in that backwater you call civilization. I do not wish to judge, not at all. It's a natural question, in regards to harvesting baby teeth."
            vivi "Oh my God."
            urshu "How do you harvest baby teeth? Do you pluck them fresh or bribe a despondent dental worker?"
            vivi "Urshunabi..."
            urshu "I suppose harvesting isn't the most important question. Ingestion is. Do you pop them whole like candy or grind them into powder for your eviscerated tree offspring? Smoothie bowls, they're called?" 
            vivi angry "Ursh!"
            "Yes?"
            vivi angry "Are you? Oh, you are." 
            urshu happy "Pulling your leg? I would never."
            vivi "This sonofabitch has wasted countless cosmic minutes!"
            "So what's the answer to your dumbass riddle?"
            #JUMP to urshu saying "No matter when..." 

    # OPTION 4
        "Games?":

            "Games?" 
            urshu happy "Games...hmm."
            vivi "There's no way that's the answer."
            "Well? Not getting any more alive here."
            urshu happy "Yes! Yes! That is the answer, Miss Sanssouci. You're the only one to have guessed correctly!"
            vivi happy "Fuck yeah!"
            "I mean, obviously I got it right. I'm brilliant."
            urshu "Let's not get ahead of ourselves. You're the only human to have guessed correctly."
            vivi "This lil' shit!"
            #JUMP to urshu saying "No matter when..." 

    urshu "No matter when, where, what, or who in the universe, across nebulae and even in the underworlds, games always have a place among emotion beings. Games are one method of reversing the naturally lawful decay we all suffer."
    vivi "Games don't get rid of crows' feet. Wait. Do they?"
    "Can you just hand them over already?"
    urshu "I'm sorry, Miss Sanssouci, these are my special cards. Given to me by...well, someone from so long ago even Asha was a young god. Humans had yet to walk upright, even. Ah, but you don't look like you want a story like that."
    vivi "Good read there, honey."
    "Are there other games, then?"
    "He looks out the cabin window wistfully." 
    urshu sad "We had something like love, then. A time and place long gone. Eternal gardens. Amber lanterns like fireflies. Buildings of floating emerald marble. What I wouldn't give..."
    vivi "He's not even speaking in full sentences. Weird."
    "Uh...Ursh?"
    urshu blush "Forgive me...you will find games where you will find your next partner. Whomever shall you challenge? I am positively vibrating with anticipation."
    vivi "Ew?"
    "I'll be sure to tell you all about it, as long as you stop vibrating...so close to me."
    urshu blush happy "As you wish, Miss Sanssouci."

    #urshu exits. 
    hide urshu

    vivi "And what the hell does he expect me to do? What will the others think of me? Oh God, do I play one I know? Then they might think I'm cheating. Maybe I play one they know...but then I might lose."
    vivi happy "Then again, I've never played any game, love or otherwise, I couldn't win."

    #JUMP to Character Selector 1

    #Character Selector 1

    #LOCATION: cabin
    scene cabin

    show vivi neutral at left

    vivi angry "A card game. Trapped on a train towards impending doom and the conductor wants me to play a fucking card game."

    #CHOICE
    vivi neutral "I suppose there's nothing better to do. Who to talk to?"

    menu:

    #OPTION 1
        "Avatar of Asha":

            vivi neutral "Maybe the goddess would like a game. It'd be nice to talk to her more."
            #JUMP to Free roam 1 / Avatar of Asha
            jump fr1_ava

    #OPTION 2
        "Inquisitor Darius Wrecker":

            vivi neutral "I want to know more about Darius. Maybe they'd be up for a game."
            #JUMP to Free roam 1 / Darius Wrecker
            jump fr1_darius

    #OPTION 3
        "Susu'Rha Balrinn":

            vivi neutral "I'm sure Susu'Rha would like a game. They seem to make things more fun."
            #JUMP to Free roam 1 / Susu'Rha Balrinn
            jump fr1_susurha

    #FREE ROAM 1 - Ava

    label fr1_ava:

        #LOCATION: observatory
        scene observatory

        show ava sad at left
        show vivi neutral at right

        vivithinking "I stroll into the observatory and who do I see staring out the window into darkness but the sun goddess?"

        show ava happy
        vivithinking "Oh, she's different, like me! Changed."

        ava sad blush "Hello, Vivi. Has our radiance tempted you today? Come, sit, and play a game. Let us see what future the cards hold."

        vivithinking "Are those tarot cards she has? They look...off."

        ava neutral "Three cards we have placed in front of you."
        vivithinking "A sun, a sea monster, or a huge snake??"

        #<CHOICE>
        ava neutral  "Choose."

        menu:

            #OPTION 1 +ATTRACTION
            "The sun card.":
            
                vivi neutral "The sun card."
                ava sad blush "The sun can represent light, truth, and love..."
                vivi surprised "Finally some good news!"
                ava sad "...we had not finished, Vivi. The sun is upside down, so it brings darkness, lies,
                indifference."
                #JUMP to vivi saying "This is silly! They're just cards. They can't tell us that!"

            #OPTION 2 +DECAY
            "The sea monster card.":

                vivi neutral "The sea monster card."
                ava surprised "Ah. Leviathan. The eater of worlds, scourge of the seas. Interesting."
                vivithinking "Our goddess keeping her cards close to her chest."
                vivi angry "Sure you're not jealous of Darius?"        
                ava angry "We know of his kind. You would be wise to stay away. His card brings 
                darkness...and deceit."
                #JUMP to vivi saying "This is silly! They're just cards. They can't tell us that!"

            #OPTION 3 +DECAY
            "The big snake card.":

                vivi neutral "The big snake card."
                ava surprised "Curious. We have not seen this card before. Curious. It resembles the 
                Ouroboros."
                vivithinking "Oh, for serious! Can't I catch a break?"
                vivi "Oddly apt, no?"
                vivithinking "Could she be projecting?"
                vivi surprised blush "Sure you aren't a wee bit jealous of susurha?"
                ava surprised "Sush'Rha? Another royal? Jealous? The card could not be clearer. Avoid 
                him, Vivi."
                #JUMP to vivi saying "This is silly! They're just cards. They can't tell us that!"

        vivi angry "This is silly! They're just cards. They can't tell us that!"
        ava surprised "Perhaps they are merely cards." 
        ava sad "In the mirror this morning, fate stared back at us. And for you, Vivi?"
        vivi "For me too, Asha."
        vivithinking "Less of me and less of the train; not totally unnerving!!"
        ava angry "Why, Vivi? *scoffs* What was the point of it all? All our sacrifices. For what?"
        vivithinking "Damn! I thought I was having trouble coping."

        #<CHOICE>
        vivi neutral "Look, Asha..."

        menu:

            #OPTION 1 +ATTRACTION +DECAY
            "...chin up, princess, or the crown slips.":

                vivi neutral "...chin up, princess, or the crown slips."
                ava angry "Princess? We were not royalty, those inbred lickspittles. We came from 
                nothing."
                vivi "More like stiff upper lip and all." 
                ava angry "Why?! We are no more! Our mother gutted us like a butcher does a fatted 
                calf."
                vivithinking "Unnecessarily graphic and undeniably tragic!!"
                vivi surprised "That's your people's tradition?"
                ava sad "We are sacrificed lest people love us too much. Once, an avatar nearly toppled 
                the royals. No longer."
                vivi neutral blush "Well, then no offence, but you're better off here. If your whole purpose 
                was sacrifice, then guess what?"
                ava happy blush "Then our service is at an end. We are free."
                vivi happy "Yes. I like that. Free."
                vivithinking "Not a great start, but a good ending, right?"
                #JUMP to vivi saying "Thank you for sharing with me, Asha."

            #OPTION 2 +ATTRACTION
            "...I know what you mean about sacrifices.":

                vivi sad "...I know what you mean about sacrifices. You're not alone. My career 
                always came first, over friends, family, lovers. Where'd it get me?" 
                vivi angry blush "Here!"
                ava angry "We shall fade to darkness, Vivi. Have you not seen it in your dreams?"
                vivi neutral "Dreams? Cards? Really? Seems to me your last sacrifice is over."
                ava happy blush "Then our service is at an end. We are free."
                vivi happy "Yes. I like that. Free."
                ava happy "Thank you, Vivi. We hope you return."
                vivi happy "Looking forward to it, Asha."
                vivithinking "Not a great start, but a good ending, right?"
                #JUMP to vivi saying "Thank you for sharing with me, Asha."

            #OPTION 3 +DECAY
            "...time to put on your big girl panties and deal with it, Asha.":

                vivi neutral "...time to put on your big girl panties and deal with it, Asha."
                ava angry "Perhaps you should heed your own advice, Vivi."
                vivithinking "Well, someone's got her big girl panties in a nasty twist!" 

        vivi neutral blush "Thank you for sharing with me, Asha."
        vivithinking "Maybe one of the others wants to talk."

        #JUMP to Character Selector 2
        jump cs2

    label fr1_darius:

        # FREE ROAM 1 - DARIUS - not sure how the jumps work

        #LOCATION: Lounge
        scene lounge

        show darius angry at center
        show vivi neutral at left

        "Darius- I can feel them. Seething."
        darius angry "Well. Cards, then?"
        vivi surprised "You actually want to play?"
        darius angry "Why not? Seems as though we can't do anything else at the moment."
        vivi neutral "I don't know a lot of card games."
        darius surprised "I thought that's all you humans did. Play games. Fritter away your time."
        "We'll play Hearts."
        "And we'll learn. About each other. About this place."
        "About Urshu."
        "Nice hands. Dextrous fingers. Manicured claws."
        "Oh- they've caught me looking. What is this? Displeasure? Embarrassment? Satisfaction?"

        # choice
        darius neutral "You start."

        menu:

        #OPTION 1 +ATTRACTION
            "Can you even play Hearts with two people?":

                vivi surprised "Can you even play Hearts with two people?"
                darius happy "Of course you can. Even a human can learn."
                vivi neutral "You deal so swiftly."
                darius happy blush "That's kind."
                vivi neutral "I'm surprised, given your history."
                "I see a flash of displeasure."
                darius angry "What could you possibly understand about my history?"
                # JUMP TO: "You still haven't played a card. Take your turn already."

        #OPTION 2 +DECAY
            "You mentioned Urshu. Why bring him up?":

                vivi neutral "You mentioned Urshu. Why bring him up?"
                darius angry "That little twerp knows more than he lets on."
                vivi surprised "You're getting angry."
                darius angry "Yes. You should be, too."
                vivi surprised "Why's that?"
                darius neutral "This place. I know it. We shouldn't be here."
                # JUMP TO: "You still haven't played a card. Take your turn already."

        darius angry "You still haven't played a card. Take your turn already."
        vivi neutral "Don't tell me what to do."
        darius neutral "There's no reason to get snippy with me. I'm not the one who trapped us all here."
        vivi neutral "Who are you calling 'snippy'? You're being aggressive. No way to talk to a lady."
        "That flare of rage again- so bright it's almost painful."
        darius surprised "Well. That's... interesting."
        vivi surprised "What is?"
        darius neutral "You're unreadable. That is... unusual."
        vivi neutral "I'm happy to answer any questions you might have about me."
        darius neutral "Why waste energy on words when I can simply read what's in front of me without them?"
        vivi happy "Ah, but you can't, can you? And you find that frustrating. Tell me about it."
        darius angry "You're needling me. Play a card, damn you."
        vivi happy "Not without knowing what's making you so testy."
        darius angry "I have never once been 'testy' in a millennia of existence."
        vivi happy "And yet... here I am, not playing a card."
        "That rage. Pure. So hot that it makes my cheeks flush."
        darius angry "Fine. Vivi. Normally I can read the beings around me. It's what makes me such an excellent judge of... character."
        "But since arriving here that's changed. I feel- cut off. Disarmed."
        vivi neutral "Darius, you shouldn't be reading my mind without asking first anyway. Bit rude."
        darius surprised blush "I- I'm not trying to-"
        vivi happy "Please don't do it again. Your turn!"
        darius neutral "Forgive me. All of this is new. As I said: unusual." 

        # choice 

        menu:

        #OPTION 1 
            "Qualify that. 'Unusual'.":

                vivi neutral "Qualify that. 'Unusual'."
                darius neutral "I don't know how else to explain it. Things were one way, now they're not. I'm... adjusting."
                vivi neutral "I guess we should do our best to adjust together."
                darius happy "We can try that."
                # JUMP TO: "They're silent. Is that good, or bad?"


        #OPTION 2 + ATTRACTION
            "That sounds difficult. Like being unmoored.":

                vivi sad "That sounds difficult. Like being unmoored."
                darius surprised "Yes, exactly. 'Unmoored.' You have a way with... words."
                vivi happy "Aw, you're just saying that. You think so?"
                darius angry "You're mocking me."
                vivi surprised "I'm not! Trust me. When I'm mocking you, you'll know."
                darius happy "Well then. I look forward to it."
                # JUMP TO: "They're silent. Is that good, or bad?"


        #OPTION 3 + DECAY
            "Well you don't hear me crying about it.":
            
                vivi neutral "Well you don't hear me crying about it."
                darius surprised "I'm sorry?"
                vivi neutral "You heard me. Things may be different but they aren't dire."
                darius angry "Not yet, anyway. Give it time, Vivi. You're just like the rest of your kind."
                vivi angry "You don't know me, Darius."
                darius neutral "I never claimed to."
                # JUMP TO: "They're silent. Is that good, or bad?"

        "They're silent. Is that good, or bad?"

        vivi neutral "You're doing a terrible job at playing this game."
        darius neutral "It would seem so. And it was my suggestion. Apologies. Perhaps another time when I'm less... distracted."
        # JUMP TO: character selector?
        jump cs2

    label fr1_susurha:
        #FREE ROAM 1 - SUSU'RHA

        #LOCATION: Dining Car
        scene diningcar

        #VISUAL: screen shakes.
        #SOUND: the dining car's door slams shut.

        show susurha neutral at right
        show vivi neutral at left

        #SOUND card shuffle

        susurha happy "Well met, Vivienne, you seem like one who enjoys a good game."
        vivi "What's the game?"
        susurha "Truth or Lies."
        vivi  "What's at stake?"
        susurha "Everything. After all, we're riding a slowly decaying death-train headed inexorably toward the cosmic weave."
        vivi "I'm not sure..."
        susurha  "Don't be coy. It doesn't suit you."
        vivi angry "I'm not coy. I'm hesitant to reveal intimate details to a stranger..."
        susurha happy "Stranger than you can imagine."
        susurha  "Time is of the essence. Sit with me, and together we'll find out what's true, and what isn't."

        # <CHOICE>
        vivithinking "Provocative. This one's certainly not boring." 

        menu:

        #OPTION 1 +Attraction
            "I'll play.":
        
                vivi "I'll play"
                susurha "Indeed you will. There's nothing quite like inappropriate personal questions to enliven the mood." 
                #JUMP to susurha saying "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."

        #OPTION 2 +Decay
            "I'd be revealing too much.":

                vivi "I'd be revealing too much."
                susurha "Are you scared I may pierce your carefully crafted veneer?"
                vivi angry "I'm a reporter. I don't do masks. I expose the masks of others."
                susurha "Either you are a bad liar, or you're suffering from an acute lack of self-awareness."
                vivithinking "The nerve of this creature!"

                #JUMP TO: susurha saying "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."

        susurha "I'm going to ask you a question. You will answer, and I will try to ascertain whether or not you are lying."
        vivi "That's it?"
        vivi "Hit me." 

        # <CHOICE>
        susurha "The card reads, 'You are hiding something.'"

        menu:

            #OPTION 1 +Attraction
                "Everyone hides something. I'm no exception.":

                    vivi neutral blush "Everyone hides something. I'm no exception."
                    susurha "I'm the exception. All my pretence has been burned away."                                                  
                    susurha  "..."
                    vivithinking "Why are they looking at me like that?"
                    susurha "The fire."  
                    vivithinking "The what?"
                    susurha "You're hiding fire."                         
                    vivithinking "I know what they're going to say..."
                    #  JUMP TO: susurha "You're... angry."
                    

            #OPTION 2 +DECAY
                "What exactly are YOU hiding behind those beady eyes?":

                    vivi "What exactly are YOU hiding behind those beady eyes?"
                    susurha surprised "Deflection!"
                    susurha  "A keen observer of everything but yourself."                            
                    susurha "Do you know what I see when I look into your eyes?"
                    susurha "A boiling ocean of fury."
                    vivithinking "How could they tell?"
                    vivi "Of course I'm angry. I didn't expect to die."
                    susurha "This goes deeper. And it's been going on for a long time."
                    #JUMP TO: susurha "You're... angry."

        susurha "You're...angry."

        # <CHOICE>
        vivithinking "What if they're right?"

        menu:

            #OPTION 1 +ATTRACTION
                "I am angry.":

                    vivi angry "I am angry."
                    vivithinking "And the cocky bastard leans back in their chair with a smile. Right on cue..."
                    susurha happy "You know what, for all my years frolicking, I believe I am too."    
                    vivi   "Who are you angry at?"
                    vivithinking"..."
                    vivithinking "That wiped their smile away."
                    susurha angry  "My... parents, the judgemental cretins."
                    vivithinking "Their exhale is literally hot. Wow."
                    vivi angry  "Okay back to me then..."
                    vivi angry "I'm angry at my ex-boyfriend. He tried to own my wins."
                    susurha angry "Sounds like.. the courtiers I grew up around! Those leering, grasping snobs, interminable features of my childhood!"
                    susurha "What else? Don't spare the sssavory details."
                    vivi angry "My ex-girlfriend stole my Datsun and got it towed in another state!"
                    vivi angry  "And...and...my teacher, Mizz Costello. She told me I was pugnacious. And she meant it as an insult!"
                    vivi angry  "The entire school system sucks! All systems do! Society at large!"
                    susurha angry  "Society! Oh, how I hate Society! I fled all the way to the Viridian forest to escape it!"           
                    vivi happy "The EXPECTATIONS of people who, at the end of the day, JUST DON'T MATTER!"
                    susurha happy  "YES!"
                    vivi   "But most of all, my agent, Chloé. It was she who told me to get the scoop on this cursed death train." 
                    susurha "And here we all are."
                    #JUMP to vivithinking "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"


            #OPTION 2 +DECAY
                "You're the one who's angry.":
            
                    vivi angry "You're the one who's angry."
                    susurha happy "Again, you're deflecting."
                    susurha angry "But you are right. I'm furious."
                    vivithinking "that exhale's like, 150 degrees. Hate to see them truly mad."
                    susurha angry "The bloodsuckers. The comers. Those with souls impervious to art and music. All of them infuriate me to no end!"
                    vivithinking "My face is literally burning."
                    susurha neutral "..."
                    susurha happy "It feels good to let it out. You should try it."
                    susurha  "That mask you wear. it extracts a toll you see. I know because I have been the way you are now."
                    vivi angry "..."    
                    vivithinking "What do they mean, 'that mask you wear'?"
                    vivi neutral "Calm down, Vivienne."
                    #JUMP to vivithinking "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"

        vivithinking "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"

        susurha "I think we got what we needed from this. I imagine whoever runs this place did too."
        susurha "See you around, dear Vivienne."

        hide susurha

        vivithinking "That was a lot. I'm going back to my room."

        #JUMP to Free Roam 2 - Character Selector
        jump cs2

    label cs2:
        #Character Selector 2

        #LOCATION: cabin
        scene cabin

        show vivi neutral at left

        vivi angry "I feel like I'm getting nowhere! How the hell am I supposed to escape this?"

        vivi neutral "I can already see the outside affecting the train. This whole place is slowly dissolving into... I don't know and I don't wanna find out."

        vivi neutral "I need some time to make a plan of escape."

        #fade out

        #fade in

        vivi angry "I can't think straight! My mind is a mess. I need to cool off if there's any chance of me creating a solid plan."

        #CHOICE
        vivi neutral "I think I saw a dartboard in the dining car. It may be a good way to blow off some steam. Maybe I can get a fellow passenger to join me. Competition always helps me think clearer."

        menu:
        #OPTION 1
            "Avatar of Asha":

                vivi neutral "Lets see how good the goddess is at darts, shall we?"
                #JUMP to Free roam 1 / Avatar of Asha
                jump fr2_ava

        # #OPTION 2
        #     "Inquisitor Darius Wrecker":

        #         vivi neutral "Darius seems like good competition."
        #         #JUMP to Free roam 1 / Darius Wrecker

        #OPTION 3
            "Susu'Rha Balrinn":

                vivi neutral "I'm sure Susu'Rha would be down for a little competition."
                #JUMP TO: Free roam 1 / susurha Balrinn
                jump fr2_susurha

    label fr2_susurha:
        #FREE ROAM 2 - SUSU'RHA

        #LOCATION: Dining Car
        scene diningcar

        show vivi neutral at left
        show susurha neutral at right
            
        susurha "What exactly is this... 'darts?'"
        vivi "You toss pointed sticks at that round board over there. You score points based on how well you hit the target, and if you score enough points, you win."
        susurha "In the Viridian Wood we played a game similar to this. Instead of a round board, we used the carcasses of Burrowers."
        vivithinking "Wow, that's kinda gore." 
        susurha "And we used magic to increase our accuracy."
        vivithinking "Well then, nice of you to be born in a magical world."

        # <CHOICE>
        susurha "Doubtful you could best me in a contest of accuracy." 

        menu:

        # OPTION +ATTRACTION
            "The arrogance on this one. I'd sure love to shut them up.":

                vivithinking "The arrogance on this one. I'd sure love to shut them up."
                vivi "Magic or no, I'm going to beat you."
                susurha "I will give you the grace of going first."

                #SOUND: Dart hits the board.

                vivi happy "Bullseye!"
                susura angry "Bullseye?"
                vivi happy "A bullseye is when you hit the dartboard dead center."
                #SOUND: Dart hits the board.
                susurha happy "Mine hit close, does that count for something?"
                vivi happy "Not as much as a bullseye!"
                susurha surprised "Hmm... seems my magic doesn't work here."
                vivi happy "Either that or I'm better at darts than you."
                # JUMP TO: "How did you get here?"

        # OPTION 2 +DECAY
            "Clearly they feel insecure - I'm going to let them win.":

                vivithinking "Clearly they feel insecure - I'm going to let them win."
                vivi "You go first."
                
                #SOUND: Dart hits the board.

                susurha happy "I made it onto the board!"
                
                #SOUND: Dart hits the board and then the floor.
                vivi angry "I didn't."
                susurha "Am I supposed to believe that you can't hit the board from this distance?"
                vivi neutral blush "..."
                vivi "Sorry. It seemed like you could use a win. After being banished from your kingdom, and well, dying."
                susurha "Actually, I banished myself." 
                susurha "And I'll thank you for not patronising me by pretending to be something you're not--in this case, bad at the darts game."

                #SOUND: Dart hits the board.

                vivi "What?"
                susurha surprised "You seem almost relaxed."
                vivi happy "I am. For a moment I almost forgot how I got here."
                # JUMP TO: "How did you get here?"

        # <CHOICE>
        susurha  "How did you get here?"

        menu:

        # OPTION 1 +ATTRACTION
            "It was an assignment given to me by my agent.":

                vivi "My agent told me to write an exposé about a mysterious train line, with an enigmatic conductor."
                vivi happy "I said yes because it reminded me of those internet horror stories I grew up with."
                vivi "Seems the stories swirling around the Ouroboros Express were more than stories."
                vivi sad "Now I'm dead..."
                show susurha sad
                vivi sad "I'm going to miss living."
                #JUMP to susurha: "So the fault lies with your "agent.""

        #OPTION 2 +DECAY
            "I didn't have a choice.":

                vivi angry "I didn't have a choice."
                susurha "Do tell."
                vivi angry "I'm a reporter. I go where the story is."
                vivi sad "What a silly reason to die."
                #JUMP to susurha: "So the fault lies with your "agent.""

        susurha "So the fault lies with your 'agent.'"
        vivi "Yeah."

        #SOUND: Dart hits the board.

        susurha "Why don't you envision your 'agent' being at the target's center?"
        vivi happy "Okay."
        susurha  "Now, hold that dart firmly in your hand."
        susurha "Concentrate on the board. See 'Chloe'..."
        susurha "...And let go."


        #<CHOICE>
        "Chloe..."

        menu:

        #OPTION +Decay
            "Pierce Chloe!":

                vivi angry "Pierce Chloe!"
                vivi angry "It's all her fault!"
                vivi angry "HER!"
                vivi angry "SHE had to discover this 'exclusive story'."
                vivi angry "SHE had to get me to come here!"
                vivi angry "SHE killed me!"
                vivi angry "It's HER FAULT!"
                susurha happy "Bullseye!"
                #VISUAL: The screen shakes.
                susurha "Want to know what brought me here?"
                #JUMP to susurha: "It was fear that brought me."

        #OPTION +Attraction
            "Pierce the idea that it was her fault.":

                vivi "Pierce the idea that it was her fault."
                #SOUND: Dart hits the board.
                susurha "Another bullseye."
                vivi "It's not her fault. It's mine."
                vivi angry "I was the master of my fate and I chose to come here!"
                vivi sad "How galactically stupid."
                #JUMP to susurha saying "It was fear that brought me."

        susurha "It was fear that brought me."
        susurha "It was a night like any other. The stars were out in their most intense configurations."
        susurha "First there was rumbling."
        susurha "Then there was smoke. So much of it. Everyone ran as fast as they could."

        susurha sad "That's when I saw it."
        susurha sad "My city. Where my family have lived for a hundred generations, besieged by Tellethor's great army."

        vivithinking "Oh wow."

        vivi sad "What did you do?"
        susurha "I ran toward home."
        susurha angry "I thought that if I could just GET THERE, I could save them."
        susurha neutral "But the smoke was too much. None of us could see. Soon, I couldn't breathe."
        susurha "Then...a sharp pain and...darkness."
        susurha sad "I woke up here."
        susurha angry "I have no idea whether my family--that I abandoned--is okay. My fear is I'll see them walk into this dining car, like me, wondering what happened."
        susurha angry "If only I was there to protect them."

        # <CHOICE>
        susurha sad "They died because I was afraid."

        menu:

        #OPTION 1 +Attraction
            "You did what you could. It isn't your fault.":

                vivi sad "You did what you could. It isn't your fault."
                susurha sad "Thank you. That means something."
                
                #SOUND: A dart smacks the board.
                #VISUAL: The screen shakes.
                vivithinking "At least there's darts."

                vivi  "I'm going to miss taking pictures."
                susurha  "I'm going to miss playing my lute under the stars."
                vivi  "I'm going to miss Internet forums. Seeing just the craziest, nonsensical things people would think to share with others."
                susurha happy "Sounds delightful."
                susurha happy "I'll miss sharing my singing voice with those who would listen."
                vivi happy "I'd love to hear your singing voice."
                susurha happy "I would happily sing for you."
                susurha sad "Quiet moments. I will miss those moments the most."
                vivi sad "I can't tell you the last time that I was alone with my thoughts."
                susurha  "Perhaps now is a good time."
                #JUMP to susurha: "Well, this has been fun as always, but I wish to return to my cabin to enjoy what your humans refer to as a quiet moment."

        #OPTION +DECAY
            "We got a raw deal. Life is unfair.":

                vivi angry "We got a raw deal. Life is unfair."
                susurha angry "Certainly nothing about our present situation is fair."
                vivi angry "I HATE this train!"
                vivi angry "And the conductor. It's his fault we're here."
                susurha angry "He runs this place."
                vivi angry "He could let us off if he wanted."
                susurha angry "Instead, he toys with us for his own enjoyment. Only a devil behaves this way!"
                susurha "But there's nothing we can do."
                vivi angry "No. Perhaps that's the lesson."
                susurha "..."
                vivi "..."
                #JUMP to susurha: "Well, this has been fun as always, but I wish to return to my cabin to enjoy what your humans refer to as a quiet moment."

        susurha neutral "Well, this has been fun as always, but I wish to return to my cabin to enjoy what your humans refer to as a quiet moment."

        hide susurha 

        vivithinking "I should steal a quiet moment for myself."
        vivithinking "I may not get many more chances."

        #JUMP TO: Debrief Anger
        jump debrief_anger

    label fr2_ava:

        #FREE ROAM 2 - ava
        scene observatory

        "Strolling into the observatory, I expect the Avatar to be where she usually perches. Instead, her short figure faces away from me, the sound of darts plunking into a corkboard fills the room."

        #SOUND Dart hitting the board

        ava neutral "Care for a game of darts? We hear the watering holes on Earth tend to host these sorts of events quite frequently." 
        vivi neutral "Watering hole? You mean a pub?"

        #SOUND Dart hitting the board 

        ava natural "There exists no such term on Soleos."
        vivi happy blush "Well I guess you could technically call it a watering hole, as strange as that sounds. But we call it a pub...or a bar if they don't have Guinness."
        vivi happy blush "What was your life like back home?"
        ava happy "As the Avatar of Asha, servants catered to our every need, people worshipped us...But beneath that outer layer there was no friendship, no family. These simple pleasures were forbidden." 
        vivi surprised "My God, that sounds..."
        #CHOICE
        menu:
        #OPTION 1 +DECAY
            "Amazing.":
                vivi happy "...amazing. Sometimes I wish I could be alone, always."
                ava sad "We would not wish that upon even our monarchy."
                #SOUND Dart hitting the board
                #JUMP to ava saying "Your turn, little one."
        #OPTION 2 +ATTRACTION
            "Awful.":
                vivi sad "...awful. I'm so sorry. I can't even begin to imagine."
                ava sad blushing "Thank you...that means more to us than you know."
                #SOUND Dart hitting the board
                #JUMP to ava saying "Your turn, little one."

        #OPTION 3
            "Crazy.":
                vivi neutral "...crazy. Your life is like a rollercoaster!"
                ava neutral "A...rollercoaster?...We do not quite understand the meaning of this word."
                vivi happy "It's something that moves quickly with lots of ups and downs."
                ava neutral "We...still struggle to grasp why you have this torture device, but your meaning is clear.."
                #SOUND Dart hitting the board
                #JUMP to ava saying "Your turn, little one."

        ava happy "Your turn, little one."
        vivi angry "I thought I asked you to stop calling me that."
        ava "Oh, do not take offence; it is a term of endearment. We are warming up to you."
        #SOUND Dart hitting the board
        vivi angry blush "Well...it's still demeaning. I don't like it."

        #CHOICE
        menu:
        #OPTION 1 +DECAY
            "But if you like it...":
                vivi happy blush "But if you like it...I guess I could get used to it."
                ava happy blush "It would not befit us to keep using a name you do not prefer. We never wish to offend you."
                vivi happy blush "You could never offend me, Asha."
                vivithinking "I'll do anything she wants if I get to spend some more time with her..."
                #SOUND Dart hitting the board
                #JUMP to vivi saying "Anyways..."

        #OPTION 2 +ATTRACTION
            "Don't ever call me that again.":
                vivi angry "Don't ever call me that again. I don't like it. I'm not your pet."
                ava sad blush "By Asha, we beg your forgiveness. Our intent was never to hurt you."
                vivi sad blush "It...just brought up some old memories. I'm sorry I snapped at you."
                vivithinking "My high school boyfriend used to call me little one in a Yoda voice...never again."
                #SOUND Dart hitting the board
                #JUMP to vivi saying "Anyways..."

        #OPTION 3 
            "My old roommates used to call me dildo":
                vivi blush "My old roommates used to call me dildo."
                ava surprised "And what is a dildo?"
                vivi blush "It's a...personal massage device of sorts. For...relaxation?"
                ava happy "Oh! We have had that before. The orgy after was the best part!"
                vivi happy blush "Oh! I didn't realize that was such a common practice on your planet."
                ava happy blush "Perhaps our other customs might intrigue you?"
                vivithinking "Write that down. WRITE THAT DOWN!"
                #SOUND Dart hitting the board
                #JUMP to vivi saying "Anyways..."

        vivi neutral "Anyways...I've been meaning to ask you:"

        #CHOICE
        menu:
        #OPTION 1 + DECAY
            "Has the advanced civilization of Soleos-":
                vivi neutral "Has the advanced civilization of Soleos affected the religious practices of its citizens?"
                ava happy "We are glad you asked. Yes, absolutely. Our science is part of our religion. We use it to transmit the voice of the Avatar to every household to hear our message."
                vivi surprised "Wow, wow."
                ava happy "Through our architecture and technology, we can reach every Soleoan."
                #JUMP to vivi saying "How...interesting."

        #OPTION 2 + ATTRACTION
            "What do you want to do with your time left?":

                vivi neutral "What do you want to do with your time left?"
                ava sad "..."
                ava neutral "We are enjoying the view. Nothing on Soleos like it."
                vivi happy "It is pretty nice, huh." 
                ava happy blush "But we would not mind spending some more time getting to know you."
                #JUMP to vivi saying "How...interesting."

        #OPTION 3
            "What are your thoughts on our conductor":

                vivi neutral "What are your thoughts on our conductor?"
                ava surprised "We have been meaning to speak with you about this. Do you think he is...alive?"
                vivi surprised "I didn't realize you were thinking about things like that. Personally...I think he's undead."
                ava surprised "Like...a zombie?"
                vivithinking "Wow she sounded almost human for a minute."
                ava angry blush "Why do you smile like that?"
                vivi happy blush "No reason!"
                #JUMP to vivi saying "How...interesting."	

        vivi neutral "How...interesting."
        #SOUND Dart hitting the board
        vivi angry "Shit..."
        ava angry "We wish you would refrain from those words...we find them...off-putting"
        vivi surprised blush "Well Asha, I'm going to keep using them anyway. If you want to get to know me better, you're going to have to put up with that language. 'Cause that's just who I am!"
        ava angry "Hmph. And to think we even thought you special..."


        #CHOICE
        menu:
        #OPTION 1 + ATTRACTION
            "Don't play games with me, bitch.":
                vivi angry "Don't play games with me, bitch. You may have been some kind of royal deity when you were alive but we're all equals in death now."
                #JUMP TO ava saying "You dare! Refer to us as Asha or not at all!"

        #OPTION 2 + DECAY
            "I'm over your bullshit, dude.":

                vivi angry "I'm over your bullshit, dude. Just because your crazy cult revered you doesn't mean that I'm going to."
                #JUMP TO ava saying "You dare! Refer to us as Asha or not at all!"


        ava surprised blush "You dare! Refer to us as Asha or not at all!"
        vivi angry "I'll call you whatever I damn well please."
        ava angry "Leave us, now."
        #*pause*
        ava angry blush "Such impertinence, even the royalty ...they never treated us so. Did you forget our conversation from earlier?"
        vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."
        ava sad blush "Please...go."

        hide ava

        vivithinking "Time to leave. I messed up. Let's try again tomorrow, maybe she'll accept my apology."

        hide vivi

        #JUMP to Debrief Anger
        jump debrief_anger

    label debrief_anger:
        #Debrief Anger

        #LOCATION: cabin
        scene cabin

        #ATTRACTION ROUTE
        "(attraction route)"

        show vivi neutral at left

        vivi neutral "Well that was interesting. Didn't expect to get that deep with anyone on this train. Don't think I've been that open with anyone before."

        vivi happy "It was refreshing. I'm glad I'm not alone here. It's nice to feel truly heard. Nobody wanting or expecting anything from me. Just two beings trying to understand each other."

        vivi neutral "I should journal my thoughts."

        #Journal entry with attraction meter high

        "(journal entry)"
        "Talking to the other passengers has helped put things into perspective. They're not so bad after all. I won't get off this train by fighting. I need more info on the conductor. He's my ticket off this ride. He seems like one who'd appreciate an exchange for his aid. Maybe some of the other passengers can help me. They seem as keen to leave as I am."

        # JUMP to Briefing Bargaining

        # DECAY ROUTE
        "(decay route)"

        show vivi angry at left

        vivi angry "I feel like the only one trying to get off this train. How are people content with playing silly card games when their lives are at stake? And the conductor! He knows he's messing with me and gets off on it."

        vivi neutral "Take a deep breath, V. This isn't getting anywhere."

        vivi neutral "Fighting with everybody is obviously not gonna work. Maybe I can get what I want another way. Urshu is the key. He must want something."

        vivi neutral "I should write."

        # Journal entry with degradation meter high
        "(journal entry with degradation meter high)"
        "This whole thing is pointless! That conductor... URG! I wanna strangle him and wipe that stupid smirk off his face. Talking to him is like solving a riddle. It's infuriating! Gotta find something on him. Maybe the others know a thing or two. There's gotta be some way to make Urshu help me. He seems like one who'd appreciate an exchange for his aid."

        # JUMP to Briefing Bargaining



    return
