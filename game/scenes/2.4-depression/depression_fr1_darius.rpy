# The scene starts here.

label depression_fr1_darius:

    # FREE ROAM 1 - Darius
    # LOCATION: Lounge
    call check_overlay from _call_check_overlay_29
    scene lounge with fade

    show darius sad at right with dissolve
    show vivi happy at left with dissolve:
        xzoom -1

    vivithinking "Perfect. They're here."

    vivi happy "Just the sad cephalopod I wanted to see—"
    vivi sad "Oh. Sorry. Is...this a bad time?"
    darius sad "It's nothing."
    vivi angry "It's clearly {i}something{/i}, you clod."

    # <CHOICE>

    menu:

        # OPTION 1 +ATTRACTION
        "Darius. I could really use someone to talk with right now.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_depression_fr1 / att_num_list_darius[4])

            vivi neutral "Darius. I could really use someone to talk with right now."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            darius sad "I'm not sure that's such a good idea."
            vivi neutral "I do. I'd like your company."
            show darius surprised blush with dissolve
            darius "No one {i}likes{/i} my company. It's my specialty."
            vivi happy blush "Well, consider me the first."
            show darius surprised -blush

            # JUMP TO: vivi happy "So. What are we drinking?"

        # OPTION 2 +DECAY 
        "You just push everyone away, don't you?":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)

            vivi angry "You just push everyone away, don't you? Fine. We can wait for the inevitable in silence."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius surprised "I didn't mean to offend."
            vivi angry blush "You never do. So cold. You're practically an icicle."
            vivithinking "That flare of rage again. Good. Burn me."
            darius angry "Sitting alone is hardly me choosing to be cold to you."
            vivi angry blush "Well, you're not alone now. Deal with it."
        
    # JUMP TO: vivi happy "So. What are we drinking?"

    # OPTION 3 NEUTRAL
        "Is it {i}really{/i} nothing? Because it feels like something.":

            vivi neutral "Is it {i}really{/i} nothing? Because it feels like something."
            darius neutral "I promise you. Nothing that concerns you."
            vivi neutral "Just because it doesn't concern me directly doesn't mean I don't want to know what it is."
            darius surprised "It's just... I don't usually have a lot of back-and-forth conversations."
            vivi happy "Good news, Darius. You're having one."

            # JUMP TO: vivi happy "So. What are we drinking?"

    # consider adding ATTRACTION ROUTE and DECAY ROUTE options

    vivi happy "So. What are we drinking?"
    darius neutral "...You can't laugh."
    vivi surprised "Why would I?"
    show darius neutral blush with dissolve
    darius "My drink of choice. It's a bit unexpected."
    vivi surprised blush "Oh no— Should I prepare to be horrified? The tears of the damned? The blood of the innocent?"
    show darius surprised blush
    darius "N-No! Nothing like that. What you all must think of me..."
    vivithinking "That's the pinkest drink I've ever seen!"
    show darius happy blush
    darius "It's called a... Singapore Sling."
    vivi surprised "A... what? It looks like a tall glass of juice!"
    darius "I'll have you know it's much more than that, Ms. Sanssouci. It's actually a sophisticated gin cocktail with hints of bitters and Cointreau..."
    darius "...layered with cherry brandy and Bénédictine..."
    darius "...lime juice, pineapple juice, and grenadine, naturally..."
    vivi happy "Monsieur Wrecker, I can say with all honesty this is the happiest I've ever seen you."
    show darius sad -blush
    vivithinking "Umph. There's the rage again, but this time it's tempered by something. Pain? Sadness?"
    darius sad "Don't get used to it."
    darius neutral "I suppose I should ask you: what's {i}your{/i} poison?"
    darius sad "I'd rather not drink alone."

    #<CHOICE>
    menu:

        # OPTION 1 +ATTRACTION
        "I'll have what you're having, handsome.":

            play sound attchoice
            show attraction_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_depression_fr1 / att_num_list_darius[4])

            vivi happy blush "I'll have what you're having, handsome."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi "I could use a little fruity delight."
            darius surprised "I assure you, this drink is enough to knock you off your feet."
            vivi happy blush "Trust me, it'll take more than a juicebox to get me sauced."
            vivithinking "Oh, my. Cripes. That's strong."
            vivi neutral blush "Delicious!"
            darius surprised "You like it? I worried it might go right to your head."

            # JUMP TO: vivi happy "Never mind all that. How about a little {i}Never Have I Ever{/i}? A distraction to keep our spirits up!"
        
        # OPTION 2 +DECAY
        "I thought you {i}wanted{/i} to be alone. Pick a lane, won't you?":

            play sound decchoice
            show decay_icon at right with dissolve:
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_depression / dec_num_depression)
    
            vivi neutral "I thought you {i}wanted{/i} to be alone. Pick a lane, won't you?"
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius angry "Which is it? Do you want to drink with me and wallow in our mutual misery or do you want to needle me?"
            vivithinking "Agh. The flash. There's definitely pain here."
            vivi angry "Don't be so sensitive. We're all in the same...train."
            darius sad "Hmph. Just...here. What do you want to drink?"

            # JUMP TO: vivi happy "Never mind all that. How about a little {i}Never Have I Ever{/i}? A distraction to keep our spirits up!"

        # OPTION 3 NEUTRAL
        "Truthfully? I'm not much of a drinker.":

            vivi neutral "Truthfully? I'm not much of a drinker."
            vivi neutral "Hasn't been great for my family."
            darius surprised "Ah. I'm... sorry to hear."
            vivi neutral "Quite alright. How could you possibly have known?"
            vivithinking "I feel their doubt. They didn't want to trigger me."

            # JUMP TO: vivi happy "Never mind all that. How about a little {i}Never Have I Ever{/i}? A distraction to keep our spirits up!"

    vivi happy "Never mind all that. How about a little {i}Never Have I Ever{/i}? A distraction to keep our spirits up!"
    darius sad "Why not? Nothing else to do."
    vivi neutral "I'll start. Never have I ever... been in love."
    show darius surprised blush with dissolve
    darius "I... neither have I."
    darius "What happens now?"
    vivi neutral blush "I think that means we both drink."
    show darius neutral -blush
    darius neutral "Let's see..."
    darius neutral "Never have I ever..."
    darius sad "Apologized."
    vivi surprised "For what?"
    darius sad "For anything."
    darius sad blush "Except to you."
    vivithinking "Radiating off of them—that uncomfortable heat."
    darius neutral "Well? Surely you must drink to that. I know your kind is always apologizing. ...Whether it's warranted or not."
    vivi neutral "You're not wrong. You know—if you'd rather talk instead of just playing a game—"
    darius sad "I wouldn't."
    show darius neutral -blush
    darius neutral "In fact, perhaps it's time we leave. This lounge is feeling a bit small. Excuse me."

    # <CHOICE>
    hide darius with dissolve
    
    menu:
        # OPTION 1
        "(I wish I could have comforted him more...)":

            vivithinking sad "I wish I could have comforted him more..."

            # JUMP TO JUMP TO: Asha Susurha convo

        # OPTION 2
        "(I'm just spectacular at this. Still, not like he wanted my help.)":

            vivithinking neutral "I'm just spectacular at this. Still, not like he wanted my help."

            # JUMP TO JUMP TO: Asha Susurha convo
    

    #JUMP TO: Asha Susurha convo
    jump depression_asha_susurha