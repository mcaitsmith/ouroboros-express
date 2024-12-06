# The scene starts here.

label bargaining_fr1_darius:

    #FREE ROAM 1 - Darius

    # LOCATION: lounge 
    # call check_overlay from _call_check_overlay_18
    scene lounge with fade
    play ambience amb_lounge if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom -1

    show darius sad at right with dissolve

    vivithinking "Now that's a curious sight. Clutching their forehead like they had a bad hangover?"
    vivi neutral "Rough night?"
    play music peacefulmusic loop
    darius sad "You could say that. The dragon, Susu'Rha, was it? Their thoughts are so loud. I could barely sleep."
    vivi neutral "It's always the thoughts with you. You can't just...turn that off?"
    darius sad "Normally I can! That's how incessant it was! Like a stampede of preschoolers rambling on and on about the most inane concepts."
    vivi neutral "Well, hopefully, I have a little less of an inane topic to discuss."
    darius neutral "Oh you could never be so inane Vivi. You're far too inquisitive. Some would say nosy."
    vivi neutral "Ahh, you're far too polite. Some would say distant, even."
    darius happy "Haha, yes, I do love our little chats. So? What is it?"
    vivi happy "Have I ever told you you're quite charming?"
    darius neutral "Oh gods, here she starts."
    vivi happy "Such a vast intelligence, but always holding it tight to the chest. So many  thoughts and words, but only picking out a select few."
    
    # <CHOICE>
    darius neutral "I can tell this is killing you. Come on, out with it."
    
    menu:
        # OPTION 1
        "(Surprisingly, no, if I'm honest. But they don't have to know that.)":

            vivithinking neutral "Surprisingly, no, if I'm honest. But they don't have to know that."
            # JUMP TO vivi neutral "Alright, fine. Urshu. Have you tried using your abilities on him? Get a good mental read?"

        # OPTION 2
        "(Ugh. They got me. Still, no harm in indulging them.)":

            vivithinking neutral "Ugh. They got me. Still, no harm in indulging them."
            # JUMP TO vivi neutral "Alright, fine. Urshu. Have you tried using your abilities on him? Get a good mental read?"
    
    vivi neutral "Alright, fine. Urshu. Have you tried using your abilities on him? Get a good mental read?"
    darius happy "Ahahaha! Oh, you humans are a riot. Comedy, that's the true gift your species possesses..."
    darius neutral "Hold on. You're serious?"
    darius neutral "Urshunabi? The ferryman of the dead? The man with an almost godly sense of perception?" 

    # <CHOICE>
    darius neutral "That's who you believe I have the ability to mindread?"

    menu:
        # OPTION 1
        "Okay, I get it.":
    
            vivi angry "Okay, I get it. No need to rub it in anymore."
            darius neutral "I apologize, but you think too highly of my abilities. Mind reading is a very involved exercise. It requires a very stable hold on one's person, almost like learning to swim in deeper waters."
            darius neutral "A mind like Urshu's would be like diving into a bottomless well, an abyss the depth of which I'd likely never find the end of." 
            darius neutral "I'd lose myself in his mind, unable to pull back."
            vivi neutral "I understand. I don't want you to do anything dangerous."
            stop music fadeout 1.0

            # JUMP TO: vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        # OPTION 2 +ATTRACTION
        "I didn't think sarcasm was in your wheelhouse.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_bargaining_fr1 / att_num_list_darius[2])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

        
            vivi neutral "I didn't think sarcasm was in your wheelhouse, Monsieur Wrecker."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            darius happy "I have many surprises in my \"wheelhouse\" as you say. Some I may even show you someday."
            vivi happy "Rather forward, aren't we? That definitely isn't in your nature."
            darius neutral "Yes, well... Maybe you're a bad influence on me, Ms. Sanssouci."
            
            show vivi neutral blush at left

            vivithinking "Huh? That was a little more than flirty..."
            stop music fadeout 1.0

            # JUMP TO: vivi neutral "My apologies, I suppose you'd want to know what this is all about."

        # OPTION 3 +DECAY
        "Can you read ANYTHING?":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')


            vivi angry "Can you read ANYTHING?" 
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            vivi angry "Just when I thought you could be useful." 
            darius angry "Only if you say please."
            vivi neutral "Please, do the one thing mindflayers are infamous for? For the benefit of us all?"
            darius neutral "But that's the curious part, isn't it? You still haven't explained yourself in the slightest. Why are you so interested in reading Urshu?"
            stop music fadeout 1.0

            # JUMP TO: vivineutral "My apologies, I suppose you'd want to know what this is all about."

    vivi neutral "My apologies, I suppose you'd want to know what this is all about."
    play music mysterymusicpiano fadein 1.0 loop
    vivi angry "It just bothers me how little we know about this ferryman. How can I trust someone I barely understand?"
    darius neutral "We do it every day, don't we? How many strangers do you meet in a day? How many do you just assume won't be a threat to you?"
    vivi neutral "But those people are like us. Urshu... isn't."
    darius neutral "Oh, he is. More than you know."
    vivi happy "So you have read him!"
    darius neutral "Not read. More... observed."
    darius sad "The faces he makes when he thinks no one is noticing. The way he listens to every word with unrelenting attention."
    darius sad "The way he dutifully attends to every need we have, but has no desire to care for his own."
    darius sad "The way he takes in everything others give in, the good and bad, but is so reluctant to give up anything of his own."
    darius sad "Perhaps I understand him so well because I know his pain. His suffering. His heartbreak. He is isolated. Alone."
    darius neutral "Know this, Vivienne. Toying with that man isn't just foolish, it's cruel."

    # <CHOICE>
    darius "He may be somewhat of a god, but he endures the same sorrows as we do."

    menu:
        # OPTION 1 +ATTRACTION
        "So caring. I wouldn't expect it from you.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound attchoice
            show attraction_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -850
            $ att_meter_darius += int(att_max_bargaining_fr1 / att_num_list_darius[2])
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')

    
            vivi happy "So caring. I wouldn't expect it from you."
            hide attraction_icon
            with { "master" : Dissolve(0.5) }
            vivi neutral "You don't have to worry. I don't plan to hurt our dear Urshu."
            vivi neutral "I was actually thinking of doing something for him later today and wanted you to read him to see what he'd like."
            darius happy "I'm glad to hear it. I can tell he cares for you a great deal."
            vivi neutral blush "What do you mean? He treats me just the same as anyone else."
            darius happy "You're inquisitive, Vivi, I told you. You get people to confront aspects of themselves they wouldn't otherwise. Urshu admires that. I can see it."
            show darius happy blush
            darius "Perhaps that is why I, too, enjoy your company so much."
            vivithinking neutral blush "This guy... When did he get so suave?"
            show darius neutral -blush
    
            # JUMP TO: vivi neutral "I think I'll be going now. Thank you for the insight."

        #OPTION 2 +DECAY
        "Okay, enough. I don't need the lecture.":

            $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(1000), replace=True, duration=0.25)
            $ renpy.music.set_volume(0.5, delay=0.25, channel='music')
            play sound decchoice
            show decay_icon at right with Dissolve(2.0):
                xoffset -500
                # xoffset -30
                yoffset -750
            $ dec_meter += int(dec_max_bargaining / dec_num_bargaining)
            $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=1.5)
            $ renpy.music.set_volume(1.0, delay=1.5, channel='music')
    
            vivi angry "Okay, enough. I don't need the lecture. I'm not about to break this guy's heart or anything."
            hide decay_icon
            with { "master" : Dissolve(0.5) }
            darius neutral "I'm sure you won't. Just a helpful reminder."
            vivi angry "Noted. Unneeded. Unasked for. But noted."

            # JUMP TO: vivi neutral "I think I'll be going now. Thank you for the insight."

        #OPTION 3 >>ATTRACTION
        "Sounds like you've had experience." if att_meter_darius >= 20:

            vivi sad "Sounds like you've had experience."
            darius sad "In suffering? More than you know, but still less than the amount I've caused."
            darius sad "In heartbreak? Much less than you'd think."
            vivi neutral "Never had someone you couldn't quite read? Someone that ended up hurting you?"
            darius sad "Honestly? No. The life I lived left little room for such ventures."
            show darius neutral blush
            darius "Until now... funny enough."
            darius "I have never met someone I couldn't read. It became almost second nature to naturally understand everyone I came across."
            darius "You however... It's strange. I feel like I'm beginning to, but it has nothing to do with my abilities."
            vivi neutral blush "You're connecting. Through natural means rather than artificial ones."
            show darius happy blush
            darius "I suppose so. It's an exhilarating experience, truth be told." 
            show darius neutral blush
            darius "I'm... thankful it's you out of all people to introduce me to this."

            show vivi neutral at left

            vivithinking "Such a simple sentence, and it has my heart fluttering like a little bird! Oh, don't make it obvious Vivi..."
            show darius neutral -blush
            # JUMP TO: vivi neutral "I think I'll be going now. Thank you for the insight."

    vivi neutral "I think I'll be going now. Thank you for the insight."
    darius neutral "Insight is a kind way of putting it. I just told you about what I've seen."
    stop music fadeout 1.0
    darius neutral "But thank you, Vivienne. I'm always open to chat."

    # JUMP TO: Darius Susu'Rha intermission scene
    jump bargaining_darius_susurha