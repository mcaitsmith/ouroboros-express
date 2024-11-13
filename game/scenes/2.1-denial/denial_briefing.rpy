# The scene starts here.

label denial_briefing:
    $ day = 1 # denial

    #Briefing Denial
    #LOCATION: cabin
    scene cabin with fade
    play ambience amb_bedroom if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking "Uhhh..."
    vivithinking "My head's pounding. Almost as bad as it did that one lunar new year in Hanoi."
    vivithinking "Did I faint yesterday?" 

    show urshu neutral at right with dissolve
    play sound swoosh

    urshu "Miss Sanssouci, the Ouroboros Express waits for no one. Least of all a reporter. Do you have a moment?"

    vivi happy "Conductor!"
    vivithinking neutral "What's his name again? Usher? Ursherbambi? Eh, whatever. Conductor, for now." 
    vivi happy "Why not? Got nothing but time here, right?"
    vivithinking "He's laughing."
    vivi neutral "What's so funny?"

    urshu neutral "I apologize, Miss Sanssouci, for not informing you earlier. The cosmic cycle of life and death and life again spirals faster than any of us like to admit."
    urshu neutral "But I digress, Miss Sanssouci. I came to check on you. Last night's excitement did not, ah, sit well with you."
    vivi neutral "To say the least..." 
    vivithinking "How many shots equate to learning you're dead? Is this how Bruce Willis felt?"
    urshu neutral "I was concerned that yesterday's revelations, on top of your physical, temporal distress, were contributing to a less than ideal mental state."
    vivi angry "Less. Than. Ideal? Temporal distress? You're talking in circles."
    urshu neutral "Come now, did you not notice your new set of crow's feet?"
    vivi neutral "Crow's feet? My skin is perfect. What the hell do you mean?"
    vivithinking "Come on Vivi. Perfect? Maybe ten years ago." 
    vivithinking "But I know what he means. Yesterday..."
    stop music fadeout 10.0
    vivithinking "Something wrong. Something sick. Feeling like something pulling my skin apart, then I fell unconscious."
    vivithinking "Huh? He's pointing at the mirror."
    vivi neutral "What's wrong? Let me have a look at myself."
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(400), replace=True, duration=1.0)
    play sound heartbeat
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=10.0)
    vivithinking "HUH?"
    vivithinking "What are these gross flakes protruding off my skin?!"
    vivithinking "They're shining like wet scales."
    vivithinking "I think I'm going to throw up."

    vivi surprised "I've never been flaky in my life. Not my skin. Never on the job." 
    vivi surprised "Explain." 

    # <CHOICE>
    urshu neutral "Would the good lady like a story? I am happy to indulge, if your quickly deteriorating time allotment permits?"
    play music mysterymusicpiano

    menu:
    # OPTION 1
        "Go on, already. A story might lift my crow's feet.":

            $ urshu_story_1 = True

            vivi neutral "Go on, already. A story might lift my crow's feet."
            urshu happy "Once, long ago, a ferryman called... Sursu toiled in the doldrums of an ordinary immortal career... ferrying souls to and fro. From mortal realms to eternal gardens, or places eternal but foul." 
            vivithinking "What did I sign up for?"
            # SOUND: urshu sighs
            #play sound sigh #REPLACED WITH VO
            urshu neutral "On one occasion, Sursu the ferryman met a sweet soul who asked of him a great favor. Too great, in reality - a lifeline, of sorts. And Sursu felt less than obliged to help this soul - they’d already tried to destroy the ferryman's precious vessel! It was audacious!" 
            urshu neutral "Furthermore, the ferryman was under great scrutiny by the gods who managed him. They were aware of his treasonous heart, which wanted to do more than ferry souls to and fro. They knew he yearned for more than those sad, sole voyages could yield..." 
            urshu neutral "But this sweet soul only did what they thought was right, for they were trapped and lost, with no north star to guide them..."
            vivithinking "I wonder what's for lunch..."
            urshu neutral "The ferryman was in great conflict about it. He had his own life to keep afloat, so to speak, and this soul's request would certainly sink it. He had a choice to make."
            vivithinking "Oh! Now I remember his name. Urshunabi. God of insufferably long stories."
            urshu neutral "The ferryman acquiesced to the request. He gave this sweet, lost soul what they asked for."
            urshu neutral "He earned their trust and recognition, and a great prize: in his dire straits, he gained a lovely companion - one who came to be his lifeline in turn. But he paid an eternal price for it."
            urshu sad "The ferryman could never return home."
            vivithinking "Damn. That's...I feel that."
            urshu happy "But not all was lost. That daring soul he aided? They invited him to their domain and he gained a new home. A safe one. A place of wonder and nature and possibility. And, for this weary ferryman, a new life."
            urshu neutral "Is that not a wonder? A tribulation transfigured into triumph? Are you not yourself in dire straits, Miss Sanssouci?"
            vivi neutral "I doubt it. You don't know me, Ursh. I've been in situations nearly as tense."
            vivithinking "But I've never been under threat of existential extinction before..." 
            urshu neutral "You might reconsider your position. Much like Sursu the ferryman, your life, now, is a vessel heading toward a certain yet unfathomable destination. Would it not be better to face this end with a companion?"
            vivi "You think you're funny, don't you? Crow's feet, vague stories, boat trip metaphors...am I the Titanic in this situation?"
            urshu happy "I think I'm just cosmical. I bid you adieu, Miss Sanssouci."
            vivi neutral "Cosmical? Com-ic-al? Oh my God."
            vivi neutral "Wait, Urshu?"
            urshu neutral "Yes, my dear?"
            vivi neutral "Why did you tell me all that? The story, with the soul and the sacrifice, and all that guff?"
            urshu happy "It makes one feel alive, no, to recall the moments where we're at our most alive? And to give those moments life of their own through our words, even when they've long since passed..."
            vivithinking "Give me a break."
            urshu happy "And now, I must attend to the day. May you enjoy yours, Miss Sanssouci!"
            hide urshu with dissolve
            vivithinking "Sursu the ferryman, eh? Something's going on there." 
            vivithinking "Jeez, I can hardly believe all this, but I have to. And he's right about the companion. I can't do this alone. If there's any chance to get off this train, it's with someone else's help."
            vivithinking "Let's get cracking! Time to investigate." 
            #Jump to Character Selector 1

    # OPTION 2
        "No, dammit! You just said I'm running out of time!":

            vivi angry "No, dammit! You just said I'm running out of time!"
            urshu sad "I hope you have a kinder word for your fellow travelers, Miss Sanssouci. Since time is your master, you should know that you are all on short leashes." 
            vivi neutral "So, not only are we dead here, but we don't have all the time in the world?" 
            vivi "Next you'll tell me to sit, stay..."
            urshu neutral "Fetch, rather, fetch the truth of your circumstances here. I'll even give you a treat, if you do."
            vivithinking "Sure, I'll fetch the truth...fetch it right up your ass." 
            vivi "What a colorful description. I wonder if you're actually the God of Condescension."
            urshu "I can only give you the truth, Miss Sanssouci."
            vivi angry "I'm not dying. It can't really be the end. Come on, why else would we get another chance here?"
            urshu neutral "All mortals resist the end. But it's the truth, Miss Sanssouci. In life, it was your sole mission to find that indelible, intangible substance."
            urshu "Might it be time to seek truth, before it decides to hunt you?"
            vivi angry "The hell does that mean?"
            urshu neutral "Tick-tock, Miss Sanssouci. If you need me, ever, give a shout."
            hide urshu with dissolve
            vivi neutral "The truth will hunt me? I don't even want to know what that means. Better get a move on."
            #JUMP TO: Character Selector 1

    jump denial_cs1
