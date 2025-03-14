# The scene starts here.

label bargaining_briefing:
    $ day = 3 # bargaining

    #Briefing Bargaining

    # LOCATION: cabin
    # call check_overlay from _call_check_overlay_12
    scene cabin with fade
    play ambience amb_bedroom if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    # SOUND: vivi yawns 
    # skipping

    vivithinking "God, what time is it? Why don't I feel rested?"

    show vivi happy at left

    vivithinking "You know what? This time, I'm going to turn the tables on Urshu. Yeah, that's right. I'll surprise him before he's had his fabuloso-lime-expresso and see how he feels!"

    show vivi neutral at left

    vivithinking "Hold on, V, that's not how you run down a lead. You gotta start with what you want and what you know."
    vivithinking "I know what I want: to stop my forthcoming eternal demise. And I want to see if I can bargain with him to get off this death metro."
    vivithinking "What I know: Urshu is an immortal, silver-tongued courier of the dead who's probably tasted and seen everything life can offer. What could I possibly exchange with him to win him over?"
    vivithinking "Well...he has told me a bit about his past. I get the feeling he's lonely. That he longs for something. For what? Doesn't matter. I can relate to a deep sense of unsatisfied longings."

    define checked_observatory = False
    define checked_lounge = False
    label search_urshu:
        # <CHOICE>
        vivithinking "Where should I look for that little peach?"
        
        menu:
            # OPTION 1
            "Let's try the lounge." if not checked_lounge:
                $ checked_lounge = True
                vivithinking "Let's try the lounge."
                stop ambience fadeout 1.0

                # LOCATION: lounge
                scene lounge with fade
                play ambience amb_lounge if_changed fadein 1.0

                show vivi neutral at left:
                    xzoom -1

                vivithinking "Well. He isn't here. Nobody's here."
                stop music fadeout 1.0
                $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=2), audio_filter.Lowpass(2000)], replace=True, duration=2.0)
                vivithinking "Wait...what is..."
                play music horrormusic loop
                $ renpy.music.set_volume(0.25, delay=0.1, channel='ambience')
                play sound trainshake loop

                

                # VISUAL: rainbows flash around the room
                show white :
                    alpha 0.0
                    ease 1.25 alpha 0.3
                    linear 1.25 alpha 0.0
                    pause 0.5
                    ease 1 alpha 0.3
                pause 4.0
                hide white with dissolve
                # scene lounge with flash
                # scene lounge with flash
                # scene lounge with flash
                scene lounge at train_shake:
                    pause 2.0
                    linear 3.0 zoom 1.05 xoffset -5
                    # xoffset -5
                # with flash

                show vivi neutral at left:
                    xzoom -1.0
                pause 1.5
                show vivi surprised at left:
                    xzoom -1.0
                vivithinking surprised "The train's shaking.. Feels like it's coming apart!"
                vivithinking "Feels like {i}I{/i} might come apart."
                show white:
                    alpha 0.5
                with dissolve
                hide white with dissolve
                vivithinking "That strange light is turning the windows into mirrors but I can't see myself in them, just endless other mirrors reflecting back. And then darkness. Darkness I can {i}feel{/i}."
                vivithinking sad "Like there's a void closing in around me, swallowing me up, and there are things waiting there... things I don't want to see. Is this what the end feels like?"
                stop sound fadeout 1.0
                $ renpy.music.set_volume(1.0, delay=1.0, channel='ambience')
                vivithinking "No, pull yourself together, Vivi. It's all just your imagination. It's just..."
                # VISUAL: a black vignette closes in on the room
                # scene lounge with flash
                $ renpy.music.set_volume(0.25, delay=0.1, channel='ambience')
                $ renpy.music.set_volume(0, delay=0.1, channel='music')
                play sound char_terror
                show lounge blur with Dissolve(2.0)
                $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
                pause 2
                $ renpy.music.set_volume(1.0, delay=3.5, channel='ambience')

                show vivi surprised
                pause 3.0
                stop sound fadeout 1.0
                stop music fadeout 1.0
                vivithinking surprised "...Yeah, I'm out."
                $ renpy.music.set_audio_filter("ambience", None, replace=False, duration=2.0)
                stop ambience fadeout 1.0


                hide vivi with dissolve
                stop sound fadeout 1.0

                scene cabin with fade
                play ambience amb_bedroom if_changed fadein 1.0

                show vivi neutral at left with dissolve:
                    xzoom -1

                # JUMP TO: vivithinking "Where should I look for that little peach?"
                jump search_urshu

            # OPTION 2
            "Perhaps Urshu's enjoying the stars." if not checked_observatory:
                $ checked_observatory = True
                vivithinking "Perhaps Urshu's enjoying the stars."

                # LOCATION: observatory
                scene observatory with fade
                play ambience amb_observatory if_changed fadein 1.0
            
                show vivi neutral at left with dissolve:
                    xzoom -1

                vivithinking "Goddamn. He isn't here."
                vivithinking "Can't deny that view, though."
                # VISUAL: starry night sky
                vivithinking neutral "Are those shooting stars?"
                # VISUAL: zoom in on night sky 
                # VISUAL: two galaxies glow, one red and one white, resembling a reptile
                vivithinking "No... Galaxies. One is white... and the other red?"
                vivithinking "The whole glowing thing looks like... a reptile. I'll never understand this space. Please wake me up. I got enough of this hell."
                $ renpy.music.set_audio_filter("sound", audio_filter.Lowpass(1500), replace=True, duration=2.0)
                play sound char_mirror fadein 2.0
                vivi surprised "What the—"
                # VISUAL: a shadow appears over vivi's face
                # CUE FOR VA: vivi is possessed here, speaking with a voice that is not her own
                vivithinking "Something just stopped by the window."
                vivithinking "That shape! A human figure like a big round head."
                play sound char_terror fadein 2.0 volume 0.7
                vivithinking "No. It can't be human."
                vivithinking "Damn, it's looking at me!"
                $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(2000), replace=True, duration=2.0)
                vivi "W-what do you want? Leave me alone!"
                # VISUAL: shadow disappears, leaving Vivi's reflection behind
                vivi surprised "What the hell?! It's gone. But wait..."
                $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=2.0)
                # VISUAL: Vivi catches sight of her decaying reflection
                vivi surprised "Where are my eyes?! I can see my reflection, but... Why does it look like my ribs are showing through my—"
                $ renpy.music.set_audio_filter("sound", None, replace=False )
                $ renpy.music.set_audio_filter("ambience", None, replace=True, duration = 2.0 )
                vivi surprised "I gotta get off this train. I gotta find Urshu."
                stop ambience fadeout 1.0
                hide vivi with dissolve

                scene cabin with fade
                play ambience amb_bedroom if_changed fadein 1.0

                show vivi neutral at left with dissolve:
                    xzoom -1

                # JUMP TO: vivithinking "Where should I look for that little peach?"
                jump search_urshu


            # OPTION 3
            "I'd bet he's at the bar.":

                vivithinking "I'd bet he's at the bar. Polishing spoons and staring at his reflection, that little twerp."
                stop ambience fadeout 1.0

                # LOCATION: dining car
                scene diningcar with fade
                play ambience amb_bar if_changed fadein 1.0

                show vivi neutral at left with dissolve:
                    xzoom -1

                show urshu sad at right with dissolve

                vivithinking "There he is. Time to wrangle him down..."

                show vivi surprised at left

                vivithinking "For clues, I mean! For information!"

                show vivi neutral at left

                vivithinking "Hold on. He doesn't look like himself..."

    urshu sad "What I wouldn't give...just one more dance with you in the Queen's Gardens..."
    urshu neutral "Miss Sanssouci. You must know I cannot be surprised from beside, before, or behind. I can hear the sound of your soul steps wherever you traipse on this train."
    urshu neutral "Please, sit. Here, I have a cup for you."

    # SOUND: glassclink
    play sound drinkstir volume 0.7
    pause 10.0

    vivi neutral "You... Of course, you knew." 
    vivi neutral "Thanks for this, Ursh. You take good care of me. When you're not being a... an impish... wisenheimer or something."
    urshu happy "I appreciate that, Miss Sanssouci. I do work very hard for all of you."
    urshu neutral "It is my joy to serve—not only to serve, but to draw out of each of you your very best."
    vivithinking "Oh, he's being sweet. And candid. And not talking in riddles!"

    show vivi angry at left:
        xzoom -1
    
    vivithinking "Focus, Vivi. Think about your goal. Now, how should I go about this?"
    play music mysterymusic loop

    show vivi neutral at left

    vivithinking "I need to be delicate. I should go in with tact and poise and—"
    vivi angry "Urshu, I want my fucking life back!"
    vivi neutral "Yes, I have distractions and good people and tasty espresso—and you here to spice up my life..."
    vivi angry "But I look out of these windows, and all I see is death!"
    vivi sad "I want off this train. Ideally, I want everyone to get off and get back to their lives. I'll do anything to make it happen."
   
    # THE BELOW TEXT AND FOLLOWING CHOICE ONLY APPEAR IF VIVI CHOSE TO HEAR BOTH URSHU'S 
    # FIRST STORY (SELECTED OPTION 1 "Go on, already. A story might lift my crow's feet." 
    # IN 2.1 DENIAL_BRIEFING) AND SECOND STORY (SELECTED OPTION 2 "Look, just tell me 
    # the story. If we have time." IN 2.2 ANGER_BRIEFING). OTHERWISE, NEEDS TO JUMP TO 
    # urshu neutral "Miss Sanssouci..." BELOW.

    if urshu_story_1 == True and urshu_story_2 == True:

        urshu neutral "It is a wonderful wish, Miss Sanssouci. I wonder..."
        vivi sad "You wonder what? How you're gonna make that happen?"
        urshu neutral "I am sure it won't have escaped your journalist's intellect that the stories I have shared with you in our time here... well, I was that ferryman. They were my stories to share."
        vivithinking "Yeah, no kidding."
        urshu neutral "And I wonder if you might now care to share one of your own? About the life you so fervently wish to return to."
        vivi neutral "Wait up, I thought you already knew a ton about us?"

        # <CHOICE>
        urshu neutral "The deepest secrets of the heart must be shared freely, Miss Sanssouci."

        menu:
            # OPTION 1
            "Urgh, ok. You win. What do you want to hear?":

                $ urshu_story_3 = True

                vivi neutral "Urgh, ok. You win. What do you want to hear?"
                vivithinking "I bet he wants to hear a {i}secret of the heart{/i}, whatever that means."
                urshu happy "I wish to hear a memory of your past that tells me best who you are at present."
                vivi neutral "Uhh..."
                vivithinking "He really digs nostalgia, huh."
                vivi neutral "Sure, I can do that. Lemme see..."
                urshu happy "I await with bated breath, Miss Sanssouci!"
                vivi neutral "Great. Well, I always loved crazy décor. Always. Like, all-out, the bigger the better. Too much is not enough, y'know?"
                vivithinking "Oh, he knows. If he had anything to do with the look of this place, anyway."
                urshu happy "I can only imagine!"
                vivi neutral "Holidays were amazing. Mom always let me go batshit with the dec's. Birthdays, BBQs, Lunar New Year - everything got tinsel and streamers and confetti, the works. But Halloween was the best."
                vivi happy "I turned the whole house orange and black. Every year bigger and better. It was a whole thing - people tripping over pumpkins, bats, and skeletons for a week."
                vivi neutral "But a few years ago I was so busy and I... I screwed up."
                vivi neutral "I was going after this scoop. It was a big catch for once, not just the usual small fry. I was finally gonna make my name."
                vivi neutral "I was chasing leads for weeks, and I totally forgot it was Halloween."
                vivi neutral "I left all the decorations at home. All of them. I was late to Mom's, and then I spent all day on the phone with sources and my editor barking at me."
                urshu neutral "How out of character that must have seemed."
                vivi sad "Mom was so sad."
                vivi sad "I said I was sorry. I told her I was just really busy chasing my dream. I was gonna make her so proud. But she was hurt, and she was worried I was gonna trip up, always looking ahead."
                vivi neutral "But I fixed it. I raided her fridge, shelves, even her vegetable garden. I rustled up a feast for the whole family."
                vivi happy "I did it all: dumplings, pumpkin stew, cakes - the lot! Auntie ate so much of my putu piring she had to lie down for hours!"
                urshu happy "A bountiful bargain!"
                vivi happy "Yeah. It was."
                vivi neutral "But I need to do that again. I've been so busy, I've barely been home the past couple years."
                vivi neutral "With Mom, and Auntie, and everyone... it's not been the same. Not for a while."
                urshu neutral "It seems your eye has been too fixed upon another time, one out of reach. It has struggled to see the present, and to bask in what it beholds."
                vivi surprised "I... I mean, I dunno. I guess so. Maybe."
                urshu neutral "Perhaps you lost your way?"
                vivi surprised "Maybe a little. Yeah."
                urshu neutral "And in this, my dear, I think we understand each other perfectly."
                vivi surprised blush "I... What d'you mean?"
                urshu neutral "I don't only urge you to use your time aboard this vessel wisely, Miss Sanssouci. I urge you to {i}see{/i} it wisely. Differently."
                vivithinking blush "Dammit Urshu, why you gotta hit me in the feels like that?! Cunning little..."
                vivithinking blush "But that does give me an idea."
                vivi neutral "Look, Ursh..."

                # JUMP TO: urshu neutral "Miss Sanssouci..."


            # OPTION 2
            "Not right now, Urshu. I've got an idea.":

                vivi neutral "Not right now, Urshu. I've got an idea."
                urshu neutral "Whatever for?"
                vivi neutral "To get off this ride."

                #JUMP TO: urshu neutral "Miss Sanssouci..."
    
    urshu neutral "Miss Sanssouci..."
    vivi neutral "Don't \"Miss Sanssouci\" me. I wanna make a deal with you in exchange for my freedom. I want to give you something you haven't had in recent memory."


    # <CHOICE> 
    vivi "Something that..."

    menu:
        # OPTION 1
        "Reminds you of your lost love.":

            vivi neutral "Reminds you of your lost love." 
            show urshu angry blush
            urshu "Don't you dare claim you can do such a thing."
            show urshu sad -blush
            urshu sad "I cannot hope for what I know is impossible."
            vivi sad "Ursh... I'm sorry. I didn't mean..." 

            show vivi neutral at left :
                xzoom -1

            vivithinking "M'kay. Time to take a risk." 
            vivi neutral "I did overhear you before coming up to you. You wished you could dance with someone?"
            urshu neutral "Yes. But there are other ways to dance. Other senses to entwine and tango with."

            # JUMP TO: urshu "Take this coffee, for instance."

        # OPTION 2
        "Takes you back to your first days ferrying souls.":

            vivi neutral "Takes you back to your first days ferrying souls."
            vivithinking "Maybe I can get him to tell me more about the Ouroboros Express."
            urshu neutral "I remember those days fondly, yet they offer nothing more for me. Most immortals like myself have a near-perfect memory, so there is little to re-experience."
            urshu neutral "Nothing to regret in those ancient libraries of my mind, just as there is nothing to regret here in the present, even if there is what you humans call \"redundancy.\""
            # JUMP TO: urshu "Take this coffee, for instance."

    urshu neutral "Take this coffee, for instance. I have it at the same time every day. The same coffee. The same luxurious, velvety liquid flooding over my tongue with its smooth splash. It dances down my throat, indeed, down into my being."
    vivithinking "That's...kinky."
    urshu happy "I long to have this feeling consume me in my totality, even if it is the same sensation each time. Don't you wish that, sometimes? To be absorbed in a bliss so powerful and certain that nothing else can shake it."
    vivi neutral "..." 
    vivithinking"He seems enthralled with his senses. That's something he craves. What could possibly..."
    vivi happy "Urshu, has anyone ever made you a meal? Like a whole, cooked-from-scratch meal?"
    show urshu neutral blush
    urshu "You know, I cannot recall..."

    show vivi happy at left:
        xzoom -1

    vivithinking happy "Got him! Now, for the bargain."
    vivi happy "I can give you that!" 
    vivi neutral "BUT I won't do it for free."
    show urshu neutral -blush
    urshu neutral "Oh? You think you can prepare a meal worthy of an exit ticket? My dear, there is no forthcoming terminus on a train that leads to life beyond. Not for you or anyone."
    vivi neutral "I don't believe that. You aren't beholden to some greater deity or being. You're Urshunabi, god of the passages between life and death. You have real power. You can, as you say, sense my soul steps. That's not something anyone without power or influence can do."
    vivi angry "So I'm gonna make you a fucking feast worthy of 10 exit tickets, and you're gonna get me off this damned train. Deal?"
    stop music fadeout 5.0
    urshu neutral "..."
    urshu happy "Very well, then. I will let you off this train if this meal TRULY is the best-tasting one I ever try." 
    urshu neutral "I look forward to whatever you produce."

    hide urshu with dissolve
    show vivi happy at left

    vivithinking "Yes! Nailed it! Time to blow his mind and taste buds!"

    show vivi neutral at left

    vivithinking "But what would he even like? I only get one shot at this, so it has to be right."

    hide vivi with dissolve
    stop ambience fadeout 1.0
    # JUMP TO: Character Selector 1
    jump bargaining_cs1