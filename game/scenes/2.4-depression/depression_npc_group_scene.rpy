label depression_npc_group_scene:

    #LOCATION: bar
    # call check_overlay from _call_check_overlay_34
    scene diningcar with fade

    #SOUND: train
    #play sound train


    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking "Well, the lounge was pretty empty too. Wonder where everyone is? Maybe I’ll check out the bar."

    hide vivi

    show ava sad at left with dissolve:
        xzoom -1

    show darius sad at center with dissolve
    show susurha sad at right with dissolve

    hide ava with dissolve
    hide darius with dissolve
    hide susurha with dissolve

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking "Oh, wow! Here they are. Huh. The vibe is kinda off. I’ll hang back. Listen to what they’re talking about on our last night."

    hide vivi

    show ava sad at left with dissolve:
        xzoom -1

    show darius sad at center with dissolve
    show susurha sad at right with dissolve

    ava sad "By Mother Asha, we face oblivion soon; our icy shadow self beckons through the glass. What say you, thrall? Druid? What dark fate awaits you?"

    darius neutral "Perhaps time on this cosmic plane has changed me. Yesterday I wouldn’t have spoken about such matters freely. But now? Now I see the horror, Goddess."

    darius sad "My past. The weight of it descending upon me all at once."

    darius neutral "The guilt appears to me in the form of a giant disembodied hand. It points directly towards my heart. I hear something echo in my mind."

    darius sad "It says, {i}‘You did this. You. You. You.’{/i} And I know they’re right."

    darius neutral "I wish it would quiet."

    ava sad "What of you, Druid?"

    susurha sad "I’m trapped by chains reaching from what lays beyond."

    susurha sad "I’m unable to move. I’m unable to speak. I’m unable to see."

    susurha sad "I’m just..."

    susurha sad "...there."

    ava surprised "Such horrors! Let us speak of them no more."

    susurha neutral "What alternative would you suggest, Avatar?"

    ava sad "Regret. What else do the dying consider?"

    ava neutral blush "Regret teaches us harshly yet fairly. What stifled desires yet cling to the fringes of your minds?"

    darius neutral "Stifled desires... A seed of doubt sprouted in my heart hundreds of years ago. I regret not nurturing that seed. I tried to kill it by any means necessary."

    darius sad "I thought the doubt was a test of faith. Maybe it was. I still ended up here."

    darius neutral "As far as regrets– that is not how I view the universe. We must suffer the consequences of the choices we make, whether we are consumed by guilt or not."

    ava neutral "We notice you have avoided the thrust of the question."

    darius surprised "...so I have. You want to hear a true regret?"

    darius sad "I did not listen enough. I scraped thoughts and wrenched what I wanted from other sentients. But I did not truly hear what my victims were saying. Where would I be if I had?"

    darius sad blush "...I suppose I also wish I had tried ice cream on earth, or one of its parallel dimensions."

    susurha sad "Where would one honestly begin?"

    susurha sad "..."

    susurha sad "I regret not being there. For my family."

    susurha sad "But I regret not leaving sooner."

    ava sad blush "We regret not sharing Asha’s love with ourselves. Her light banishes shadows and sadness evaporates at her warm touch. Why did we not love ourselves more?"

    ava neutral "When we were newly anointed as Avatar, our moon passed between Soleos and our sun. The people feared doom; we held the truth."

    susurha surprised "Why would you not explain, O Enlightened One?"

    ava angry blush "We shall pass over your mockery, Druid."

    ava neutral "Few truths give comfort. Great Mother Asha had saved Soleos from darkness, we said. Safety and order followed."

    darius surprised "Was it worth the price?"

    ava angry blush "Every decision eats at our soul, Inspector."

    ava sad "Of which so little remains."

    hide ava with dissolve
    hide darius with dissolve
    hide susurha with dissolve

    show vivi neutral at left:
        xzoom -1

    show urshu neutral at right

    urshu happy "Ah, Vivienne! A journalist to the bitter end, I see, eh? Glad I found you. Let us allow our fellow passengers some space. Perhaps I could regale you instead?"

    vivi angry "Thanks, Urshunabi, but I think my bed is calling my name, and I’d hate to ignore it. Night."

    #JUMP TO Depression debrief

    jump depression_debrief