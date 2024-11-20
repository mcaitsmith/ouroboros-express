# The scene starts here.

label interview_ava:

    # Interviews / Avatar of Asha

    # LOCATION: diningcar
    play ambience amb_bar if_changed fadein 3.0
    # scene diningcar with fade

    show ava neutral at right with dissolve:
        xzoom 1.0
    show vivi at left with dissolve:
        xzoom -1
    # SOUND: train

    vivithinking neutral "What's your story, gorgeous?"
    ava neutral "Ah. A fellow traveler. Do you wish to bask in our radiance?"
    vivithinking neutral "Radiance? You sure think highly of yourself, sunshine."
    ava neutral "What may we call you?"
    vivi neutral "My full name's Vivienne Sanssouci, Vivi for short."
    ava neutral "As you wish, Vivi."
    ava happy "We are the Avatar of Asha, the  Eternal Light."
    play sound sparkle #oneshot sparkle
    pause  0.5
    vivithinking neutral "What's with this royal plural stuff?"
    ava neutral "You may call us Asha. What draws you to us if not our light?"

    # <CHOICE>
    vivi neutral "Well for starters, maybe you could ..."

    menu: 
        # OPTION 1
        "Drop the act and help a fellow human out?":

            vivi neutral "Drop the act and help a fellow human out?"
            ava angry "Act? We are a diplomat, not a clown. And we are not pathetic, pretending humans either...like some."
            vivithinking surprised "Are they referring to me?!"
            # <CHOICE>
            ava neutral "Still, we are unsurprised you came to us. How may we help you, little one?"

            menu:
                # OPTION 1A
                "(Little one?! What a snob!)":

                    vivithinking angry "Little one?! What a snob!"

                    # JUMP TO vivithinking neutral "Deep breaths, Vivi. It's just a job."

                # OPTION 1B
                "(Ugh, “little one”? That reminds me of... never mind. Focus.)":

                    vivithinking neutral "Ugh, “little one”? That reminds me of... never mind. Focus."

                    # JUMP TO vivithinking neutral "Deep breaths, Vivi. It's just a job."

            
            vivithinking neutral "Deep breaths, Vivi. It's just a job."

            # JUMP TO: "Mind telling me a little about yourself?"

        # OPTION 2
        "...answer a few questions?":

            vivi neutral "...answer a few questions?" 
            vivi neutral blush "For my boss, Chloe, who sent me here?"
            vivithinking neutral "And for my crumbling sanity?"
            vivi happy blush "Just basic boilerplate stuff."
            ava neutral "Boilerplate?"
            vivi neutral "Ugh...it means...Wait what does it mean?"
            vivi neutral "Nevermind."     
            ava happy "Very well. We shall do our best."

            # JUMP TO: "Mind telling me a little about yourself?"

    vivi neutral "Mind telling me a little about yourself?"
    ava neutral "In our home, we are the Avatar of the Eternal Light. We serve as a diplomat and peacemaker. We are dedicated to service."
    vivithinking neutral "Sounds dull as death."
    ava neutral "We speak for many with one voice. The All is the One."
    vivithinking neutral "Wow. Another egomaniac. Great."
    vivi neutral "That's great. Must be pretty time-consuming. I can relate."
    vivi neutral "I spend a lot of hours traveling for my job, and writing about my experiences."
    ava happy "A writer? Interesting. We learned writing, the arts, and many different tongues."
    vivithinking neutral "Oh la di da. I get it, you're cultured."

    # <CHOICE>
    vivi neutral "So, umm...?"

    menu:
        # OPTION 1
        "Where are you from?":

            vivi neutral "Where are you from?"

            # JUMP TO: "Soleos. You do not know of its existence."

        # OPTION 2
        "Where's home?":

            vivi "Where's home?"

            # JUMP TO: "Soleos. You do not know of its existence."

    ava neutral "Soleos. You do not know of its existence."
    vivi neutral "Because it's far away from Earth?"
    ava neutral "It is on another plane entirely."
    vivi surprised "Like...You're from the future? Or the past?"
    show ava neutral blush
    
    # <CHOICE>
    ava "We are not bound by your facile definitions of time."
    
    menu:
        # OPTION 1
        "(An egomaniac AND rude. Even better.)":

            vivithinking angry "An egomaniac AND rude. Even better."
    
        # JUMP TO show ava neutral -blush

        # OPTION 2
        "(I'm starting to wonder if any of us are, here, honey.)":

            vivithinking neutral "I'm starting to wonder if any of us are, here, honey."

            # JUMP TO show ava neutral -blush
    
    show ava neutral -blush

    # <CHOICE>
    vivi "So, one last question, if you don't mind?"

    menu:
        # OPTION 1
        "Why are you here?":

            vivi neutral "Why are you here?"
            ava angry "We go where we are called in service of Mother Asha."
            ava angry "And we advise you not to ask such impudent questions in our presence going forward, human."
            ava angry "This questioning ceases now." 

            # ava leaves
            hide ava with dissolve

            vivithinking angry "Wow. Good thing she's tall - that's one high horse she's clambered up on."
            vivithinking angry "At least she's not wrong. She really is on another planet. In every sense of the word."

            # JUMP TO: "Well, what now?"

        # OPTION 2
        "Do you remember boarding this train?":

            vivi neutral "Do you remember boarding this train?"
            show ava neutral blush
            ava "..."
            show ava sad -blush
            ava sad "Mother Asha! We try to seize our memory, but like a desert wind it repels us."
            vivi surprised "How'd you get there then?"
            ava neutral "Ah, Vivienne. We often travel; it becomes a blur. Odd, though. We do not recall boarding this time."
            vivithinking neutral "Kinda culty vibe going on, but she's interesting. I'm...intrigued."
            vivi neutral "Okay, well...Thanks, Asha. Maybe we can talk again?"
            ava neutral "Goodbye, Vivienne. The All is the One."

            # ava leaves
            hide ava with dissolve

            vivi happy "Oh, sure—all for one and one for all to you, too!"

            # JUMP TO: "Well, what now?"

    vivithinking neutral "Well, what now?"


    # JUMP TO: Figuring it out
    jump interview_choice