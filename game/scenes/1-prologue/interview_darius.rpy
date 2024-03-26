# The scene starts here.

label interview_darius:

    # Interviews/Darius Wrecker

    # LOCATION: diningcar
    # scene diningcar with fade

    # show vivi neutral at left with dissolve

    show darius neutral at right with dissolve

    # SOUND: train

    vivithinking neutral "This one's imposing. Tall and solid, despite that slender frame." 
    vivithinking sad "But what's this unease I sense?"
    vivi neutral "Hello? Hi, I'm Vivi, nice to meet you. I'm doing an article on the train and I'm interested in your thoughts about it so far."
    darius neutral "Hmm? Sorry, I'm busy."
    vivi neutral "Busy... sitting here?"
    darius neutral "Yes."
    vivi angry "Listen, if you don't want to be interviewed, that's fine. But could we not lie about—"
    darius neutral "A question. Do you {i}always{/i} badger other people minding their own business, or is that just for me?"
    vivi neutral "I—I just asked you a simple question!"
    darius neutral "And I responded in kind. Nothing else was needed between us."
    darius neutral "But you reporters are never satisfied, are you?"
    darius neutral "{i}Sigh{/i}. If you make it quick, I'll humor you."
    vivithinking angry "Oh, I'm about to eviscerate this jerk. Every character flaw. In print. Forever."
    vivi neutral "Thank you for your patience, um... Well, we never established your name, did     we?"
    darius neutral "Just call me Darius."
    vivi neutral "No last name?"
    darius neutral "Does it really matter?"
    vivi neutral "I'd like to have a proper way of referring to you."
    darius neutral "Gods, it never ends. It's Wrecker."
    vivi neutral "Really? That's the best you could come up with?"
    darius neutral "The best my lineage could, apparently. Now, could you please get to the questions?"
    vivithinking neutral "You're that into your cosplay, huh? Fine, I'll play ball."
    vivithinking neutral "That being said, it is a really nice costume. So lifelike..."
    # <CHOICE>
    vivi neutral "Right, let's see."

    menu:
        # OPTION 1
        "What's your costume?":

            vivi neutral "What's your costume?"
            darius neutral "My... costume?"
            vivi neutral "Yeah, you know. The overcoat, tentacles, mask. What're you going for?"
            show darius neutral blush with dissolve
            darius "I don't... A detective? Yes, a detective."
            vivi neutral "Not quite what I meant, but sure, an octopus detective."
            show darius neutral -blush
            darius neutral "You... don't know what I am, do you?"
            vivi neutral "Sorry, I'm a bit out of the loop with current trends so I don't get the reference."
            vivithinking neutral blush "But I can already imagine the fan fiction..."
            vivithinking angry "Get it together, Vivi!"

            # JUMP TO vivi neutral "Okay, next question."

        # OPTION 2
        "Tell me about yourself.":

            vivi neutral "Tell me about yourself."
            darius neutral "I'd... rather not."
            vivi neutral "Come on, can't you give me something? Even the tiniest shred?"
            darius neutral "A detective. I'm a detective."
            vivithinking neutral "Well, then. This suddenly got a lot more interesting."
            vivi neutral "A detective, huh? Here on a case?"
            darius neutral "No. And if I were, you don't really think I'd say so, do you?"
            vivi angry "Just looking to make conversation."
            darius neutral "And we agreed there is no need."
            vivithinking angry "You want to rush this? Fine. I'm sure the other guests will be more talkative."
        
            # JUMP TO vivi neutral "Okay, next question."

    vivi neutral "Okay, next question."

    # <CHOICE>
    darius neutral "Make it a simple one, will you?"

    menu:
        # OPTION 1
        "Where are you from?":

            vivi neutral "Where are you from?"
            darius neutral "Nowhere you're familiar with."
            vivi angry "Do you intend to be so difficult throughout this entire process?"
            darius neutral "I am simply being honest. I come from a rather small garden."
            vivi neutral "Octopus puns? Really?"
            darius neutral "It wasn't intended, but take it how you will."

            # JUMP TO vivi neutral "Forget it. Last question."

        # OPTION 2
        "How'd you find out about the train?":

            vivi neutral "How'd you find out about the train?"
            darius neutral "I don't remember."
            vivi neutral "This is going nowhere."
            darius neutral "How would you have me answer, hmm? Tell me and I'll do just that. We both walk out of here happier."

            # JUMP TO vivi neutral "Forget it. Last question."

    vivi neutral "Forget it. Last question."
    vivi neutral "Why did you decide to take this little excursion?"
    darius neutral "Well I... I..."
    darius sad "Why..."
    vivithinking neutral "His whole demeanor changed. No witty remark this time?"
    darius sad "Sorry, I'm...not feeling very well. Why am I here, you asked?"
    vivi neutral "Essentially, yes."
    darius neutral "Duty... yes."
    vivithinking neutral "Duty? You're a detective. What, did you need inspiration for your wardrobe?"
    vivi neutral "Very interesting, I—"
    vivithinking sad "It's like a chill just came in. Why is the room so...heavy? Such a sickly atmosphere, like wet clothes sticking to your skin."
    vivi neutral "Thank you, uh...Darius. I'll leave you be."
    vivithinking sad "It's like he doesn't even see me."

    hide darius with dissolve

    # JUMP TO: Figuring it out
    jump interview_choice

    # Interviews/Susu'Rha Balrinn

    #     # LOCATION: lounge

    #     show susurha neutral at right

    #     show vivi neutral at left

    #     vivithinking surprised "Wait a minute..."
    #     vivithinking surprised "A humanoid...lizard? Seriously, whoa."
    #     vivithinking neutral "And so relaxed." 
    #     vivithinking neutral "A literal lounge lizard."
    #     vivithinking surprised "What is happening on this train?"
    #     susurha neutral "May I help you?"
    #     vivithinking neutral "It speaks. Holy shit."
    #     vivi neutral "Hello."
    #     susurha neutral "Hello yourself."
    #     vivi neutral "You seem quite relaxed."
    #     susurha neutral "I'm proud to say I've developed relaxation into an art form."
    #     vivi neutral "Damn! The only art form I've ever developed is pimple-popping." 
    #     susurha neutral "...Pimple...popping?"
    #     vivi neutral "...Nevermind!" 
    #     vivi neutral "What should I call you?"
    #     susurha neutral "I am Susu'Rha of Balrinn. Balrinn is my surname."
    #     vivi neutral "I'm Vivienne Sanssouci, but everyone calls me Vivi."
    #     susurha neutral "Vivi...Vivi..."
    #     susurha happy "Like Bon Vivant!"
    #     vivithinking neutral "Bon vivant - one fond of good living eh? I like that."
    #     vivithinking sad "Even if it hasn't always been true..."
    #     susurha neutral "So...What inspired you to approach me, Vivi?"
    

    #     # <CHOICE>
    #     vivi neutral "I'm a journalist. I'm writing a piece on the Ouroboros Express."

    #     menu:
    #     # OPTION 1
    #     "Can you tell me a little about yourself?":

    #     vivi neutral "Can you tell me a little about yourself?"
    #     susurha happy "My favorite topic!"
    #     susurha neutral "I'm heir to the throne of Balrinn. Or was."
    #     vivi surprised "Was?" 
    #     susurha neutral "I abdicated my position because I found that life stultifying."
    #     susurha happy "And instead embarked upon a life of mirth, art, expression, and pleasure."
    #     susurha sad "This had...consequences."
    #     vivi neutral "Like what?"
    #     susurha neutral "..." 
    #     susurha neutral "I don't know if I'm quite comfortable talking about that."

    #     # JUMP TO: "Bury the lede, why don't you?"

    #     # OPTION 2
    #     "Where are you from?!":

    #     susurha neutral "Balrinn. The capital city of my home country." 
    #     susurha neutral "Which is also my family name."
    #     vivithinking neutral "So...royalty. You're royalty."
    #     vivi neutral "You seem very nonchalant about that."
    #     susurha neutral "It's not something that I really discuss."
        
    #     # JUMP TO: "Bury the lede, why don't you?"

    #     vivithinking neutral "Bury the lede, why don't you?"
    #     vivithinking angry "And why are they looking at me like I'M the freak?! THEY'RE the talking wellness-guru gecko!"
    #     vivithinking angry "The attitude on this one."

    #     susurha neutral "Your face right now...You're judging me."
    #     vivi neutral "No, I..."
    #     susurha neutral "I'd say stay awhile and relax with me, but I don't think you'd know how."

    #     # <CHOICE>
    #     vivithinking angry "Oooh! This one is getting on my nerves."

    #     menu:
    #     # OPTION 1
    #     "I know how to relax!":

    #     vivi angry "I know how to relax!"
    #     susurha neutral "Oh, really? Take a seat then."
    #     vivi neutral "I will."
    #     vivithinking neutral "The seat cushions are warm."
    #     vivithinking neutral "Oh man. I could fall asleep."
    #     susurha happy "There you go."
    #     vivi happy "This is actually kind of nice."
    #     susurha happy "You see? That's why I practice it so often."     

    #     # JUMP TO: "So enough about me. Who are you, Vivienne?"

    #     # OPTION 2
    #     "I can relax! This just isn't the time.":

    #     vivi neutral "I can relax! This just isn't the time."
    #     susurha happy "There is always time to lay back and relax."
    #     susurha neutral "If you let the stress of everything get to you, you'll age like milk in the blistering sun."
    #     vivi angry "Look, my skin's already shit from corporate America. I don't care what it looks like anymore.
    #     vivithinking neutral "Well, except when I'm popping a zit..."     
    #     vivi angry "I just came here to get this assignment done, not get a self-care lecture from a talking lizard."
    #     susurha angry "Ss-uit yourself."
    #     susurha neutral "Alright, then. I've spoken enough about myself for one conversation."
    #     vivi neutral "I mean, not really. You kinda avoided my--"

    #     # JUMP TO: "So enough about me. Who are you, Vivienne?"

    #     susurha neutral "So enough about me. Who are you, Vivienne?"
    #     susurha neutral "Let's see if I can get there. You're a writer. Which means you're an artist, of sorts."
    #     susurha neutral "But also a pragmatist. With an allergy to art for art's sake."
    #     susurha neutral "I could see how journalism suits you."
    #     vivithinking angry "Get out of my head, lizard...gecko...whatever you are!" 
    #     susurha neutral "But have you ever indulged in poetry? Or songwriting?"
    #     vivi neutral "I...not seriously."
    #     susurha sad "You're missing out."
    #     susurha neutral "What else should I know about you, Vivi?"
    #     vivi neutral "I'm here to talk about you. Not the other way around."
    #     susurha happy "Hm. Whatever you say."
        

    #     # <CHOICE>
    #     vivithinking neutral "This is taking too long. I just have to ask the right question..."

    #     menu:
    #     # OPTION 1
    #     "Where are you heading?":

    #     vivi neutral "Where are you heading?"
    #     susurha neutral "On this train? Home..."
    #     susurha sad "I hope."
    #     vivi neutral "You hope?"
    #     susurha sad "That's where I was heading before I found myself in this bizarre, yet well-appointed cabin."
    #     vivi neutral "Found yourself?"
    #     vivi neutral "You don't remember boarding?"
    #     susurha neutral "I sure don't."
    #     vivithinking neutral "Funny...Neither do I."

    #     # JUMP TO: "Where are you headed?"
    
    #     # OPTION 2
    #     "Why are you on this train?":

    #     vivi neutral "Why are you on this train?"
    #     susurha neutral "..."
    #     susurha neutral  "I don't...know."
    #     susurha neutral "I don't remember boarding."
    #     vivi surprised "Really?"
    #     susurha neutral "I was in the woods, running toward my ancestral home..."
    #     susurha sad "And then I found myself here."
    #     vivithinking neutral "Something is clearly bothering them."
    #     vivithinking sad "I can't say that I blame them."
    #     vivithinking surprised "If I woke up here without knowing I got here..."
    #     vivithinking "..."
    #     vivithinking neutral "Something must be going on."

    #     # JUMP TO: "Where are you headed?"

    #     susurha neutral "Where are you headed?"
    #     susurha neutral "Or are you just going to leave as soon as you get your story?"
    #     vivi neutral "I haven't decided yet."
    #     susurha neutral "Ah, well, please try to enjoy the trip while it lasts."
    #     vivithinking surprised "Wait, that's it?"
    #     vivithinking neutral "All that talk and nothing was actually said!"
    #     susurha neutral "Perhaps we'll chat again. I'd love to know more about the person behind that disarming smile."
    #     vivithinking neutral blush "Now, they're charming me?!"
    #     vivithinking neutral blush "And did I even smile? How is it disarming? 
    #     vivithinking neutral blush "Crap, is it getting warm in here?"
    #     vivithinking neutral blush "No! Don't fall for it, Vivi. Keep it together."
    #     susurha happy "Talk soon, Vivienne."
    #     vivi happy "See you later."

    #     # JUMP TO: Figuring it out
    # Figuring it out

    # # LOCATION: cabin 

    # show vivi neutral at left

    # vivithinking angry "My head's spinning. This is not normal. Something's not okay."
    # vivithinking sad "Am I...okay?"
    # vivithinking neutral "I'm missing something. I must be."
    # vivithinking neutral "Fine, let's look at the facts, shall we? I wish I had a working voice recorder. Or a blank wall and lots of red string."

    # # <CHOICE>
    # # NOTE: Set up a conditional: player should exhaust Options 1-3 before 4 appears
    # "For now, what do I know?"

    # menu:
    #     # OPTION 1 
    #     vivithinking neutral "I'm on a train. Sort of?":

    #     vivithinking neutral "I'm on a train. Sort of?"
    #     vivithinking neutral "Except this train isn't flying through the Florentine countryside. And it's shrouded in mist."
    #     vivithinking neutral "Chloe did put me on this assignment, right? Ugh, my memory's Swiss cheese."
    #     vivithinking neutral "Oh, and who prepared that meal? Besides the other travelers, there's only that badonk-blessedbedonk-blessed conductor. No other staff around. That's weird, right?"

    #     # JUMP TO vivi neutral "What else do I know?"
    #     # list remaining choice options

    #     # OPTION 2
    #     vivithinking neutral "I'm traveling with {i}very{/i} strange people.":

    #     vivithinking neutral "I'm traveling with {i}very{/i} strange people."
    #     vivithinking neutral "And no one remembers how we got onto the train. But we know {i}why{/i} we came aboard. For me, I was chasing down another story."
    #     vivithinking neutral "Little did I know I'd be on a train with a goddess, a detective-octopus-thing, and a lounge lizard prince."
    #     vivithinking surprised "Wait, what am I saying? When I get off this train, I'll have enough material to start a media empire!"
    #     vivithinking neutral  "Huh. Where {i}am{/i} I getting off this train?"
    #     vivithinking neutral "The conductor would know. Urshu seems like part of the puzzle."

    #     # JUMP TO vivithinking "What else do I know?"
    #     # list remaining choice options

    #     # OPTION 3
    #     vivithinking neutral "The conductor is the only one who knows what's going on.":

    #     vivithinking neutral "The conductor is the only one who knows what's going on."
    #     vivithinking neutral "Urshunabi is so cryptic. So infuriating. And... adorable?"
    #     vivithinking neutral blush "No, he's poised. In control. Unimpressed."
    #     vivithinking neutral "In short, this ain't his first rodeo. He {i}knows{/i} things."
    #     vivithinking neutral "So he drinks espresso and knows things. Sounds kinda like paradise."
    #     vivithinking neutral "Huh. Paradise. Why does that make my mind prickle?"

    #     # JUMP to vivithinking neutral "What else do I know?"
    #     # list remaining choice options

    #     # OPTION 4
    #     vivithinking neutral "Time to simplify. Reduce. Distill.":

    #     vivithinking neutral "Time to simplify. Reduce. Distill."
    #     vivithinking neutral "A train heading nowhere. Nothing to see out the windows."
    #     vivithinking neutral "A group of weirdos with holes in their memory."
    #     vivithinking neutral "A mysterious conductor who knows more than he lets on."
    #     vivithinking neutral "And then there's me: an investigative reporter desperately trying to keep it together. With the facts."
    #     vivithinking neutral "So, the facts: This is not normal. This is not a normal, human existence."
    #     vivithinking neutral "And if I'm not hallucinating or having an absinthe-soaked bender in the Paris catacombs...again..."
    #     vivithinking neutral "Then this is another plane of existence."
        
    #     # EFFECT: pixellate

    #     vivithinking surprised "Am I...not {i}alive{/i}?"

    #     # JUMP to vivi "Dead? Really?"
        
    # # only visible after options 1-3 are exhausted; conditional!

    # vivithinking surprised "Dead? Really?"
    # vivithinking blush happy "Nope! Nah. I must be hallucinating."
    # vivithinking neutral "But if I'm not, then...being dead {i}is{/i} the most logical thing."
    # vivithinking neutral "But it feels too...normal. How?"
    # vivithinking neutral "I need to talk to someone. Someone who {i}knows{/i} what's going on."
    # vivithinking angry "And I bet that smug-as-shit conductor was just waiting for me to put it all together."
    # vivithinking angry "I'm going to make him tell me the truth."

    # # Room selector, lounge as only option.
    # # button text: Find Urshu.
    # # EFFECT: fade out
    # # JUMP TO: Confrontation
    # Confrontation
    # # LOCATION: lounge

    # show urshu happy at right
    # show vivi angry at left

    # urshu happy "Doo doo doo, dee dee dee, dum dum dum!"
    # vivithinking angry "There he is. Humming a jaunty tune. Polishing the leather. The audacity!"
    # vivithinking angry "Just look at his smug face, his perfectly tailored navy suit with that crimson pinstripe, his huge caboose in fine detail—"
    # urshu neutral "Miss Sanssouci?"
    # vivithinking blush surprised "Shit! How long have I been staring?"
    # urshu neutral "I am flattered by your gaze, my dear, but do take care. In some lands, the victim of such a gaze is entitled to divorce your head from your shoulders."
    # vivi angry "I'd love nothing more than that for {i}you{/i} right now."
    # urshu neutral "Oh? Is there no bread? Shall you eat cake?"
    # vivithinking angry "Oh, the {i}gall{/i}."
    # vivi angry "I {i}know{/i}, Urshu."
    # urshu neutral "You know? Know what? Recipes for cake? My waist size? It does take some doing, you know, finding a tailor who can accommodate my, hmm, dimensions."
    # vivi angry "I know."
    # urshu neutral "..."
    # urshu neutral "Ah, so you have followed your investigative proclivities. Tell me, what is it you {i}know{/i}?"
    # vivi angry "For starters, this train exists on some sort of cosmic plane heading nowhere good, and—"
    # vivi surprised "Why are you getting excited?"
    # urshu happy "No reason, Miss Sanssouci! Do go on."
    # vivi angry "Well, uh, okay. Oh, and I'm one of four passengers, all of us from different worlds."
    # vivi angry "And you, or someone, or {i}something{/i} has taken our memories of boarding the train!"
    # urshu happy "How delightful you've learned so much about your peers!"
    # vivi angry "Don't interrupt me. I'm furious with you!"
    # show urshu happy blush with dissolve
    # urshu "My apologies."
    # vivi neutral "Which means one of three things: One, I'm having a delusion my therapist is just {i}loving{/i} because she knows her findings are going to get her a Nobel Prize."
    # show urshu neutral -blush
    # urshu neutral "Interesting."
    # vivi neutral "Two: I'm projecting my spirit into this astral plane while lying butt naked in a yurt in Cuzco."
    # show urshu happy blush with dissolve
    # urshu "What a sight that would be!"
    # vivi angry "This isn't a game, Urshunabi!"
    # show urshu neutral -blush
    # urshu neutral "No, indeed. Not yet, anyhow."
    # vivi angry "What?"
    # urshu happy "What is your final theory, Miss Sanssouci?"
    # vivi angry "..."
    # urshu neutral "Cosmic cat got your tongue?"
    # vivi sad "If I tell you, I'll know it's true."
    # urshu neutral "Truth swallowed sickens the soul, my dear. Please, share what you have discovered."
    # vivi sad "I..."
    # vivi sad "We're..."
    # urshu angry "Say it!"
    # vivi sad "Dead! We're all dead! Except for you."
    # urshu happy "Well done, Miss Sanssouci. Well done."

    # # SOUND: teleport
    # # VISUAL: screen shakes

    # # VISUAL: fade out
    # # TRANSITION TO DINING CAR
    # # JUMP TO: REVEAL
    # Reveal
    # # LOCATION: diningcar

    # show vivi surprised at left
    # vivi "{i}*cough* *cough*{/i}"

    # show darius surprised at right
    # darius surprised "Huh."

    # show ava neutral at right
    # ava neutral "Another trick?"

    # show susurha angry at right
    # susurha angry "Teleportation? That's rude."

    # vivithinking surprised "We're in the dining car? How?"

    # # SOUND: heartbeat

    # vivithinking surprised "I can't focus."
    # vivithinking surprised "There's stuff at the edges of my view. Like, shards?"
    # vivithinking sad "Can't think straight..."

    # show urshu happy at right
    # urshu happy "How delightful. Attention over here, please! Lovely! Now, it's finally time—for the welcoming party!"
    # urshu happy "I know, I know. Apologies for the ruse, my dear passengers."
    # vivi sad "What ruse?"
    # urshu neutral "Perhaps the swiftest explanation is a reintroduction. My good people, I am known by many names, but you may call me Urshunabi, ferryman of the dead."
    # urshu happy "Or conductor of the dead, I should say."

    # show susurha happy at left
    # susurha happy "Ha! A joke! How droll!"

    # show darius neutral at left
    # darius neutral "Hmph."

    # show ava angry at left
    # ava angry "What trickery is this? We've had enough of this game. Release us this instant."
    # urshu neutral "This is neither game nor jest, Illuminated One. Your flicker is extinguished—what a shame—and now you spiral into the elder dark." 
    # urshu happy "For you are all dead! Haha!"

    # # SOUND: heartbeat

    # show vivi surprised at left
    # vivithinking surprised "No, no, no... This isn't real."

    # show susurha happy at left
    # susurha "Haha! A funny conductor! Say it again!"

    # show ava angry at left
    # ava angry "Retract. Mocking death is a grave sin and a banner of poor judgment."

    # urshu happy "Do not be afeared, dear ones, for you have some time yet. I have made every care to ensure this final journey is a productive one."
        
    # show susurha neutral at left
    # susurha "Oh, come on, Lady Bright. Don't tell me you believe him."

    # show ava angry at right
    # ava angry "We, in fact, believe we have been captured."
    # susurha surprised "Oh, well, then that's funny, see? It'll take more than a fool in uniform to keep me captive."

    # show darius neutral at left
    # darius "Hmph."
    # ava "What is the matter, master of thralls? Care to elaborate?"
    # darius "I-I'm a mere observer."

    # show urshu happy at right
    # urshu happy "And observe, you shall—the greatest theater of all, after curtain call, in the liminal wings on your way to center stage to take your final bow."
    # urshu neutral "But even in this cosmic plane, the light wanes and there is time but for one encore. Will you play as you were, broken characters of your respective tragedies? Or flip the script?"

    # show ava angry at left
    # ava angry "Tragedies. You dare?"

    # urshu happy "Well, the reviews don't write themselves. A reporter would surely have sat to the end of a play or two. Well, dear Miss Sanssouci, have you any thoughts?"

    # show vivi sad at left
        
    # # SOUND: heartbeat

    # vivithinking sad "This is too much. Everyone's looking at me."
    # vivithinking sad "What am I supposed to do? I can't help them. I can't even stand straight."

    # show ava angry at left
    # ava "Ignore the pawn. {i}We{/i} will ask the ques--"

    # # EFFECT: Brighten or distort the display
    # # SOUND: heartbeat

    # show vivi sad at left
    # vivithinking sad "I see them shouting, but... I can't hear them."
    # Vivithinking sad "Why's everything...so bright?"

    # show urshu surprised at right
    # urshu surprised "Miss Sanssouci?"


    # # EFFECT: Fade out

    # vivithinking sad "Bright...like a mirror..."

    # # SOUND: crash

    # # JUMP TO: Briefing Denial
