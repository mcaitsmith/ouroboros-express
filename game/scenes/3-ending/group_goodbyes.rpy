# The scene starts here.

label group_goodbyes:

    #group goodbyes

    # fade in

    # LOCATION: diningcar
    scene diningcar with fade
    
    show ava silhouette at left with dissolve:
        xzoom -1.0

    show darius silhouette at center with dissolve

    show susurha silhouette at right with dissolve
    
    show urshu neutral at right with dissolve
    show vivi sad at left with dissolve :
        xzoom -1

    vivi sad "Well, here comes the hard part."
    urshu sad "Perhaps it would aid you to think of easy goodbyes as far sadder than hard ones. No one who mattered to you should be easy to part with."
    vivi neutral "You know, that's not the dumbest thing you've ever said."
    urshu happy "Marvellous, then I must now leave you to your parting, as I have a few small things to prepare. Try not to be too sad, but if you are, remember tears are the diamonds of the soul!"
    vivi neutral "...And that is."
    urshu happy "I'll return momentarily. In the meantime, you'll find a bumper box of tissues under the bar 'designed for big weeps and unpleasant seeps.'"
    vivi surprised "{i}Gross.{/i}"
    vivi sad "But okay, I'm as ready as I'll ever be. Lets go."
    
    # urshu exits
    hide urshu with dissolve
    
    vivithinking sad "Who knew after just a few days it would be such a wrench to say goodbye."
    vivithinking neutral "There isn't much time. I'd better get myself together and make a start."
    
    #NOTE all options will be explored before continuing.

    $ goodbye1 = False
    $ goodbye2 = False
    $ goodbye3 = False

    label goodbye_choice:
        hide vivi with dissolve
        if goodbye1 == True and goodbye2 == True and goodbye3 == True:
            hide ava
            hide darius
            hide susurha
            with { "master" : Dissolve(0.5) }
            pause 1.0
            jump train_epilogue
        else:
            if not goodbye1:
                show ava silhouette at left with dissolve:
                    xzoom -1.0
            else:
                show ava neutral at left with dissolve:
                    xzoom -1.0
            if not goodbye2:
                show darius silhouette at center with dissolve
            else:
                show darius neutral at center with dissolve
            if not goodbye3:
                show susurha silhouette at right with dissolve
            else:
                show susurha neutral at right with dissolve

            # <CHOICE>
            if goodbye1 == False and goodbye2 == False and goodbye3 == False:
                vivithinking neutral "I know who to speak to first."
            else:
                vivithinking neutral "Who should I speak to next?"

            menu:
                # OPTION 1 
                "I need to say something to Asha." if goodbye1 == False:

                    $ goodbye1 = True

                    hide darius silhouette with dissolve

                    hide susurha silhouette with dissolve

                    vivithinking neutral "It's my last chance to bask in Asha's radiance. I need to tell her I'll miss that."

                    show ava silhouette at right with moveinright
                    show ava silhouette at right:
                        xzoom 1.0

                    # JUMP TO: Goodbye / Avatar of Asha
                    jump goodbyeava

                # OPTION 2
                "Time to say goodbye to Darius." if goodbye2 == False:

                    $ goodbye2 = True

                    hide ava silhouette with dissolve

                    hide susurha silhouette with dissolve

                    vivithinking neutral "I'll never eat calamari again after knowing him. One last chance to get him to crack a smile."

                    show darius silhouette at right with moveinright

                    # JUMP TO: Goodbye / Darius Wrecker
                    jump goodbyedarius

                # OPTION 3
                "Susurha... how do I even start this?" if goodbye3 == False:

                    $ goodbye3 = True

                    hide ava silhouette with dissolve

                    hide darius silhouette with dissolve

                    vivithinking neutral "There's a soft heart behind those shiny scales, but even they can't be relaxed right now."

                    show susurha silhouette at right with moveinright

                    # JUMP TO: Goodbye / Susu'Rha Balrinn
                    jump goodbyesusu
                    
                    
    label goodbyeava:
 
    hide susurha silhouette with dissolve

    hide darius silhouette with dissolve  
    show ava happy at right with dissolve
    show vivi happy at left with dissolve:
        xzoom -1.0
    
    vivithinking neutral "There she is, radiant as always. But today she really is glowing! Like a beacon in the darkness."
    vivi happy "Asha! I'm so glad you're here."
    ava neutral "Of course. We would not miss wishing you well. Though our conductor tells us your journey is to continue."
    vivi neutral "I think all our journeys will, somehow. Just in different places, and ways. And... I guess I decided I really like train food."
    ava happy "We are so pleased for you. Although, we will never understand the latter curious idiosyncracy."
    ava happy "But listen to me, Vivienne. For time is of the essence, and there is something we wish to impart."
    vivi surprised "Go ahead, I'm all ears."
    ava happy "Knowing you... it has changed us. Your determination. Watching as you discovered yourself. It has given us courage in return. Courage so that we..."
    ava surprised "We? No, no, so that {i}I{/i} can tell you this: from now on, we are Asha no more. {i}I{/i} am Ava. And I would like you to remember me, Vivi. As a friend."
    vivi surprised "Ava. That's a beautiful name. I'm so glad to meet you, Ava. I'll miss your brightness, but I'll never forget who you are."
    ava happy "Nor I you. But I will not take more of your time. There is precious little left."
    
    #JUMP TO goodbye_choice
    jump goodbye_choice
    
    
    label goodbyedarius:
 
    hide ava silhouette with dissolve
    hide susurha silhouette with dissolve
    show darius neutral at right with dissolve
    show vivi neutral at left with dissolve:
        xzoom -1.0
   
   
    vivithinking neutral "Here he is. He's standing tall. And there's a sense of peace around him. No... acceptance. It's easing my mind."
    darius neutral "I'm glad to see you. I wasn't sure if we'd have the chance to talk again."
    vivi neutral "Like I'd let you leave without saying goodbye."
    darius sad "You would be forgiven for wanting nothing more to do with me. I am... worthless. A murderer. Degraded beyond belief."
    darius neutral "But there is something about you, Vivi. Meeting you has taught me I can... must... be better. I must own these sins I carry with me, I can't pretend they mean nothing anymore."
    vivi neutral "I've done that?"
    darius neutral "You have been a witness. It matters more than you know."
    vivi neutral "Darius, I can't absolve the things you've done, but I believe accepting your past took more strength than you're letting on. As for your future... you have a lot to figure out on your own."
    vivi happy "But you know what? I think you'll get there. I hope you do."
    darius happy "I hope so, too. As ever, I appreciate the confidence... and your honesty."
    darius happy "Have a safe onward journey, friend."
    
    #JUMP TO goodbye_choice
    jump goodbye_choice
    
    label goodbyesusu:
 
    hide ava silhouette with dissolve
    hide darius silhouette with dissolve
    show susurha happy at right with dissolve
    show vivi at left with dissolve:
        xzoom -1.0
    
    vivithinking neutral "They're gazing out of the window. Right into that strange, haunting glow. Only they could look so peaceful in a moment like this."
    susurha happy "It's wondrous, isn't it? I don't know quite what it heralds, but I'm eager to find out."
    vivi neutral "Eager isn't the word I think I'd be using. You're not afraid of the great unknown?"
    susurha happy "Quite the contrary, I find myself intrigued by it. And knowing you has helped with that, Vivi."
    vivi surprised "Me? I don't know if I've embraced the unknown. I'm staying on this train... although I can't say how that will go. It just feels right."
    susurha happy "You've been true to yourself, but you're not overlooking the sacrifice that requires. That's what I've learned from you."
    susurha neutral "All my life, all I wanted was to be myself and live life on my own terms. But I overlooked the responsibility that comes with that."
    susurha happy "Here, in this place, you helped me take responsibility for my decisions and their consequences but... not to punish myself for things beyond my control."
    susurha happy "Now nothing binds me anymore. The past stays where it belongs."
    vivi happy "You feel free. That is wondrous, I'll give you that."
    vivi happy "I'm glad to have met you, Susu'Rha. A friend to the end."
    susurha happy "Ha! See? You are a poet. Farewell, Vivienne."
    
    #JUMP TO goodbye_choice
    jump goodbye_choice
