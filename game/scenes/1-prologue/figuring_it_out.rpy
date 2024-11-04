# The scene starts here.

label figuring_it_out:

    # Figuring it out

    # LOCATION: cabin 
    scene cabin with fade
    stop music fadeout 2.0
    play ambience amb_bedroom fadein 2.0


    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking angry "My head's spinning. This is not normal. Something's not okay."
    vivithinking sad "Am I...okay?"
    play music mysterymusicpiano loop
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
                vivithinking neutral "Oh, and who prepared that meal? Besides the other travellers, there's only that tight-assed conductor. No other staff around. That's weird, right?"

                # JUMP TO vivi neutral "What else do I know?"
                # list remaining choice options
                jump facts_choice

            # OPTION 2
            "I'm traveling with {i}very{/i} strange people." if facts2 == False:

                $ facts2 = True

                vivithinking neutral "I'm traveling with {i}very{/i} strange people."
                vivithinking neutral "And no one remembers how we got onto the train. But we know {i}why{/i} we came aboard. For me, I was chasing down another story."
                vivithinking neutral "Little did I know I'd be on a train with a goddess, a detective-squid-thing, and a lounge lizard prince."
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
                stop music fadeout 1.0
                $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(400), replace=True, duration=1.0)
                play sound heartbeat
                pause 3.0
                $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5.0)
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
    vivithinking angry "And I bet that smug little so-and-so conductor was just waiting for me to put it all together."
    vivithinking angry "I'm going to make him tell me the truth."

    # Room selector, lounge as only option.
    # button text: Find Urshu.
    # EFFECT: fade out
    # JUMP TO: Confrontation
    stop ambience fadeout 1.0
    jump confrontation