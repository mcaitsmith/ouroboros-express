# The scene starts here.

label denial_fr1_ava:

    #FREE ROAM 1 - Ava

    #LOCATION: Observatory
    scene observatory with fade

    show ava sad at right with dissolve

    vivithinking "On to the observatory. Who do I see staring out the window into darkness but the sun goddess herself?"

    show ava surprised at right

    # SOUND: ava gasps.
    show ava happy at right
    vivithinking "Oh, she's noticed me. So imposing~"

    ava happy blush "Hello, little one. Has our radiance tempted you today? Come, sit with us for a moment."

    vivithinking "When she says it like this. It's not like I can say no."

    # <CHOICE>
    ava neutral "Your sandal has a pebble, little one?"

    menu:

    # OPTION 1
        "She'd know where we're headed and how to escape.":

            vivithinking "She'd know where we're headed and how to escape."
            vivi surprised "Where do you think we're really headed? Or how does one escape?"
            ava happy "Where are we going? A destination. The train will stop, we will leave..."
            vivi neutral "Not very specific."
            ava happy "Correct. For how can we tell you what we do not yet know?"
            vivithinking "What is wrong with her?"
            #JUMP to vivi saying "Beats me!"

    # OPTION 2 +ATTRACTION
        "I wonder what she saw in the window.":

            vivithinking "I wonder what she saw in the window."
            vivi happy "I'm a little overwhelmed by everything going on. What are you looking at?"
            ava happy blush "We exist to spread the light of knowledge. We have looked into the darkness. Above us."
            vivi surprised "What'd you see?"
            ava surprised "A cold void stares back at us. A sun, black as night. Inescapable emptiness."
            vivi surprised "How terrifying!" 
            ava neutral "Perhaps it was just our imagination, hm?"
            #JUMP to vivi saying "Beats me!"

    vivi neutral "Beats me!"

    # <CHOICE>
    ava sad "The pebble remains. Speak your mind."

    menu:

    # OPTION 1 +ATTRACTION
        "I should share my worries with her.":

            vivithinking "I should share my worries with her."
            vivi surprised "I don't even know what to think anymore...this whole journey has thrown me for a loop. I mean, if the conductor was telling the truth, then are we all really dead...?"
            ava neutral "We can understand why you feel that way, but the Avatar shall not perish before twenty and five years! It is as obvious as the sunrise. We can still feel the Goddess' power surging through us."
            vivi surprised "But maybe we really are gone. You'd think I'd remember dying!" 
            vivi "Maybe that's why we're here...to come to terms with...with this."
            ava angry "Silly mortal... But... we know how you feel. We scarcely recall boarding this train; home one moment, here the next. Why has our memory forsaken us?...ugh! Let us speak of other things."

            # JUMP TO: vivi "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."

    # OPTION 2 
        "I should interview her for more info.":

            vivithinking "I should interview her for more info."
            vivi neutral "How has this luxury liner been for you?"
            ava neutral "Let us bring Light to your darkness. Besides last night, the journey, like so many, has been pleasant."
            # JUMP TO: vivi "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."

    vivi neutral "I can't imagine we're actually dead... I mean we're still breathing, eating, and drinking! If that's not alive, then I don't know what is."
    ava neutral "Ridiculous. Of course we are alive. Look around you. Breathe. Have a drink and calm those nerves of yours."

    # <CHOICE>
    ava happy blush "What say you, little one?"

    menu:

    # OPTION 1 +ATTRACTION
        "Drink, yes? Little one? No!":

            vivithinking "Drink, yes? Little one? No!"
            vivi happy blush "Another time! But please stop calling me \"little one.\" I'm thirty."
            ava sad blush "Ah. Our words have offended. A thousand pardons." 
            ava happy blush "We admire you standing up for yourself. It is...appealing."
            ava happy "May the Goddess guide your travels. The All is the One."
            vivi happy "Thanks, Asha! May the Goddess guide your journey too."
            #JUMP TO: vivi: "That was interesting. Wonder what's next..."

    # OPTION 2
        "More of the cat chasing its tail.":

            vivithinking "More of the cat chasing its tail."
            vivi neutral "Maybe later. Thank you for listening, Asha. I'll keep you updated with my investigation as it progresses."
            ava neutral "May the Goddess guide your travels. The All is the One."
            vivi neutral "Sure thing, sunshine. See ya."
            #JUMP to vivi saying, "That was interesting. Wonder what's next..."

    hide ava with dissolve
    vivithinking "That was interesting. Wonder what's next..."
    # JUMP TO: Character Selector 2

    # FREE ROAM 1 - Darius
    # LOCATION: lounge

    # show vivi neutral at left

    # show darius neutral at right

    # vivithinking "Darius is doing their best to fill out that loveseat. Even in such a casual position, they're so graceful. Guess that's the benefit of that mindflayer physique."

    # vivi "Excuse me, it's Darius, right?"

    # darius surprised "Yes."

    # vivithinking "They seem surprised. Loner type maybe?"

    # darius neutral "I'm surprised you walked over to me of all people. Surely the goddess or dragon would be more approachable? Not many humans would chat up a mindflayer like you just have."

    # vivithinking "Bingo on the loner call."

    # vivi "You seem approachable enough. I actually had a question if you don't mind."

    # darius neutral "Go ahead."

    # vivithinking "If anyone has a good idea what the hell is going on here, it has to be the mindflayer."

    # vivi  "Tell me, you must have experience with otherworldly phenomena, right?"

    # darius neutral "In a sense. This whole situation is unlike anything I've seen however."

    # vivithinking "Crap. Swing and a miss."

    # vivi  "Interesting. Do you believe him then? That this is some sort of intermission before we all die?"

    # vivithinking "Their... phalanges? Tentacles? Whatever they are. They keep them hidden from me. Strange."

    # darius neutral "I'm not entirely sure, but he's given us no reason to doubt. We should find out soon regardless."

    # show vivi angry 
    # vivithinking "Real charmer, this one. Who knows if this is some sort of trap, a messed up fantasy for this conductor? Are we supposed to just take him at his word?."

    # # <CHOICE>

    # darius neutral "Now that you mention it, I am... curious. What do you make of this "Urshu's" claim that we must come to terms?"

    # # OPTION 1 
    #     "I'm not sure."

    #     vivi  "I'm not sure." 
    #     vivi "The man speaks in riddles, and I can't make heads or tails of them right now."

    #     darius neutral "That is understandable. Last night was a shock to be sure."

    #     vivi "Is that something you're interested in? Coming to terms?"

    #     darius neutral "You could say that. The details of my life are still cloudy but they're coming back slowly. I'm sure the same goes for you?"

    #     vivi "Yes, some things are coming back slowly."

    #     vivithinking "There's a pain in their voice, it's almost... melancholic?"

    #     vivi "If you don't mind me asking, what happened--"

    #     darius neutral "Ahem..."

    #     # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"

    # # OPTION 2 
    #     "It's nonsense."

    # vivi "It's nonsense." 
    #     vivi "If we're dead, we're dead. There is no coming to terms."

    #     darius sad "Hmm. I suppose so. Apologies for the foolish question."

    #     show vivi sad blush 
    #     vivithinking "Oops. I get the feeling I might've offended them somehow."

    #     vivi neutral "Of course, if that's what you're looking for, there's nothing wrong with that!"

    #     darius sad "No no, you're right. There's no chance of redemption if we've passed already."

    #     show vivi surprised 
    #     vivithinking "Redemption?"

    #     # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"

    # # OPTION 3 
    #     "It's interesting."

    #     vivi  "It's a thinker, that's for sure. If you're into that, then I guess there's some merit to it. I don't know about you though, but I can't "come to terms" here of all places."

    #     darius surprised "Interesting. I wouldn't have expected that answer from you. Thank you for humoring me."

    #     # vivi surprised "{i}What does THAT mean? You don't know me. Unless... oh god, are they reading my mind?{/i}"

    #     darius happy "Wondering if I'm reading your mind are you?"

    #     # vivi surprised blush "So you ARE then!"

    #     darius happy "Hah, I don't rely on such cheap tricks. I'm naturally quite skilled at reading people you see."

    #     vivthinking "Is that a hint of annoyance I sense?"

    #     vivi "So then, what do you see when you look at me?"

    #     darius blush "I-- uhh, erm... my detective skills are a bit off today, you see. Try asking me again tomorrow, I'm sure I'll have a better answer for you."

    #     show vivi happy 
    #     vivithinking "Who knew mindflayers could get flustered. And even a little cute?"

    #     # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"


    # darius neutral "Enough about that for now. Don't you find this train strange?"

    # vivithinking "That deflection was about as subtle as their outfit."

    # vivi "I suppose so. In what way exactly?"

    # darius neutral "The way it bends, twists, almost shifts to the eye, as if it isn't entirely there. Have you noticed it too?"

    # vivi "I've noticed some oddities yes, but I chalked that up to the conductor pulling some tricks. Do you think there's something more to it?"

    # darius neutral "Possibly, yes. It's just as much a mystery to me as that conductor is."

    # vivithinking "Their words are somber but curious. It's soothing to listen to."

    # vivi "Where do you think we're going?"

    # darius "In my...religion, we believed that oblivion was at the end of it all. Maybe this train is leading us to that."

    # vivithinking "Do mindflayers have religions? No, that's probably a dumb question."

    # vivi "You seemed interested in making amends before. What's the point if you're headed for oblivion regardless?"

    # darius "That's... a little too complex a topic for me to get into right now. I apologize."

    # # <CHOICE>

    # darius "That being said though, which would you prefer awaits us at the end of this little trip? Oblivion, or some sort of rebirth?"

    # # OPTION 1 

    #     "Oblivion."

    #     vivi "Oblivion"
    #     vivi  "I kind of like the idea that we just fade away into the ether when everything's said and done. It's like finally being able to rest after a long day's work."

    #     darius sad "It's a very appealing option to many. It was for me as well, long ago."

    #     darius sad "But doesn't it bother you? The idea that things are left unsaid, apologies left unmade?"

    #     vivi "Not entirely. The same fate awaits us all, and we can't make every wrong right again."

    #     vivi "Besides, that's assuming that this place is really what that conductor claims it is. Which I'm not that sure of, personally."

    #     darius neutral "I see."

    #     # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."


    # # OPTION 2 

    #     "Rebirth."

    #     vivi "Rebirth."
    #     vivi  "I like the idea that we are reborn in some way. It's a comforting thought that life never truly leaves, it just renews itself."

    #     darius happy "I feel much the same way. The opportunity to take what you've learned with you in some form, to grow and try again? It's a welcome fate."

    #     vivi "Interesting that you assume that we could take our past experiences with us. What if we couldn't? Would you still be so interested?"

    #     vivithinking "Were they always fidgeting with their hands like that?"

    #     darius sad "You're right, that was rather optimistic of me." 

    #     darius neutral "I would still be interested, even if it meant losing the experiences I've had. I suppose in some cases, that would even be a better outcome."

    #     vivi "That's assuming that this place is really what that conductor claims it is. Which I'm not that sure of, personally."

    #     darius neutral "I see."

    #     # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."


    # # OPTION 3

    #     "Something else."

    #     vivi "Something else."
    #     vivi "I don't think either of those are really true. I think whatever comes after is just another form of life. We might not know what it is exactly, but it doesn't make it any less than this stage."

    #     darius surprised "Fascinating. I've never considered that perspective."

    #     darius neutral "A clean slate, a new experience... that doesn't sound terrible."

    #     vivi "That's assuming that this place is really what that conductor claims it is. Which I'm not that sure of, personally."

    #     darius neutral "I see."

    #     # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    # # OPTION 4 

    #     "Doesn't matter."

    #     vivi "Doesn't matter."
    #     vivi "It's pointless to prefer one or the other. If it is the case that the conductor is telling the truth, then we'll find out soon."

    #     vivi "Why place assumptions and hopes on something we have no control over? It'll only hurt you in the long run."

    #     darius sad "Hmm. I suppose you're right. My apologies."

    #     vivi "No need to apologize. It's just that in my experience, hope can keep you going but it can just as easily end you. I'd rather focus on what I can do now."

    #     darius sad "A very wise statement."

    #     # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    # darius neutral "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    # vivi "Sure. Thank you for being open to my questions."

    # darius "Anytime, Ms. Sanssouci."

    # # JUMP TO: Character Selector 2
    # FREE ROAM 1 - Susu'Rha

    # LOCATION: Dining Car

    # # SOUND: Footsteps storm into the room.

    # show susurha happy at right

    # "Wait."
    # "Susu'Rha? What are they doing?"
    # "Are they literally feasting on a slice of cake?"
    # "Okay, that's cute."

    # # SOUND: The train car door slams shut.
    # # VISUAL: The screen shakes.

    # show susurha surprised at right

    # # SOUND: Susu'Rha drops their fork against the table.

    # susurha neutral "Oh my... are you as hungry as I? I too get flustered when I haven't eaten all day."

    # show vivi neutral at left

    # # SOUND: Vivi sighs.

    # # <CHOICE> 
    # vivi neutral "I'm not hungry. I'm..."

    # # OPTION 1 
    #     "I'm fine." 
        
    #     vivi "I'm fine."
    #     susurha "Are you positive?"
    #     vivi "Yes, I'm positive. There is just a lot on my mind at the moment."
    #     susurha "Mmmhmm... That much I can glean."
    #     # JUMP TO: susurha "Here. Join me and enjoy a slice."

    # # OPTION 2 +ATTRACTION
    #     "Honestly, I don't know."

    #     vivi "Honestly, I don't know."
    #     show susurha sad
    #     susurha sad "Yeah, I get that too. I'm..."
    #     show susurha happy
    #     susurha happy "Well, I'm here doing what I know can lift the spirits."
    #     # JUMP TO: susurha "Here. Join me and enjoy a slice."

    # #OPTION 3 
    #     "Are you eating cake right now?"
    #     vivi "Are you eating cake right now?"
    # susurha "Ah yes. This angel food cake is quite delectable. I wonder if that angel beauty had anything to do with this being here."
    #     susurha "..."
    #     susurha "I do hope that you aren't judging me."
    #     vivi "I'm not."
    #     susurha "Good."
    #     #JUMP to susurha "Here. Join me and enjoy a slice." 

    # susurha happy "Here. Join me and enjoy a slice."

    # vivithinking "Deep breaths."

    # # SOUND: Vivi inhales and exhales.

    # vivithinking "Alright, let's just sit down and chill."

    # vivithinking "What's the worst that can happen?"

    # # SOUND: Vivi takes a seat at the table.

    # vivithinking "They carve a slice of cake and nudge it my way."
    # vivithinking "Fine. I take the fork and take a bite."

    # vivi happy "Oh my goodness, this is amazing."

    # susurha happy "I told you. The Archdruids back in the living forest can't even dream of conjuring such savory delights. This angel food cake is to die for."

    # show susurha neutral
    # show vivi neutral

    # susurha "..."

    # vivi "..."

    # vivithinking "Oh no..."
    # vivithiking "Awkward silence alert..."

    # # <CHOICE> 
    # susurha "Alas... Please tell me you weren't paying attention to that Urshu fellow the other day when he was spouting off about..."

    # # OPTION 1 
    #     "Urshu has no idea what he was rambling about."

    #     vivi "Urshu has no idea what he was rambling about."
    #     susurha happy "Ah... music to my ears. So clearly I haven't found myself entirely surrounded by those more insane than I."
    #     vivi "No, I am very much sane, but this place is testing that."
    #     susurha happy "I couldn't agree anymore."
    #     susurha happy "Hehe."
    #     susurha happy "Dead..."
    #     susurha happy "My father could have told better crafted jokes than that back home."
    #     susurha sad "Hmm."
    #     show vivi sad
    #     #JUMP TO: susurha saying "I'm sorry..."
        
    # # OPTION 2 +Attraction
    #     "How could I not? I can't stop thinking about it."

    #     vivi "How could I not? I can't stop thinking about it."
    #     susurha angry "Uh.... Wrong answer. Not quite what I was looking to hear. Thank you very much. Now please tell me that the next thing that you utter isn't just echoing..."
    #     vivi "I don't know. What if we are truly dead?"
    #     susurha neutral "That."
    #     susurha "Great, everyone has gone mad and I'm soon to join them."
    #     vivi "Are you telling me that you haven't thought about the possibility?"
    #     susurha "No ma'am, I haven't. I would very much be aware if I was dead. I'd either be roasting in an abyss of flames with like-minded individuals or be experiencing the sweet void of nothingness."
    #     susurha "NOT some poorly designed metallic tube flying to who knows where."
    #     Susurha sad "I... I don't know."
    #     vivithinking "Oh wow. They're breaking."
    #     show susurha neutral
    #     # JUMP TO: susurha saying "I'm sorry..."

    #     susurha sad "I'm sorry..."

    #     susurha sad "I really know how to go and spoil a mood, don't I?"

    #     vivithinking "Whoop. He just slid the entire cake dish to my side."

    #     susurha sad "I've lost my appetite."

    #     susurha neutral "Please do enjoy what you can of it. I'd hate to see it waste away."

    # # <CHOICE>
    # susurha "...I think I'm going to go lay my head down and not think."

    # # OPTION 1 +Attraction
    #     "Are you okay?"

    #     vivi "Are you okay?"
    #     show susurha happy
    #     #JUMP TO: hide susurha.

    # # OPTION 2 
    #     "Alright."
        
    #     vivi "Alright."
    #     show susurha sad
    #     #JUMP TO: hide susurha.
        
    # hide susurha

    # "Hey! Oh no, they're leaving!"
    # "Well..."

    # # SOUND: Door closes.

    # # SOUND: A headache inducing ringing echoes.

    # vivithinking "Ugh... my head feels like something is crawling at the walls of my skull."

    # vivi "I think that was enough for me too."

    # vivi "I better head back to my cabin and collect myself."

    # # JUMP TO: Character Selector 2





    # Character Selector 2

    # LOCATION: cabin

    # show vivi left neutral

    # vivi neutral "That was... interesting. Looks like I wasn't the only one blindsided by this train. I need some time to gather my thoughts."

    # # Fade to blur if possible.

    # vivithinking "This car has big windows..."
    # vivithinking "What I see behind those windows makes...zero sense though."
    # vivithinking "Surreal landscapes–blending into a swirl of colors. The train's breathtaking speed blurs everything into cosmic spaghetti. It gets darker. Darker."

    # # Fade back in.

    # vivi sad "This can't be happening."
    # vivi angry "It can't end like this."

    # # <CHOICE>
    # vivi neutral "I should go talk to someone else. I can't be the only one who wants off this ride."

    # # Note that whoever you talked to in free roam 1 should be unavailable as an option.

    # # OPTION 1
    #     "Avatar of Asha"

    #     vivi happy "I should try the ‘goddess. I think she's in the observatory."
    #     #JUMP TO: Free Roam 2 / Avatar of Asha

    # #OPTION 2
    #     "Inquisitor Darius Wrecker"

    #     vivi neutral "I have a feeling Darius knows more than he's letting on. I believe they're in the dining car."
    #     #JUMP TO: Free Roam 2 / Inquisitor Darius Wrecker

    # #OPTION 3
    #     "Susu'Rha Balrinn"

    #     vivi neutral "I feel like the druid wants out too. Maybe they can help me figure this all out. I think they're in the lounge."
    #     #JUMP TO: Free Roam 2 / Susu'Rha Balrinn

    # FREE ROAM 2 - Avatar of Asha
    # LOCATION: observatory

    # show vivi neutral at left

    # vivithinking "Many thoughts... Head full."
    # vivithinking "Oh. I ended into the observatory."
    # vivithinking "Well, the goddess is here, staring into the darkness."

    # show ava neutral at right
    # vivi happy "Hey Ash, I think I found us a way out of this bi-
    # ava angry "You may refer to us as Asha or Avatar of the Eternal Light,...but your proposition has intrigued us. Proceed."
    # vivithinking "Bruh. Stick up your ass much?!"
    # vivi neutral "I'll go grab the others!
    # ava surprised "Those poor creatures? Pay them no mind. Their only worry is their own insignificance."
    # vivithinking "What a self-important prickle this Avatar of ASSha is!" 
    # ava sad "Like sand in the wind."

    # # <CHOICE>
    # "Who does she think she is?"

    # # OPTION 1 
    #     "Asha! Or Avatar! Whatever! How dare you!"

    #     vivi angry "Asha! Or Avatar! Whatever! How dare you!" 
    #     vivi angry "If you feel that way, why are we even speaking? I'm one of them, you know!"
    #     ava sad blush "Our humblest apologies, Vivi. We never intended to offend you. We have led vastly different lives, you see."
    #     vivi neutral "Well you've managed to offend me regardless." 
    #     ava neutral "Why don't we talk about something else...you were saying earlier?"
    #     #JUMP to vivi saying "Yeah, so about that exit I mentioned..." 

    # # OPTION 2 +ATTRACTION
    #     "Maybe we all matter, Asha."

    #     vivi neutral "Maybe we all matter, Asha,"
    #     vivi sad "Maybe we're all just specks of sand on a cosmic beach."
    #     vivi sad "Our lives only have the value we give it. Yours. Mine. Theirs."
    #     ava sad "There are times we wished for a simpler life. Family. Friends. Love, perhaps? All forbidden. Even tears."
    #     vivithinking "Whoa. Even tears? Here I thought I was a hot mess."
    #     vivi sad "That must've been awful. Well, I'm here now, so dry those eyes."
    #     ava sad blush "Your heart speaks strangely, but with truth. Tears do not come easily to us. Thank you, Vivi."
    #     # JUMP TO: vivi saying "Yeah, so about that exit I mentioned..." 


    # # OPTION 3 +ATTRACTION
    #     "Asha, respectfully, I disagree with you."

    #     vivi neutral "Asha, respectfully, I disagree with you."
    #     vivi neutral "Humans have identities, lives, and belief systems. Like you. We're complex. Like you. And you're no goddess. You're just a woman calling herself one."
    #     ava happy "Really? In our world, humans are simple creatures incapable of conscious thought." 
    # vivithinking "Hold my bujo, I'm about to destroy this woman."
    #     vivi happy blush: "Well you're speaking with me right now, are you not? I'm human. Would you say I'm incapable of conscious thought?"
    #     ava surprised blush: "Well, when you put it as such...who are we to argue? We apologize."
    # vivithinking "About time! Still, I can't forget why I came here."
    #     #JUMP TO: vivi saying "Yeah, so about that exit I mentioned..." 

    # vivi happy "Yeah, so about that exit I mentioned..."
    # vivi neutral "I spotted an emergency hatch in the glass above you. We can pop it open and escape. Look here at the win-"
    # vivi surprised "...dow"
    # vivithinking "What the heck am I seeing?"
    # vva surprised "Radiance protect me! What-"
    # vivi surprised "IT'S LIKE MORTON'S SALT GIRL COVERED IN TINFOIL AND ROASTED UNDER A JET ENGINE?!"
    # vivithinking "Dammit. I've seen this thing in nightmares." 
    # vivithinking "I can't move, I can't breathe."
    # ava neutral "Do you...jest? We see a cold abyss, pulsing with hunger and emptiness."

    # show urshu happy at left

    # urshu happy "You are both correct! Those are the spirits of passengers lost to the fabric of space-time. Or perhaps how you see them.. hard to say sometimes."

    # show vivi sad at left
    # vivi sad "Those poor souls...is there no help for them?" 
    # ava sad "Is there no help for us?"
    # show sad at left
    # urshu sad "None for them, I fear."
    # show vivi neutral at left

    # # <CHOICE>

    # #OPTION 1 
    #     "Nightmarish. That's the only word for it."

    #     vivi surprised "Nightmarish. That's the only word for it."
    #     vivi angry "And I want nothing to do with whatever that is."
    #     ava surprised "Were you not lamenting those same souls?"
    #     vivi angry "Since when do you care? There's no point to all of this."
    #     show urshu happy at left
    #     urshu happy "Ah, but there is. That could be you one day."
    #     urshu neutral "So..."
    # #JUMP TO: urshu "Do you..have any questions?"


    # #OPTION 2 +ATTRACTION
    #     "Terrifying. I can't imagine how it feels."

    #     vivi sad "Terrifying. I can't imagine how it feels."
    #     ava sad "A circular void haunts my every thought. We fear it."
    #     show urshu happy at left
    #     urshu happy "Best not to think too hard about it."
    #     urshu neutral "So instead..."
    #     # JUMP TO: urshu "Do you..have any questions?"

    # urshu neutral "Do you..have any questions?"
    # urshu happy: " Anything about the Ouroboros Express you want to know..?"
    # ava surprised "So are we truly dead? Our service to the Goddess has ended?
    # urshu neutral "‘All quite true. All of it. I wish I could offer better news, but on the Ouroboros Express your soul is bound for the afterlife."
    # ava sad "But..this cannot be!"

    # show vivi sad at left
    # vivi "Oh, Asha! I'm so sorry. I would say I couldn't imagine, but given the circumstances..."
    # vivithinking "Oh my God, c'mon, Vivi, shut up, summon your inner reporter, and ask the Conductor something clever!"

    # # <CHOICE>
    #     #OPTION 1 +ATTRACTION
    #     "Can we get out of here?"

    #     vivi surprised "Can we get out of here?"
    #     show urshu neutral at right
    #     urshu "No, Miss Sanssouci. Your lives belong to the cosmic fabric now. Tomorrow you will see, should any lingering doubt remain."
    #     vivi surprised "But how did I...?
    #     urshu "Not important. The destination is."
    #     vivithinking "Maybe it's not important to you, but why can't I remember how I died?"
    #     vivi angry "Mind divulging our destination then?"
    #     urshu "The destination? Why, that is up to you, is it not?"
    #     vivithinking "Like getting blood from a turnip, this guy!"
    #     Urshu neutral "Vivi, Asha, the universe does not decide your fate here; fate has placed the compass in your hands. Here and now."
    #     # JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"

    # #OPTION 2 
    #     "So am I going to Hell, then?"

    #     vivi surprised "So am I going to Hell then?"
    #     show urshu neutral at right
    #     urshu neutral "Depends. Were you good, deserving of reward, or a villain, destined to rot eternally in Hell? Hell! A silly tale to frighten ill-mannered children, at best."
    #     vivi surprised "So...Heaven?"
    #     urshu surprised "Heaven - what a noble concept. The word boring also comes to mind..."
    #     vivi angry "Fine, it's not either one."
    #     vivithinking "Just like pulling teeth..."
    #     #JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"
        
    # #OPTION 3
    #     "Why do you do this job?"

    #     vivi sad "Why do you do this job?"
    #     show urshu surprised at right
    #     urshu surprised blush "That is the first time anybody has asked me that! Well to be honest, the tale is long, so perhaps another time?"
    #     vivi sad: "Oh..."
    #     urshu happy "In short, my destiny is to be on this train, one way or another."
    #     #JUMP TO: vivi "We all die, one way or another, so what's the point of all this?"

    # vivi sad "We all die, one way or another, so what's the point of all this?"
    # show ava happy at right
    # ava happy "The answer to that lies within you, Vivi."
    # vivi neutral "Well, I cannot thank you both enough for this wonderful chat. Time to head back to my room, now."
    # ava happy "See you soon, Vivi. The All is the One."
    # ava sad "We have much to ponder. May your dreams be peaceful and warm."
    # vivi neutral "Yeah yeah...you too, Asha."
    # vivithinking "Ugh, I think I need to go lie down. That was a lot to take in."

    # # JUMP TO: Debrief Denial



    # FREE ROAM 2 - Inquisitor Darius

    # LOCATION: dining car

    # show vivi neutral at left

    # show darius neutral at right

    # vivithinking "Darius is... drinking? Guess mindflayers need a break every now and then too."

    # vivi "Enjoying a drink?"

    # # <CHOICE>

    # darius surprised "Hmm? Oh, yes. Would you like one? I'm a bit of a lightweight."
        
    # #OPTION 1 
    #     "Sure."

    #     vivi "Sure."
    #     # SOUND: glassclink
    #     darius neutral "There you are."

    #     vivi "Thank you."

    #     vivithinking "Is this... piña colada?"

    #     vivi happy "Didn't think you had a sweet tooth."

    #     darius happy "It's actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."

    #     darius sad "Mindflayers and hard alcohol... don't mix."

    #     vivithinking "They shudder at this, it ripples through their sleek frame like a gentle breeze. Gotta be a story there."

    #     # JUMP TO: vivithinking "Why is the air here so... heavy?"


    # #OPTION 2
    #     "I'm okay, thank you."

    #     vivi "I'm okay, thank you."
    #     darius neutral "Not a fan? That's fine. I can make you a non-alcoholic version."

    #     # SOUND: glassclink

    #     vivi surprised "Fruits? I didn't think you had a sweet tooth."

    #     darius happy "It's actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."

    #     darius sad "Mindflayers and hard alcohol... don't mix."

    #     vivithinking "They shudder at this, it ripples through their sleek frame like a gentle breeze. Gotta be a story there."

    #     #JUMP TO: vivithinking "Why is the air here so... heavy?"


    # vivithinking "Why is the air here so... heavy?"

    # darius neutral "Are you ok, Ms. Sanssouci? You look a little... sickly."

    # darius surprised "Ahh! My apologies."

    # vivithinking  "A quick flick of the wrist, graceful as ever. Did they do something..? Things feel a lot lighter."

    # darius neutral "A mindflayer's brain is a powerful thing. Sometimes emotions and thoughts can leak out into the atmosphere. I believe you may have been feeling my...malaise, so to speak."

    # darius neutral "I don't speak with humans often, so I've developed a bit of a bad habit of letting my emotions wander."

    # vivi neutral "It's alright, I figured you didn't get to speak with humans much. You can just call me Vivi by the way, no need for formalities."

    # darius neutral "Very well."

    # vivi neutral "What had you so bothered?"

    # darius sad "Well aside from some unpleasant memories... I've been thinking."

    # darius sad "I have many questions about this place and this conductor. But I don't believe asking him will get me any of them..."

    # darius neutral "I've let myself fall into passivity too often, simply allowing the current to wash over me. This time, I'll act."

    # vivithinking "They want to act huh? Looks like we're on the same page."

    # vivi neutral  "Listen, I was thinking about looking for a way off of this damnable train. What do you think?"

    # darius neutral "Hmm. I'm not interested in leaving just yet, but I think there is a way our needs could both be met."

    # darius neutral "I am going to trail the conductor. Should you wish, you could join me and look for any sign of an exit strategy."

    # vivi surprised "Trail? Are you some sort of detective?"

    # darius surprised "What? Ahem I'm-- something like that, yes. I have the skills needed for the job, don't you worry."

    # vivithinking "What a weirdo. They seem pretty confident though, so I'll take their lead on this. Nice to be able to rely on someone for once."

    # vivi happy "Sounds good to me. When did you want to start?"

    # darius neutral "Well... now is as good a time as any, don't you think?"

    # vivi surprised "Straight to business then? Lead on."


    # LOCATION: lounge


    # show darius neutral at right

    # show vivi neutral at left

    # darius neutral "Stay behind me and follow my motions."

    # vivithinking "Where is he?"

    # hide darius

    # hide vivi

    # show urshu happy at left

    # show vivi angry right 

    # # SOUND: whistling

    # vivithinking "Is he... whistling? This asshole has us captive here and he's whistling?"

    # hide urshu 

    # hide vivi

    # show darius neutral at left

    # show vivi right angry

    # darius neutral "Calm yourself."

    # vivi angry "Can't you just ask your questions now and I'll go off to look for an exit while he's distracted?"

    # darius angry "That isn't what we agreed on. Besides, you've spoken to him. Do you really think he'd just give up his secrets so easily?"

    # darius neutral "This is the best way to find out more. So please, it may be human nature to be quick to anger but calm yourself."

    # vivithinking "Those last words held an undercurrent to them. Like the rumble of an oncoming storm."

    # vivithinking "Where the hell did that come from? Darius was pretty agreeable up until now."

    # darius neutral "Vivi, look."

    # hide darius

    # hide vivi
    # show urshu happy at left

    # urshu happy "Suppose it's time to retire for the evening. Should do the rounds, ensure nothing is out of order."

    # hide urshu

    # show darius surprised at left

    # show vivi surprised at right

    # # SOUND: teleport

    # darius surprised "Is that..."

    # vivi surprised "Magic. Yeah I think so."

    # darius happy "This is exactly what I wanted to see. Come, let's pursue him."

    # show vivi happy blush 

    # vivithinking "Aww, their little mouth tentacles curl up when they're happy."

    # show vivi angry blush 

    # vivithinking "What am I thinking? This isn't the time Vivi!"

    # LOCATION: observatory

    # show darius surprised at right

    # show vivi surprised at left

    # darius surprised "Been a while since I had to track a mage. Hopefully my senses are somewhat intact here."

    # # <CHOICE>

    # vivithinking "They're a natural at this. I'm kinda curious to know more. Should I ask them?"

    # # OPTION 1 
    #     "Hey, how did you develop these skills anyways?

    #     vivi neutral "Hey, how did you develop these skills anyways?"

    #     darius neutral "Oh, I was trained in observation since I was young. Making myself scarce, learning my target's habits and routines. As for reading people, that comes rather naturally to mindflayers."

    #     vivi neutral "Cause of the whole mind reading thing?"

    #     darius neutral "Yes, there's always that to fall back on. But we're also very good at sensing emotional shifts, lapses in thought... lies."

    #     vivithinking "!"

    #     vivi neutral "Must come in handy as a detective."

    #     darius blush surprised "Yes, it's uhh...very useful."

    # # OPTION 2
    #     "Never mind."

    #     vivithinking "Never mind."
    #     darius neutral "You seem rather quiet back there."

    #     vivi neutral "Just looking out for any sign of an escape route."

    #     #JUMP TO: darius neutral "Found anything yet?"


    # darius neutral "Found any sign of an escape yet?"

    # vivi angry "No. It's like nothing makes sense on this train, the doors just lead to more doors.    There's no final car either. It's almost like it just... keeps going."

    # darius neutral "Hmm. If my hunch is correct, then there's a good chance there is no escape from this train."

    # vivi angry "What? So you think that Urshu is telling the truth?"

    # darius neutral "Maybe part of it. There are things he's keeping from us, of that I'm sure."

    # vivi neutral "Hold on."

    # vivithinking "Speaking of hunches, I've got one of my own."

    # #I'd like Vivi to move to the right here and Darius to move to the left. Is that possible without making them disappear and reappear?

    # darius surprised "Ms. Sanssouci, I didn't take you to be one for stargazing, but this hardly seems the time for it."

    # vivi neutral "Shut up."

    # # SOUND: crash

    # vivithinking "What... what the fuck is that through the window?"

    # darius surprised "Vivi? You look like you've seen a ghost."

    # vivi surprised "Just... just take a look for me will you? Do you see it? The weird... figure out there?"

    # darius neutral "Very well. What kind of figure?"

    # vivi angry "Just look! It's in a dress but it's like it has no torso or anything! It has some sort of mirror thing for a head!"

    # darius surprised "I don't see this figure you're speaking of, but... oh my."

    # vivi surprised "What? What do you see?"

    # darius surprised "I... I knew it. This place... it is his."

    # vivithinking "There's awe in those words but also something else. Fear?"

    # show urshu neutral at right

    # urshu neutral "Interesting! What do you see out there?"

    # vivi surprised "Where the hell did you come from?"

    # urshu neutral "I appear when I am needed my dear! Now Mx. Wrecker, I believe from your tailing of me tonight that you have something you desire. May it be related to what you see out there, I wonder?"

    # show darius surprised at right
    # darius surprised "You... Are you not an ambassador of the Eternal Rest?"

    # urshu surprised "Oh? And what would make you think that?"

    # darius surprised "Out there... I could've sworn I saw its tendrils grasping out for me."

    # urshu neutral "Ahh, now I see. I'm afraid to disappoint you Mr. Wrecker, but unfortunately that is not the case."

    # urshu neutral "The cosmos holds many things, not all of them friendly. Some may draw themselves to you, while others may find another passenger more appealing. What you saw is simply one of those entities."

    # show vivi angry at right

    # # <CHOICE>

    # vivithinking "Are they really going to act like I'm not here? I have questions too you know!"

    # # OPTION 1 
    #     "Excuse me? You're going to answer my questions now."

    #     vivi angry "Excuse me? You're going to answer my questions now."

    #     urshu neutral "I know asking questions is in a reporter's nature, but is decorum not? Mx. Wrecker is clearly "going through something" as it were, so I'd appreciate your silence."

    #     vivi angry blush "I–"

    #     vivithinking "Scolded like a schoolgirl. I hate that he's right."

    #     #JUMP TO: darius neutral "I've been having... visions."

    # # OPTION 2
    #     "Darius, compose yourself. Didn't you have questions for him?"
        
    #     vivi neutral "Darius, compose yourself. Didn't you have questions for him?"

    #     darius surprised "You're right, Vivi. Thank you."

    #     #JUMP TO: darius neutral "I've been having... visions."

    # darius neutral "I've been having... visions."

    # darius sad "A loving couple, screams, confusion... I can't make sense of it all."

    # show urshu neutral at right
    # urshu neutral "I see. Tell me, how much of your... end, do you remember?"

    # darius sad "My end?"

    # urshu sad "I wasn't lying to you. Any of you. All of you here have well and truly passed on from the world of the living."

    # vivithinking "That sounded... honest. He can't be serious, right? He can't be..."

    # urshu sad "As for you Mx. Wrecker, hmm. I promised I wouldn't get involved in any of your journeys, but I believe showing you this will help."

    # vivithinking "He stretches out his hand. Darius takes it."

    # #SOUND: twinkle

    # #SOUND: horror

    # darius surprised "What... WHAT IS THIS?"

    # urshu sad "I understand this must be hard. But nothing I've shown you is an illusion. These were your choices, your actions."

    # show vivi sad at left

    # vivithinking "}I've never seen Darius like this before."

    # urshu sad "And as for you Ms. Sanssouci, I know this must've been hard for you as well. You may not believe it, but I am here to help you, you know."

    # vivi sad "So it's true then? We're really gone?"

    # vivithinking "He simply nods."

    # Vivthinking "... I don't know what to say."

    # show darius angry at left
    # darius angry "Urshu. What was it all for then? Who am I anymore?"

    # urshu sad "Unfortunately, I can't answer that for you my friend. I'm sure you'll learn the answer yourself, in time."

    # urshu neutral "Ms. Sanssouci, if you don't mind, could you meet me at your cabin shortly? We have some matters to discuss."

    # show vivi neutral at left
    # vivithinking "We have things to discuss?"

    # vivithinking "The tension hangs in the air. It's like a miasma, cutting the oxygen and making my heart pace."

    # urshu happy: "...On a lighter note, we will be serving brunch tomorrow! Do come... well I'd say "early" but time has no meaning here anyways. Ta-ta!" 

    # hide urshu

    # show darius surprise at right
    # darius surprised "What?"

    # vivithinking "The air is getting thin, heated even. It's just like before in the dining car. Darius is..."

    # darius angry "Don't toy with me! COME BACK!"

    # #screen shake

    # darius angry "I AM AN INQUISITOR OF THE LORD–"

    # vivi sad "Darius... your emotions are–"

    # #screen shake

    # # pause

    # vivithinking "They stop."

    # darius blushing sad "I... I suppose I'm not anymore."

    # darius blushing sad "I'm sorry Vivi, I lost my temper. Thank you for joining me, and I hope you can forgive that little outburst." 

    # vivithinking "Are they muttering to themselves?"

    # darius sad "It was all pointless..."

    # hide darius

    # vivi sad "This is all too much... I need to sleep."

    # # JUMP TO: Debrief Denial.



    # FREE ROAM 2 - Susu'Rha

    # LOCATION: Lounge

    # vivithinking "This train is driving me insane. I refuse to play into the conductor's games."

    # vivithinking "Yep. It seems Susu'Rha is lounging on one of the recliners."

    # show vivi neutral at left

    # vivi "What are you doing?"

    # show susurha netural at right

    # susurha "What does it look like I'm doing at the moment? I'm deep in the meditative process of trying not to think about the circumstances that surround me."

    # susurha "And girl... let me tell you that the cushions this contraption houses are just soooo.... Welcoming."

    # #<CHOICE>
    # susurha "You should give it a try."

    # #OPTION 1 
    #     "I'll stand."

    #     vivi "I'll stand."
    #     susurha "Suit yourself but I see you weak at the knees. Eyes drawn to where I lay. The cushions calling your name."
    #     susurha "Vivi..."
    #     vivi "What?"
    #     susurha "I'm saying you look exhausted, but to each their own."
    #     vivithinking "Susu'Rha goes silent as they sink into their chair."
    #     vivithinking "Ouch. The headache is only getting worse."
    #     vivithinking "Maybe this was a mistake."
    #     # JUMP TO: susurha "This place is a prison."

    # #OPTION 2 +ATTRACTION
    #     "I'd love to."

    #     vivi "I'd love to."
    #     vivithinking "They reach out and slide a chair my way with ease."
    #     # SOUND: Vivi sits down in a super comfortable recliner.
    #     vivithinking "Holy shit..."
    #     susurha happy "Feels like a dream, don't it?"
    #     vivi "Feels like I'm sinking."
    #     vivithinking "We sit in silence, enjoying the simple comforts."
    #     vivithinking "The headache eases off, only somewhat."
    #     #JUMP TO: susurha "This place is a prison."

    # susurha "This place is a prison."

    # susurha "The Archdruids warned of daemons that kidnap their prey and treat them to endless luxuries."

    # susurha "Perhaps this is that. We are being fed lies and comfort just so that we can become sooo relaxed and THAT is when they'll strike...to feast on our satisfied souls."

    # susurha "To be frank with you, I always believed such tales to be nothing more than a bunch of creative nonsense to make the less fortunate in the clan okay with their shitty life conditions."

    # susurha "But..."

    # # <CHOICE>
    # susurha "I'm beginning to think that those sad old sods that lived in a forest their entire lives weren't completely high as the stars above."

    # #OPTION 1 +ATTRACTION
    #     "This place freaks me out."
        
    #     vivi "This place freaks me out."
    #     susurha "I feel that in my bones. Oh, this place worms its way down my spine like a spider in the night."
    #     susurha "Makes me feel like burning the whole place down."
    #     susurha "Imagine..."
    #     susurha "You're walking in the woods one day, lost in the spiraling storm of every possible thought you've ever had bouncing around in your head, and then..." 
    #     susurha "Suddenly finding yourself trapped with a bunch of odd looking individuals, no offense, in a metal tube speeding to an unknown locale."
    #     susurha "All the while you're being told that..."
    #     susurha sad "You are dead."
    #     vivi "Is that how you died? I mean ended up here."
    #     susurha "How you'd figure that?"
    #     #JUMP TO: susurha neutral "We will be dead if we stay here any longer."

    # #OPTION 2 
    #     "That's absurd. That can't be the case."

    #     vivi "That's absurd. That can't be the case."
    #     "..."
    #     vivithinking "They're glaring at me. Looking me up and down.""
    #     susurha angry "Let me tell you what is absurd." 
    #     susurha angry "You're walking in the woods one day, lost in the spiraling storm of every possible thought you've ever had bouncing around in your head, and then..."
    #     susurha "Suddenly finding yourself trapped with a bunch of odd looking individuals in a metal tube speeding to an unknown locale."
    #     susurha angry "All the while you're being told that YOU ARE DEAD."
    #     # JUMP TO: susurha neutral "We will be dead if we stay here any longer."

    # susurha neutral "We will be dead if we stay here any longer."

    # vivi "We need to get out of here."

    # vivithinking "They raise a nonexistent eyebrow. Now I've got their attention."

    # susurha happy "Now that is something I absolutely LOVE hearing. Please tell me you have some sort of idea of getting off this thing."

    # vivithinking "..."

    # vivi "I do not."

    # susurha neutral "Hmm..."

    # susurha happy "Well, lucky for you, I have been indulging in some...sightseeing around this fine place and I think I know just the perfect spot for us to run away together."

    # Vivi happy "Where?"

    # susurha happy "The observatory and its thin glass windows."

    # susurha happy "Oh, I do so very much love gazing up at the stars above like I did when I was a young prince."

    # vivi happy "Now?"

    # susurha happy "Why wait?"

    # vivi happy "Are we really doing this?"

    # susurha happy "Sweetie, it's a date."

    # vivithinking "They take me by the hand and drag me along."


    # LOCATION: Observatory

    # show susurha surprised at right
    # show vivi surprised at left

    # vivithinking "Golden fiery flashes shine through the glass windows of the cabin, and in-between those sparkles of light..."

    # vivithinking "Darkness."

    # vivithinking"Where are we?"

    # show vivi neutral

    # # <CHOICE>
    # susurha surprised "So strange, when I was just here I saw the night sky riddled with an ocean of stars, but now... it's just nothing."

    # #OPTION 1 +ATTRACTION
    #     "Worried?"

    #     vivi "Worried?"
    #     show susurha neutral
    #     # SOUND: Susu'Rha scoffs.
    #     susurha "Me, worried? Never. I make sure to go out of my way to avoid feeling worried, but this..."
    #     susurha "It just doesn't make sense.  I was so sure I knew what I saw. It had the same constellations burned into my mind from that night and..."
    #     susurha "It hasn't even been an hour since I scouted the place."
    #     susurha "Where are we?"
    #     vivi "I was thinking the same thing."
    #     susurha happy "I suppose there is only one way to find out."
    #     #JUMP TO: susurha "This way."

    # #OPTION 2
    #     "Where is this exit you sold me?"

    #     vivi "Where is this exit you sold me?"
    #     susurha neutral "Forgive me."
    #     # JUMP TO: susurha "This way."

    # #OPTION 3 
    #     "Maybe you didn't get a clear view?"

    #     vivi "Maybe you didn't get a clear view?"
    #     susurha "Maybe..."
    #     susurha neutral "But I was so sure I knew what I saw. It had the same constellations burned into my mind from that night and..."
    #     susurha "It hasn't even been an hour since I scouted the place."
    #     vivithinking"..."
    #     susurha "Doesn't matter."
    #     # JUMP TO: susurha "This way."

    # susurha "This way."

    # susurha "Help me stack these chairs up under that central window on the ceiling."

    # # SOUND: Vivi and Susu'Rha exert themselves stacking chairs on top of each other.

    # vivithinking "This seems incredibly unplanned, but I don't really have a choice."

    # vivithinking "I need to get off this train."

    # vivithinking "And this one is my best chance."

    # susurha happy "This reminds me of back when I was younger and I'd sneak out of my tower bedroom to wander on top of the surrounding castle walls."

    # vivithinking "They climb the tower of stacked chairs and wrestle with the loose screws of the ceiling's window. Golden light is glistening off their scaly skin."
    # vivithinking "I wonder how it is, living in a castle..."

    # # <CHOICE>
    # vivithinking "All I can see is the biggest smile I've ever seen."

    # #OPTION 1 
    #     "Can we please hurry this up?"

    #     vivi "Can we please hurry this up?"
    #     # SOUND: Susu'Rha scoffs.
    #     susurha neutral "You know, you remind me a lot of the nobility that I grew up around."
    #     susurha "They too found my voice to be annoying."
    #     vivi "That's not what I meant."
    #     susurha "Nevertheless, they listened as I slowly found my way out of that hell."
    #     "Aha... Susu'Rha appears soft, but they actually have a nerve..."
    #     #JUMP TO: susurha "Voila."

    # #OPTION 2 +ATTRACTION
    #     "It sounds like you lived a fairy tale."

    #     #SOUND: Susu'Rha laughs.
    #     susurha "I suppose from the outside it could come across with that poetic fantasy allure."
    #     # <CHOICE>
    #     susurha neutral "Apologies, I believe you were cracking a joke at me."
        
    #         #OPTION 2-1 +ATTRACTION
    #         "I wasn't. Tell me more."

    #         vivi "I wasn't. Tell me more."
    #         susurha happy "Perhaps I shall at another time."
    #         # JUMP TO: susurha "Voila."

    #         #OPTION 2-2
    #         "It's okay."

    #         vivithinking "It's okay"
    #         # JUMP TO: susurha "Voila."

    # susurha happy "Voila."

    # # SOUND: The window clicks open.

    # susurha happy "We are homeward bound."

    # hide vivi
    # hide susurha

    # vivithinking "I climb up the tower of chairs and we both peak our heads out of the opened window."

    # vivithinking "..."

    # vivithinking "This is..."

    # vivithinking "Unimaginable."

    # vivithinking "Spiraling celestial bodies swirl all around as the train speeds faster than anything I've ever seen."

    # vivithinking "Flames burst from the train's tracks and were sucked into the void."

    # vivithinking "My hair flaps in my face. I really wanna scream. But I can't."

    # vivithinking "Susu'Rha stares out into the visual abyss of...wherever we are. They mumble to themselves but I can't hear anything."

    # vivithinking "All I could get was the sight of a tear rolling down their cheek."

    # vivithinking "I turn to see what they are staring at and I see..."

    # vivithinking "That thing."

    # vivithinking "A reflective dress floating in the wind, but it slowly inches closer to us."

    # vivithinking "It moves with purpose. It moves like it's alive."

    # vivithinking "Dangling like a puppet as it comes closer and I can see its face."

    # vivithinking "My face."

    # vivithinking "Reflecting on the concave mirror plate it has on its shoulders."

    # vivithinking "It crawls closer to us, inches away from my own face."

    # vivithinking "I feel the wind stroking my face like cold hands, pulling me closer to it."

    # vivithinking "I cannot breathe."

    # vivithinking "I cannot breathe."

    # vivithinking "I cannot breathe!"

    # vivithinking "It reaches out to me..."

    # urshu angry "Get down from there!"

    # #SOUND: The sounds of chairs clashing and Vivi and Susu'Rha hitting the floor.
    # #VISUAL: The screen shakes.
    # #SOUND: The window slams shut.
    # Show urshu angry at right

    # vivithinking "I can breathe again!"

    # show vivi surprised at left

    # vivi surprised "What the hell was that?"

    # urshu angry "When I told you to go seek the truth I didn't quite mean to go and make us all something's meal."

    # vivi surprised "What the hell was that?!"

    # urshu neutral "The truth, Miss Sanssouci. The truth of the matter whether you choose to accept it or not is that you and Druid Balrinn here have passed in life and there is no getting off this ride."

    # urshu "Please, don't try to get off this train again. I may not be there next time to save you."

    # show susurha neutral at left

    # susurha "What was that thing I saw out there?"

    # urshu "What you and Miss Sanssouci witnessed depends entirely on yourselves."

    # urshu "May I suggest returning to your cabins and getting some rest?"

    # vivithinking "Oh baby. Caught between hell and a better place."

    # vivithinking "Ugh... I need a drink."

    # #  JUMP TO: Debrief Denial.



    # Debrief Denial

    # LOCATION: cabin

    # show vivi angry at left

    # show urshu neutral at right

    # vivi neutral "Outside this train... the void... it's too much. I thought I was living a nightmare before, but that outside...  That was chilling to my core."

    # vivi angry "Do you get off in seeing all of us in pain? Giving us all an existential dread that we can't fix?"

    # urshu neutral "Seeing the outside is sobering for many. I'm glad you're no longer denying the gravity of the situation. I understand that this is a lot to process." 

    # urshu happy "We've left a journal for you. I thought a reporter such as yourself would like the ability to write down her thoughts."

    # urshu neutral "I hope you utilize it. Please know that nobody else, including myself, can ever read what's inside. Everyone deserves a private place to think."

    # hide urshu

    # vivi angry "He's so infuriating! I don't know why I even bother asking him anything."

    # vivi neutral "But, he might be right. Might as well use the journal."

    # #Journal entry

    # "This is real. It doesn't make sense but it's all really happening. There was no way off the train. How the hell did I die? I thought I'd leave a mark on the world before I left. Or at least someone special. It's all so frustrating. The conductor is the worst, acting like this is a game. THIS IS OUR LIVES! At least I'm not the only one going through this."

    # # JUMP TO: Briefing Anger


    jump scene2
