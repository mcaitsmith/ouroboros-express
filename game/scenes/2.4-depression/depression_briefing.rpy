# The scene starts here.

label depression_briefing:

    # Briefing Depression

    # LOCATION: cabin
    scene cabin with fade

    show vivi sad at left with dissolve :
        xzoom -1

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
    urshu sad "Oh...don't turn away from me. I will not hurt you."
    vivi angry "Why don't I believe you?"
    urshu "You have always had my support."
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
    urshu "I understand. I wish to help {i}you{/i} understand something about our locomotive existence."
    vivithinking "If this turns into another trite anecdote..."
    urshu "I have been on this journey countless times, will be on it for an eternity still. This is what I do. It is what I am."
    vivi angry "A torturer in a sharp suit who could bounce silver dollars off his ass?"
    show urshu neutral blush with dissolve
    urshu "Well...How flattering."
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
    urshu angry "No! No, Miss Sanssouci. You have more to do and live for. In a manner of speaking."
    urshu neutral "Moreso, it is not true that you have nothing. You have time, still. And it is not time to lie here, falling into yourself."
    
   
    # THE BELOW TEXT AND FOLLOWING CHOICE ONLY APPEAR IF VIVI CHOSE TO HEAR BOTH URSHU'S 
    # FIRST STORY (SELECTED OPTION 1 "Go on, already. A story might lift my crow's feet." 
    # IN 2.1 DENIAL_BRIEFING) AND SECOND STORY (SELECTED OPTION 2 "Look, just tell me 
    # the story. If we have time." IN 2.2 ANGER_BRIEFING) AND THIRD STORY (SELECTED 
    # OPTION 1 "Urgh, ok. You win. What do you want to hear?":. OTHERWISE, 
    # NEEDS TO JUMP TO urshu neutral "It is time to embrace the void with others." BELOW.

    if urshu_story_1 == True and urshu_story_2 == True and urshu_story_3 == True:
    
        vivi neutral "Great. Want to tell me what you think it {i}is{/i} time for, 'Sursu'?"
        urshu happy "Ah, I see you've begun to predict my ruses. Very good, Miss... Vivi. Then I think you know: it is time for a story."
        vivithinking "He finally remembered to use my first name..."
        vivi neutral "Is this one going to be so long that I start to wish for death? That could be a neat trick."
        urshu neutral "This one is long, but not as long as some believe it should be."
        urshu neutral "In fact, it is precisely the length of a lifetime. Your lifetime."
        vivi surprised "What the –"
        urshu neutral "I think it's a wonderful story. Will you help me tell it, Vivi?"
        menu:
            # OPTION 1
            "Only because I don't trust you to tell it alone.":

                $ urshu_story_4 = True
            
                vivi neutral "Only because I don't trust you to tell it alone."
                vivi "You'd probably have me speaking in rhyming couplets and giving everyone flouncy pet names, right, 'my dear'?"
                urshu happy "I may upon occasion take the slightest trace of poetic license. But in your story there truly is no need to embellish what is already there."
                vivi sad "Yeah, right. I never achieved what I wanted. Never got the bylines I deserved, the scoops I should've... scooped. It had potential, maybe, but all  my life will be now is unfulfilled, meaningless and short."
                urshu neutral "Meaningless? A foolish term. Even a babe who draws one breath has lived a life which meant everything to someone. But you, Vivi, why there are almost too many moments to choose from. Why don't we start with the smile?"
                vivi neutral "The smile? You might have to narrow that down."
                vivithinking sad "I've smiled a lot. That's something, I suppose."
                urshu happy "The small but reassuring smile you once gave an elderly man as he took a few moments longer than he should to select items at the grocery store."
                vivi neutral "I once smiled at an old man? {i}That's{/i} the wonderful story of my life you wanted to tell?"
                urshu neutral "It was his first time leaving the house after his wife died. That smile gave him the courage to step back into a world that seemed a lonely place. He remembers it still."
                vivi surprised "I... I never knew."
                urshu happy "There is so much we don't know about our own stories, beyond their endings. That article you wrote about being raised between two cultures reached others navigating the same world. You inspired a young girl to write her own story: in five years, it will become a bestseller."
                vivi surprised "But that was just a student article!"
                urshu happy "And yet it changed lives. Your life was never about the bylines you got, Vivienne. It was about the bystanders you never knew, who will think of you all their lives."
                vivi sad "Long after I'm gone..."
                urshu neutral "Long after you are gone, you will live on. In the old man. In the young girl. In the heart and soul of your family, whose love for you is as undying as the stardust from which you are formed. In the college romance who still sleeps in your sweater. In the young journalist who remembers your mentorship with every word they write."
                urshu neutral "You are no single story. You are the meeting point in the narrative of every life that has ever touched yours. You are made up of their stories, and they of yours. A thousand hearts whose beats each tell a fragment of your tale."
                vivi angry "...You know all this – somehow you know every damn thing about me, so why are you wasting your time getting me to tell my story?"
                urshu neutral "Because I am not the one who has forgotten the value of your life. You can never be nothing, Vivi. You have already been too much, to too many, for that to ever be the case."
                vivithinking angry "I hate that I almost feel better. I don't want to feel better. Why won't he let me be miserable!"
                vivi neutral "You're like the old man, aren't you."
                urshu surprised "I..."
                vivi neutral "Lonely, and afraid to step into the world. You just watch the rest of us like we're your little soap opera, hoping we'll form the connections you're too afraid to."
                urshu angry "I shared with you what became of my last connection. What point would there be in my... extending my affections in such a way when the only certain thing is that you will all leave. And I will be –"
                vivi sad "Alone. Again. Are you sure you don't want to bury your head in the blankets with me, Urshu? It's starting to seem like we feel similarly about the end being nigh."
                urshu neutral "Ha... no, no time for such frivolous misery, my dear."
                vivi neutral "No time, again. So, what's it time for now?"
    
            # JUMP TO: urshu neutral "It is time to embrace the void with others."

    
            
            
            # OPTION 2
            "Ugh, no. I don't want to replay my life for you. Its meaningless now. It's over.": 
            
                vivi angry "Ugh, no. I don't want to replay my life for you. Its meaningless now. It's over."
                vivi sad "I just want to lie here. On my face."
                urshu angry "With my most sincere apologies, there is no time for that either, Miss Sanssouci."
                urshu sad "I do wish I could make you see how very little time you have. How very important it is to use it."
                vivi neutral "And I wish you'd cut the sinister, cryptic crapola and tell me what you think it's time for, Urshunabi."
            
            # JUMP TO: urshu neutral "It is time to embrace the void with others."
    
    
    
    urshu neutral "It is time to embrace the void with others."
    vivi neutral "That is the worst advice to give to someone in my state."
    urshu neutral "Then you misunderstand me. I speak not of embracing the void itself, but rather the chance for true companionship at the end."
    urshu neutral "Not death, but the fleeting moments before. When nothing holds you back. When it does not matter that there is no tomorrow, because it is when you have only the present that you can be truly fearless."
    vivi angry "Shut up. I won't take this flowery language, not now. Make sense or leave."
    urshu angry "Don't you get it? This is all on purpose and you only have so much time! You must complete--"
    vivithinking "Well that was... unusually direct. No creative metaphor? And he's never used that kind of tone with me. He sounds almost... desperate. What the hell?"
    vivi neutral "Complete what?" 
    show urshu neutral blush with dissolve
    urshu "Nothing. I apologize, Miss Sanssouci, for losing my composure."
    show urshu sad -blush
    #Here starts a reminder for the player: that the chosen person for FR1 will not be available in FR2, i.e. Vivi's "last moments" before the endings
    urshu neutral "What I meant is, please be careful in the next choice you make. It will likely be the last time you speak with that person privately in this plane of existence. You may wish to choose someone with whom your bond is less strong."
    urshu sad "The connections you make here have consequences, for your own ending and for others. If there is one companion you wish to have at your side in the end, do not visit them yet."
    urshu neutral "Though of course, your choice is your own! I merely offer these words as a lowly ferryman, but... one who cares for you."

    hide urshu with dissolve

    # JUMP TO: character selector 1
    jump depression_cs1