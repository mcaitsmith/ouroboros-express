# The scene starts here.

label depression_fr2_darius:

    # FREE ROAM 2 - Darius
    # LOCATION: observatory
    scene observatory with fade

    show darius sad at right with dissolve
        
    show vivi neutral at left with dissolve:
        xzoom -1

    darius sad "You're here."
    vivi neutral "Expecting me?"
    show darius sad blush with dissolve
    darius "I don't think I ever expected you."
    vivi surprised "Honestly, I...don't think I expected you, either."
    vivi "I can't say I've ever been in an observatory quite like this."
    show darius happy -blush
    darius happy "Beautiful, isn't it? The cosmos are alight tonight."
    darius "I could watch the stars swirl like this forever. I just might."
    vivi neutral "Surely you'd tire of them eventually. Everything bright burns out after a time."
    darius sad "Too right. Sometimes even {i}before{/i} their time."
    darius "I'm surprised you wanted to see me. If Urshu is to be believed, this is it. One last conversation before...well. I guess we'll see."

    # <CHOICE>

    menu:
        # OPTION 1 +ATTRACTION
        "There's so much more I want to learn about you.":

            play sound attchoice
            $ att_meter_darius += int(att_max_depression_fr2 / att_num_list_darius[5])

            vivi sad "There's so much more I want to learn about you."
            show darius surprised blush with dissolve
            darius "Surely not. I'm an open book."
            vivi happy blush "If you call {i}this{/i} being an open book then I shudder to imagine what closed off looks like."
            show darius happy blush
            darius "Heh. I suppose there's no harm in being open."
            show darius neutral -blush
            darius neutral "At least, there won't be any more consequences."

            # JUMP TO: vivi surprised "What do you mean by that?"

        # OPTION 2 +DECAY
        "I won't say it's been nice getting to know you.":

            play sound decchoice
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi neutral "I won't say it's been nice getting to know you."
            darius neutral "You {i}really{/i} don't mince words. I suppose I respect that."
            vivi neutral "There isn't a point. May as well say what we mean."
            vivi "There's still a lot I don't know about you. I'd like to unearth those truths."
            darius sad "You won't like it. Though, as you implied...it doesn't matter anymore."

            # JUMP TO: vivi surprised "What do you mean by that?"

        # OPTION 3 NEUTRAL
        "You think this is it? Really and truly? No más?":
        
            vivi surprised "You think this is it? Really and truly? No más?"
            darius neutral "No reason to think otherwise. May as well enjoy the void as best we can. Maybe even make some amends."

            # JUMP TO: vivi surprised "What do you mean by that?"

        # OPTION 4 >>ATTRACTION
        "I'm grateful my last moments are with you." if att_meter_darius >= 60:

            vivi neutral blush "I'm grateful my last moments are with you."
            show darius neutral blush with dissolve
            darius "You don't even know me."
            vivi happy blush "I know enough. You care deeply."
            show darius sad blush
            darius "Vivi."
            vivi happy blush "You feel deeply."
            show darius sad -blush
            darius sad "Vivi-"
            vivi happy blush "You want to make others happy."
            darius angry "VIVI."
            darius "Stop. Please... stop. I'm not that person. I'm {i}nothing like{/i} that person."
    
            # JUMP TO: vivi surprised "What do you mean by that?"

        # OPTION 5 >>DECAY
        "Do you see them, Darius?" if dec_meter >= 50:

            vivi neutral "Do you see them, Darius?"
            darius surprised "I do. You do, as well?"
            vivi neutral "I thought maybe they were nightmares. Something I hallucinated. But I see them clearly now."
            darius neutral "I have to ask... What do they look like?"
            vivi surprised "Why, don't you see them?"
            darius sad "It's different for everyone. Mine are long claws—outstretched fingers. Pointing directly at me."
            darius "At my heart."
            vivithinking "Terrifying."
            vivi neutral "I see... It's difficult to describe. An empty dress. Reflective surface. I see myself in the creases and folds. It draws me in."
            vivi "It wants to swallow me."
            darius sad "Ah. Guilt. I know it well."

            # JUMP TO: vivi surprised "What do you mean by that?"

    vivi surprised "What do you mean by that?"
    darius neutral "I'm not who you think I am, Ms. Sanssouci. Vivi."
    darius "I'm a monster. Worse, even, I'm a coward."
    vivi happy "Come on, now. You're too hard on yourself. I—"
    vivithinking "AH. Ah. This energy coming from him... It's like the worst migraine I've ever experienced, all at once."              
    darius angry "I'm responsible for the deaths of millions of sentient beings. {i}Millions{/i}."
    darius sad "I deserve to be crushed by those hands. I long for it."
    vivi surprised "I... I don't know how to respond."
    darius neutral "I'm not asking you to. I just want you to know who you're choosing to spend your time with."
    darius "I loved my god. I loved the Inquisition. I would have done anything for them. And I did. Frequently."
    vivithinking "Is it weird that I'm pulling out my notebook? Who is even going to read this...?"
    vivi neutral "Who were they?"
    darius neutral "I don't think a human tongue could say their name without considerable effort. They are ancient."
    darius sad "Eldritch."
    darius neutral "You may think of them as That Which Gathers. Or, perhaps— Za'deeh."
    vivi neutral blush "Your terrifying ancient eldritch god is a zaddy?"
    show darius surprised blush with dissolve
    darius "What? No! Their very gaze would melt your mind, much less your face! Put some respect on Za'deeh's name!"
    vivi happy blush "Listen, I get it. I'll always respect a zaddy when I see one."
    show darius happy blush
    darius happy blush "You... you are..."
    show darius happy -blush

    # <CHOICE>

    menu:
        # OPTION 1 +ATTRACTION
        "Adorable? Cute? A sassy lil' cupcake who you can't help but open up to?":

            play sound attchoice
            $ att_meter_darius += int(att_max_depression_fr2 / att_num_list_darius[5])

            vivi happy blush "Adorable? Cute? A sassy lil' cupcake who you can't help but open up to?"
            darius happy "You know what? Sure."
            vivi surprised blush "FINALLY! You admit it!"

            # JUMP TO: vivi neutral "Now. Let's get real."

        # OPTION 2 +DECAY
        "More open than you'll ever be?":

            play sound decchoice
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi sad "More open than you'll ever be?"
            darius sad "I suppose so. There's just— the weight. Of everything."
            vivi neutral "There you are."
        
            # JUMP TO: vivi neutral "Now. Let's get real."

        # OPTION 3 NEUTRAL
        "Just a gal in need of some company.":

            vivi neutral "Just a gal in need of some company."
            darius neutral "I'm happy to provide it."
            
            # JUMP TO:vivi neutral "Now. Let's get real."

    vivi neutral "Now. Let's get real."
    darius sad "Better late than never."
    vivi neutral "You said you were an Inquisitor?"
    darius sad "That's what I called myself."
    darius "My joy was in rooting out the faithless. In bringing them in to face judgment."
    darius "Across dimensions. Planes. Realities. No one could hide from me."
    darius "I found them. And brought them before my god. None could withstand their gaze."
    darius "They died. Or went mad. ...And I relished their fear."
    vivithinking "..."
    darius sad "Until one day. There was a couple. Human. Man and woman. No matter; I'd captured couples before."
    darius "But this one... something about them. Even as their minds broke before Za'deeh's baleful glare, they only thought of each other. Of what they meant to one another."
    darius surprised "They were unafraid to die. To be reduced to gibbering husks. As long as they were near each other."
    darius sad "I've been thinking about them for the last 500 years."
    darius neutral "Is that what you call \"love\"? That fearlessness? Certitude?"
    darius "Whatever it is, I knew that I'd never felt it. In any galaxy."
    vivi neutral "You didn't kill them, Darius. Your god did."
    darius sad "I appreciate you saying that. But you're wrong. I'm just as responsible."
    darius "I think that's why I'm here. Torment. It's a fitting punishment."
    darius neutral "Let's enjoy the stars together. At least one person has been witness to my unburdening. I thank you."
    vivithinking "Darius is... a monster. But not a remorseless one."

    # ??ATTRACTION
    if att_meter_darius >= 60:
        vivi neutral blush "You're not beyond redemption, Darius."
        darius surprised "After all that... You believe so?"
        vivi happy blush "I know so."
    # END

    # ??DECAY (ELSE)
    elif dec_meter >= 50:
        vivi sad "Darius...that's horrifying. I don't know that I can look at you the same way."
        darius sad "I know. I don't expect you to."
        darius sad "Let the horrors take me. It's what I deserve."
    # END

    # JUMP TO: Debrief Depression
    jump depression_debrief