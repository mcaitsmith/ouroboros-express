# The scene starts here.

label good_briefing:

    # Good Ending/Briefing

    play music goodendmusic volume 0.5
    
    # fade in

    # LOCATION: cabin
    # call hide_overlay from _call_hide_overlay_2
    scene cabin with fade

    show vivi happy at left with dissolve:
        xzoom -1

    vivithinking neutral "Something seems different today."
    vivithinking neutral "The decay... It's...slowed? The train is looking back to its gaudy self."
    vivithinking happy "Hmm. Coincidentally, I feel the same."

    # SOUND: knocking on the door
    play sound knock
    pause 1.0

    show urshu happy at right with dissolve

    urshu happy "Hello, Vivienne! I hope you are well."
    vivi happy "Hey, Urshu. Yeah, I surprisingly feel okay."
    vivi sad "Don't get me wrong, though, I'm still {i}really{/i} afraid of... well, everything that awaits."
    urshu neutral "What is it exactly that scares you?"
    vivi neutral "... Well, um. That's it right there."
    vivi neutral "The unknown..."
    vivi sad "And... feeling that I could've done more with my time."
    vivi sad "And ending up... alone."
    urshu happy "My darling Vivienne, you needn't worry. This train has a habit of taking folks exactly where they need to go. The unknown is scary, yes, but it's less scary with company. I have a feeling it will all work out."
    vivi neutral "How do you know?"
    urshu happy "I trust you."
    vivithinking neutral "He trusts me? With what?"
    vivi neutral "Oh, well... Thanks Urshu."
    vivi happy "You're in a really good mood today!"
    urshu happy "I'm not the only one. Come see who's waiting for you in the lounge."
    
    # The choice that follows will be between the player choosing to move on to the 
    # romance / confession character selector OR choosing to talk to Urshu instead, 
    # in which case they will not get to select / confess to any other character. 
    # This choice only appears if vivi chose to hear URSHU'S FIRST STORY (SELECTED 
    # OPTION 1 "Go on, already. A story might lift my crow's feet." IN 
    # 2.1 DENIAL_BRIEFING) AND SECOND STORY (SELECTED OPTION 2 "Look, just tell me 
    # the story. If we have time." IN 2.2 ANGER_BRIEFING) AND THIRD STORY (SELECTED 
    # OPTION 1 "Urgh, ok. You win. What do you want to hear?" AND FOURTH STORY 
    # (SELECTED OPTION 1 vivi neutral "Only because I don't trust you to tell it alone."  
    # Otherwise the remainder of this scene is skipped and we jump to romance_cs
    
    # <CHOICE>
    menu:
        # OPTION 1
        "I have a feeling I know. At least, there's someone I want to see.":
        
            vivithinking happy "I have a feeling I know. At least, there's someone I want to see."
        
            # JUMP to: Romance/Confession/Character Selector
            jump romance_cs
    
        # OPTION 2
        "Hold your horses. I've decided to step into the unknown with you." if urshu_story_1 == True and urshu_story_2 == True and urshu_story_3 == True and urshu_story_4 == True:
        
            vivi happy "Hold your horses. I've decided to step into the unknown with you."
            vivithinking happy "The way he's staring at me right now. Rude, but also kind of hot."
            urshu neutral "Ah. I'm afraid I am not an option as a companion, my dear. I believe I have explained to you why?"
            vivi neutral "Yeah, you tried. Something about {i}'I'm Urshu and I'm afraid of connection because everybody leaves me, so I just strut around being mysterious and flipping the number on my 'it's been 9000099 days since my last heartbreak'{/i} sign."
            show urshu sad blush with dissolve
            urshu sad "That {i}may{/i} bear some form of resemblence to the truth. But as I have made quite clear, the rules aren't mine to break. When you leave this train, you will go to your final destination and I will remain here, forever moving on."
            vivi neutral "Right, except for how you're wrong. You told me I couldn't get off the train early. You never told me I couldn't {i}stay on.{/i}"
            show urshu sad -blush
            urshu sad "My darling Vivienne..."
            vivi happy "Don't you 'darling Vivienne' me. For one thing, I told you to call me Vivi, and for another I hate how cute I'm starting to find it. I'm staying, Urshu. Unless doing so is going to blow up the universe or something. I want to stay here."
            urshu sad "Yes, I understand. So many do."
            vivi surprised "You mean people have asked to stay before?"
            vivithinking surprised "Could the rage that thought stirs up be... jealousy? C'mon Vivi, pull yourself together, of course you're not the only one who's ever fallen for..."
            urshu sad "Ah yes, it's barely unusual for your fellow travellers to grasp at a last chance to save themselves: staying on this train long enough to learn the method of escaping from it. I can't blame them. Or you. You are far too bright a spark not to have thought of such an idea."
            urshu neutral "But I'm afraid I must disappoint you. To stay here would not free you from your fate, but subject you to a worse one. Any who failed to disembark at the end of their journey would be cursed to stay on this train forever."
            vivi neutral "Forever?"
            urshu sad "Until the very cosmos slips its moorings and spins out into oblivion. Which I am sure you will see is almost the same thing."
            vivithinking happy "Oh, oh he's ridiculous. Can't use one word where three will do. Can't see the nose in front of his face. I can't think why I adore him."
            vivithinking surprised "Because I do... right? That's what this is. I love him. {i}Now{/i} who's ridiculous?"
            urshu neutral "Vivi, you're making a very curious sound. You should know this is no laughing matter."
            vivi happy "I'm sorry, Ursh. It's just, being with you until the cosmos slips its moorings sounds pretty good to me."
            urshu neutral "Yes, and now that you understand the bitter consequences of... pardon? Did you say {i}pretty good?{/i}"
            vivi happy "I did. You see, it turns out I don't want to escape my fate after all. I just want the chance to do what you told me, and choose my own. I want to tell my own story."
            vivi neutral "{i}I'm afraid.{/i} You don't know what it took to admit that to you. Afraid of the unknown. Of not doing more with my time. Of being alone. What I didn't say was that I'm afraid of losing you. And correct me if I'm wrong, but I think you're afraid, too."
            show urshu surprised blush with dissolve
            urshu neutral "You were right. I should never have risked saying so much in front of a journalist."
            vivi happy "Ha! Told ya, we're the best people readers around. Cosmic entity readers. Whatever."
            vivi neutral "Listen, I know you paid an eternal price for the last favour you granted a soul in need, and now you're scared to take the chance again. But the favour I'm asking for won’t take anything from you. I want to give you something, instead. Company."
            vivi neutral "You’ve been alone so damn long, and I’ve never given myself the chance to love. I want that chance, Urshu. With you. And if you let me stay we'll have more than a chance - we’ll have eternity. Together."
            urshu surprised "..."
            show urshu surprised blush with dissolve
            vivithinking happy "Is he seriously lost for words?"
            vivithinking surprised "I've broken him! No, wait, I've–"
            vivi happy "I just {i}surprised{/i} you, didn't I."
            urshu happy blush "That... ahem... {i}may{/i} be the case."
            vivi happy "Yes! Finally, Mister can't be surprised from beside, before or behind!"
            urshu happy -blush "I confess, I never expected you to strike straight at the heart."
            vivi neutral "And your heart... how does it feel?"
            urshu happy "Won, Miss Sanssouci. Well and truly won."
            vivi happy "Vivi, doofus. From now until forever. Call me Vivi."
            vivithinking happy blush "When I look back, it seems like I never made a single decision that was true to myself, to who I really am rather than what I thought I should be."
            vivithinking happy blush "Is it weird to make the best decision of your life when you're already dead?"
            vivithinking happy blush "His smile. The way his arms fit around me like they were designed to. The stupid, highfalutin words he whispers in my ear."
            vivithinking happy blush "I'm not sure forever's going to be long enough."
  
      
            # VISUAL: the screen shakes, flickering
            show cabin with hpunch
            show cabin with flash
            show cabin with flash        
    
            vivi surprised "What's that? Urshu, what's happening?"
            urshu neutral "The journey nears its end, at least for three of our travellers. Vivi, take my hand, there are some goodbyes you may want to say, and quickly!"
         
            urshu happy "...and then, perhaps a change of outfit."
            vivi happy "Wait, death has a dress code? Are you kidding me?"
    
            #SOUND: both of their laughter, softly fading out.
            #JUMP TO group_goodbyes
            jump group_goodbyes
