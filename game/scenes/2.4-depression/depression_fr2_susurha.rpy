# The scene starts here.

label depression_fr2_susurha:

    # FREE ROAM 2 - Susu'Rha (DEPRESSION)

    # LOCATION: observatory
    scene observatory with fade

    show susurha sad at right with dissolve

    vivithinking "Susu'Rha looks like they're holding up about as well as me."
    susurha "The stars are out tonight. As beautiful and endless as the night I left home."

    show vivi neutral at left with dissolve

    susurha "Ah. Vivacious Vivi. What brings you to me in these final moments?"

    # ??DECAY (DECAY ROUTE?)
    vivi "Don't know. You're not boring."
    #END

    # <CHOICE>
    vivi "I wanted to see you because...."
            
    menu:
        #OPTION 1 +ATTRACTION
        "I didn't want to be alone.":

            vivi "I didn't want to be alone."
            susurha "I very much hoped you'd come."
            vivi "Is it okay if I stay here?"
            susurha "Please do."
            #JUMP TO: vivithinking "It feels so warm being next to them."
        
        #OPTION 2 >>ATTRACTION +ATTRACTION
        "I also needed to see a friendly face.":
                
            vivi "I also needed to see a friendly face."
            show susurha happy blush with dissolve
            vivi "..."
            show susurha neutral -blush
            susurha neutral "Please... sit with me."
            # JUMP TO: vivithinking "It feels so warm being next to them."

        #OPTION 3 >>DECAY +ATTRACTION
        "I don't...know why.":

            vivi "I don't...know why."
            susurha "I wish you knew, but I'll take it."
            susurha "Thank you for your honesty."
            vivi "Is it okay if I stay here?"
            susurha "Yes."
            # JUMP TO: vivithinking "It feels so warm being next to them."

    vivithinking "It feels so warm being next to them."
    vivithinking "I could almost fall asleep right here."

    # ??DECAY
    vivithinking "Why do I feel this way?"
    susurha "Even with all the druidic teachings in my life..."
    susurha "The space out there seems so peaceful in all its chaos."
    susurha "It feels so welcoming..."
    susurha "Yet I can't trust it."
    susurha "Do you think it will hurt..."
    susurha "...when we merge with the cosmic weave?"
    #END

    #<CHOICE>
    susurha "Will we know when we're gone?"

    menu:
        #OPTION 1 
        "We'll never know until it happens.":

            vivi "We'll never know until it happens."
            susurha "That's what I'm afraid of."
            # JUMP TO: susurha "So you ARE afraid?"

        #OPTION 2 +ATTRACTION
        "I don't want to go.":

            vivi "I don't want to go."
            susurha sad "Yeah..."
            # JUMP TO: susurha "So you ARE afraid?"

    # <CHOICE>
    susurha "So you ARE afraid?"

    menu:
        #OPTION 1 +ATTRACTION
        "Yes.":

            vivi "Yes."
            vivi "I'm very afraid."
            vivi "Who wouldn't be?"
            # JUMP TO: susurha "Well, I know I am."

        #OPTION +DECAY
        "No.":

            vivi "No."
            vivi "What's the point in being afraid?"
            vivi "You cease to be, and it's lights out. Poof."
            susurha "Your confidence feels as if it is made of glass."
            # JUMP TO: susurha "Well, I know I am."

        #OPTION 3
        "...":

            vivi "..."
            # JUMP TO: susurha "Well, I know I am."

    susurha "Well, I know I am."
    susurha sad "..."
    susurha neutral "That abomination that stalks me..."
    susurha "I've tried to talk to it. Reason with it. Understand its motives."
    susurha "I thought it chose to not speak to me when I begged for it to free me, but I realize now that it never had a voice to begin with."
    susurha "Its body is chained at the wrists and ankles, making it unable to move."
    susurha "Its eyes, blinded so that it couldn't see a path ahead."
    susurha "Its mouth, muzzled so that it can never express thoughts."
    vivi sad "That sounds awful"
    susurha sad "I ran away from home because I was afraid I would never get to live the life I wanted to."
    susurha sad "Now I'm afraid that thing, void of life, is my fate. Ceasing to exist..."
    susurha sad "I don't want to cease to exist."
    susurha sad "I want to be ME."

    # <CHOICE>
    vivithinking "I want to be me!"

    menu:
        #OPTION 1 +ATTRACTION
        "I want to be ME as well.":

            vivi "I want to be ME as well."
            vivi "My whole life... I felt I was living someone else's life."
            vivi "Think like someone else. Act like someone else."
            vivi "I'm afraid I've missed my chance to be me."
            susurha "Right here, right now, you are you."
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."
                

        #OPTION 2 >>DECAY +ATTRACTION
        "I get what you mean.":

            vivi "I get what you mean."
            susurha "You do?"
            vivi "My whole life, everyone has said \"Vivi, just be yourself!\""
            vivi "I don't think I ever understood what that meant."
            susurha "Right here, in this moment of vulnerability, you are you."
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

        #OPTION 3 >>ATTRACTION +ATTRACTION
        "Nothing can take away who you are.":

            vivi "Nothing can take away who you are."
            vivi "You're one of the most unique creatures I have ever met."
            vivi "There aren't many poet-musicians druids that were once heir to a throne, but chose to not take that power so that they could be THEMSELVES."
            vivi happy blush "You are truly one of a kind."
            show susurha happy blush with dissolve
            susurha "STOP... You flatter me, Vivienne."
            susurha "Nothing can take away who you are."
            show susurha happy -blush
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

        #OPTION 4 >>DECAY +DECAY
        "I know who I am.":

            vivi "I know who I am."
            susurha "Are you sure about that?"
            susurha "This whole time that I've interacted with you, it has always felt like I was talking to a mirror that bends and flows with the wind."
            vivithinking sad "This son of a..."
            susurha "I told you the thing that stalks me. Tell me, what does the thing that haunts you appear as?"
            vivi sad "It's... I can't tell you. It's personal"
            susurha "Oh. As I thought."
            #JUMP TO: susurha "Thank you for staying with me, if even for a moment."

    susurha "Thank you for staying with me, if even for a moment."

    # ??DECAY
    susurha "I hope I brought some worth to you."
    #END

    susurha "The only thing worse than being alone is never being at all."

    #DECAY ROUTE (??DECAY)
    #SAL'S NOTE: Lines below are supposed to be a DECAY ending of the scene.
    vivi "Everything will turn out for the best."
    susurha "You lie to yourself so easily."
    susurha "I hope there is someone behind that mask."
    susurha "Even if you don't show them to me."
    vivithinking "I..."
    vivithinking "I think I have had enough of this."
    vivi "Good night."
    susurha "Rest easy, Vivi."
    # END

    #SAL'S NOTE: Lines below show if decay is NOT high
    # ELSE
    vivi "We can sit here for a little while longer."
    vivi "And watch the cosmos fly by."
    show susurha neutral blush with dissolve
    susurha "I'd love that."
    vivithinking "In its own strange way, the view sure is beautiful from here."
    # END

    #JUMP to Debrief Depression
    jump depression_debrief


    # Debrief Depression

    # # LOCATION: cabin

    # #??ATTRACTION

    # show vivi neutral at left

    # # SOUND knocking

    # show urshu neutral at right

    # urshu neutral "I trust you had a good evening?"

    # vivi happy "Yeah, it was nice."
    # vivi neutral "About what you said before. Writing my own story... I think I'm starting to understand."
    # urshu happy "I live to serve, Miss Sanssouci."
    # vivi neutral "You know you're a cosmic entity, right? No need to be so formal with me."
    # urshu happy "As you wish."
    # vivi neutral "Hey Urshu, before you go, can I ask you something?"
    # vivi neutral "Why'd you put us four together?"
    # urshu happy "Maybe it was preordained. Maybe it was random. Or maybe, I think you four just fit together. I do love puzzles after all."
    # vivi neutral "You've been quite the conductor, Urshu."
    # urshu neutral "And you have been quite the puzzle."
    # urshu neutral "Enjoy your final night here."
    # vivi sad "It's really ending, huh?"
    # urshu happy "All may not be as lost as you think."
    # vivi happy "Goodnight, Urshu."
    # Urshu happy "Goodnight, Vivienne."
    # vivithinking neutral "My mind is buzzing. I need to write."
    # # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH

    # #Journal entry with attraction meter high
    # Wow. At the beginning of all this, I would've never thought I'd get to know some of the other passengers this well. We're all more similar than I thought. Even Urshu, believe it or not. Time is weird here. I feel like I've been riding this train for ages, but I think I finally understand this place. It's a lot to process, but I'm glad I didn't have to do it alone.


    # #NOTE: SCENE VARIATION IF DECAY IS HIGH
    # show vivi neutral at left

    # # SOUND Knocking on door

    # show urshu neutral at right

    # urshu neutral "I trust you had a good evening?"
    # vivi neutral "It was fine. I am glad this is ending though."
    # urshu surprised "Oh? Do tell."
    # vivi neutral "I was scared at first. Of changing, of the unknown, of leaving my past behind..."
    # vivi neutral "I'm not anymore."
    # urshu neutral "And what changed?"
    # vivi neutral "Nothing. I guess I realized wherever I'm going can't be worse than here."
    # vivi angry "The more I talk to the people on this train the more I realize how much I hate it here. I'm not myself anymore. You took that from me. I've withered away just like this train."
    # vivi angry "I don't even recognize myself in the mirror. I can't tell if I've physically changed or if my perception of self has warped. My thoughts... they're not entirely my own anymore."
    # vivi angry "The only thing I had were my thoughts!"
    # urshu sad "I'm sorry you feel that way."
    # vivi angry "And I'm sorry I wasn't your perfect little plaything to be experimented on!"
    # vivi neutral "I will thank you for one thing: You've pushed me beyond all knowable limits. Now I can guarantee I'll be ready for anything in the next life."
    # urshu neutral "Thank you for the feedback. Goodnight, Miss Sanssouci."

    # hide urshu

    # vivithinking neutral "I should write whatever thoughts I have left. By tomorrow, I'm not sure they'll be mine."

    # # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH

    # # Journal entry with degradation meter high
    # I can't take this anymore. There's something growing inside me. A hunger I, we can't explain. What is happening to us? This is the conductor's fault. He's behind everything. The other passengers too. They must be working with him. None of them feel the way we do. They're all out to get us. We won't go. Not like this. They'll see.

