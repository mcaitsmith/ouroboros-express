# The scene starts here.

label anger_cs1:

    #Character Selector 1

    # LOCATION: cabin
    # scene cabin with fade

    # show vivi neutral at left with dissolve

    vivi neutral "Alright. Time to play. What better to do when trapped on a train towards impending doom."

    # <CHOICE>
    vivi neutral "Who can I talk to?"

    menu:
        # OPTION 1
        "Avatar of Asha":

            $ fr1_anger_choice = "Ava"

            vivi neutral "Maybe the goddess would like a game. It'd be nice to talk to her more."
            # JUMP TO: FREE ROAM 1 - Ava

        # OPTION 2
        "Inquisitor Darius Wrecker":

            $ fr1_anger_choice = "Darius"

            vivi neutral "I want to know more about Darius. Maybe they'd be up for a game."
            # JUMP TO: FREE ROAM 1 - DARIUS

        # OPTION 3
        "Susu'Rha Balrinn":

            $ fr1_anger_choice = "Susu'Rha"

            vivi neutral "I'm sure Susu'Rha would like a game. They seem to make things more fun."
            # JUMP TO: FREE ROAM 1 - SUSU'RHA



    # FREE ROAM 1 - Ava

    # # LOCATION: observatory

    # show vivi neutral at left

    # vivithinking sad "Looks like our friendly neighborhood sun goddess is here."

    # show ava left happy

    # vivithinking surprised "Oh, what's this? A sunny disposition?"

    # show ava sad blush with dissolve
    # ava "Hello, Vivi. Has our radiance tempted you today? Come, sit, and play a game. Let us see what future the cards hold."
    # vivi neutral "Are those tarot cards? They look...off."
    # show ava neutral -blush
    # ava "We know not what a "tarot" is, but we have placed three cards in front of you."
    # vivithinking surprised "A sun, a sea monster, and a huge snake?!"
    # vivi neutral "Uh...okay?"

    # # <CHOICE>
    # ava neutral "Choose wisely.":

    # menu:
    #     # OPTION 1 +ATTRACTION
    #     "The sun card.":
        
    #     vivi neutral "The sun card."
    # show ava sad blush with dissolve
    #     ava "The sun can represent light, truth, and love..."
    #     vivi surprised "Finally some good news!"
    # show ava sad -blush
    #     ava "...we had not finished, Vivi. The sun is upside down, so it brings darkness, lies,
    #     indifference."
    #     # JUMP TO: vivi "This is silly! They're just cards. They can't tell us that!"

    #     # OPTION 2 +DECAY
    #     "The sea monster card.":

    #     vivi neutral "The sea monster card."
    #     ava surprised "Ah. Leviathan. The eater of worlds. Scourge of the seas. Dominance. Aggression. We find this interesting."
    #     vivi neutral "Wait, was that a dig at...Darius?"
    #     ava angry "We know of his kind. You would be wise to stay away. His card brings 
    #     darkness...and deceit."
    #     # JUMP TO: vivi "This is silly! They're just cards. They can't tell us that!"


    #     # OPTION 3 +DECAY
    #     "The big snake card.":

    #     vivi neutral "The big snake card."
    #     ava surprised "Curious. We have not seen this card before. Curious, indeed. It resembles the snake biting its own tail, the Ouroboros."
    #     Ava neutral "But of course, snakes, reptiles. They are of the same family. A warning... "
    #     vivi surprised "Oh?"
    #     vivi neutral "Is this a dig at Susu'rha?"
    #     ava surprised "I merely am the messenger. And the card could not be clearer. Avoid 
    #     him, Vivienne."
    #     # JUMP TO: vivi angry "This is silly! They're just cards. They can't tell us that!"

    # vivi angry "This is silly! They're just cards. They can't tell us that!"
    # ava surprised "Perhaps, you're right. They are merely cards." 
    # ava sad "..."
    # ava sad "In the mirror this morning, fate stared back at us. And for you, Vivienne?"
    # vivi sad "For me too, Asha."
    # vivithinking neutral "We're fading even faster than we were yesterday. There's less of me and the train every second. Not totally unnerving at all!"
    # # VISUAL: screen shakes, light flashes 
    # # SOUND: ava says "ugh"
    # ava angry "Why, Vivienne?" 
    # ava angry "What was the point of it all?! All our sacrifices. For what?"
    # vivithinking surprised "Damn! And I thought I was having trouble coping."

    # # <CHOICE>
    # vivi neutral "Look, Asha..."

    # menu:
    # # OPTION 1 +ATTRACTION +DECAY
    #     "...chin up, princess, or the crown slips.":

    #     vivi neutral "...chin up, princess, or the crown slips."
    #     ava angry "Princess? We were not royalty, those inbred lickspittles. We came from 
    #     nothing."
    #     vivithinking neutral "With that stiff upper lip and all? Yeah, right." 
    #     ava angry "Why?! We are no more! Our mother sacrificed us. Gutted us like a butcher 
    #     does a fatted calf."
    #     vivithinking surprised "Unnecessarily graphic and undeniably tragic!"
    #     vivi surprised "That's your people's tradition? Sacrifice?!"
    #     ava sad "We are sacrificed lest people love us too much. Once, an avatar nearly toppled the royals. But now, that is only but a distant fairytale ."
    #     vivi neutral blush "Well, then no offense, but you're better off here. If your whole purpose was to be sacrificed, then guess what?"
    # show ava happy blush with dissolve
    #     ava "Then our service is at an end. We are free."
    #     vivi happy "Yes. I like that. Free."
    #     vivithinking happy "Not a great start, but a good ending, right?"
    # show ava happy -blush
    #     # JUMP TO: vivi neutral blush "Thank you for sharing with me, Asha."

    # # OPTION 2 +ATTRACTION
    #     "...I know what you mean about sacrifices.":

    #     vivi sad "...I know what you mean about sacrifices. You're not alone. My career always came first, over friends, family, love. Where'd it get me?" 
    #     vivi angry blush "Here!"
    #     ava sad "I'm aware of your tale, little one. And I am sorry for that."
    #     ava angry "We shall fade to darkness soon. Have you not seen it in your dreams?"
    #     vivi angry "You mean nightmares? Yeah..."
    #     vivi neutral "Well... at least we don't have to make any more sacrifices, right?"
    # show ava happy blush with dissolve
    #     ava "That is true, yes. Our service is at an end. We are free."
    #     vivi happy "Yes. I like that. Free."
    # show ava happy -blush
    #     ava "Thank you, Vivi. We hope you return."
    #     vivithinking happy "Not a great start, but a good ending, right?"
    #     # JUMP TO: vivi neutral blush "Thank you for sharing with me, Asha."

    # # OPTION 3 +DECAY
    #     "...Wanna know what they say on earth where I'm from? Pull yourself up by your  
    #     bootstraps, and deal with it, Asha.":

    #     vivi neutral "...Wanna know what they say on earth where I'm from? Pull yourself up by 
    #     your bootstraps, and deal with it, Asha."
    #     ava angry "Perhaps you should heed your own advice, Vivienne."
    #     vivithinking angry "Hmph. Well, someone's got their knickers in a 
    #     twist!" 

    # # ava exits

    # # vivi exits

    # vivi neutral blush "Thank you for sharing with me, Asha."
    # vivithinking neutral "That went better than I thought. Maybe one of the others wants to play a game as well."
    # vivithinking angry "Ugh. And I still gotta find out Urshu's riddle. How am I gonna get off this doomsday train?

    # # JUMP TO: Character Selector 2








    # FREE ROAM 1 - DARIUS 

    # # LOCATION: lounge

    # show darius angry at center

    # vivithinking angry "I can feel them. Seething."

    # show darius neutral at right

    # show vivi neutral at left

    # darius neutral "Well. Cards, then?
    # vivi surprised "Of course you read my mind already. Do you actually want to play?"
    # darius angry "Why not? Seems as though we can't do anything else at the moment."
    # vivi neutral "I don't know a lot of card games."
    # darius surprised "I thought that's all you humans did. Play games. Fritter away your time."
    # darius neutral "We'll play a game I know called Hearts. No need to explain. You'll catch on quickly, even as a human. And we'll learn about each other. About this place. About Urshu."
    # vivithinking neutral "Mon dieu, his hands. Dextrous fingers. Manicured claws."
    # darius neutral "..." 
    # vivithinking blush "Oh shit! They caught me looking. Ughhh, I got distracted. Wait, what is this feeling? Displeasure? Embarrassment? Satisfaction?

    # # <CHOICE>
    # darius neutral "You start."

    # menu:
    # # OPTION 1 +ATTRACTION
    #     "Can you even play this with two people?:

    #     vivi surprised "Can you even play this with two people?"
    #     darius happy "Of course you can. Watch me."
    #     # SOUND: cards shuffling
    #     vivi neutral "You deal so swiftly."
    # show darius happy blush with dissolve
    #     darius "That's kind."
    #     vivi neutral "I'm surprised, given your history."
    #     show darius angry -blush
    #     vivithinking surprised "Definitely should not have said that."
    #     darius "What could you possibly understand about my history?"
    #     vivi surprised "..."
    #     # JUMP TO: darius angry "You still haven't played a card. Take your turn already."

    # # OPTION 2 +DECAY
    #     "You mentioned Urshu. Why bring him up?":

    #     vivi neutral "You mentioned Urshu. Why bring him up?"
    #     darius angry "That little twerp knows more than he lets on."
    #     vivi surprised "You're getting angry."
    #     darius angry "Yes. You should be, too."
    #     vivi surprised "What makes you think I'm not?"
    #     darius neutral "Tsk. This place. I know it. We shouldn't be here."
    #     vivithinking "Now, what does that mean?"
    #     # JUMP TO: darius angry "You still haven't played a card. Take your turn already."

    # darius angry "You still haven't played a card. Take your turn already."
    # vivi angry "Don't tell me what to do."
    # darius neutral "There's no reason to get snippy with me. I'm not the one who trapped us all here."
    # vivi angry "Who are you calling 'snippy'? You're being aggressive. No way to talk to a lady."
    # # SOUND: whoosh
    # vivithinking surprised "That flare of rage again. So bright, it's almost painful."
    # darius surprised "Well. That's... interesting."
    # vivi surprised "What is?"
    # darius neutral "You're unreadable. That is... unusual."
    # vivi neutral "I'm happy to answer any questions you might have about me."
    # darius neutral "Why waste energy on words when I can simply read what's in front of me without them?"
    # vivi happy "Ah, but you can't, can you? And you find that frustrating. Tell me about it."
    # darius angry "You're needling me. Play a card, damn you."
    # vivi happy "Not without knowing what's making you so testy."
    # darius angry "I have never once been 'testy' in a millennia of existence."
    # vivi happy "And yet... here I am, not playing a card."
    # vivithinking surprised "That rage. Pure. So hot that it makes my cheeks flush."
    # darius angry "Fine. Vivi. Normally, I can read the beings around me. It's what makes me such an excellent judge of... character. But since arriving here, that's changed. I feel...cut off. Disarmed."
    # vivi neutral "Darius, you shouldn't be reading my mind without asking first anyway. Bit rude."
    # show darius surprised blush with dissolve
    # darius "I...I'm not trying to-"
    # vivi happy "Please don't do it again. Your turn!"


    # # <CHOICE>
    # show darius neutral blush
    # darius "Forgive me. All of this is new. As I said: unusual." 

    # menu:
    # # OPTION 1 
    #     "Qualify that. 'Unusual'.":

    #     vivi neutral "Qualify that. 'Unusual'."
    # show darius neutral -blush
    #     darius "I don't know how else to explain it. Things were one way. Now, they're not. I'm... adjusting."
    #     vivi neutral "I guess we should do our best to adjust together."
    #     darius happy "We can try that."
    #     vivi neutral "..."
    # # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."

    # # OPTION 2 + ATTRACTION
    #     "That sounds difficult. Like being unmoored."

    #     vivi sad "That sounds difficult. Like being unmoored."
    # show darius surprised -blush
    #     darius "Yes, exactly. 'Unmoored.' You have a way with... words."
    #     vivi happy "Aw, you're just saying that. You think so?"
    #     darius angry "You're mocking me."
    #     vivi surprised "I'm not! Trust me. When I'm mocking you, you'll know."
    #     darius happy "Well then. I look forward to it."
    #     vivi happy "..."
    #     # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."


    # # OPTION 3 + DECAY
    #     "Well, you don't hear me crying about it."
        
    #     vivi neutral "Well you don't hear me crying about it."
    # show darius surprised -blush
    #     darius "I'm sorry?"
    #     vivi neutral "You heard me. Things may be different, but they aren't dire."
    #     darius angry "Not yet, anyway. Give it time, Vivienne. You're just like the rest of your kind."
    #     vivi angry "You don't know me, Darius."
    #     darius neutral "I never claimed to."
    #     vivi angry "..." 
    #     darius angry "..."
    #     # JUMP TO: vivi neutral "You're doing a terrible job at playing this game."


    # vivi neutral "You're doing a terrible job at playing this game. And you didn't even explain it."
    # darius neutral "It would seem so. And it was my suggestion. Apologies. Perhaps another time when I'm less... distracted."

    # # darius exits

    # # vivi exits

    # FREE ROAM 1 - SUSU'RHA

    # # LOCATION: dining car

    #     # VISUAL: screen shakes
    #     # SOUND: the dining car's door slams shut

    #     show susurha neutral at right

    #     show vivi neutral at left

    #     # SOUND card shuffle

    #     susurha surprised "Vivienne! What brings you here?"
    #     vivi blush surprised "Uh... nothing. Never mind. It's stupid. 
    #     vivi neutral "...Well, actually...Do you want to...play a game with me?"
    #     susurha happy "Certainly! There's a wonderful game from my childhood that I'd be 
    #     honored to share with you!"
    #     vivi neutral "What's the game"?
    #     susurha neutral "Truth or Lies."
    #     vivi neutral "What's at stake?"
    #     susurha neutral "Everything. After all, we're riding a slowly decaying train headed 
    #     inexorably toward the cosmic weave."
    #     vivi neutral "I'm not sure..."
    #     susurha neutral "Don't be coy. It doesn't suit you."
    #     vivi angry "I'm not coy."
    #     susurha happy "Okay then."
    #     susurha neutral "Time is of the essence. Sit with me, and together, we'll find out what's 
    #     true, and what isn't."

    # # <CHOICE>
    # vivithinking neutral "Provocative. This one's certainly not boring." 

    # menu:
    #     # OPTION 1 +Attraction
    #         "I'll play.":
        
    #         vivi neutral "I'll play"
    #         susurha happy "Indeed you will. There's nothing quite like an intimate question to 
    #         enliven the mood." 
    #         # JUMP TO: susurha neutral "I'm going to ask you a question. You will answer, 
    #         and I will try to ascertain whether or not you are lying."

    #     # OPTION 2 +Decay
    #         "I'd be revealing too much.":

    #         vivi neutral "I'd be revealing too much."
    #         susurha neutral "You don't even know the contents of the game yet, and you're already  
    #         scared I may pierce your carefully crafted veneer.
    #         vivi angry "I'm a reporter. I don't do masks. I expose the masks of others."    
    #         susurha neutral "Either you're suffering from an acute lack of self-awareness, or you're 
    #         simply a bad liar."
    #         vivithinking angry "The nerve of this creature!"

    #         # JUMP TO: susurha neutral "I'm going to ask you a question. You will answer, 
    #         and I will try to ascertain whether or not you are lying."

    #     susurha neutral "I'm going to ask you a question. You will answer, and I will try to 
    #     ascertain whether or not you are lying."
    #     vivi surprised "That's it?"
    #     vivi neutral "Hit me." 

    #     # <CHOICE>
    #     susurha neutral "The card reads, "You are hiding something.""


    #     menu:
    #         # OPTION 1 +Attraction
    #             vivi neutral blush "Everyone hides something. I'm no exception.":

    #             vivi neutral blush "Everyone hides something. I'm no exception."
    #             susurha neutral "I'm the exception. All of my pretense has been burned away."                                                  
    #             susurha surprised "..."
    #             vivithinking "Why are they looking at me like that?"
    #             susurha neutral "The fire."  
    #             vivi surprised "The what?"
    #             susurha neutral "You're hiding fire."                         
    #             vivithinking "I know what they're going to say..."
    #             # JUMP TO: susurha surprised "You're... angry."
                    

    #         # OPTION 2 +DECAY
    #         vivi angry "Me? Hiding? What about you?!":
    #         vivi angry "Me? Hiding? What about you?! What exactly are YOU hiding behind 
    #         those beady eyes?"
    #         susurha surprised "Deflection!"
    #         susurha surprised "A keen observer of everything but yourself."                            
    #         susurha neutral "Do you know what I see when I look into your eyes? 
    #         susurha surprised "A boiling ocean of fury!"
    #         vivithinking surprised "How could they tell?"
    #         vivi angry "Of course I'm furious. I didn't expect to die."
    #         susurha neutral "This goes deeper. And it's been going on for a long time."
    #         # JUMP TO: susurha surprised "You're... angry."

    #     susurha surprised "You're...angry. And you've been angry far before before your demise."

    #     # <CHOICE>
    #     vivithinking "What if they're right?"


    #     menu:
    #         #OPTION 1 +ATTRACTION
    #             vivi angry "I am angry.":

    #             vivi angry "I am angry."
    #             vivithinking angry "And the cocky bastard leans back in their chair with a smile 
    #             too. Right on cue..."
    #             susurha happy "You know what? For all of my years of frolicking, I believe I am too."    
    #             vivi neutral "Who are you angry at?"
    #             susurha sad "..."
    #             vivithinking neutral "That wiped their smile away."
    #             susurha angry "My... parents, the judgemental cretins."
    #             vivithinking surprised "Their exhale is literally so hot. Wow."
    #             vivi sad  "I'm sorry..."
    #             vivi angry "I'm angry at my ex-boyfriend. He tried to own my wins."
    #             susurha angry "Sounds like.. the courtiers I grew up around! Those leering, grasping 
    #             snobs, interminable features of my childhood!  
    #             susurha neutral "What else? Don't spare the sssavory details."
    #             vivi angry "My ex-girlfriend stole my Datsun and got it towed in another state!"
    #             vivi angry  "And...and...my teacher, Mizz Costello. She told me I was pugnacious. 
    #             And she meant it as an insult!"
    #             vivi angry  "The entire school system sucks! All systems do! Society at large!"
    #             susurha angry "Society! Oh, how I hate Society! I fled all the way to the Viridian 
    #             Wood to escape it!"           
    #             vivi happy "The EXPECTATIONS of people who, at the end of the day, JUST DON'T 
    #             MATTER!"
    #             susurha happy "YES!"
    #             vivi angry "But most of all, my agent, Chloe. It was she who told me to get the scoop 
    #             on this cursed death train." 
    #             susurha neutral "And here we all are."
    #             # JUMP TO: vivithinking neutral "To see them like that. Vulnerable. Staring 
    #             back at me. It's been a while, hasn't it?"


    #     #OPTION 2 +DECAY
    #     vivi angry "You're the one who's angry.":
        
    #         vivi angry "You're the one who's angry."
    #         susurha happy "Again, you're deflecting."
    #         susurha angry "But you are right. I'm furious."
    #         # SOUND: sigh
    #         vivithinking surprised "that exhale's like, 150 degrees. Hate to see them truly 
    #         mad."
    #         susurha angry "The bloodsuckers. The leeches. Those with souls impervious to art and 
    #         music. All of them infuriate me to no end!"
    #         vivithinking surprised "My face is literally burning."
    #         susurha neutral "..."
    #         susurha happy "It feels good to let it out. You should try it."
    #         susurha neutral "That mask you wear, it extracts a toll, you see. I know because I have 
    #         been before the way you are now."
    #         vivi angry "..."
    #         vivithinking angry "What do they mean, "That mask you wear"? I don't have a mask!"
    #         vivithinking neutral "Calm down, Vivienne. Just look at them."
    #         # JUMP TO: vivithinking neutral "To see them like that, vulnerable, staring back at me. It's been a while, hasn't it?"

    #     vivithinking neutral "To see them like that, vulnerable, staring back at me. It's been 
    #     a while, hasn't it?"
    #     susurha happy "I think we got what we needed from this. I imagine whoever runs this 
    #     place did too."
    #     susurha happy "See you around, dear Vivienne."

    #     # susurha exits

    #     vivithinking neutral "That was a lot. I'm going back to my room."

    #     # JUMP TO: Character Selector 2


    # Character Selector 2

    # # LOCATION: cabin

    # show vivi neutral at left

    # vivithinking angry "I feel like I'm getting nowhere! How the hell am I supposed to escape this?"

    # vivithinking neutral "I can already see the outside affecting the train. There are black tendrils wrapping around the outside of the cars. And those noises! They're awful. It sounds like demonic whales fighting. This whole place is slowly dissolving into... I don't know, and I don't wanna find out."

    # vivithinking neutral "I need some time to make a plan of escape."

    # # fade out

    # # fade in

    # vivithinking angry "I can't think straight! My mind is a mess. I need to cool off if there's any chance of me creating a solid plan."

    # # <CHOICE>
    # vivithinking neutral "I think I saw a dartboard in the dining car. It may be a good way to blow off some steam. Maybe I can get a fellow passenger to join me. Competition always helps me think clearer."

    # menu:
    # # OPTION 1 
    # "Avatar of Asha":

    # vivi neutral "Let's see how good the goddess is at darts, shall we?"
    # # JUMP TO: Free Roam 2 / Ava

    # #OPTION 2 
    # "Inquisitor Darius Wrecker":

    # vivi neutral "Darius seems like good competition."
    # # JUMP TO: Free Roam 2 / Darius 

    # # OPTION 3 
    # "Susu'Rha Balrinn"

    # vivi neutral "I'm sure Susu'Rha would be down for a little competition."
    # # JUMP TO: Free Roam 2 / Susurha


    # FREE ROAM 2 - DARIUS 

    # # LOCATION: dining car

    # show vivi happy at left

    # vivithinking neutral: "Their heat is a trail that's easy to follow. I hope Darius doesn't mind that I followed him to the dining car."

    # show darius neutral at right

    # vivi happy "Well well. If it isn't the melancholy mindflayer."
    # darius surprised "Melancholy? Heh. Then what do I call you? The rapacious reporter? The insensitive investigative journalist?"
    # vivi happy blush "You can call me whatever you like. As long as you call me."
    # show darius surprised blush with dissolve
    # darius "I'll be sure to call you on my... shell phone."
    # vivi happy "..."
    # show darius sad blush
    # darius "I can't believe I stooped to punnery. I swear, something about this place is making me go soft."
    # vivi happy blush "If you're tired of going soft, maybe I can recommend something with more of a point?"
    # show darius surprised blush
    # darius "I'm sorry?"
    # vivi happy blush "Something where you have to do it just right to score..."
    # darius "Ms. Sanssouci, I think this is hardly the time or place-"
    # vivi neutral "Darts, Darius. I'm talking about darts."
    # show darius neutral blush
    # darius "Right. Darts."
    # vivi neutral "Unless you'd prefer something a bit more direct?"
    # show darius neutral -blush
    # darius "Darts is fine. I could use the distraction."
    # vivithinking surprised "Something feels different than the last time we talked. Am I being too forward?"
    # vivi neutral "Darius..."
    # vivi neutral blush "I'm sorry. I guess this place is getting to me. Trying to lighten the mood with some harmless flirting."
    # darius neutral "It's alright. I don't mean to imply that I didn't like it. I'm just not used to it."
    # vivi surprised "What, no mindflayer partner for you?"
    # darius sad "Not exactly, no. I've been a bit... busy for the last thousand years."
    # darius neutral "And as a side note, not all flirting is harmless. Trust me."
    # vivi sad "I...I didn't mean to bring up anything painful."
    # vivithinking sad "He's staring at me- No, through me- So intensely."
    # vivi neutral "So... What have you been busy with?"
    # darius neutral "Oh, this and that. My kind live a long time. At least...we're supposed to."
    # vivi neutral "I suppose I wouldn't know what that's like. We only get about 80 good years if we're lucky. And I suppose I wasn't lucky."
    # vivi neutral "Seems you weren't either."
    # darius angry "No. Not lucky at all."
    # vivi angry "You're awfully coy. Come out with it."
    # darius surprised "Excuse me?"
    # vivi angry "At least you had a life. Mine was cut short. I had more I wanted to do. You could at least clue me into what you're so upset about."
    # darius angry "I owe you no such explanation."
    # vivi angry "It's not about owing anything, I'm not keeping a ledger-"
    # darius angry "Neither am I. Not anymore."
    # vivithinking surprised "He's practically shaking."
    # vivi neutral "I've touched a nerve. I'm sorry. Again. I swear I'm not trying to get under your skin."
    # show darius neutral blush with dissolve
    # darius "Whether you were trying or not, you've a talent for it."
    # vivi neutral blush "Should we...play some darts?"


    # # <CHOICE>
    # show darius sad -blush
    # darius "Why not."

    # menu:
    # # OPTION 1 +ATTRACTION
    # Throw a dart while looking straight into Darius' eyes.

    # # SOUND: dart lands on board
    # darius surprised "Huh. Nice throw. Good... darting."
    # vivi happy blush "When I want something, I go straight at it."
    # darius surprised "Again. Noted."

    # # JUMP TO: vivi neutral "I want to know what's on your mind."

    # # OPTION 2 +DECAY
    #     "Actually...forget it."

    #     vivi neutral "Actually...forget it."
    #     darius surprised "I thought you wanted to play."
    #     vivi angry "Play? At a time like this? Seems a waste of time."
    #     darius surprised "I... actually agree."
    #     vivi angry "Urshu is messing with us. It seems clear to me. I think it's tied to our lives, our 
    #     former lives. You seem to have some insight."

    #     # JUMP TO: vivi neutral "I want to know what's on your mind."
        
    # vivi neutral "I want to know what's on your mind."
    # darius angry "Fine. You've pestered me enough. My purpose was clear and simple: find heretics. Break them. Consign their souls to the Lord of Eternal Rest." 
    # darius angry "That is what's on my mind. Now and always."
    # darius angry "You wanted to know. Now, you know."
    # vivi surprised "That's...I had no idea."

    # # <CHOICE>
    # vivi sad "But that's not the end of the story, is it? There's something missing."

    # # OPTION 1 +ATTRACTION
    #     "If I tell you a secret, will you tell me one of yours?"

    #     vivi neutral "If I tell you a secret, will you tell me one of yours?"
    #     darius surprised "Hm. Let's hear yours first."
    #     vivi surprised "That's...it's a yes-or-no kind of situation."
    #     darius happy "And I'm sure it worked on difficult interview subjects. Go ahead."
    #     vivi sad "Okay. I once faked a quote in an interview, and I never got caught."
    #     darius surprised "That's pretty serious. A breach of ethics."
    #     vivithinking surprised "Definitely not the worst thing I've ever done, but hey."
    #     vivi happy "Now you."

    #     # JUMP TO: "Less of a secret and more of a...regret."

    # # OPTION 2 +DECAY
    #     "Sounds like you miss it a little."

    #     vivi neutral "Sounds like you miss it a little."
    #     darius angry "I beg your pardon."
    #     vivi neutral "Is that why you're so quiet and pensive? Moody? You wish you could still be 
    #     out there, in service of your god."
    #     darius angry "Could not be further from the truth."
    #     vivi angry "Then clarify it for me. Why keep your past a secret? It's not like it matters now."

    # # JUMP TO: "Less of a secret and more of a...regret."

    # darius sad "Less of a secret and more of a...regret."
    # vivi neutral "One regret? Can't be that bad."
    # darius angry "Try several lifetimes' worth. It was all for nothing. Nothing."
    # vivi surprised "How can you be so sure?"
    # darius angry "I'm here, aren't I? With the likes of you. And them. I am nothing like any of you."

    # # darius exits

    # vivithinking surprised "Jeez. In all my years of journalism, I haven't seen anything like that. I need some rest.

    # # vivi exits


    # FREE ROAM 2 - SUSU'RHA

    # # LOCATION: dining car

    # show vivi neutral at left
    # show susurha neutral at right
        
    # vivi neutral "Susu'rha! My second favorite Gecko behind the Geico guy! Care to play some darts?
    # susurha neutral "What is \"Geico\"? And what exactly is this...\"darts?\""
    # vivi neutral "You toss pointed sticks at that round board over there. You score points based on how well you hit the target, and if you score enough points, you win."
    # susurha happy "In the Viridian Wood, we played a game similar to this. Instead of a round board, we used the carcasses of Burrowers."
    # vivithinking "And that's what happens when you don't have a TV." 
    # susurha neutral "And we used magic to increase our accuracy."
    # vivithinking neutral "Well then, nice of you to be born in a magical world."

    # # <CHOICE>
    # susurha neutral "Doubtful you could best me in a contest of accuracy." 

    # menu:
    # # OPTION 1 +ATTRACTION
    #     "The arrogance on this one. I'd sure love to shut them up."

    #     vivithinking "The arrogance on this one. I'd sure love to shut them up."
    #     vivi neutral "Magic or not, I'm gonna beat you."
    #     susurha neutral "I will give you the grace of going first."

    #     # SOUND: dart hits the board

    #     vivi happy "Bullseye!"
    #     susura angry "Bullseye?!"
    #     vivi happy "A bullseye is when you hit the dartboard dead center."

    #     # SOUND: dart hits the board

    #     susurha happy "Mine hit close, does that count for something?"
    #     vivi happy "Not as much as a bullseye!"
    #     susurha surprised "Hmm... seems my magic doesn't work here."
    #     vivi happy "Either that, or I'm better at darts than you."
    #     # JUMP TO: susurha neutral "In that case, thank you for not patronizing me by 
    #     pretending to be something you're not -- in this case, inadequate at this darts 
    #     game."



    # # OPTION 2 +DECAY
    #     "Clearly, they're insecure. I'm gonna let them win."

    #     vivithinking "Clearly, they feel insecure. I'm gonna let them win."
    #     vivi neutral "You go first."
        
    #     # SOUND: dart hits the board

    #     susurha happy "Bullseye! Oh, how simple!"
    #     susurha happy "No wonder you humans enjoy this."
        
    #     # SOUND: dart hits the board and then the floor

    #     vivi angry "Urghhh. Stupid dart."
    #     susurha happy "Am I supposed to believe that you can't hit the board from this distance?"
    #     vivi neutral blush "..."
    #     vivi neutral "Sorry. It seemed like you could use a win. After being banished from your 
    #     kingdom, and well, dying."
    #     susurha neutral "Actually, I banished myself." 
    #     # JUMP TO: susurha neutral "In that case, thank you for not patronizing me by 
    #     pretending to be something you're not -- in this case, inadequate at this darts 
    #     game."

    #     susurha neutral  "In that case, thank you for not patronizing me by pretending to be 
    #     something you're not -- in this case, inadequate at this darts game."

    #     # SOUND: dart hits the board

    #     vivi neutral "You're...welcome." 
    #     susurha neutral "..."
    #     susurha surprised "Vivienne. You seem almost relaxed."
    #     vivi happy "I am. For a moment I almost forgot how I got here."
    #     susurha neutral "How did you get here?"

    # # <CHOICE>

    # menu:
    # # OPTION 1 +ATTRACTION
    #     "It was an assignment given to me by my agent."

    #     vivi neutral "It was an assignment given to me by my agent. She told me to write an 
    #     exposé about a mysterious train line with an enigmatic conductor."
    #     vivi happy "I said yes because it reminded me of those internet horror stories I grew up 
    #     with."
    #     vivi neutral "Seems like the stories swirling around the Ouroboros Express were more 
    #     than just stories."
    #     vivi sad "Now I'm dead..."
    #     show susurha sad
    #     vivi sad "I'm going to miss living."
    #     susurha sad "Vivienne. I'm so sorry, my dear. But you cannot blame yourself for this 
    #     travesty."
    #     # JUMP TO: susurha neutral "The fault lies with your "agent.""

    # # OPTION 2 +DECAY
    #     "I didn't have a choice."

    #     vivi angry "I didn't have a choice."
    #     susurha neutral "Do tell."
    #     vivi angry "I'm a reporter. I go where the story is."
    #     vivi sad "What a silly reason to die."
    #     susurha sad "Oh, Vivienne. I'm sorry. 
    #     susurha neutral But you must remember that you did not come here on your own. 
    #     Someone told you to come.
    #     # JUMP TO: susurha neutral "The fault lies with your \"agent.\""

    # susurha neutral "The fault lies with your "agent.""
    # vivi neutral "Yeah. It does."

    # # SOUND: dart hits the board

    # susurha neutral "Why don't you envision your \"agent\" being at the target's center?"
    # vivi happy "Okay!"
    # susurha neutral "Now, hold that dart firmly in your hand."
    # susurha neutral "Concentrate on the board. And see \"Chloe\"..."
    # susurha neutral "...Now, let go."

    # # <CHOICE>
    # "Chloe..."
    # menu:
    # #OPTION 1 +DECAY
    #     "Pierce Chloe!"

    # # mica, I believe the above is an action rather than something vivi says. Same w/ option 2

    #     vivi angry "Pierce Chloe!"
    #     vivi angry "It's all her fault!"
    #     vivi angry "HER!"
    #     vivi angry "SHE had to discover this \"exclusive story.\""
    #     vivi angry "SHE had to get me to come here!"
    #     vivi angry "SHE killed me!"
    #     vivi angry "It's HER FAULT!"
    #     # VISUAL: the screen shakes
    #     susurha happy "You got a bullseye!"
    #     vivithinking neutral "God, I'm out of breath!"
    #     susurha neutral: Thank you, Vivienne. I hope you feel a bit better now.
    #     susurha neutral: Would you like to know what brought me here?
    #     vivi neutral "*GASPS* Sure. *HEAVES* Why not.
    #     # JUMP TO: susurha sad "It was fear that brought me here."

    # #OPTION +Attraction
    #     "Pierce the idea that it was her fault."

    #     vivi neutral "Pierce the idea that it was her fault."
    #     # SOUND: dart hits the board
    #     susurha happy "Bullseye!"
    #     vivi sad "It's not her fault. It's mine."
    #     vivi angry "I was the master of my fate, and I chose to come here!"
    #     vivi sad "How galactically stupid."
    #     susurha neutral: Would you like to know what's even more galactically stupid?"
    #     # JUMP TO: susurha sad "It was fear that brought me here."

    # susurha sad "It was fear that brought me here."
    # susurha neutral "It was a night like any other. The stars were out in their most intense configurations, lighting the sky as the gods had always intended. All was quiet."
    # susurha neutral "But then we heard rumbling in the distance."
    # susurha neutral "Then there was smoke. So much of it. Everyone ran as fast as they could."
    # susurha sad "That's when I saw it."
    # susurha sad "My city, where my family had lived for hundreds of generations, besieged by Tellethor's great army."
    # vivithinking surprised "Oh wow."
    # vivi sad "What did you do?"
    # susurha sad "I ran home."
    # susurha angry "I thought that if I could just GET THERE, I could save them."
    # susurha neutral "But the smoke was too much. None of us could see. I couldn't breathe."
    # susurha neutral "Then...a sharp pain and...darkness."
    # susurha sad "I woke up here."
    # susurha angry "I have no idea whether my family--that I abandoned--is okay. My fear is I'll see them walk into this dining car, like me, wondering what happened."    
    # susurha angry "If only I was there to protect them."
    # susurha sad "They died because I abandoned them."

    # # <CHOICE>

    # menu:
    # #OPTION 1 +Attraction
    #     "You did what you could. It isn't your fault."

    #     vivi sad "You did what you could. It isn't your fault."
    #     susurha sad "Thank you. That means something."
        
    #     # SOUND: dart smacks the board
    
    #     vivithinking neutral "At least there's darts."
    #     vivi sad  "I'm going to miss taking pictures."
    #     susurha sad "I'm going to miss playing my lute under the stars."
    #     vivi sad "I'm going to miss internet forums. Seeing just the craziest, most nonsensical things that people would ever think to share with others.
    #     susurha happy "Sounds delightful."
    #     susurha happy "I'll miss sharing my singing voice with those who would listen."
    #     vivi happy "I'd love to hear your singing voice."
    #     susurha happy "I would happily sing for you."
    #     susurha sad "Quiet moments. I will miss them the most."
    #     vivi sad "I can't tell you the last time that I was alone with my thoughts. I was always busy."
    #     susurha sad "Perhaps now is a good time."
    #     vivi sad "..."
    #     # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    # #OPTION +DECAY
    #     "We got a raw deal. Life is unfair."

    #     vivi angry "We got a raw deal. Life is unfair."
    #     susurha angry "Certainly nothing about our present situation is fair."
    #     vivi angry "I HATE this train!"
    #     vivi angry "And the conductor. It's his fault we're here."
    #     susurha angry "He runs this place."
    #     vivi angry "He could let us off if he wanted."
    #     susurha angry "Instead, he toys with us for his own enjoyment. Only a devil behaves this 
    #     way!"
    #     susurha sad "But there's nothing we can do."
    #     vivi angry "No. Perhaps that's the lesson."
    #     susurha "..."
    #     vivi "..."
    #     # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    # susurha neutral"Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    # #VISUAL: susurha exits

    # vivithinking "It's not a bad idea. I could use this time to reflect."
    # vivithinking "I may not get many more chances."

    # # JUMP TO: Debrief Anger

    # FREE ROAM 2 - AVA

    # # LOCATION: dining car

    # show vivi neutral at right

    # # SOUND: dart hitting the board

    # vivithinking neutral "I hear darts. Is that...Asha? Here already?

    # show ava angry at left

    # ava neutral: "Ah, bullseye. Game of darts, Vivienne? We hear your watering holes often host such competitions." 
    # vivi neutral: "Watering holes? You mean a pub?"

    # # SOUND: dart hitting the board 

    # ava neutral: "Good throw, Vivienne. But no such term exists on Soleos."
    # vivi happy blush: "Well, technically you could call it a watering hole. But we call it a pub...or a bar if they don't have Guinness."
    # vivi sad blush: "I miss my pub back home, but that's all. What was your home like?"
    # ava happy: "Though servants catered to us, people worshipped us...it was but an ornate patina, we were forbidden friendship and family. We lived in solitude."

    # # <CHOICE>
    # vivi surprised: "My God, that sounds..."

    # menu:
    #     # OPTION 1 +DECAY
    #     "Amazing.":
        
    #         vivi happy "Amazing. Peace and quiet? Now that's luxury."
    #         ava sad "No, Vivienne, perpetual loneliness. We would not wish that upon even our monarchy."
    #         # SOUND: dart hitting the board
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    #     # OPTION 2 +ATTRACTION
    #     "Awful.":
    #         vivi sad "Awful. I'm so sorry. I can't even begin to imagine."
    # show ava sad blush with dissolve
    #         ava "Thank you...that means more to us than you know."
    #         # SOUND: dart hitting the board
    # show ava happy -blush
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    #     #OPTION 3
    #     "Crazy.":
    #         vivi neutral "Crazy. Your life is like a rollercoaster!"
    #         ava neutral "A...rollercoaster?... We do not quite understand the meaning of this 
    #         word."
    #         vivi happy "It's something that moves quickly with lots of ups and downs."
    #         ava neutral "We...still struggle to grasp why you have this torture device, but 
    #         your meaning is clear."
    #         # SOUND: dart hitting the board
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    # ava happy "Another bullseye. Your turn, little one."
    # vivi angry "I thought I asked you to stop calling me that."
    # ava sad "Oh, do not take offense at our term of endearment. We are warming up to you."
    # vivithinking angry "I'm feeling warm too. Hot blood's creeping up into my face. Ughhh. I gotta let this out...And THROW!"
    # # SOUND: dart hitting the board

    # # <CHOICE>
    # vivi angry blush "Well...it's still demeaning. I don't like it."

    # menu:
    #     #OPTION 1 + DECAY
    #     "But if you like it...":

    #         vivi happy blush "But if you like it...I guess I could get used to it."
    # show ava happy blush with dissolve
    #         ava "No. We never wish to offend you."
    #         vivithinking happy "I'll do anything she wants to spend some more time with 
    #         them...!"
    # show ava happy -blush
    #         # JUMP TO: vivi neutral "Sure. Anyways..."

    #     #OPTION 2 + ATTRACTION
    #     "Don't ever call me that again.":

    #         vivi angry "Don't ever call me that again. I don't like it. I'm not your pet."
    # show ava sad blush with dissolve
    #         ava "By Asha, we beg forgiveness. We never intended harm."
    #         vivi  "..." 
    #         vivi sad blush "It's...just...old memories. Sorry, I snapped."
    #         vivithinking angry "An ex-boyfriend called me 'little one' à la Yoda. Ugh!"
    # show ava sad -blush
    #         ava "There is no need to explain. We understand...Vivienne."
    #     # JUMP TO: vivi neutral "Sure. Anyways..."

    #     #OPTION 3 
    #     "My old roommates called me dildo.":

    #         vivi blush "My old roommates called me dildo. It's a...personal massage 
    #         device. For...relaxation?"
    #         ava happy "Oh! Those. The orgies after were most pleasureable!"
    #         vivi happy blush "Oh! I didn't know Soleos did...that."
        # show ava happy blush with dissolve
    #         ava "Perhaps our other customs might tempt you?"
    #         vivithinking surprised "Write this down. WRITE THIS DOWN!"
    #         # SOUND: dart hitting the board
        # show ava happy -blush
    #         # JUMP TO: vivi neutral "Sure. Anyways..."

    #     vivi neutral "Sure. Anyways..."
        
    # # <CHOICE>
    #     vivi neutral blush "I've been meaning to ask you:"

    # menu:
    #     # OPTION 1 + DECAY
    #     "What are your thoughts on our conductor?":

    #         vivi neutral "What are your thoughts on the conductor?"
    #         ava surprised "Ah, Urshu. A mystery."
    #         vivi "Personally...I think he's undead."
    #         ava surprised "A zombie?"
    #         vivithinking surprised "Wow, she almost sounded human for a sec."
    #         ava neutral "Why do you smile so?"
    #         vivi neutral "..."
    #         vivi happy blush "No reason!"
    #         ava neutral "I suppose humans do rank in the highest percentile for creatures who 
    #         smile without cause." 
    #         # JUMP TO: vivi neutral "How...interesting."    

    #     # OPTION 2 + ATTRACTION
    #     "What do you want to do with your time left?":

    #         vivi neutral "What do you want to do with your time left?"
    #         ava sad "..."
    #         ava neutral "Enjoy the view. We seldom saw nighttime. It is strange. Nice."
    #         vivi happy "It is pretty nice, huh." 
    # show ava happy blush with dissolve
    #         ava "We would enjoy spending more time talking with you."
    #         vivithinking surprised blush "BRRRRT BRRRTT! Flirt alert!!"
    # show ava happy -blush
    #         # JUMP TO: vivi neutral "How...interesting."    
    
    #     vivi neutral "How...interesting."
    #     # SOUND: dart hitting the board and dropping to the floor
    #     vivi angry "Aw shit. Dumbass dart."
    #     ava angry "We wish you would refrain from such vulgarity."
    #     vivi angry "If you really want to get to know me better, then deal! Like I do with your 
    #     ego."
        
    # # <CHOICE>
    #     ava angry "Hmph. And to think we ever considered you special..."


    # menu:
    #     #OPTION 1 +ATTRACTION +DECAY
    #     "Don't play games with me.":

    # vivi angry "Don't play games with me."
    # ava neutral "Ah. Because you lack skill at darts?" 
    # vivi angry "Look, you may have been some kind of big deal deity on Soleos, but we're all equals here on death row, you silly moose!"
    # # JUMP TO: ava blush angry "You dare speak to us with such impudence! 
    # Refer to us as Asha or not at all!"

    # #OPTION 2 +DECAY
    #     "I don't need you to think I'm special.":

    # vivi angry "I don't need you to think I'm special. Just because your crazy cult revered you doesn't mean that I'm going to, ass hat!"
    # # JUMP TO: ava blush angry "You dare speak to us with such impudence! Refer to 
    # us as Asha or not at all!"

    #         ava angry "You dare speak to us with such impudence! Refer to us as Asha or not at 
    #         All!"
    #         vivithinking "..."
    #         vivithinking "Nice one, Vivi, you handled that with all the grace of an ornery bull."
    #         vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."
    #         ava sad "Please...go."
    #         vivithinking sad "Ugh! I messed up. Maybe they'll accept my apology 
    #         tomorrow..."

    # # JUMP TO: Debrief Anger

    # Debrief Anger

    # # LOCATION: cabin

    # # ATTRACTION ROUTE

    # show vivi neutral at left

    # vivithinking neutral "Well, that was...interesting. Didn't expect to get that deep with anyone on this train. I can't remember the last time I've been that open with anyone before."

    # vivithinking happy "It was kinda refreshing! I'm glad I'm not alone here. It's nice to be seen. Nobody wanting or expecting anything from me. Just two beings trying to understand each other."

    # vivithinking neutral "I should journal my thoughts."

    # # Journal entry with attraction meter high

    # Talking to the other passengers has helped put things into perspective. They're not so bad after all. I won't get off this train by fighting. I still need more info on the conductor. He's my ticket off this ride. He seems like one who'd appreciate an exchange for his aid. Maybe some of the other passengers can help me? We can maybe figure out together what Urshu would want from us...

    # # JUMP TO: Briefing Bargaining

    # # DECAY ROUTE

    # show vivi angry at left

    # vivithinking angry "I feel like the only one trying to get off this train. How are people content with playing silly card games when their lives are at stake? And the conductor! He knows he's messing with me and gets off on it."

    # vivithinking neutral "Take a deep breath, V. This isn't getting me anywhere."

    # vivithinking neutral "Fighting with everybody is obviously not gonna work. Maybe I can get what I want another way. Urshu is the key. He must want something."

    # vivithinking neutral "I should write."

    # # Journal entry with degradation meter high

    # This whole thing is pointless! That conductor... URG! I wanna strangle him and wipe that stupid smirk off his face. Talking to him is like solving a riddle. It's infuriating! Gotta find something on him. Maybe the others know a thing or two. There's gotta be some way to make Urshu help me. He seems like one who'd appreciate an exchange for his aid. 

    # # JUMP to Briefing Bargaining
