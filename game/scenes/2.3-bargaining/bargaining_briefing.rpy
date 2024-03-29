# The scene starts here.

label bargaining_briefing:

    #Briefing Bargaining

    # LOCATION: cabin
    scene cabin with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    # SOUND: vivi yawns 
    # skipping

    vivithinking "God, what time is it? Why don't I feel rested?"

    show vivi happy at left

    vivithinking "You know what? Not! This time, I'm going to turn the tables on Urshu. Yeah, that's right. I'll surprise him before he's had his fabuloso-lime-expresso and see how he feels!"

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

                # LOCATION: lounge
                scene lounge with fade

                show vivi neutral at left with dissolve:
                    xzoom -1

                vivithinking "Welp. He isn't here. Nobody's here."
                vivithinking "Wait...what is..."
                show vivi surprised

                # VISUAL: rainbows flash around the room
                scene lounge with flash
                scene lounge with flash
                scene lounge with flash
                # VISUAL: a black vignette closes in on the room
                show lounge blur with dissolve
                # SOUND: Screams, scary cosmic horror shit
                play sound horror
                pause 3.0

                vivithinking surprised "Yeah, I'm out."

                hide vivi with dissolve

                stop sound fadeout 1.0

                scene cabin with fade

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
                vivi surprised "What the--"
                # VISUAL: a shadow appears over vivi's face
                # CUE FOR VA: vivi is possessed here, speaking with a voice that is not her own
                vivithinking "Something just stopped by the window."
                vivithinking "That shape! A human figure like a big round head."
                vivithinking "No. It can't be human."
                vivithinking "Damn, it's looking at me!"
                vivi "W-what do you want? Leave me alone!"
                # VISUAL: shadow disappears
                vivi surprised "What the hell!? It's gone."
                vivi surprised "I gotta get off this train. I gotta find Urshu."

                hide vivi with dissolve

                scene cabin with fade

                show vivi neutral at left with dissolve:
                    xzoom -1

                # JUMP TO: vivithinking "Where should I look for that little peach?"
                jump search_urshu


            # OPTION 3
            "I'd bet he's at the bar.":

                vivithinking "I'd bet he's at the bar. Polishing spoons and staring at his reflection, that little twerp."

                # LOCATION: dining car
                scene diningcar with fade

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
    play sound glassclink
    pause 5.0
    stop sound fadeout 1.0

    vivi neutral "You... Of course, you knew." 
    vivi neutral "Thanks for this, Ursh. You take good care of me. When you're not being a petulant pissant."
    urshu happy "I appreciate that, Miss Sanssouci. I do work very hard for all of you."
    urshu happy "It is my joy to serve--not only to serve, but to draw out of each of you your very best."
    vivithinking "Oh, he's being sweet. And candid. And not talking in riddles!"

    show vivi angry at left:
        xzoom -1
    
    vivithinking "Focus, Vivi. Think about your goal. Now, how should I go about this?"

    show vivi neutral at left

    vivithinking "I need to be delicate. I should go in with tact and poise and--"
    vivi angry "Urshu, I want my fucking life back!"
    vivi neutral "Yes, I have distractions and good people and tasty espresso--and you here to spice up my life..."
    vivi angry "But I look out of these windows, and all I see is death!"
    vivi sad "I want off this train. Ideally, I want everyone to get off and get back to their lives. I'll do anything to make it happen."
    urshu neutral "Miss Sanssouci..."
    vivi neutral "Don't \"Miss Sanssouci\" me. I wanna make a deal with you in exchange for my freedom. I want to give you something you haven't had in recent memory."

    # <CHOICE> 
    vivi "Something that..."

    menu:
        # OPTION 1
        "Reminds you of your lost love.":

            vivi neutral "Reminds you of your lost love." 
            show urshu angry blush with dissolve
            urshu "Don't you dare claim you can do such a thing."
            show urshu sad -blush
            urshu sad "I cannot hope for what I know is impossible."
            vivi sad "Ursh... I'm sorry. I didn't mean." 

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
            urshu neutral "I remember those days fondly, yet they offer nothing more for me. Most immortals like myself have a near-perfect memory, so there is little to re-experience. Nothing to regret in those ancient libraries of my mind, just as there is nothing to regret here in the present, even if there is what you humans call \"redundancy.\""
            # JUMP TO: urshu "Take this coffee, for instance."

    urshu neutral "Take this coffee, for instance. I have it at the same time every day. The same coffee. The same luxurious, velvety liquid flooding over my tongue with its smooth splash. It dances down my throat, indeed, down into my being."
    vivithinking "That's...kinky."
    urshu happy "I long to have this feeling consume me in my totality, even if it is the same sensation each time. Don't you wish that, sometimes? To be absorbed in a bliss so powerful and certain that nothing else can shake it."
    vivi neutral "..." 
    vivithinking"He seems enthralled with his senses. That's something he craves. What could possibly..."
    vivi happy "Urshu, has anyone ever made you a meal? Like a whole, cooked-from-scratch meal?"
    show urshu neutral blush with dissolve
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
    urshu neutral "..."
    urshu happy "Very well, then. I will let you off this train if this meal TRULY is the best-tasting one I ever try." 
    urshu neutral "I look forward to whatever you produce."

    hide urshu with dissolve
    show vivi happy at left

    vivithinking "Yes! Nailed it! Time to blow his mind and taste buds!"

    show vivi neutral at left

    vivithinking "But what would he even like? I only get one shot at this, so it has to be right."

    hide vivi with dissolve

    # JUMP TO: Character Selector 1
    jump bargaining_cs1