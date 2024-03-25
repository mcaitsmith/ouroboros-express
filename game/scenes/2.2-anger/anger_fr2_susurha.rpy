# The scene starts here.

label anger_fr2_susurha:

    #FREE ROAM 2 - SUSU'RHA

    # LOCATION: dining car
    scene diningcar with fade

    show vivi neutral at left with dissolve
    show susurha neutral at right with dissolve
        
    vivi neutral "Susu'rha! My second favorite Gecko behind the Geico guy! Care to play some darts?"
    susurha neutral "What is \"Geico\"? And what exactly is this...\"darts?\""
    vivi neutral "You toss pointed sticks at that round board over there. You score points based on how well you hit the target, and if you score enough points, you win."
    susurha happy "In the Viridian Wood, we played a game similar to this. Instead of a round board, we used the carcasses of Burrowers."
    vivithinking "And that's what happens when you don't have a TV." 
    susurha neutral "And we used magic to increase our accuracy."
    vivithinking neutral "Well then, nice of you to be born in a magical world."

    # <CHOICE>
    susurha neutral "Doubtful you could best me in a contest of accuracy." 

    menu:
    # OPTION 1 +ATTRACTION
        "The arrogance on this one. I'd sure love to shut them up.":

            vivithinking "The arrogance on this one. I'd sure love to shut them up."
            vivi neutral "Magic or not, I'm gonna beat you."
            susurha neutral "I will give you the grace of going first."

            # SOUND: dart hits the board

            vivi happy "Bullseye!"
            susurha angry "Bullseye?!"
            vivi happy "A bullseye is when you hit the dartboard dead center."

            # SOUND: dart hits the board

            susurha happy "Mine hit close, does that count for something?"
            vivi happy "Not as much as a bullseye!"
            susurha surprised "Hmm... seems my magic doesn't work here."
            vivi happy "Either that, or I'm better at darts than you."
            # JUMP TO: susurha neutral "In that case, thank you for not patronizing me by pretending to be something you're not -- in this case, inadequate at this darts game."



    # OPTION 2 +DECAY
        "Clearly, they're insecure. I'm gonna let them win.":

            vivithinking "Clearly, they feel insecure. I'm gonna let them win."
            vivi neutral "You go first."
            
            # SOUND: dart hits the board

            susurha happy "Bullseye! Oh, how simple!"
            susurha happy "No wonder you humans enjoy this."
            
            # SOUND: dart hits the board and then the floor

            vivi angry "Urghhh. Stupid dart."
            susurha happy "Am I supposed to believe that you can't hit the board from this distance?"
            vivi neutral blush "..."
            vivi neutral "Sorry. It seemed like you could use a win. After being banished from your kingdom, and well, dying."
            susurha neutral "Actually, I banished myself." 
            # JUMP TO: susurha neutral "In that case, thank you for not patronizing me by pretending to be something you're not -- in this case, inadequate at this darts game."

    susurha neutral  "In that case, thank you for not patronizing me by pretending to be something you're not -- in this case, inadequate at this darts game."

    # SOUND: dart hits the board

    vivi neutral "You're...welcome." 
    susurha neutral "..."
    susurha surprised "Vivienne. You seem almost relaxed."
    vivi happy "I am. For a moment I almost forgot how I got here."
    susurha neutral "How did you get here?"

    # <CHOICE>

    menu:
    # OPTION 1 +ATTRACTION
        "It was an assignment given to me by my agent.":

            vivi neutral "It was an assignment given to me by my agent. She told me to write an exposé about a mysterious train line with an enigmatic conductor."
            vivi happy "I said yes because it reminded me of those internet horror stories I grew up with."
            vivi neutral "Seems like the stories swirling around the Ouroboros Express were more than just stories."
            vivi sad "Now I'm dead..."
            show susurha sad
            vivi sad "I'm going to miss living."
            susurha sad "Vivienne. I'm so sorry, my dear. But you cannot blame yourself for this travesty."
            # JUMP TO: susurha neutral "The fault lies with your "agent.""

    # OPTION 2 +DECAY
        "I didn't have a choice.":

            vivi angry "I didn't have a choice."
            susurha neutral "Do tell."
            vivi angry "I'm a reporter. I go where the story is."
            vivi sad "What a silly reason to die."
            susurha sad "Oh, Vivienne. I'm sorry. "
            susurha neutral "But you must remember that you did not come here on your own. Someone told you to come."
            # JUMP TO: susurha neutral "The fault lies with your \"agent.\""

    susurha neutral "The fault lies with your \"agent.\""
    vivi neutral "Yeah. It does."

    # SOUND: dart hits the board

    susurha neutral "Why don't you envision your \"agent\" being at the target's center?"
    vivi happy "Okay!"
    susurha neutral "Now, hold that dart firmly in your hand."
    susurha neutral "Concentrate on the board. And see \"Chloe\"..."
    susurha neutral "...Now, let go."

    # <CHOICE>
    vivithinking "Chloe..."
    menu:
    #OPTION 1 +DECAY
        "Pierce Chloe!":

    # mica, I believe the above is an action rather than something vivi says. Same w/ option 2

            vivi angry "Pierce Chloe!"
            vivi angry "It's all her fault!"
            vivi angry "HER!"
            vivi angry "SHE had to discover this \"exclusive story.\""
            vivi angry "SHE had to get me to come here!"
            vivi angry "SHE killed me!"
            vivi angry "It's HER FAULT!"
            # VISUAL: the screen shakes
            susurha happy "You got a bullseye!"
            vivithinking neutral "God, I'm out of breath!"
            susurha neutral "Thank you, Vivienne. I hope you feel a bit better now."
            susurha neutral "Would you like to know what brought me here?"
            vivi neutral "*GASPS* Sure. *HEAVES* Why not."
            # JUMP TO: susurha sad "It was fear that brought me here."

    #OPTION +Attraction
        "Pierce the idea that it was her fault.":

            vivi neutral "Pierce the idea that it was her fault."
            # SOUND: dart hits the board
            susurha happy "Bullseye!"
            vivi sad "It's not her fault. It's mine."
            vivi angry "I was the master of my fate, and I chose to come here!"
            vivi sad "How galactically stupid."
            susurha neutral "Would you like to know what's even more galactically stupid?"
            # JUMP TO: susurha sad "It was fear that brought me here."

    susurha sad "It was fear that brought me here."
    susurha neutral "It was a night like any other. The stars were out in their most intense configurations, lighting the sky as the gods had always intended. All was quiet."
    susurha neutral "But then we heard rumbling in the distance."
    susurha neutral "Then there was smoke. So much of it. Everyone ran as fast as they could."
    susurha sad "That's when I saw it."
    susurha sad "My city, where my family had lived for hundreds of generations, besieged by Tellethor's great army."
    vivithinking surprised "Oh wow."
    vivi sad "What did you do?"
    susurha sad "I ran home."
    susurha angry "I thought that if I could just GET THERE, I could save them."
    susurha neutral "But the smoke was too much. None of us could see. I couldn't breathe."
    susurha neutral "Then...a sharp pain and...darkness."
    susurha sad "I woke up here."
    susurha angry "I have no idea whether my family--that I abandoned--is okay. My fear is I'll see them walk into this dining car, like me, wondering what happened."    
    susurha angry "If only I was there to protect them."
    susurha sad "They died because I abandoned them."

    # <CHOICE>

    menu:
    #OPTION 1 +Attraction
        "You did what you could. It isn't your fault.":

            vivi sad "You did what you could. It isn't your fault."
            susurha sad "Thank you. That means something."
            
            # SOUND: dart smacks the board
        
            vivithinking neutral "At least there's darts."
            vivi sad  "I'm going to miss taking pictures."
            susurha sad "I'm going to miss playing my lute under the stars."
            vivi sad "I'm going to miss internet forums. Seeing just the craziest, most nonsensical things that people would ever think to share with others."
            susurha happy "Sounds delightful."
            susurha happy "I'll miss sharing my singing voice with those who would listen."
            vivi happy "I'd love to hear your singing voice."
            susurha happy "I would happily sing for you."
            susurha sad "Quiet moments. I will miss them the most."
            vivi sad "I can't tell you the last time that I was alone with my thoughts. I was always busy."
            susurha sad "Perhaps now is a good time."
            vivi sad "..."
            # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    #OPTION +DECAY
        "We got a raw deal. Life is unfair.":

            vivi angry "We got a raw deal. Life is unfair."
            susurha angry "Certainly nothing about our present situation is fair."
            vivi angry "I HATE this train!"
            vivi angry "And the conductor. It's his fault we're here."
            susurha angry "He runs this place."
            vivi angry "He could let us off if he wanted."
            susurha angry "Instead, he toys with us for his own enjoyment. Only a devil behaves this way!"
            susurha sad "But there's nothing we can do."
            vivi angry "No. Perhaps that's the lesson."
            susurha "..."
            vivi "..."
            # JUMP TO: susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    susurha neutral "Well, this has been fun as always, but I wish to return to my cabin for some solitude."

    #VISUAL: susurha exits
    hide susurha with dissolve

    vivithinking "It's not a bad idea. I could use this time to reflect."
    vivithinking "I may not get many more chances."

    # JUMP TO: Debrief Anger
    jump anger_debrief

    # FREE ROAM 2 - AVA

    # # LOCATION: dining car

    # show vivi neutral at right

    # # SOUND: dart hitting the board

    # vivithinking neutral "I hear darts. Is that...Asha? Here already?

    # show ava angry at left

    # ava neutral: "Ah, bullseye. Game of darts, Vivienne? We hear your watering holes often host such competitions." 
    # vivi neutral: "Watering holes? You mean a pub?"

    # # SOUND: dart hitting the board 

    # ava neutral: "Good throw, Vivienne. But no such term exists on Soleos."
    # vivi happy blush: "Well, technically you could call it a watering hole. But we call it a pub...or a bar if they don't have Guinness."
    # vivi sad blush: "I miss my pub back home, but that's all. What was your home like?"
    # ava happy: "Though servants catered to us, people worshipped us...it was but an ornate patina, we were forbidden friendship and family. We lived in solitude."

    # # <CHOICE>
    # vivi surprised: "My God, that sounds..."

    # menu:
    #     # OPTION 1 +DECAY
    #     "Amazing.":
        
    #         vivi happy "Amazing. Peace and quiet? Now that's luxury."
    #         ava sad "No, Vivienne, perpetual loneliness. We would not wish that upon even our monarchy."
    #         # SOUND: dart hitting the board
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    #     # OPTION 2 +ATTRACTION
    #     "Awful.":
    #         vivi sad "Awful. I'm so sorry. I can't even begin to imagine."
    # show ava sad blush with dissolve
    #         ava "Thank you...that means more to us than you know."
    #         # SOUND: dart hitting the board
    # show ava happy -blush
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    #     #OPTION 3
    #     "Crazy.":
    #         vivi neutral "Crazy. Your life is like a rollercoaster!"
    #         ava neutral "A...rollercoaster?... We do not quite understand the meaning of this 
    #         word."
    #         vivi happy "It's something that moves quickly with lots of ups and downs."
    #         ava neutral "We...still struggle to grasp why you have this torture device, but 
    #         your meaning is clear."
    #         # SOUND: dart hitting the board
    #         # JUMP TO: ava happy "Another bullseye. Your turn, little one."

    # ava happy "Another bullseye. Your turn, little one."
    # vivi angry "I thought I asked you to stop calling me that."
    # ava sad "Oh, do not take offense at our term of endearment. We are warming up to you."
    # vivithinking angry "I'm feeling warm too. Hot blood's creeping up into my face. Ughhh. I gotta let this out...And THROW!"
    # # SOUND: dart hitting the board

    # # <CHOICE>
    # vivi angry blush "Well...it's still demeaning. I don't like it."

    # menu:
    #     #OPTION 1 + DECAY
    #     "But if you like it...":

    #         vivi happy blush "But if you like it...I guess I could get used to it."
    # show ava happy blush with dissolve
    #         ava "No. We never wish to offend you."
    #         vivithinking happy "I'll do anything she wants to spend some more time with 
    #         them...!"
    # show ava happy -blush
    #         # JUMP TO: vivi neutral "Sure. Anyways..."

    #     #OPTION 2 + ATTRACTION
    #     "Don't ever call me that again.":

    #         vivi angry "Don't ever call me that again. I don't like it. I'm not your pet."
    # show ava sad blush with dissolve
    #         ava "By Asha, we beg forgiveness. We never intended harm."
    #         vivi  "..." 
    #         vivi sad blush "It's...just...old memories. Sorry, I snapped."
    #         vivithinking angry "An ex-boyfriend called me 'little one' à la Yoda. Ugh!"
    # show ava sad -blush
    #         ava "There is no need to explain. We understand...Vivienne."
    #     # JUMP TO: vivi neutral "Sure. Anyways..."

    #     #OPTION 3 
    #     "My old roommates called me dildo.":

    #         vivi blush "My old roommates called me dildo. It's a...personal massage 
    #         device. For...relaxation?"
    #         ava happy "Oh! Those. The orgies after were most pleasureable!"
    #         vivi happy blush "Oh! I didn't know Soleos did...that."
        # show ava happy blush with dissolve
    #         ava "Perhaps our other customs might tempt you?"
    #         vivithinking surprised "Write this down. WRITE THIS DOWN!"
    #         # SOUND: dart hitting the board
        # show ava happy -blush
    #         # JUMP TO: vivi neutral "Sure. Anyways..."

    #     vivi neutral "Sure. Anyways..."
        
    # # <CHOICE>
    #     vivi neutral blush "I've been meaning to ask you:"

    # menu:
    #     # OPTION 1 + DECAY
    #     "What are your thoughts on our conductor?":

    #         vivi neutral "What are your thoughts on the conductor?"
    #         ava surprised "Ah, Urshu. A mystery."
    #         vivi "Personally...I think he's undead."
    #         ava surprised "A zombie?"
    #         vivithinking surprised "Wow, she almost sounded human for a sec."
    #         ava neutral "Why do you smile so?"
    #         vivi neutral "..."
    #         vivi happy blush "No reason!"
    #         ava neutral "I suppose humans do rank in the highest percentile for creatures who 
    #         smile without cause." 
    #         # JUMP TO: vivi neutral "How...interesting."    

    #     # OPTION 2 + ATTRACTION
    #     "What do you want to do with your time left?":

    #         vivi neutral "What do you want to do with your time left?"
    #         ava sad "..."
    #         ava neutral "Enjoy the view. We seldom saw nighttime. It is strange. Nice."
    #         vivi happy "It is pretty nice, huh." 
    # show ava happy blush with dissolve
    #         ava "We would enjoy spending more time talking with you."
    #         vivithinking surprised blush "BRRRRT BRRRTT! Flirt alert!!"
    # show ava happy -blush
    #         # JUMP TO: vivi neutral "How...interesting."    
    
    #     vivi neutral "How...interesting."
    #     # SOUND: dart hitting the board and dropping to the floor
    #     vivi angry "Aw shit. Dumbass dart."
    #     ava angry "We wish you would refrain from such vulgarity."
    #     vivi angry "If you really want to get to know me better, then deal! Like I do with your 
    #     ego."
        
    # # <CHOICE>
    #     ava angry "Hmph. And to think we ever considered you special..."


    # menu:
    #     #OPTION 1 +ATTRACTION +DECAY
    #     "Don't play games with me.":

    # vivi angry "Don't play games with me."
    # ava neutral "Ah. Because you lack skill at darts?" 
    # vivi angry "Look, you may have been some kind of big deal deity on Soleos, but we're all equals here on death row, you silly moose!"
    # # JUMP TO: ava blush angry "You dare speak to us with such impudence! 
    # Refer to us as Asha or not at all!"

    # #OPTION 2 +DECAY
    #     "I don't need you to think I'm special.":

    # vivi angry "I don't need you to think I'm special. Just because your crazy cult revered you doesn't mean that I'm going to, ass hat!"
    # # JUMP TO: ava blush angry "You dare speak to us with such impudence! Refer to 
    # us as Asha or not at all!"

    #         ava angry "You dare speak to us with such impudence! Refer to us as Asha or not at 
    #         All!"
    #         vivithinking "..."
    #         vivithinking "Nice one, Vivi, you handled that with all the grace of an ornery bull."
    #         vivi sad blush "I'm sorry. I didn't mean it. I'm just...in a crappy mood."
    #         ava sad "Please...go."
    #         vivithinking sad "Ugh! I messed up. Maybe they'll accept my apology 
    #         tomorrow..."

    # # JUMP TO: Debrief Anger

    # Debrief Anger

    # # LOCATION: cabin

    # # ATTRACTION ROUTE

    # show vivi neutral at left

    # vivithinking neutral "Well, that was...interesting. Didn't expect to get that deep with anyone on this train. I can't remember the last time I've been that open with anyone before."

    # vivithinking happy "It was kinda refreshing! I'm glad I'm not alone here. It's nice to be seen. Nobody wanting or expecting anything from me. Just two beings trying to understand each other."

    # vivithinking neutral "I should journal my thoughts."

    # # Journal entry with attraction meter high

    # Talking to the other passengers has helped put things into perspective. They're not so bad after all. I won't get off this train by fighting. I still need more info on the conductor. He's my ticket off this ride. He seems like one who'd appreciate an exchange for his aid. Maybe some of the other passengers can help me? We can maybe figure out together what Urshu would want from us...

    # # JUMP TO: Briefing Bargaining

    # # DECAY ROUTE

    # show vivi angry at left

    # vivithinking angry "I feel like the only one trying to get off this train. How are people content with playing silly card games when their lives are at stake? And the conductor! He knows he's messing with me and gets off on it."

    # vivithinking neutral "Take a deep breath, V. This isn't getting me anywhere."

    # vivithinking neutral "Fighting with everybody is obviously not gonna work. Maybe I can get what I want another way. Urshu is the key. He must want something."

    # vivithinking neutral "I should write."

    # # Journal entry with degradation meter high

    # This whole thing is pointless! That conductor... URG! I wanna strangle him and wipe that stupid smirk off his face. Talking to him is like solving a riddle. It's infuriating! Gotta find something on him. Maybe the others know a thing or two. There's gotta be some way to make Urshu help me. He seems like one who'd appreciate an exchange for his aid. 

    # # JUMP to Briefing Bargaining
