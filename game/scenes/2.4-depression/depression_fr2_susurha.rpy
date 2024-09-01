# The scene starts here.

label depression_fr2_susurha:

    # FREE ROAM 2 - Susu'Rha (DEPRESSION)

    # LOCATION: observatory
    scene observatory with fade

    show susurha sad at right with dissolve

    vivithinking "Susu'Rha looks like they're holding up about as well as me."
    susurha "The stars are out tonight. As beautiful and endless as the night I left home."

    show vivi neutral at left with dissolve:
        xzoom -1

    susurha "Ah. Vivacious Vivi. What brings you to me in these final moments?"

    # ??DECAY (DECAY ROUTE?)
    if dec_meter >= 50:
        play sound decchoice
        vivi "Don't know. You're not boring."
        jump dep_fr2_susu_end
    #END

    # <CHOICE>
    vivi "I wanted to see you because...."
            
    menu:
        #OPTION 1 +ATTRACTION
        "I didn't want to be alone.":

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "I didn't want to be alone."
            susurha "I very much hoped you'd come."
            vivi "Is it okay if I stay here?"
            susurha "Please do."
            #JUMP TO: vivithinking "It feels so warm being next to them."
        
        #OPTION 2 >>ATTRACTION +ATTRACTION
        "I also needed to see a friendly face." if att_meter_susurha >= 50:

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])
                
            vivi "I also needed to see a friendly face."
            show susurha happy blush with dissolve
            vivi "..."
            show susurha neutral -blush
            susurha neutral "Please... sit with me."
            # JUMP TO: vivithinking "It feels so warm being next to them."

        #OPTION 3 >>DECAY +ATTRACTION
        "I don't...know why." if dec_meter >= 40:

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "I don't...know why."
            susurha "I wish you knew, but I'll take it."
            susurha "Thank you for your honesty."
            vivi "Is it okay if I stay here?"
            susurha "Yes."
            # JUMP TO: vivithinking "It feels so warm being next to them."

    vivithinking "It feels so warm being next to them."
    vivithinking "I could almost fall asleep right here."

    # ??DECAY
    if dec_meter >= 45:
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

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "I don't want to go."
            susurha sad "Yeah..."
            # JUMP TO: susurha "So you ARE afraid?"

    # <CHOICE>
    susurha "So you ARE afraid?"

    menu:
        #OPTION 1 +ATTRACTION
        "Yes.":

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "Yes."
            vivi "I'm very afraid."
            vivi "Who wouldn't be?"
            # JUMP TO: susurha "Well, I know I am."

        #OPTION +DECAY
        "No.":

            play sound decchoice
            $ dec_meter += int(dec_max_depression / dec_num_depression)

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
    vivi sad "That sounds awful."
    susurha sad "I ran away from home because I was afraid I would never get to live the life I wanted to."
    susurha sad "Now I'm afraid that thing, void of life, is my fate. Ceasing to exist..."
    susurha sad "I don't want to cease to exist."
    susurha sad "I want to be ME."

    # <CHOICE>
    vivithinking "I want to be me!"

    menu:
        #OPTION 1 +ATTRACTION
        "I want to be ME as well.":

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "I want to be ME as well."
            vivi "My whole life... I felt I was living someone else's life."
            vivi "Think like someone else. Act like someone else."
            vivi "I'm afraid I've missed my chance to be me."
            susurha "Right here, right now, you are you."
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."
                

        #OPTION 2 >>DECAY +ATTRACTION
        "I get what you mean." if dec_meter >= 45:

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "I get what you mean."
            susurha "You do?"
            vivi "My whole life, everyone has said \"Vivi, just be yourself!\""
            vivi "I don't think I ever understood what that meant."
            susurha "Right here, in this moment of vulnerability, you are you."
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

        #OPTION 3 >>ATTRACTION +ATTRACTION
        "Nothing can take away who you are." if att_meter_susurha >= 60:

            play sound attchoice
            $ att_meter_susurha += int(att_max_depression_fr2 / att_num_list_susurha[5])

            vivi "Nothing can take away who you are."
            vivi "You're one of the most unique creatures I have ever met."
            vivi "There aren't many poet-musicians druids that were once heir to a throne, but chose to not take that power so that they could be THEMSELVES."
            vivi happy blush "You are truly one of a kind."
            show susurha happy blush with dissolve
            susurha "STOP... You flatter me, Vivienne."
            susurha "Nothing can take away who you are either."
            show susurha happy -blush
            # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

        #OPTION 4 >>DECAY +DECAY
        "I know who I am." if dec_meter >= 50:

            play sound decchoice
            $ dec_meter += int(dec_max_depression / dec_num_depression)

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
    if dec_meter >= 50:
        susurha "I hope I brought some worth to you."
    #END

    susurha "The only thing worse than being alone is never being at all."

    label dep_fr2_susu_end:

        #DECAY ROUTE (??DECAY)
        #SAL'S NOTE: Lines below are supposed to be a DECAY ending of the scene.
        if dec_meter >= 50:
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
        else:
            vivi "We can sit here for a little while longer."
            vivi "And watch the cosmos fly by."
            show susurha neutral blush with dissolve
            susurha "I'd love that."
            vivithinking "In its own strange way, the view sure is beautiful from here."
        # END

        #JUMP to Debrief Depression
        jump depression_debrief