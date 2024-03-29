# The scene starts here.

label anger_briefing:

    #Briefing Anger
    # LOCATION: cabin
    scene cabin with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    show urshu neutral at right with dissolve

    urshu "Good cosmic morning, Miss Sanssouci!"
    vivithinking surprised "He's so light on his feet. Are all short kings also ninja-quiet? Are all short kings also ninjas?"
    vivi surprised "Urshu! You shouldn't sneak up on someone this early."
    vivi "Especially when they haven't had their coffee yet..."
    urshu happy "The perfect way to start every morning, whether careening toward oblivion on the Ouroboros Express or not, is with Narubian citrus-infused espresso. There's some prepared in the lounge." 
    vivithinking angry "Can he read minds?"
    vivi neutral "The lounge. Where there's people, I'm guessing."
    vivithinking "What scheme is he getting at today?"
    urshu happy "..."
    vivi neutral "Urshu, are you being cute again?"
    urshu happy "I'm never not being cute. I have a surprise for you."
    vivithinking neutral "His hands are behind his back. What fresh hell is this?"
    vivi angry "Ursh...what is it?"
    urshu happy "Guess, Miss Sanssouci."
    vivithinking "I am not in the mood for guessing games."
    vivi angry "Is it espresso with fancy-ass lemon juice in it?"
    urshu happy "No, my dear. Guess again. I'll narrow it down for you...with a riddle."
    vivithinking angry "Oh, spare me."
    vivi angry "Today is NOT a good day for riddles." 
    vivithinking angry "There's never a good day for riddles, actually."

    # <CHOICE>
    urshu happy "I am something everyone needs, but so few use me. I am something that keeps you young, but adults deny me. I am at home among children but taken away as they age. What am I?"

    menu:
        # OPTION 1
        "I don't have time or patience, patience or time!":

            vivi angry "I don't have time or patience, patience or time! Get me, Urshu?!"
            # SOUND: urshu sighs
            play sound sigh
            pause 4.0
            urshu neutral "Patience enough to repeat yourself."
            vivi angry "What was that?" 
            vivithinking angry "What is he on today?" 
            urshu neutral "Nothing, Miss Sanssouci. Here is the answer to my riddle."
            # VISUAL: urshu hands over playing cards (maybe SOUND: shuffling?)
            play sound shuffle
            pause 2.0
            vivi neutral "What are these...playing cards?" 
            urshu happy "Games, my dear. The answer is games. They bring unity and competition. They challenge you and change you. They--"
            vivi neutral "Look, Ursh, I've got your number now. You think I should play games with the other passengers."
            vivi neutral "No, let me rephrase. You want me to shoot the breeze while this bullet train screams on down to our universal heat death?"
            urshu happy "Well, excuse me. You're already playing love games with the delicious denizens of death here, Miss Sanssouci. Why not something less challenging?"
            # VISUAL: Urshu reveals a set of playing cards.  (maybe SOUND: shuffling?)
            play sound shuffle
            pause 2.0
            vivithinking neutral "Now he's got another set of cards."
            vivithinking surprised "Where is he keeping them all? Nevermind, I don't think I wanna know..." 
            vivi angry "Normal playing cards? Really?" 
            # JUMP TO: urshu happy "No matter when..." 

            # OPTION 2
        "Innocence.":

            vivi neutral "Innocence." 
            vivithinking neutral "That's a good guess, right? Don't even need to question it. I nailed it."
            urshu happy "Ah! Innocence is precious, is it not? A purity of existence where all emotions are in touch and rhythm. Doubt, fear, and anger all have their freedom."
            vivi neutral "So...?"
            urshu happy "I'm afraid not, my dear! The answer is not innocence. Good guess, though! In truth, the answer is far less altruistic. Here, take a look."
            vivithinking angry "Cards. CARDS?! All this to get me to play poker? Let me tell you, I wanna be free with my feelings right now. I'll show Urshu my innocence..." 
            vivi angry "Give me a break, Ursh. I woke up today, still dead. Still hurtling towards THE end. And I haven't even had coffee yet. Narubian or otherwise."
            # JUMP TO: urshu happy "No matter when..." 

        # OPTION 3
        "Baby teeth?":

            vivi neutral "Baby teeth?"
            urshu neutral "..."
            vivi neutral "What?" 
            vivithinking neutral "Why is he looking at me like I'm crazy?"
            urshu surprised "That is the most logically nonsensical answer I've yet received."
            vivi neutral "So, I'm right."
            urshu happy "Ha...no."
            urshu neutral "It concerns me greatly to think that you believe baby teeth will keep you young. Do you consider baby teeth to be a source of eternal life? The philosopher's enamel, if you will."
            vivi surprised "I--what?"
            urshu neutral "Are you in a cult? You must be, back in that backwater you call civilization. I do not wish to judge, not at all. It's a natural question, in regards to harvesting baby teeth."
            vivi neutral "Oh my God."
            urshu neutral "How do you harvest baby teeth? Do you pluck them fresh or bribe a despondent dental worker?"
            vivi neutral "Urshunabi..."
            urshu neutral "I suppose harvesting isn't the most important question. Ingestion is. Do you pop them whole like candy or grind them into powder for your eviscerated tree offspring? Smoothie bowls, they're called?" 
            vivi angry "Ursh!"
            urshu neutral "Yes?"
            vivi angry "Are you? Oh, you are." 
            urshu happy "Pulling your leg? I would never."
            vivithinking "This sonofabitch has wasted countless cosmic minutes!" 
            vivi angry "So what's the answer to your tiresome riddle?"
            # JUMP TO: urshu happy "No matter when..." 


        # OPTION 4
        "Games?":

            vivi neutral "Games?" 
            urshu happy "Games...hmm."
            vivithinking neutral "There's no way that's the answer." 
            vivi neutral "Well? Not getting any more alive here."
            urshu happy "Yes! Yes! That is the answer, Miss Sanssouci. You're the only one to have guessed correctly!"
            vivithinking happy "Fuck yeah!" 
            vivi happy "I had no doubt. I'm brilliant."
            urshu happy "Let's not get ahead of ourselves. You're the only human to have guessed correctly."
            vivithinking angry "This lil' shit!"
            # JUMP TO: urshu happy "No matter when..."

    urshu happy "No matter when, where, what, or who in the universe, across nebulae and even in the underworlds, games always have a place among emotional beings."
    urshu happy "Games are one method of reversing the naturally lawful decay we all suffer."
    vivithinking neutral "Games don't get rid of wrinkles. Wait. Do they?" 
    vivi neutral "Can you just hand them over already?"
    urshu neutral "I'm sorry, Miss Sanssouci. These are my special cards. Given to me by...well, someone from so long ago even Asha was a young deity. Humans had yet to walk upright, even. Ah, but you don't look like you want a story like that."
    vivithinking neutral "Good read there, honey." 
    vivi neutral "Are there other games, then?"
    urshu sad "..."
    urshu sad "We had something like love, then. A time and place long gone. Eternal gardens. Amber lanterns like fireflies. Buildings of floating emerald marble. What I wouldn't give..."
    vivithinking neutral "He's not even speaking in full sentences. Weird." 
    vivi neutral "Uh...Ursh?"
    show urshu sad blush with dissolve
    urshu "Forgive me...you will find games where you will find your next partner. Whoever shall you challenge? I am positively vibrating with anticipation."
    vivithinking neutral "Ew?"
    vivi neutral "I'll be sure to tell you all about it, as long as you stop vibrating...so close to me."
    show urshu happy blush
    urshu "As you wish, Miss Sanssouci."

    # VISUAL: urshu exits
    hide urshu with dissolve

    vivithinking angry "What the hell does he expect me to do? What will the others think of me? Oh God. Do I play one I know? Then they might think I'm cheating. Maybe I play one they know...but then I might lose."
    vivithinking happy "Then again, I've never played any game, love or otherwise, I couldn't win."

    # JUMP TO: Character Selector 1
    jump anger_cs1