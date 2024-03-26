# The scene starts here.

label depression_briefing:

    # Briefing Depression

    # LOCATION: cabin
    scene cabin with fade

    show vivi sad at left with dissolve

    vivithinking "I'm...awake."
    vivithinking "Alive."
    vivithinking "Dying. But still goddamn alive."
    vivithinking "I'm just a shell."
    vivithinking "Empty, breaking."
    vivithinking "I'm nothing."
    vivithinking "Or..I will be soon."
    vivithinking "Please, make it soon."

    # SOUND: knocking
    play sound knock
    pause 1.0
    
    vivi "Go away."

    # SOUND: knocking
    play sound knock
    pause 1.0

    # <CHOICE>

    vivithinking "Can I bring myself to talk to anyone?"

    menu:

        #OPTION 1
        "I guess so...":

            vivithinking neutral "I guess so..."
            vivi neutral "God, who is it?"
            urshu "Your worst enemy, I imagine."
            vivi angry "You...you fucker! You've done enough! Leave me here to die."
            urshu neutral "At the risk of sounding pedantic, you are already dead, my dear." 
            urshu neutral "You're merely on your way to become a part of the cosmic weave. And that will occur whether I deliver your breakfast or not."
            # JUMP TO: vivi angry "I don't care. Do what you want, like always. Little cretin."

        #OPTION 2
        "No. Let them knock till their knuckles bleed. Especially if it's Urshu.":

            vivithinking "No. Let them knock till their knuckles bleed. Especially if it's Urshu."
            urshu neutral "Miss Sanssouci, time is passing - you may as well enjoy a delicious breakfast."
            vivithinking angry "Oh, no. He doesn't get to bring me breakfast!"
            urshu "The only thing worse than being dead is being dead and bored. Might as well let me in, I'll cheer you up."
            # JUMP TO: vivi angry "I don't care. Do what you want, like always. Little cretin."

    vivi angry "I don't care. Do what you want, like always. Little cretin."

    show urshu neutral at right with dissolve

    vivi "Know what? After seeing your smug face, I've changed my mind. Would you kindly jump off this train?"
    urshu "Espresso. Fresh croissant. Passionfruit juice. Warm congee with crispy garlic and cosmic ocean-caught catfish."
    vivithinking sad "Why does this feel like a gut punch?"
    urshu sad "This is the last meal you ate as a mortal. You might not recall it, but I do. I remember your whole life. All your lives; those who came before and those yet to jump aboard."
    urshu "It is written on my heart and remains my burden: to remember everyone who travels with me."
    vivithinking "I can't face this. Whatever Ursh is doing...it hurts worse now."
    vivithinking "When will it stop hurting?"
    vivithinking "Why can't I just disappear?"
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
    vivi angry "Liar! Son of a bitch! Traitor! Crawl back to your hole, you worm!"
    urshu sad "..."
    vivi sad "I...want to live."
    urshu neutral "I wish you could."
    vivi "I want to-- God. There's no words for it."
    urshu "I understand. I wish to help {i}you{/i} understand something about our locomotive 
    existence."
    vivithinking "If this turns into another trite anecdote..."
    urshu "I have been on this journey countless times, will be on it for an eternity still. This is what I do. It is what I am."
    vivi angry "A torturer in a sharp suit who could bounce silver dollars off his ass?"
    show urshu neutral blush with dissolve
    urshu "Well... How flattering."
    show urshu neutral -blush
    urshu neutral "But a torturer? No. A caretaker of poor souls. A ferryman. And the only currency I accept is the pleasure of conversation and high-stakes romantic drama. It is {i}all{/i} I have here."
    vivi neutral "So what? You're immortal. That can't be your excuse to manipulate us."
    vivithinking "If he's keen on being honest..."
    vivithinking "I can get him to admit more!"
    vivi neutral "And what about you and me? We had a moment yesterday. An incredible one, over some goddamn espresso."
    urshu "Yes..."
    vivi neutral "And the food I made you?"
    urshu sad "It was divine!"
    vivi neutral "And we've had weird, wonderful sparring matches!"
    urshu neutral "Yes! A thousand times, yes!"
    vivi angry "Then why did {i}you{/i} lie to {i}me{/i}?"
    vivi "Now, I have no hope."
    vivi "I have nothing."
    vivi "Can't you just...finish me off?" 
    vivithinking "I don't even have the juice for innuendo..."
    urshu angry "No! No, Miss Sanssouci. You have more to do and live for. In a matter of speaking."
    urshu neutral "Moreso, it is not true that you have nothing. You have time, still. And it is not time to lie here, falling into yourself."
    urshu "It is time to embrace the void with others."
    vivi neutral "That is the worst advice to give to someone in my state."
    urshu neutral "I urge you to embrace not death, but the fleeting moments before. When nothing holds you back. When it does not matter that there is no tomorrow, because you have the present, and it is wholly yours."
    vivi angry "Shut up. I won't take this fluffy language. Make it make sense or leave."
    urshu angry "Don't you fucking get it? This is all on purpose and you only have so much time! You have to complete--"
    vivithinking "He just used a contraction. And said 'fucking'? What the hell?"
    vivi neutral "Complete what?" 
    show urshu neutral blush with dissolve
    urshu "Nothing. I apologize, Miss Sanssouci, for losing my composure."
    show urshu sad -blush
    urshu sad "And I {i}am{/i} sorry."
    urshu neutral "I care for you. Please, give yourself a little more time. Just, be free with it."

    hide urshu with dissolve

    # JUMP TO: character selector 1
    jump depression_cs1