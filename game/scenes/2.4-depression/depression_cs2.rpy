# The scene starts here.

label depression_cs2:

    # Character Selector 2

    # LOCATION: cabin
    scene cabin with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    vivithinking sad "Ugh... I think I might've had a little too much."
    vivithinking neutral "Then again, there's nothing to look toward. Might as well take advantage of the open bar."

    # SOUND: knocking
    play sound knock
    pause 1.0

    show urshu neutral at right with dissolve

    urshu neutral "Ms. Sanssouci, I see you've found the liquor cabinet."
    vivi neutral "Top shelf stuff, Urshu."
    vivithinking neutral "What does he want now?"
    vivi neutral "So, has the conductor of this fine train come to reprimand me?"
    urshu neutral "Not at all. The way you spend your time is entirely up to you."
    vivithinking angry "This guy is impossible!"
    vivi angry "You got a problem with the way I'm spending my time? I'm sick of you looking down at all of us. You may ferry people to the next life but you don't know how it feels."
    vivi sad "We're just trying to have a moment of peace." 
    vivi sad "We don't want to think about this train falling apart, or the horrible things outside..."
    vivi angry "Or you."
    vivi sad "I don't want to think anymore. I just want rest."
    vivi sad "I'm tired of being so tired. And scared and angry and..."
    vivi angry "...Argh!"
    vivi sad "..."
    urshu sad "I'm sorry you feel that way. Truly, I am."
    urshu neutral "Countless have boarded my train. Some have sung its praise. Many more have cursed it out. But this place, whether you see it or not, is a gift."
    urshu neutral "You have been granted a final chance. A place to right your deepest regrets. There's a reason it's not a solo voyage."
    vivi sad "What does it matter? It ends all the same."
    urshu neutral "Heed my advice, or don't. Only one thing is certain:"
    urshu happy "Your story, my dear? It's not finished. Yes, the finale draws near, but the last act is yours to write. Make it a good one."
    vivi neutral "And how do you figure I do that?"

    # ??ATTRACTION
    #Dialog appears if any of the meters is high
    if att_meter_ava >= 50 or att_meter_darius >= 50 or att_meter_susurha >= 50:
        urshu neutral "Believe it or not, you have had a profound effect on the other passengers. I'm sure one of them would love to spend time with you as we approach our destination."
    # END

    # ??DECAY (ELSE)
    else:
        urshu neutral "That is for you to discover. We approach our destination. Now would be a good time for final goodbyes."
    # END
    hide urshu with dissolve

    vivithinking neutral "I suppose there might be something to what he said."

    # <CHOICE>
    # ??ATTRACTION
    #Dialog appears if any of the meters is high
    if att_meter_ava >= 50 or att_meter_darius >= 50 or att_meter_susurha >= 50:
        vivithinking happy "Let's find someone to hold one last time before this thing ends."
    # END

    # ??DECAY (ELSE)
    else:
        vivithinking neutral "Time to finally leave this purgatory. I reckon goodbyes are in order."
    # END

    menu:

        # OPTION 1
        "Avatar of Asha" if fr1_depression_choice != "Ava":

            vivithinking neutral "The goddess. I want to spend my last moments with her."
            # JUMP TO: Free roam 2 / Avatar of Asha
            jump depression_fr2_ava

        # OPTION 2
        "Darius Wrecker" if fr1_depression_choice != "Darius":

            vivithinking neutral "Darius. I want to spend my last moments with them."
            # JUMP TO: Free roam 2 / Darius Wrecker
            jump depression_fr2_darius

        # OPTION 3
        "Susu'Rha Balrinn" if fr1_depression_choice != "Susu'Rha":

            vivithinking neutral "Susu'Rha. I want to spend my last moments with them."
            # JUMP TO: Free roam 2 / Susu'Rha Balrinn
            jump depression_fr2_susurha