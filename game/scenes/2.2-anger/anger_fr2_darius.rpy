# The scene starts here.

label anger_fr2_darius:

    #FREE ROAM 2 - DARIUS 

    # LOCATION: dining car
    # call check_overlay from _call_check_overlay_7
    scene diningcar with fade
    play ambience amb_bar fadein 1.0

    show vivi happy at left with dissolve:
        xzoom -1

    vivithinking neutral "The heat he gives off is a trail that's easy to follow. I hope Darius doesn't mind that I followed him to the dining car."
    stop music fadeout 10.0

    show darius neutral at right with dissolve

    vivi happy "Well well. If it isn't the melancholy mindflayer."
    darius surprised "Melancholy? Heh. Then what do I call you? The rapacious reporter? The insensitive investigative journalist?"
    vivi happy blush "You can call me whatever you like. As long as you call me."
    show darius surprised blush with dissolve
    darius "I'll be sure to call you on my... shell phone."
    vivi happy "..."
    show darius sad blush
    darius "I can't believe I stooped to punnery. I swear, something about this place is making me go soft."
    vivi happy blush "If you're tired of going soft, maybe I can recommend something with more of a point?"
    show darius surprised blush
    darius "I'm sorry?"
    vivi happy blush "Something where you have to do it just right to score..."
    darius "Ms. Sanssouci, I think this is hardly the time or place—"
    vivi neutral "Darts, Darius. I'm talking about darts."
    show darius neutral blush
    darius "Right. Darts."
    vivi neutral "Unless you'd prefer something a bit more direct?"
    show darius neutral -blush
    darius "Darts is fine. I could use the distraction."
    vivithinking surprised "Something feels different than the last time we talked. Am I being too forward?"
    vivi neutral "Darius..."
    vivi neutral blush "I'm sorry. I guess this place is getting to me. Trying to lighten the mood with some harmless flirting."
    darius neutral "It's alright. I don't mean to imply that I didn't like it. I'm just not used to it."
    vivi surprised "What, no mindflayer partner for you?"
    darius sad "Not exactly, no. I've been a bit... busy for the last thousand years."
    darius neutral "And as a side note, not all flirting is harmless. Trust me."
    vivi sad "I...I didn't mean to bring up anything painful."
    vivithinking sad "He's staring at me—No, through me—So intensely."
    vivi neutral "So... What have you been busy with?"
    darius neutral "Oh, this and that. My kind live a long time. At least...we're supposed to."
    vivi neutral "I suppose I wouldn't know what that's like. We only get about 80 good years if we're lucky. And I suppose I wasn't lucky."
    vivi neutral "Seems you weren't either."
    darius angry "No. Not lucky at all."
    vivi angry "You're awfully coy. Come out with it."
    darius surprised "Excuse me?"
    vivi angry "At least you had a life. Mine was cut short. I had more I wanted to do. You could at least clue me into what you're so upset about."
    darius angry "I owe you no such explanation."
    vivi angry "It's not about owing anything, I'm not keeping a ledger—"
    darius angry "Neither am I. Not anymore."
    vivithinking surprised "He's practically shaking."
    vivithinking neutral "Yep. There goes Vivi, running her mouth like a bull in a china shop again."
    vivi neutral "I've touched a nerve. I'm sorry. Again. I swear I'm not trying to get under your skin."
    show darius neutral blush with dissolve
    darius "Whether you were trying to or not, you've a talent for it."
    vivi neutral blush "Should we...play some darts?"

    # <CHOICE>
    show darius sad -blush
    darius "Why not."

    menu:
    # OPTION 1 +ATTRACTION
        "Throw a dart while looking straight into Darius' eyes.":

            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_anger_fr2 / att_num_list_darius[1])
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            pause 1.0

            # SOUND: dart lands on board
            play sound darts
            pause 1.0
            show darts_darius with dissolve
            $ renpy.pause()
            hide darts_darius with dissolve
            darius surprised "Huh. Nice throw. Good... darting."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi happy blush "When I want something, I go straight at it."
            darius surprised "Again. Noted."

            # JUMP TO: vivi neutral "I want to know what's on your mind."

    # OPTION 2 +DECAY
        "Actually...forget it.":

            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_anger / dec_num_anger)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "Actually...forget it."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius surprised "I thought you wanted to play."
            vivi angry "Play? At a time like this? Seems a waste of time."
            darius surprised "I... actually agree."
            vivi angry "Urshu is messing with us. It seems clear to me. I think it's tied to our lives, our former lives. You seem to have some insight."

            # JUMP TO: vivi neutral "I want to know what's on your mind."
        
    vivi neutral "I want to know what's on your mind."
    play music dariusmusic fadein 10.0
    darius angry "Fine. You've pestered me enough. My purpose was clear and simple: find heretics. Break them. Consign their souls to the Lord of Eternal Rest." 
    darius angry "That is what's on my mind. Now and always."
    darius angry "You wanted to know. Now, you know."
    vivi surprised "That's...I had no idea."

    # <CHOICE>
    vivi sad "But that's not the end of the story, is it? There's something missing."

    menu:

    # OPTION 1 +ATTRACTION
        "If I tell you a secret, will you tell me one of yours?":

            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_anger_fr2 / att_num_list_darius[1])
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "If I tell you a secret, will you tell me one of yours?"
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            darius surprised "Hm. Let's hear yours first."
            vivi surprised "That's...it's a yes-or-no kind of situation."
            darius happy "And I'm sure it worked on difficult interview subjects. Go ahead."
            vivi sad "Okay. I once faked a quote in an interview, and I never got caught."
            darius surprised "That's pretty serious. A breach of ethics."
            vivithinking surprised "Definitely not the worst thing I've ever done, but hey."
            vivi happy "Now you."

            # JUMP TO: "Less of a secret and more of a...regret."

    # OPTION 2 +DECAY
        "Sounds like you miss it a little.":

            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_anger / dec_num_anger)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi neutral "Sounds like you miss it a little."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius angry "I beg your pardon."
            vivi neutral "Is that why you're so quiet and pensive? Moody? You wish you could still be out there, in service of your god."
            darius angry "That could not be further from the truth."
            vivi angry "Then clarify it for me. Why keep your past a secret? It's not like it matters now."

            # JUMP TO: "Less of a secret and more of a...regret."

    darius sad "Less of a secret and more of a...regret."
    vivi neutral "One regret? Can't be that bad."
    darius angry "Try several lifetimes' worth. It was all for nothing. Nothing."
    vivi surprised "How can you be so sure?"
    darius angry "I'm here, aren't I? With the likes of you. And them. I am nothing like any of you."

    # darius exits
    hide darius with dissolve

    vivithinking surprised "Jeez. In all my years of journalism, I haven't seen anything like that. I need some rest."

    # vivi exits
    hide vivi with dissolve
    stop ambience fadeout 1.0

    jump anger_urshu_darius