# The scene starts here.

label figuring_it_out:

    # Figuring it out

    # LOCATION: cabin 
    scene cabin with fade

    show vivi neutral at left with dissolve

    vivithinking angry "My head's spinning. This is not normal. Something's not okay."
    vivithinking sad "Am I...okay?"
    vivithinking neutral "I'm missing something. I must be."
    vivithinking neutral "Fine, let's look at the facts, shall we? I wish I had a working voice recorder. Or a blank wall and lots of red string."

    # <CHOICE>
    # NOTE: Set up a conditional: player should exhaust Options 1-3 before 4 appears

    $ facts1 = False
    $ facts2 = False
    $ facts3 = False

    label facts_choice:

        vivithinking "For now, what do I know?"

        menu:
            # OPTION 1 
            "I'm on a train. Sort of?" if facts1 == False:

                $ facts1 = True

                vivithinking neutral "I'm on a train. Sort of?"
                vivithinking neutral "Except this train isn't flying through the Florentine countryside. And it's shrouded in mist."
                vivithinking neutral "Chloe did put me on this assignment, right? Ugh, my memory's Swiss cheese."
                vivithinking neutral "Oh, and who prepared that meal? Besides the other travelers, there's only that badonk-blessedbedonk-blessed conductor. No other staff around. That's weird, right?"

                # JUMP TO vivi neutral "What else do I know?"
                # list remaining choice options
                jump facts_choice

            # OPTION 2
            "I'm traveling with {i}very{/i} strange people." if facts2 == False:

                $ facts2 = True

                vivithinking neutral "I'm traveling with {i}very{/i} strange people."
                vivithinking neutral "And no one remembers how we got onto the train. But we know {i}why{/i} we came aboard. For me, I was chasing down another story."
                vivithinking neutral "Little did I know I'd be on a train with a goddess, a detective-octopus-thing, and a lounge lizard prince."
                vivithinking surprised "Wait, what am I saying? When I get off this train, I'll have enough material to start a media empire!"
                vivithinking neutral  "Huh. Where {i}am{/i} I getting off this train?"
                vivithinking neutral "The conductor would know. Urshu seems like part of the puzzle."

                # JUMP TO vivithinking "What else do I know?"
                # list remaining choice options
                jump facts_choice

            # OPTION 3
            "The conductor is the only one who knows what's going on." if facts3 == False:

                $ facts3 = True

                vivithinking neutral "The conductor is the only one who knows what's going on."
                vivithinking neutral "Urshunabi is so cryptic. So infuriating. And... adorable?"
                vivithinking neutral blush "No, he's poised. In control. Unimpressed."
                vivithinking neutral "In short, this ain't his first rodeo. He {i}knows{/i} things."
                vivithinking neutral "So he drinks espresso and knows things. Sounds kinda like paradise."
                vivithinking neutral "Huh. Paradise. Why does that make my mind prickle?"

                # JUMP to vivithinking neutral "What else do I know?"
                # list remaining choice options
                jump facts_choice

            # OPTION 4
            "Time to simplify. Reduce. Distill."  if facts1 == True and facts2 == True and facts3 == True:

                vivithinking neutral "Time to simplify. Reduce. Distill."
                vivithinking neutral "A train heading nowhere. Nothing to see out the windows."
                vivithinking neutral "A group of weirdos with holes in their memory."
                vivithinking neutral "A mysterious conductor who knows more than he lets on."
                vivithinking neutral "And then there's me: an investigative reporter desperately trying to keep it together. With the facts."
                vivithinking neutral "So, the facts: This is not normal. This is not a normal, human existence."
                vivithinking neutral "And if I'm not hallucinating or having an absinthe-soaked bender in the Paris catacombs...again..."
                vivithinking neutral "Then this is another plane of existence."
                
                # EFFECT: pixellate
                show cabin with pixellate

                vivithinking surprised "Am I...not {i}alive{/i}?"

                # JUMP to vivi "Dead? Really?"
        
    # only visible after options 1-3 are exhausted; conditional!

    vivithinking surprised "Dead? Really?"
    vivithinking blush happy "Nope! Nah. I must be hallucinating."
    vivithinking neutral "But if I'm not, then...being dead {i}is{/i} the most logical thing."
    vivithinking neutral "But it feels too...normal. How?"
    vivithinking neutral "I need to talk to someone. Someone who {i}knows{/i} what's going on."
    vivithinking angry "And I bet that smug-as-shit conductor was just waiting for me to put it all together."
    vivithinking angry "I'm going to make him tell me the truth."

    # Room selector, lounge as only option.
    # button text: Find Urshu.
    # EFFECT: fade out
    # JUMP TO: Confrontation
    jump confrontation

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
