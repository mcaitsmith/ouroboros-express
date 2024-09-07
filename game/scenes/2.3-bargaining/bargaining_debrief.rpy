# The scene starts here.

label bargaining_debrief:

    # Debrief Bargaining

    play music mainmusic

    # LOCATION: cabin
    call check_overlay
    scene cabin with fade

    # ??DECAY
    if dec_meter >= 30:

        show vivi angry at left with dissolve:
            xzoom -1

        vivithinking angry "He knew. He knew from the very start and just led me along! Why give any of us hope?"
        vivithinking sad "There is no hope. All of my time here was pointless."
        vivithinking sad "I am pointless."
        vivithinking neutral "I can't even recognize myself. I feel like I'm trying to swim to shore but the current keeps me from ever making it."
        vivithinking surprised "This place is changing me. I'm withering away into     something dark and no amount of clawing back can save me."
        vivithinking sad "I'm doomed."
        vivithinking neutral "Maybe I should write out my thoughts."

        play sound writing

        $ message = "Urshu...that stupid, cruel son of a...\n\nThis is all hopeless!\nI can see changes in all of us.\nI don't feel fully human anymore.\nThose creatures outside the windows...\nWill we end like them?\n\nAt least the bar is stocked.\nTomorrow's plan is to drink the place dry.\nHopefully, if I'm lucky, it'll\npiss the conductor off."

        # Journal entry with degradation meter high
        call display_journal from _call_display_journal_3
        $ cycle = 3

        stop sound

    # ELSE
    else:

        show vivi sad at left with dissolve:
            xzoom -1

        vivithinking sad "I should've known better than to think there was an {i}actual{/i} way out. What the hell was the point in even trying?"

        vivithinking sad "I really shouldn't have shared my plan with anyone else. I didn't just get my hopes up. Now I've let down friends."
        vivithinking happy "Never thought I'd call the folks on this train friends."
        vivithinking sad "And I managed to fuck that up too. What's wrong with me?"

        vivithinking neutral "I need to write."

        play sound writing

        $ message =  "If cooking for him didn't work, what would?\n\nI'm beginning to think that this is it.\nThe end of the line.\nEverything I worked for... gone.\n\nI bet "+ fr2_bargaining_choice  +" has more to say.\nI should pay them a visit sometime\n\nIt beats cloud gazing through\nthese creepy windows."

        # Journal entry with attraction meter high
        call display_journal from _call_display_journal_4
        $ cycle = 3

        stop sound

    # END

    jump bargaining_asha_urshu