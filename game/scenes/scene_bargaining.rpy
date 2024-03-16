### EXAMPLE OF TEMPLATE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene_bargaining:

    #Briefing Bargaining
    # LOCATION: cabin
    scene cabin

    "Vivi rises early. Well, it may or not be early as the Ouroboros Express goes. Diurnal and nocturnal cycles are meaningless in this uncertain dimension."

    show vivi neutral at left

    "Vivi yawns."

    vivi neutral "God, why don't I feel rested?"
    vivi happy "Time to get the drop on Urshu. Yeah, that's right. I'll surprise him before he's had his fabuloso-lime-expresso and see how he feels!"
    "..."
    vivi neutral "Hold on, Vivi, that's not how you run down a lead. You gotta start with what you want and what you know."
    "I know what I want: to stop my forthcoming eternal demise. What I know: Urshu is an immortal, silver-tongued courier of the dead who's probably tasted and seen everything life can offer. What could I possibly bargain with him over?"
    "But...he has told me a bit about his past. I get the feeling he's lonely. That he longs for something. For what? Doesn't matter. I can relate to a deep sense of unsatisfied longings."

    label bargaining_search:
        menu:
            # OPTION 1
            # CHOICE
            vivi "Where should I look for that little peach?"
            # Urshu not here
            "Lounge":
                
                vivi neutral "Let's try the lounge."

                vivi neutral "Let's try the lounge."

                # LOCATION: lounge
                scene lounge

                show vivi neutral at left

                vivi neutral "Welp. He isn't here. Nobody's here."
                "Vivi peers into the empty room. It's quiet. Disquietingly quiet. Vivi is disquieted. Why? Perhaps the violent, raging rainbows flashing by in the windows. Or the way the leather chairs are giving off fumes of aging creosote. Is the room getting smaller all of a sudden, or?"

                vivi "I'm out."
                # JUMP TO: vivi saying "Where should I look for that little peach?"
                jump bargaining_search


            # OPTION 2
            # Urshu not here
            "Observatory":
                
                vivi neutral "Perhaps Urshu's enjoying the stars."

                vivi neutral "Perhaps Urshu's enjoying the stars."

                # LOCATION: observatory
                scene observatory

                show vivi neutral at left

                vivi neutral "Goddamn. He isn't here."
                "Can't deny that view, though."

                "Vivi cranes her neck to get a better look. The universe unfurls before her, wondrous and terrifying. It's so large it hardly moves even with the great speed of the Ouroboros Express."

                "Are those shooting stars?"

                #EFFECT: Zoom in.

                "A pair of galaxies appear to be shifting, growing larger. They align themselves to be parallel, looking to Vivi like burning reptilian eyes, one bright white, one searing red."

                "What--"

                "A shadow crosses over her face. She speaks with a voice that is not her own."

                "I see you, child of We. Child of stardust. Child of mine emptiness. Come to me. Lead them all to me. Embrace the end of yourself and the end of all..."

                "She comes back to herself, chilled and queasy."

                "S--something just...what the shit?"
                "I gotta get the hell off this train. I gotta find Urshu."
                # JUMP TO: vivi saying "Where should I look for that little peach?"
                jump bargaining_search


            # OPTION 3
            # Urshu is here
            "Bar":
                vivi neutral "I'd bet he's at the bar polishing spoons and staring at his reflection."

                # LOCATION: diningcar
                scene diningcar

                show vivi neutral at left

                vivi "There he is. Time to wrangle him down..."

                "Her imagination gets a lil' spicy."

                "For clues! For information."
                "Hold on. He doesn't look himself."

                #JUMP TO: Urshu is slouched...

    "Urshu is slouched forward over the bar, staring into the shallow vacuum of an empty espresso cup."

    show urshu sad at right

    urshu sad "What I wouldn't give...just one more dance with you in the Queen's Gardens..."

    "Vivi creeps up."

    urshu neutral "Miss Sanssouci. You must know I cannot be surprised from beside, before, or behind. I can hear the sound of your soul steps wherever you traipse on this train."
    "Please, sit. Here, I have a cup for you."

    vivi neutral "You...of course you knew." 
    "She sips the coffee."
    "Holy shit. This could wake the dead."
    "Maybe if I drink enough of this I can get my life back."
    "She slams it back. Closes her eyes. Opens them."
    "Nope, still dead."
    "Thanks for this, Ursh. You take good care of me. When you're not being a petulant pissant."
    urshu happy "I appreciate that, Miss Sanssouci. I do work very hard for all of you. It is my joy to serve--not only to serve, but to draw out of each of you your best."
    vivi neutral "Oh, he's being sweet. And candid. And not talking in riddles!"
    "You sure have a funny way of doing that. Less heart masseuse, more a maniacal miner drilling away at my sanity."
    urshu happy "I appreciate that metaphor. It lends to you this unspoken truth: you and your companions are diamonds who have convinced themselves to be of lesser materials."
    vivi happy blush "Wow...that's...you're..."
    "This bitch is getting to me! Red alert! Red alert!"
    urshu neutral "Would you share a quiet moment with me? Here, let me refill your cup."

    "They sit together, sipping, saying nothing. This shared solitude fills them both up."

    "Vivi's mind stirs. This moment is lovely, but it's not enough."

    vivi neutral "I could almost die happy. Yet--"

    "Her heart races. Is it the caffeine? Is it Urshu's shoulder, brushing against hers? No. She can't stop whatever THIS is. A hunger. A panicked for life."
    "She wants her life back."
    vivi "Urshu, look at me."
    urshu "Yes, Miss Sanssouci?"
    "She looks into his brown eyes, deep as those timeless rivers he once crossed, still crosses."
    vivi "I need to do this delicately. With tact and poise and--"
    "Urshu, I want my fucking life back."
    urshu neutral "Do you truly, Miss Sanssouci? Is this afterlife not to your liking?"
    vivi "Do I have to spell it out? No. He's toying with me again. Bitch! Just when we were having a moment."
    "No, I'm not happy here. Yes, I have distractions and good people and tasty espresso, and even you spice up my life..."
    urshu neutral "But, Miss Sanssouci?"
    vivi "I have crow's feet! Flaky skin! I look out these windows and I see death! So what if I find love here? It's just gonna end!"
    "Hot tears have crawled down Vivi's lovely cheeks."
    vivi angry blush "Don't you get it?" 

    "Urshu gently dabs at her eyes with a fresh cloth that smells like a strange mix of cinnamon and pepper and truffle."

    vivi neutral "Let me try again."
    urshu neutral "Of course, my dear."
    vivi "I want off this train. Ideally, I want everyone to get off--"
    "Ha!"
    "and get back to their lives."
    "I'll do anything to make it happen."
    urshu "What if I wanted to get off--"
    vivi "EEP!"
    urshu "...this train, Miss Sanssouci? Just like you?"
    vivi "I'd take you in a heartbeat. But I'm not the one with power here. You are."
    urshu "I cannot be certain what you mean. I am a steward. I am a mystical steward, I can grant you that. But powerful?"
    "Urshu sucks in air through his teeth."
    "All the power lies with you, my diamond."
    vivi "Whooooomama. No one's ever called me that."
    "I wanna make a deal with you, then. It's in my power to offer you much. I want to give you something you haven't had in recent memory."
    urshu neutral blush "Oh my, Miss Sanssouci. You presume too much."
    vivi "If only..."
    "Ursh, not like that."
    "I'd do it right now."
    "But something else. Something you'd truly value."

    # <CHOICE> 
    vivi "Something that..."

    menu:

        # OPTION 1
        "Reminds you of your lost love.":

            vivi neutral "Reminds you of your lost love." 
            urshu angry blush "Don't you dare claim you can do such a thing."
            urshu sad "I cannot hope for what I know is impossible."
            vivi sad "Ursh...I'm sorry. I didn't mean."
            "M'kay, time to take a risk."
            "I did overhear you before coming up to you. You wished you could dance with someone?"
            urshu neutral "Yes. But there are other ways to dance. Other senses to entwine and tango with."

            # JUMP TO: urshu saying "Take this coffee, for instance."

        # OPTION 2
        "Takes you back to your first days ferrying souls.":

            vivi neutral "Takes you back to your first days ferrying souls."
            "Maybe I can get him to tell me more about the Ouroboros Express."
            urshu neutral "I remember those days fondly, yet they offer nothing more for me. Most immortals like myself have a near-perfect memory, so there is little to re-experience. Nothing to regret in those ancient libraries of my mind."
            vivi surprised "It pays to be immortal, I suppose."
            "I could use a memory like that for my reporting."
            urshu "Perhaps you and your friend Ava could discuss her oldest memories??"
            vivi "Hold it, right there, partner. Don't dissemble. It sounds like you have some regrets.?"

            # JUMP TO: urshu saying "Take this coffee, for instance."


    urshu neutral "Take this coffee, for instance. I have it at the same time every day. The same coffee. The same luxurious, velvety liquid flooding over my tongue with its bite and savor. It dances down my throat, indeed, down into my being."
    vivi "Kinky."
    "I long to have this feeling consume me, in my totality. Don't you wish that, sometimes? To be absorbed in a bliss so powerful and certain that nothing else can shake it."
    vivi "Coffee and longing? How is this helpful?" 
    "Urshu says nothing for a long moment. He simply inhales the aroma off hot bean water (that's literally what it is, folks) and then sips the espresso delicately, aerating it over his tongue and teeth."
    vivi "He seems enthralled with his senses. That's something he craves. What could possibly--"
    "Vivi freezes."
    urshu "Miss Sanssouci...?"
    vivi happy "Urshu, has anyone ever made you a meal? Like a whole, cooked-from-scratch meal?"
    urshu neutral blush "You know, I cannot recall...well, there was this singular occasion." 
    urshu happy blush "But that is not relevant. I would love nothing more than for someone to proffer for me an extravagant meal, a feast for the senses!"
    vivithinking happy "Got him! Yes. Now, for the bargain."
    vivi happy "Rein it in there, Ursh. I won't do this for free. I can give you what you want--"
    "And more!"
    "and you know what I want."
    urshu neutral "Oh? You think you can prepare a meal worthy of an exit ticket? My dear, there is no forthcoming terminus with a train that leads to life. Not for you or anyone."
    vivi "I don't believe that. You aren't beholden to some greater deity or being. You're Urshunabi, god of the passages between life and death. You have real power. You can, as you say, sense my soul steps. That's not something anyone without power or influence can do."
    "So, here's the deal: I make you a fucking feast, and you get me off this damned train."
    "Urshu is taken aback, at first. He holds Vivi's brilliant gaze. He has been seen. She has let herself be seen. This exchange means something to him."
    "He offers her his open hand."
    "Vivi takes it."
    urshu "I look forward to whatever you produce."
    # urshu exits
    hide urshu
    vivi happy "Yes! Nailed him! Time to blow his mind and his taste buds!"
    "But I can't do this alone. I need a sous chef. Luckily I have people from distant lands who can add their own twist on things..."

    # JUMP TO: Character Selector 1

    label b_cs1:

        #Character Selector 1

        #LOCATION: cabin
        scene cabin

        show vivi neutral at left

        vivithinking happy "Yeah... Alright! There's an actual path off this train. All I have to do is satisfy the conductor."

        vivithinking neutral blush "Ahem... With a meal, I mean."

        # <CHOICE>
        vivithinking neutral "I need to figure out what the conductor's likes and dislikes. Hopefully one of my fellow passengers knows something. But which one?"

        menu:
        #OPTION 1
            "Avatar of Asha.":

                vivi neutral "I'm sure the goddess can help me out."
                #JUMP TO: Free roam 1 / Avatar of Asha
                jump b_fr1_ava

        #OPTION 2
            "Inquisitor Darius Wrecker.":

                vivi neutral "Darius must've gleaned something from the conductor's emotions."
                #JUMP TO: Free roam 1 / Darius Wrecker
                jump b_fr1_darius

        #OPTION 3
            "Susu'Rha Balrinn.":

                vivi neutral "Susu'Rha is probably the friendliest with Urshu. They must know something."
                #JUMP TO: Free roam 1 / susurha Balrinn
                jump b_fr1_susurha

    label b_fr1_ava:
        #FREE ROAM 1 - Ava

        #LOCATION: observatory
        scene observatory

        # SOUND: The train on its tracks.

        show ava neutral at left

        vivithinking "I stroll into the observatory and who do I see staring out the window into darkness but the sun goddess?"

        show ava happy

        # <CHOICE>
        vivi "I have a question for you, Asha..."
        menu: 
            # OPTION 1 +DECAY
            "Who or what is our mysterious train conductor?":

                vivi neutral "Who or what is our mysterious train conductor?"
                ava neutral "He is known by many names, the conveyor of souls. Charon? Urshu? Anubis? The trickster Hermes seems fitting, no?"
                vivi neutral "Think we can convince him to let us off?"
                ava sad "We know the will of the gods, Vivi."
                "(if decay)"# ?? DECAY
                vivi sad "Well, I guess you would, huh? So in layman's terms for me?" 
                ava sad "We are like a dog chasing its tail, round and round. Catch the tail, Vivi, 
                and you know their will."
                vivi sad "So no?"
                ava "The stars would all burn out first, Vivi. No."
                # END
                # JUMP TO: vivi saying "It's always memorable talking with you, Asha."

            # OPTION 2 <<ATTRACTION
            "If you could redo a past event, what would it be?":

                vivi neutral "If you could change something that might have caused this, what would it be?"
                ava sad blush "Once, we broke taboo. We found a bird, hurt and dying. We hid it, cared for it, grew attached to it."
                vivi neutral "What happened?"
                ava sad "We returned and found the prince and princess eating it. They had found it and decided to punish us."
                vivi angry "Those entitled little turds! How awful for you!"
                ava sad "Had we not taken the bird, we would not have lost it."
                vivi angry "If you hadn't taken the bird, it would've died alone and sooner!"
                ava neutral "This is true." 
                vivi neutral blush "At least you gave it some happiness at the end. That's gotta be worth something!"
                ava happy "We want to be happy at the end."
                #JUMP TO: vivi saying "It's always memorable talking with you, Asha."

            # OPTION 3 +ATTRACTION
            "That was a big sigh. Pebble in your sandal, Asha?":

                vivi neutral "That was a big sigh. Pebble in your sandal, Asha?"
                ava sad "Regrets, Vivi. Many. No Avatar is allowed a family, a name, men, even tears."
                # <CHOICE>
                vivithinking "Damn! Which one's worst?!"
                "(decay route)" #DECAY ROUTE 
                vivi surprised "Which one—?"
                ava angry "We have no answer."
                menu:
                    #OPTION 1 +DECAY
                    "No family?":

                        vivi surprised "No family?"
                        ava sad "Our mother gave us to Asha at birth, and then sends us back."
                        vivi suprised "Sends you back?"
                        ava sad "We are sacrificed. We are grateful we do not remember our mother 
                        or our death. Praise Asha."
                        #JUMP TO: vivi saying "I'm glad you made the most of it, Asha."
                    
                    #OPTION 2 +ATTRACTION
                    "No name?":

                        vivi surprised "No name?"
                        ava sad "We speak for our people, so we are all and we are one."
                        vivithinking "That puts a lot into perspective."
                        ava neutral "Better us than the royals. We care."
                        vivi happy "Since your service is over, why not name yourself?"
                        ava happy "Your idea has interested us."
                        #JUMP TO: vivi saying "I'm glad you made the most of it, Asha."

                    #OPTION 3 +ATTRACTION
                    "No tears?":

                        vivi surprised "No tears?"
                        ava sad "We have felt the onset once. We have never cried."
                        vivithinking "Explains a lot!"
                        "(if attraction)"# ?? ATTRACTION
                        vivi neutral "What happened?"
                        ava sad "A serving girl in the palace. We tried to befriend her."
                        vivi angry "Don't tell me something awful happened?"
                        ava sad blush "No. Far worse. We never saw her again."
                        # END
                        vivi sad "Yeah, I've been there before. Not quite like that, but people just up 
                        and left my life, tent stakes and all. It sucks."
                        ava sad blush "Strange you think sucking to be bad, but yes, we understand. 
                        Thank you for sharing with us."
                        #JUMP TO: vivi saying "I'm glad you made the most of it, Asha."

                    #OPTION 4 +ATTRACTION
                    "No men?":

                        vivi surprised "No men?"
                        ava happy "We never had one, but we knew many women."
                        "(if attraction)"# ?? ATTRACTION
                        vivithinking "Whoa! Did I underestimate Her Radiance?"
                        ava happy "When we go to lands run by women, our diplomacy always 
                        prevails, no matter the tongue."
                        # SOUND heartbeat
                        vivithinking "I think my pulse is pounding louder than the train. Wait! Is...she...flirting with me?"
                        # END
                        vivi happy blush "Well, practice makes perfect, right?"
                        vivithinking "OMG AWKWARD, VIVI!!"
                        ava happy "Practice makes us better always."
                        #JUMP TO: vivi saying "I'm glad you made the most of it, Asha."

                vivi happy blush "I'm glad you made the most of it, Asha."
                "(if attraction)"# ??ATTRACTION
                ava happy blush "We sighed differently then. And we sigh looking at you now."
                # END
                # JUMP TO: vivi saying "It's always memorable talking with you, Asha."

        vivi neutral blush "It's always memorable talking with you, Asha."
        ava neutral "Indeed. Goodbye, Vivi. The All is the One."
        vivithinking "That was something. Wonder if the other two can help me?"
        jump b_cs2

    label b_fr1_darius:
        #FREE ROAM 1 - Darius

        #LOCATION: lounge 
        scene lounge

        show vivi neutral at left

        show darius sad at right

        vivi neutral "Now that's a curious sight. Clutching their forehead like they had a bad hangover?"

        vivi neutral "Rough night?"

        darius sad "You could say that. The dragon, Susu'Rha, was it? Their thoughts are so loud. I could barely sleep."

        vivi neutral "It's always the thoughts with you. You can't just... turn that off?"

        darius sad "Normally I can! That's how incessant it was! Like a stampede of preschoolers rambling on and on about the most inane concepts."
        vivi neutral "Well, hopefully I have a little less of an inane topic to discuss."

        darius neutral "Oh you could never be so inane Vivi. You're far too inquisitive. Some would say nosy."

        vivi neutral "Ahh, you're far too polite. Some would say distant, even."

        darius happy "Haha, yes, I do love our little chats. So? What is it?"

        vivi happy "Have I ever told you you're quite charming?"

        darius neutral "Oh gods, here she starts."

        vivi happy "Such a vast intelligence, but always holding it tight to the chest. So many thoughts and words, but only picking out a select few."

        darius neutral "I can tell this is killing you. Come on, out with it."

        vivi neutral "Surprisingly, no, I'm being honest. But they don't have to know that."

        vivi neutral "Really? I was just getting to your deftly manicured hands and perfect skin."

        darius angry blush "I-- no! Enough of this. Get to the point already!"

        vivi neutral "Fine, fine. Can't blame a girl for having a little fun in the afterlife, can you?"

        vivi neutral "Urshu. Have you tried using your abilities on him? Get a good mental read?"

        darius happy "Ahahaha! Oh you humans are a riot. Comedy, that's the true gift your species possesses... hold on. You're serious?"

        #CHOICE

        darius neutral "Urshunabi? The ferryman of the dead? The man with an almost godly sense of perception? That's who you believe I have the ability to mindread?"

        menu:
        #OPTION 1 NEUTRAL
            "Okay, I get it.":
                vivi angry "Okay, I get it. No need to rub it in any more."

                darius neutral "I apologize, but you think too highly of my abilities. Mind reading is a very involved exercise. It requires a very stable hold on one's person, almost like learning to swim in deeper waters."

                darius neutral "A mind like Urshu's would be like diving into... hmm, what's the right example for you humans... the Mariana Trench, I believe it's named?"

                darius neutral "I'd lose myself in his mind, unable to pull back."

                vivi neutral "I understand. I don't want you to do anything dangerous."

                #JUMP TO vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        #OPTION 2 +APPEAL
            "I didn't think sarcasm was in your wheelhouse.":
                vivi neutral "I didn't think sarcasm was in your wheelhouse, Mx. Wrecker."

                darius happy "I have many surprises in my 'wheelhouse' as you say. Some I may even show you someday."

                vivi happy "Rather forward, aren't we? That definitely isn't in your nature."

                darius neutral "Yes, well... maybe you're a bad influence on me, Ms. Sanssouci."

                vivi neutral blush "Huh? That was a little more than flirty..."

                #JUMP TO vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        #OPTION 3 +DECAY
            "Can you read ANYTHING?":
                vivi angry "Just when I thought you could be useful. Can you read ANYTHING?"

                darius angry "Only if you say please."

                vivi neutral "Please do the one thing mindflayers are infamous for? For the benefit of us all?"

                darius neutral "But that's the curious part, isn't it? You still haven't explained yourself in the slightest. Why are you so interested in reading Urshu?"

                #JUMP TO vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        vivi angry "It just bothers me how little we know about this ferryman. How can I trust someone I barely understand?"

        darius neutral "We do it every day, don't we? How many strangers do you meet in a day? How many do you just assume won't be a threat to you?"
        vivi neutral "But those people are like us. Urshu... isn't."

        darius neutral "Oh he is. More than you know."

        vivi happy "So you have read him!"

        darius neutral "Not read. More... observed."

        darius sad "The faces he makes when he thinks no one is noticing. The way he listens to every word with unrelenting attention."

        darius sad "The way he dutifully attends to every need we have, but has no desire to care for his own."

        darius sad "The way he takes in everything others give in, the good and bad, but is so reluctant to give up anything of his own."

        darius sad "Perhaps I understand him so well because I know his pain. He is isolated. Alone."

        #CHOICE

        darius neutral "Know this Vivi. Toying with that man isn't just foolish, it's cruel. He may be somewhat of a god, but he suffers just as we do."

        menu:
        #OPTION 1 +APPEAL
            "So caring. I wouldn't expect it from you.":
                vivi happy "So caring. I wouldn't expect it from you."

                vivi neutral "You don't have to worry. I don't plan to hurt our dear Urshu."

                darius happy "I'm glad to hear it. I can tell he cares for your opinion a great deal."

                vivi neutral blush "What do you mean? He treats me just the same as anyone else."

                darius happy "You're inquisitive Vivi, I told you. You get people to confront aspects of themselves they wouldn't otherwise."

                darius happy blush "Perhaps that is why I, too, enjoy your company so much."

                vivi neutral blush "This guy... when did he get so suave?"

                #JUMP to vivi neutral "I think I'll be going now. Thank you for the insight."

        #OPTION 2 +DECAY
            "Mind your business.":
                vivi neutral "Mind your business. Besides, I'm not about to break this guy's heart or anything."
                darius neutral "I'm sure you won't. Just a helpful reminder."

                vivi angry "Noted. Unneeded. Unasked for. But noted."

                #JUMP to vivi neutral "I think I'll be going now. Thank you for the insight."

        #OPTION 3 >>ATTRACTION
            "Sounds like you've had experience.":
                vivi sad "Sounds like you've had experience."

                darius sad "In suffering? More than you know, but still less than the amount I've had causing it."

                darius sad "In heartbreak? Much less than you'd think."

                vivi neutral "Never had someone you couldn't quite read? Someone that ended up hurting you?"

                darius sad "Honestly? No, the life I lived left little room for such ventures."

                darius neutral blush "Until now... funny enough."

                darius neutral blush "I have never met someone I couldn't read. It became almost second nature to naturally understand everyone I came across."

                darius neutral blush "You however... it's strange. I feel like I'm beginning to, but it has nothing to do with my abilities."

                vivi neutral blush "You're connecting. Through natural means rather than artificial ones."

                darius neutral blush "I suppose so. It's an exhilarating experience, truth be told." 

                darius neutral blush "I'm... thankful it's you of all people to introduce me to this."

                vivi neutral blush "Such a simple sentence and it has my heart aflutter. Don't make it obvious Vivi..."

            #JUMP to vivi neutral "I think I'll be going now. Thank you for the insight."

        vivi neutral "I think I'll be going now. Thank you for the insight."

        darius neutral "Insight is a kind way of putting it. I just told you about what I've seen."
        darius neutral "But thank you Vivi. I'm always open to chat."
        jump b_cs2

    label b_fr1_susurha:
        #FREE ROAM 1 - Susu'Rha

        #LOCATION - Dining Car
        scene diningcar

        #SOUND: Door opens and shuts.

        show vivi neutral at left

        vivithinking "I need to learn more about Urshu."

        vivithinking "Susu'Rha picks up on details. They'd be a good one to talk to."

        show susurha neutral at right

        susurha "When we made our way around the last turn I was able to see the entire length of the train for a brief moment."
        vivi "And?"
        susurha "It's decaying. Parts of the train that were visible during the start of our voyage are now impossible to see."
        susurha "Shrouded in mist."
        vivi "I know."
        susurha "The phenomenon is becoming more pronounced as time goes on."
        vivithinking "Right. Yes. Which means it's time to take action. But wait. Can I trust them? Maybe I should hedge." 

        # <CHOICE 1>
        vivithinking "How much do I reveal?"

        vivi "Tell me...what do you know about Urshu?"
        susurha "Our oh-so articulate, impeccably-dressed conductor? Why do you want to know?"

        "(decay route)"# DECAY ROUTE
        "You're such an observant lizard. What did you pick up on?" 

        vivi  "You're such an observant lizard. What did you pick up on?"  
        susurha angry "The one so seemingly dedicated to self-deception has the temerity to call me a lizard."
        susurha "He seems well-spoken. I also think he dresses well."
        vivi "You said that already."
        susurha happy "..."
        vivi "Fine. Keep your assiduous observations to yourself."
        #JUMP to vivi thinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."
        
        menu:
            #OPTION >>Decay +Decay
            "He just seems like such an enigmatic character.":

                vivi "He just seems like such an enigmatic character..."
                susurha "...and after that statement I'm supposed to fill in the blanks about what I know."
                susurha "Even if I did know anything useful about Urshu, what makes you think I'd tell you?"
                vivi "I thought we had a good rapport. I guess not."
                susurha "I thought you were a good reporter. I guess not."
                vivithinking "Ouch!"
                vivithinking "I must have really ticked them off."
                vivithinking "I should come at this from a different angle."
                #JUMP to vivi thinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."

            #OPTION +Attraction
            "I struck a bargain with Urshu. I'm going to make him a meal and I need your help.":
                
                vivi "I struck a bargain with Urshu. I'm going to make him a meal and I need your help."
                susurha "A meal...to die for?"
                vivi angry "Witty."
                susurha happy "I'm listening."
                vivi "If it's a test, I don't know where the test is."
                Susurha "Which begs the question... can we trust him?"
                #JUMP to vivi thinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."

            #OPTION +Decay +Attraction
            "Well, I may have a plan, but I need to know everything I can about that conductor to get it to come off properly.":
                
                vivi "Well, I may have a plan, but I need to know everything I can about that conductor to get it to come off properly." 
                susurha "..." 
                vivi "You want me to tell you about my plan."
                susurha "Or you could keep me in suspense, and while we stand here awkwardly, more and more of this train is reclaimed by whomever or whatever Entity rules this cursed liminality."
                vivi happy "We need to make him a meal. If he enjoys it, we get our lives back."
                susurha "He told you that."
                vivi "Not in so many words."
                susurha "..."
                susurha "That man or... thing, or whatever he is—what makes you think we can trust him?"
                vivithinking "Because we don't have a CHOICE."
                #JUMP to vivi thinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."

        vivithinking "I need to discover more about Urshu if I'm to have any hope of keeping up my end of the deal."
        susurha "He's not human, that much I know."
        vivi surprised "How do you know?"
        susurha "When I stand next to him, there's a low, resonant hum. Typical of phantasms. Humans don't have it."

        vivi "Then what is he exactly?"

        "(decay route)"#DECAY ROUTE
        vivithinking "you know what he is. You can feel it." 
        vivithinking "He's in league with your horror. Your fear. Your scaly, mirrored nightmare."
        vivithinking "LEAVE ME ALONE!"
        vivithinking "I will not."

        susurha "Back home, there was this ancient tome my family stole from a crypt of a country they burned to the ground when I was 3."
        susurha "Late some nights I would sneak down to the libraries and take a peek into the stories it told."
        susurha "One story in particular haunted my nightmares for years."
        vivi "What was it?"
        susurha "Boskala Nah, a sentient mass of ooze that floods the very fabric of reality."
        susurha "The stories claimed that when someone dies they return to all that is. Become one with everything... existence, if you will."
        susurha "And the Boskala Nah drowns you, as a test...watching to see if you sink or swim."
        susurha "This Urshu I reckon, holds a similar function."

            # <CHOICE 2>
        susurha "All I know is that bargaining with Boskala Nah was useless."

        menu:
            #OPTION +Attraction
            "So you're calling Urshu a slimy freak?":

                vivi "So you're calling Urshu a slimy freak?"
                susurha "Oh yes, I am."
                susurha "He is the slimiest of them all."
                susurha "I know you feel as I do about him."
                susurha "I imagine him lounging around, reading romance novels nightly."
                susurha "And laughing at all twists and betrayals."
                susurha "Wishing he was human."
                vivithinking "They laugh."
                vivithinking "Seeing them like this makes me feel... warm."
                #JUMP to vivi saying "I still need to try at least."

            #OPTION +Attraction+Decay
            "I don't think Urshu is that bad.":

                vivi "I don't think Urshu is that bad."
                susurha "Oh come now, I know a woman as skilled as yourself can sniff bullshit from a bullshitter."
                susurha "The man or whatever he is has been presenting us the face of a well dressed human conductor as we travel on a train built for the dead."
                susurha "I love your ability to think positively of others, but..."
                susurha "...when we can't even trust that the mask they wear is their own face..."
                susurha "There's room for doubt."
                vivithinking "Perhaps they have a point, but I need to try something."
                #JUMP to vivi saying "I still need to try at least."

            #OPTION +Decay
            "Are you absolutely sure we can't bargain with Urshu?":

                vivi "Are you absolutely sure we can't bargain with Urshu?"
                susurha "Oh sweetie, I wouldn't trust him if my life depended on it."
                susurha "Heh... I suppose it is, isn't it?"
                vivi "This isn't a joke."
                susurha "You don't see me laughing about it, do you?"
                susurha "That conductor evokes the same emotions of a slimy weasel crawling up your spine on a blistering summer day."
                susurha "I'd imagine he has always been flexible with what he reveals and to whom."
                susurha "No doubt the boredom of leading this train does its toll on the mind."
                #JUMP to vivi saying "I still need to try at least."

            #OPTION >>Attraction +Attraction
            "Urshu is quite the slimy freak.":

                vivi "Urshu is quite the slimy freak."
                susurha "The slimiest of them all."
                vivi "I bet he thinks he looks good in that garb he has on every day."
                susurha "I imagine him lounging around, reading romance novels nightly."
                vivi "An sipping of the most expensive of red wines."
                susurha "And laughing at all twists and betrayals."
                vivi "Snooping on all of our drama."
                susurha "Wishing he was human."
                vivithinking "HAH! Yes."
                vivithinking "This is nice."
                #JUMP to vivi saying "I still need to try at least."

            #OPTION >>Decay +Decay
            "I NEED his help if I am to get off this train.":

                vivi "I NEED his help if I am to get off this train."
                susurha "Do the prisoners trust their escape with the jailors?"
                susurha "I've had my fair share of desperation, but this..."
                susurha "You can do better."
                vivithinking "This is getting nowhere."
                #JUMP to vivi saying "I still need to try at least."

        vivi "I still need to try at least."

        susurha "You know how I feel."
        susurha "But your choice is your own."
        susurha "I need to go see if I have any snacks left in my cabin. This talk of cooking has made me hungry."

        "(if attraction)"#ATTRACTION ROUTE
        susurha "Take care and see you later, Vivi."

        "(if decay)"#DECAY ROUTE
        susurha "Try not to burn yourself, Vivi."

        #JUMP TO: Free Roam 2 - Character Selector
        jump b_cs2

    label b_cs2:
        #Character Selector 2

        #LOCATION: cabin
        scene cabin

        show vivi neutral at left

        vivithinking sad "I've spent the whole morning trying to learn about Urshu but found out exactly nothing useful."

        vivithinking neutral "I guess I'm gonna have to wing it. Urshu better get ready for a meal better than any he's had for eons."

        #<CHOICE>
        vivithinking surprised "On second thought, I could use some help in the kitchen."

        menu:
        # <OPTION>
            "Avatar of Asha":

                vivi neutral "I could use the pallet of a goddess. Nothing but the best, right?"
                #JUMP TO: Free roam 2 / Avatar of Asha
                jump b_fr2_ava

        # # <OPTION>
        #     "Inquisitor Darius Wrecker":

        #         vivi neutral "Darius would be an excellent sous chef."
        #         #JUMP TO: Free roam 2 / Darius Wrecker

        # <OPTION>
            "Susu'Rha Balrinn":

                vivi neutral "Susu'Rha could definitely help me win over the conductor."
                #JUMP TO: Free roam 2 / Susu'Rha Balrinn
                jump b_fr2_susurha

    label b_fr2_ava:

        #FREE ROAM 2 - Ava
        #Naj's note for character experts - please write this scene right up until Vivi and the NPC finish cooking. Also, you look great today.

        # Location: Dining Car
        scene diningcar

        #Sound: Cooking, Dining Sounds

        show vivi neutral at right

        show ava neutral at left

        vivithinking "I didn't expect to see Miss Sunshine herself away from the perch today, but I'm glad that I got her out."

        vivithinking "If I can just convince her to cook something good with me, maybe I'll finally have a way out of this place."

        ava happy "So what brings you here today, my radiant companion?"

        vivi surprised blush "Asha, to be entirely honest...well..."

        # <CHOICE>
        menu:
            #OPTION 1 + ATTRACTION
            "I want to cook together...with you.":

                vivi surprised blush "I want to cook together...with you. I bet we can whip up something really incredible."
                ava happy blush "We would be honored to cook with you. It has been over a decade since we set foot in a kitchen. This should prove...interesting."

                vivithinking "Interesting indeed..."

                vivi happy blush "I can't wait! Let's get cooking."

                #JUMP TO: ava saying "So what shall we make, then?"


            #OPTION 2 + DECAY
            "Urhsu asked me...":

                vivi surprised blush "Urshu asked me to cook something for everyone, so I figured we could do it together. What do you think?"

                ava happy "We wish you would have asked us sooner. The sun is nearly gone today."

                vivi neutral "So...whaddya say?"

                #JUMP TO: ava saying "So what shall we make, then?"

            #OPTION 3 << ATTRACTION
            "Be my sous chef. Together, we'll rule this train.":

                vivi surprised blush "Be my sous chef. Together, we'll rule this train."

                ava surprised blush "We're not sure exactly what you mean, but your passion is coming through."

                vivi surprised blush "Did you just...use a contraction?"

                ava happy blush "A what?"

                #JUMP TO: ava saying "So what shall we make, then?"

        ava neutral "So what shall we make, then?"

        vivi neutral "Good question! What meal feels like home for you?"

        ava surprised blush "Well, whenever I was feeling unhappy, the servants would bring me a cornucopia of croquembouche."

        vivithinking "That sounds like a nightmare to make..."

        ava happy "Do you enjoy cooking at home? Allegedly the food culture on Earth has few rivals."

        vivi happy blush "You heard right! I've taken a few cooking classes back home. They even taught me how to make soufflé!"

        ava happy blush "That sounds lovely, but it couldn't compare to the delight of croquembouche."

        vivithinking "I swear she's speaking differently today."
        vivi happy "I think we should make..."

        #<CHOICE>
        menu:
            #OPTION 1 + DECAY
            "Croquembouche":

                vivi happy " Let's make the croquembouche you used to have at home. I'm sure it'll put us in a good mood."

                ava happy "Delightful. We shall gather the 74 ingredients required to make the dish."

                vivi surprised "74 ingredients? What is this, Masterchef?"

                ava happy "Do not worry, my radiance."

                #JUMP TO: vivi saying "Let's get cooking!"

            #OPTION 2 + ATTRACTION
            "Something simple.":

                vivi happy "Something simple. A good old American breakfast!"

                ava surprised "We are not familiar with American...?"

                vivi happy "Well, I'm glad you asked, Asha! Americans love to eat, and they wake up most days with a massive meal."

                vivi happy blush "You can never be sad eating breakfast back home! Hot pancakes with eggs and crispy bacon could make a grown man cry."

                ava surprised "We don't wish to cry today, please."

                vivi surprised blush "Don't worry, love, it's just an expression."

                #JUMP TO: vivi saying "Let's get cooking!"

            #OPTION 3 + DECAY 
            "Soufflé.":

                vivi neutral "Soufflé. I think I can remember the recipe from my class."
                ava happy "The last soufflé we ate was made with the highest quality eggs and milk on all of Soleos. We wonder how this will compare."

                vivi surprised blush "Don't get your hopes up too high, now, missy."

                #JUMP TO: vivi saying "Let's get cooking!"

        vivi happy blush "Let's get cooking!"

        ava happy blush "We shall wash our hands, just in case."

        #HIDE ava here
        hide ava

        vivithinking "The Goddess, washing her dirty hands? Wonder what she's been up to..."

        show ava happy at left

        ava happy blush "Apologies..."

        vivi happy blush "For what, Asha? You worry too much."

        ava happy blush "We just know how much this means to you."

        vivi happy blush "Oh, Asha. You're far too kind. Thank you."

        vivi neutral "Do you mind-"

        # <CHOICE>
        menu:
            #OPTION 1 + ATTRACTION
            "If we work together?":

                vivi blush "Do you mind if we work together? I'm not the most comfortable in the kitchen."

                ava blush "Of course, Vivi. Let's do this together."

                vivi blush "I like this new Asha. Where has she been?"

                ava blush "Whatever do you mean?"

                # JUMP TO: vivi saying "Nothing at all..."


            #OPTION 2 + DECAY
            "Beating the eggs and sifting the flour for me?":

                vivi neutral "Do you mind beating the eggs and sifting the flour for me? I'll take care of the other stuff and we can combine ingredients."

                ava neutral "We'll get right to it!"

                vivi neutral "Thank you, sunshine...Wait a minute...have you done this before?"

                ava neutral "Certainly! We learned from the finest chefs on Soleos so that we bring peace and food as diplomats."

                vivi surprised "Oh! Good to know..."

                ava surprised "What's wrong?"

                #JUMP TO: vivi saying "Nothing at all..."


        vivi happy blush "Nothing at all..."

        # PAUSE
        # SOUND Cooking sounds

        vivi surprised "Wow. I can't believe we actually did it. It tastes so good too!"

        ava happy blush "Shall we present our creation to the conductor?"

        vivi happy "Let's do it!"
        jump debrief_bargaining


    #Naj's note for Zach or Gideon - insert conversation here where Vivi unveils her culinary masterpiece for Urshu, only for him to wriggle out of their deal by explaining the loophole (he can't physically enjoy meals, he doesn't eat). Once this is written, character experts can insert reactions from the NPC.

    #Naj's note for character experts - please write this scene right up until Vivi and the NPC finish cooking. Also, you look great today.

    label b_fr2_susurha:
        #FREE ROAM 2 - Susu'Rha

        #LOCATION - Dining Car
        scene diningcar

        show vivi neutral at left
        show susurha neutral at right

        vivi "Next item of business--we make a meal that knocks the sock suspenders off Urshu."
        susurha "If you would have told me that the fate of my soul rested on my ability to cook..."
        susurha "...I would have said, 'WHY DIDN'T YOU TELL ME SOONER!'"
        vivithinking "I wish my Nana was here."
        vivi "..."
        susurha "Where'd you go just then?"
        vivi "I was thinking about my Grandmother. My mother's mother. She was from the far side of my world. An excellent chef. And an all-around brilliant human." 

        # <CHOICE>    
        susurha "What makes her so brilliant?"

        menu:
            #OPTION 1 +ATTRACTION
            "She could see down to the essence of a person.":

                vivi "She could see down to the essence of a person."
                susurha "I sense that power in you too, milady."
                vivi "I have it..."
                vivi "...when my agenda doesn't get in the way."
                susurha "That's a rare trait. Where I'm from, everyone is power-mad, agenda-driven."
                susurha "This leads to war."
                vivi "It's like that where I'm from too."
                susurha "Yet you're dying to go back there."
                vivi "there are things I miss, I'm not gonna lie. And a lot of them are food-related."
                susurha "Which reminds me..."
                #JUMP to susurha "We have a meal to cook."

            #OPTION 2 +DECAY
            "Whatever it was, it skipped over me.":

                vivi "Whatever it was, it skipped over me."
                susurha "Whatever do you mean?"
                vivi "Nana could read people. She could bargain. She had grit. Tenacity." 
                susurha "Those are good qualities."
                vivi "She lived a long life and everyone loved her."
                vivi "Somehow I don't think she's ever set foot on this train."
                susurha "Winding up on this train is evidence that you did something wrong?"
                vivi "It sure isn't evidence that I did something right!"
                susurha "Maybe we have a chance to turn it all around, if we let the food speak for us."
                vivithinking "This is never going to work."
                #JUMP TO: susurha "We have a meal to cook."

            #OPTION 3 >>ATTRACTION+ATTRACTION
            "She was a hustler. She knew how to get what she wanted.":

                vivi "She was a hustler. She knew how to get what she wanted."
                susurha "Well let's use some of that hustle to get us off this train."
                vivi "if we work together, we can make it happen."
                susurha "I dare say, working in close quarters with you, I hope I don't get too distracted...by your energy."
                vivi "Are you flirting with me?"
                susurha "I meant that in earnest."
                vivi "So... no?"
                susurha "I didn't say that."
                #JUMP TO: susurha "We have a meal to cook."
                

        susurha "We have a meal to cook."
        # <CHOICE>
        susurha "What should we cook?"
        "(decay route)"# DECAY ROUTE
        "I can't...seem to make up my mind...."
        vivithinking "Susu'Rha glances out the window."
        vivithinking "The cosmic spirals twist violently like tornados."
        vivithinking "Drawing me in..."
        vivithinking "Like someone is calling me."
        vivithinking "I can't breathe."
        susurha "Vivi you must collect yourself..."
        # JUMP TO: vivi "Okay. Let's make magic happen.." 

        menu:

            # OPTION 1 +DECAY
            "Let's try to appeal to Urshu's taste.":
            
                vivi "Let's try to appeal to Urshu's taste."
                susurha "We would only be guessing."
                vivi "If I were that penguin-dressed doubletalking astral weirdo I'd eat...meatloaf."
                susurha "Which is?"
                vivi "A loaf. Of meat."
                vivi "Thickened with breadcrumbs."
                susurha "That sounds like prison food."
                vivi "Do you have a better idea?"     
            # JUMP TO: vivi "Okay. Let's make magic happen.." 

            # OPTION 2 +ATTRACTION
            "We'll just try to cook the best dish we possibly can.":
            
                vivi "We'll just try to cook the best dish we possibly can."     
                susurha "Unluckily for you, I eat nothing but grubs and Burrowers."
                vivi angry "..."
                susurha "Of course I'm joking. I grew up making my own dishes from the family larder."
                vivi "I too, am something of a gourmand."
                # JUMP TO: vivi "Okay. Let's make magic happen.."  

            # OPTION 3 >>ATTRACTION+ATTRACTION
            "I'll let my grandmother's spirit guide me.":
                
                vivi "I'll let my grandmother's spirit guide me."
                susurha "The spirit of your ancestors...Yes!"
                susurha "Ooh, that 'cumin' tastes like Ra'Taa. You're using a lot of it however." 
                vivi "She'd want me to use a lot of it."
                vivi "If she was here, she'd tell me to do it by feeling."
                vivi "To eyeball things."
                # JUMP TO: vivi "Okay. Let's make magic happen.." 

        vivi "Okay. Let's make magic happen."
        vivithinking "spices, check. Wow, the beef is quite succulent for...wherever we are. I wonder if they have cows here. Ghost cows."
        vivithinking "That's wonky."
        vivi "Voila!"
        vivi "Okay, Susu'Rha. What do you think?"
        susurha happy blush "It's... really good."
        vivi angry "Really?"
        susurha neutral blush "I don't want to hurt your feelings."   
        susurha "I can't put my claw on it, but..."
        # <CHOICE>
        susurha "It needs...something."

        "(decay route)"# DECAY ROUTE

        susurha "If you'd just let me help you."
        vivi "I've got this under control!"
        susurha "Clearly."
        susurha "It's as if you WANT to displease him!"
        vivi "Maybe I do! Maybe I know it's all pointless!"

        menu:
            
            #OPTION +Attraction
            "It needs more spice.":

                vivi "It needs more spice."
                vivi "Nana would want things spicy."
                vivi "More cardamom."
                vivi "More cinnamon."
                vivi "More, more, more!"
                susurha "I like how you do that."
                vivi "What?"
                susurha "There's so much life in you. Even beyond..."
                vivi "Beyond death."
                susurha "I didn't want to say it, but... yes." 
                # JUMP TO: vivi "Let's serve this up" 

            #OPTION +Decay
            "It's fine the way it is.":
                
                vivi "It's fine the way it is."
                susurha "There's no part of you that believes that."
                vivi "So what. We're being scammed."
                vivi "In what myth is it written that food somehow placates the Guardian of the Beyond."
                susurha "We don't have a myth like that."
                vivi "Us neither."
                # JUMP TO: vivi "Let's serve this up" 

            #OPTION >>Decay+Decay
            "Screw it. We'll do what you want.":
            
                vivi "Screw it. We'll do what you want."
                vivithinking "don't you give me that side-eye, lizard!"
                susurha "I can help you, but it should be a collaboration."
                vivi "I tried my best, and I failed. What more do you want?"
                susurha "Maybe for you not to give up so easily, seeing as my fate is tied to yours!"
                vivi "..."
                susurha "It needs love."
                vivi "That's a tall order right now."
                # JUMP TO: vivi "Let's serve this up" 
                
        vivi "Let's serve this up."
        jump debrief_bargaining

    #Naj's note for Zach or Gideon - insert conversation here where Vivi unveils her culinary masterpiece for Urshu, only for him to wriggle out of their deal by explaining the loophole (he can't physically enjoy meals, he doesn't eat). Once this is written, character experts can insert reactions from the NPC.

    #  JUMP TO: Debrief Denial.

    label debrief_bargaining:
        #Debrief Bargaining

        #LOCATION: cabin
        scene cabin

        "(attraction route)"#ATTRACTION ROUTE

        show vivi sad at left

        vivithinking sad "I should've known better than to think there was an actual way out. What the hell was the point in even trying?"

        vivithinking sad "I really shouldn't have shared my plan with anyone else. I didn't just get my hopes up. Now I've let down friends."
        vivithinking happy "Never thought I'd call the folks on this train friends."
        vivithinking sad "And I managed to fuck that up too. What's wrong with me?"

        vivithinking neutral "I need to write."

        "(journal entry)"#Journal entry with attraction meter high
        "If cooking for him didn't work, what would? I'm beginning to think that this is it. The end of the line. Everything I worked for... gone. Maybe the other's will join me at the bar. I definitely owe them all a drink. Good a place as any to forget everything."


        "(decay route)"# DECAY ROUTE

        show vivi angry at left

        vivithinking angry "He knew. He knew from the very start and just led me along! Why give any of us hope?"

        vivithinking sad "There is no hope. All of my time here was pointless."

        vivithinking sad "I am pointless."

        vivithinking neutral "I can't even recognize myself. I feel like I'm trying to swim to shore but the current keeps me from ever making it. I'm tortured to see the shore but always be out of reach."

        vivithinking surprised "This place is changing me. I'm withering away into something dark and no amount of clawing back can save me."

        vivithinking sad "I'm doomed."

        vivithinking neutral "Maybe I should write out my thoughts."

        "(journal entry)"# Journal entry with degradation meter high

        "Nothing is good enough for the conductor. This is all hopeless! I can see changes in all of us. I don't feel fully human anymore. Those creatures outside the windows... will that be us? At least the bar is stocked. Tomorrow's plan is to drink the place dry. Hopefully if I'm lucky, it'll piss the conductor off."



        return
        # jump scene_depression
