label bargaining_darius_susurha:

    # call check_overlay from _call_check_overlay_15
    scene lounge with fade
    play ambience amb_lounge if_changed fadein 1.0
    $ darius_fullbody = True
    $ susurha_fullbody = True
    show vivi neutral at left with dissolve :
        xzoom -1

    vivithinking neutral "There’s got to be a way out. Surely I can convince one of these strangers to help me."

    vivithinking surprised "Oh scat, someone’s coming. I could sense that roiling mind anywhere. Better make myself scarce, see if I can learn anything."

    play music peacefulmusic loop
    hide vivi

    # vivi portrait disappears, fades away or something

    show darius neutral at left with dissolve :
        xzoom -1

    show susurha neutral at center with dissolve

    darius angry "Leave me alone, princeling."

    susurha happy "Come on, show me."

    darius angry "I don’t know what you’re talking about. There is nothing to show."

    susurha happy "Are you telling me that as old and powerful as you are, you can’t show me a little sliver of something? A spark? A tendril."

    darius neutral blush "Who said I’m old and powerful? Go away."

    susurha happy "You won’t get rid of me that easily. I’ve got a sense for these things. Been around magic myself, you know."

    darius surprised "Hm. I’ll take your word for it."

    susurha happy "So...read my mind. Do it. What number am I thinking about? What shape is my tail making? How many claws am I holding up?"

    darius angry "Drop it."

    susurha neutral "Feh. You’re no fun. You probably couldn’t be of use anyway."

    darius neutral "So that’s it then. That’s why you’ve been hounding me through every damn car."

    susurha surprised "Well, I certainly didn’t do it for the company. You’d think the two of us would get along."

    stop music fadeout 1.0 
    darius surprised "Why would we...ever get along?"

    susurha happy "Because we have so much in common!"
    play music dariusmusic fadein 2.0

    darius neutral "This is a joke. You’re mocking me. My time is better spent elsewhere."

    susurha neutral "No, wait. Wait. Seriously. I feel like between the two of us we can break out of here. Aren’t your kind supposed to be super powerful?"

    darius angry blush "I keep telling you no–"

    susurha happy "With your abilities and my magic affinity, I feel like we could slip away no problem! Or at least convince that sultry little conductor to cut us a deal."

    darius sad "I’ve cut enough deals. Once again: I decline. Leave my presence. Or I will leave yours."

    susurha sad "...I can feel you, you know. Through the walls. Across this whole train. It billows off of you, like ink dissipating through a glass of water."

    vivithinking "I’m not the only one who feels them?"

    darius neutral "Well. That’s just– it’s nothing. A psychic field, amplified by distress. Good day, little prince."

    stop music fadeout 5.0

    hide darius with dissolve

    hide susurha with dissolve

    $ darius_fullbody = False
    $ susurha_fullbody = False

    show susurha neutral at right with dissolve

    #darius fades, vivi potrait slides left?

    susurha happy "Your scent is pretty recognizable, you can come out whenever you feel comfortable. Hi!"

    show vivi happy blush at left with dissolve :
        xzoom -1

    vivi happy blush "Why the hell didn’t you say anything?"

    susurha happy blush "Wouldn’t want to make you uncomfortable. What do you say? Care to lounge with me?"

    vivi neutral "I– I’d better not. I should get back to the others. Another time."

    susurha happy "Suit yourself!"

    stop ambience fadeout 1.0

    jump bargaining_cs2