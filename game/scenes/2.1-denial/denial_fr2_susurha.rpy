﻿# The scene starts here.

label denial_fr2_susurha:

    #FREE ROAM 2 - Susu'Rha

    #LOCATION: Lounge
    scene lounge with fade
    play ambience amb_lounge

    vivithinking "This train is driving me insane. I refuse to play into the conductor's games."

    vivithinking "Yep. It seems Susu'Rha is lounging on one of the recliners."

    show vivi neutral at left with dissolve :
        xzoom -1

    vivi "What are you doing?"

    show susurha neutral at right with dissolve
    play music susumusic loop fadein 3.0

    susurha "What does it look like I'm doing at the moment? I'm deep in the meditative process of trying not to think about the circumstances that surround me."

    susurha "And let me tell you...the cushions this contraption houses are just soooo...Welcoming."

    #<CHOICE>
    susurha "You should give it a try."

    menu:

    #OPTION 1 
        "I'll stand.":

            vivi "I'll stand."
            susurha "Suit yourself but I see you weak at the knees. Eyes drawn to where I lay. The cushions calling your name."
            susurha "Vivi..."
            vivi surprised "What?"
            susurha "I'm saying you look exhausted, but to each their own."
            vivithinking sad "They're positively drooping in their seat."
            vivithinking sad "Ouch. The headache is only getting worse."
            vivithinking sad "Maybe this was a mistake."
            # JUMP TO: susurha "This place is a prison."

    #OPTION 2 +ATTRACTION
        "I'd love to.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi "I'd love to."
            vivithinking "The way they slid that chair my way with ease..."
            # SOUND: Vivi sits down in a super comfortable recliner.
            # skipping
            vivithinking "Hot damn..."
            susurha happy "Feels like a dream, doesn't it?"
            vivi neutral "Feels like I'm sinking."
            vivithinking happy "It's nice sitting in silence. I'm enjoying their company."
            vivithinking neutral "I think my headache's easing off."
            #JUMP TO: susurha "This place is a prison."

    susurha sad "This place is a prison."

    susurha sad "The Archdruids warned of daemons that kidnap their prey and treat them to endless luxuries."

    susurha sad "Perhaps this is that. We are being fed lies and comfort just so that we can become sooo relaxed and THAT is when they'll strike...to feast on our satisfied souls."

    susurha sad "To be frank with you, I always believed such tales to be nothing more than a bunch of creative nonsense to make the less fortunate in the clan okay with their shitty life conditions."

    susurha sad "But..."

    # <CHOICE>
    susurha sad "I'm beginning to think that those sad old sods that lived in a forest their entire lives weren't completely high as the stars above."

    menu:

    #OPTION 1 +ATTRACTION
        "This place freaks me out.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')
        
            vivi "This place freaks me out."
            susurha angry "I feel that in my bones. Oh, this place worms its way down my spine like a spider in the night."
            susurha angry "Makes me feel like burning the whole place down."
            susurha angry "Imagine..."
            susurha angry "You're walking in the woods one day, lost in the spiraling storm of every possible thought you've ever had bouncing around in your head, and then..." 
            susurha angry "Suddenly finding yourself trapped with a bunch of odd looking individuals, no offense, in a metal tube speeding to an unknown locale."
            susurha angry "All the while you're being told that..."
            susurha sad "You are dead."
            vivi "Is that how you died? I mean ended up here."
            susurha sad "How'd you figure that?"
            #JUMP TO: susurha sad "We will be dead if we stay here any longer."

    #OPTION 2 
        "That's absurd. That can't be the case.":

            vivi "That's absurd. That can't be the case."
            susurha angry "..."
            vivithinking "They're glaring at me. Looking me up and down."
            vivithinking "Alright, chill Vivi. Maybe that was a bit too-"
            susurha angry "Let me tell you what is absurd." 
            susurha angry "You're walking in the woods one day, lost in the spiraling storm of every possible thought you've ever had bouncing around in your head, and then..."
            susurha "Suddenly finding yourself trapped with a bunch of odd looking individuals in a metal tube speeding to an unknown locale."
            susurha angry "All the while you're being told that YOU ARE DEAD."
            # JUMP TO: susurha sad "We will be dead if we stay here any longer."

    susurha sad "We will be dead if we stay here any longer."

    vivi "We need to get out of here."

    vivithinking happy "Now I've got their attention."

    susurha happy "Now that is something I absolutely LOVE hearing. Please tell me you have some sort of idea of getting off this thing."

    vivithinking "..."

    vivi sad "I do not."

    susurha neutral "Hmm..."

    susurha happy "Well, lucky for you, I have been indulging in some...sightseeing around this fine place and I think I know just the perfect spot for us to run away together."

    vivi happy "Where?"

    susurha happy "The observatory and its thin glass windows."

    susurha happy "Oh, I do so very much love gazing up at the stars above like I did when I was a young prince."

    vivi happy "Now?"

    susurha happy "Why wait?"

    vivi happy "Are we really doing this?"

    susurha happy "It's a date, my dove."

    vivithinking surprised "Whoa - I didn't expect them to literally drag me along!"
    stop music fadeout 1.0
    play sound swoosh
    stop ambience fadeout 1.0
    #LOCATION: Observatory
    scene observatory with fade
    play music mainmusic
    play ambience amb_observatory fadein 1.0

    show susurha surprised at right with dissolve
    show vivi surprised at left with dissolve :
        xzoom -1

    vivithinking "Golden fiery flashes shine through the glass windows of the cabin, and in between those sparkles of light..."

    vivithinking "Darkness."

    vivithinking "Where are we?"

    show vivi neutral

    # <CHOICE>
    susurha surprised "So strange, when I was just here I saw the night sky riddled with an ocean of stars, but now...it's just nothing."

    menu:

    #OPTION 1 +ATTRACTION
        "Worried?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi "Worried?"
            show susurha neutral
            # SOUND: Susu'Rha scoffs.
            # skipping
            susurha "Me, worried? Never. I make sure to go out of my way to avoid feeling worried, but this..."
            susurha "It just doesn't make sense.  I was so sure I knew what I saw. It had the same constellations burned into my mind from that night and..."
            susurha "It hasn't even been an hour since I scouted the place."
            susurha "Where are we?"
            vivi "I was thinking the same thing."
            susurha happy "I suppose there is only one way to find out."
            #JUMP TO: susurha "This way."

    #OPTION 2
        "Where is this exit you sold me?":

            vivi "Where is this exit you sold me?"
            susurha neutral "Forgive me."
            # JUMP TO: susurha "This way."

    #OPTION 3 
        "Maybe you didn't get a clear view?":

            vivi "Maybe you didn't get a clear view?"
            susurha "Maybe..."
            susurha neutral "But I was so sure I knew what I saw. It had the same constellations burned into my mind from that night and..."
            susurha "It hasn't even been an hour since I scouted the place."
            vivithinking "..."
            susurha "Doesn't matter."
            # JUMP TO: susurha "This way."

    susurha "This way."

    susurha "Help me stack these chairs up under that central window on the ceiling."

    # SOUND: Vivi and Susu'Rha exert themselves stacking chairs on top of each other.
    play sound crash
    pause 3.0

    vivithinking "This seems incredibly unplanned, but I don't really have a choice."

    vivithinking "I need to get off this train."

    vivithinking "And this one is my best chance."

    susurha happy "This reminds me of back when I was younger and I'd sneak out of my tower bedroom to wander on top of the surrounding castle walls."

    vivithinking "Aaaaand they're climbing the tower of stacked chairs and wrestling with the loose screws of the ceiling's window."
    vivithinking "You don't see that every day. Huh...Golden light is glistening off their scaly skin."
    vivithinking "I wonder what it's like, living in a castle..."

    # <CHOICE>
    vivithinking "All I can see is the biggest smile I've ever seen."

    menu:

        #OPTION 1 
        "Can we please hurry this up?":

            vivi "Can we please hurry this up?"
            # SOUND: Susu'Rha scoffs.
            # skipping
            susurha neutral "You know, you remind me a lot of the nobility that I grew up around."
            susurha "They too found my voice to be annoying."
            vivi "That's not what I meant."
            susurha "Nevertheless, they listened as I slowly found my way out of that hell."
            vivithinking surprised "Aha...Susu'Rha appears soft, but they actually have a nerve..."
            #JUMP TO: susurha "Voila."

    #OPTION 2 +ATTRACTION
        "It sounds like you lived a fairy tale.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            pause 1.0
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

            vivi "It sounds like you lived a fairy tale."
            #SOUND: Susu'Rha laughs.
            # skipping
            susurha "I suppose from the outside it could come across with that poetic fantasy allure."
            # <CHOICE>
            susurha neutral "Apologies, I believe you were cracking a joke at me."

            menu:
            
                #OPTION 2-1 +ATTRACTION
                "I wasn't. Tell me more.":

                    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
                    $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
                    play sound attchoice
                    pause 1.0
                    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
                    $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

                    vivi "I wasn't. Tell me more."
                    susurha happy "Perhaps I shall at another time."
                    # JUMP TO: susurha "Voila."

                #OPTION 2-2
                "It's okay.":

                    vivithinking "It's okay."
                    # JUMP TO: susurha "Voila."

    susurha happy "Voila."
    stop music fadeout 1.5

    # SOUND: The window clicks open.
    play sound windowopen

    susurha happy "We are homeward bound."

    hide vivi with dissolve
    hide susurha with dissolve

    show observatory blur with dissolve
    $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=8), audio_filter.Lowpass(2000)], replace=True, duration=2.0)
    play cd_ambience amb_cosmicdecay fadein 2.0
    #Complex filter - Filters out a little bit of the high, and boosts the low end by A LOT. Like wind! Also force plays cosmic decay.

    vivithinking "I haven't done this much climbing since I was a kid. Now to look out the opened window."

    vivithinking "..."

    vivithinking "This is..."

    vivithinking "Unimaginable."
 
    $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=2), audio_filter.Lowpass(1000)], replace=True, duration=2.0)
    play music horrormusic
    
    vivithinking "Spiraling celestial bodies swirl all around as the train speeds faster than anything I've ever seen."

    play sound trainwhistle volume 0.25
    vivithinking "Flames burst from the train's tracks and are sucked into the void."

    vivithinking "I can feel my hair whipping around my face. I really wanna scream. But I can't."

    vivithinking "Susu'Rha's staring out into the visual abyss of...wherever we are. They're mumbling...I can't hear what they're saying."

    vivithinking "There's a tear rolling down their cheek."

    vivithinking "What are they looking at...?"

    vivithinking "What is that thing?!"

    vivithinking "A reflective dress floating in the wind, but it slowly inches closer to us."

    vivithinking "It moves with purpose. It moves like it's alive."

    vivithinking "Dangling like a puppet as it comes closer and I can see its face."
    
    $ renpy.music.set_volume(0.00, delay=1.5, channel='music')
    play sound char_mirror
    vivithinking "My face."
    $ renpy.music.set_volume(1.00, delay=10.00, channel='music')

    vivithinking "Reflecting on the concave mirror plate it has on its shoulders."

    vivithinking "It crawls closer to us, inches away from my own face."

    vivithinking "The wind's stroking my face like cold hands, pulling me closer to it."

    vivithinking "I can't breathe."
    $ renpy.music.set_audio_filter("ambience", [audio_filter.Lowshelf(frequency=200, gain=2), audio_filter.Lowpass(400)], replace=True, duration=2.0)
    play sound heartbeat
    
    vivithinking "I can't breathe."

    stop music fadeout 0.5
    vivithinking "I CAN'T BREATHE!"
    $ renpy.music.set_volume(0.25, delay=0.1, channel='ambience')
    $ renpy.music.set_volume(0.25, delay=0.1, channel='cd_ambience')
    play sound char_terror
    pause 5
    $ renpy.music.set_volume(1.0, delay=3.5, channel='ambience')
    $ renpy.music.set_volume(1.0, delay=3.5, channel='cd_ambience')

    vivithinking "It's reaching out to me..."

    urshu angry "Get down from there!"
    
    stop cd_ambience fadeout 5.0
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5.0)

    #SOUND: The sounds of chairs clashing and Vivi and Susu'Rha hitting the floor.
    play sound crash
    pause 2.0
    #VISUAL: The screen shakes.
    play sound cineboom
    show observatory with hpunch
    #SOUND: The window slams shut.
    play sound windowshut
    pause 1.0
    show urshu angry at left with dissolve:
        xzoom -1.0
    show vivi jump_surprised at center with hpunch:
        xzoom 1
        linear 0.3 ypos 1000
        linear 0.5 ypos 1500
    play sound cineboom
    
    vivithinking "I can breathe again!"
    show vivi surprised at center:
        xzoom 1
    play music mysterymusic
    show vivi surprised at center with dissolve:
        xzoom 1

    show observatory -blur with dissolve



    vivi surprised "What the hell was that?"

    urshu angry "When I told you to go seek the truth I didn't quite mean to go and make us all something's meal."

    vivi surprised "What the hell was that?!"

    urshu neutral "The truth, Miss Sanssouci. The truth of the matter whether you choose to accept it or not is that you and Druid Balrinn here have passed in life and there is no getting off this ride."

    urshu "Please, don't try to get off this train again. I may not be there next time to save you."

    show susurha neutral at right with dissolve

    susurha "What was that thing I saw out there?"

    urshu "What you and Miss Sanssouci witnessed depends entirely on yourselves."

    urshu "May I suggest returning to your cabins and getting some rest?"

    vivithinking "Oh baby. Caught between hell and a better place."

    vivithinking "Ugh...I need a drink."
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5.0)
    stop ambience fadeout 1.0
    #  JUMP TO: Debrief Denial.
    jump denial_debrief