# The scene starts here.

label interview_darius:

    # Interviews/Darius Wrecker

    # LOCATION: diningcar
    # scene diningcar with fade

    show vivi neutral at left with dissolve:
        xzoom -1

    show darius neutral at right with dissolve

    # SOUND: train
    play ambience amb_bar

    vivithinking neutral "This one's imposing. Tall and solid, despite that slender frame."
    vivithinking sad "But what's this unease I sense?"
    vivi neutral "Hello? Hi, I'm Vivi, nice to meet you. I'm doing an article on the train and I'm interested in your thoughts about it so far."
    darius neutral "Hmm? Sorry, I'm busy."
    vivi neutral "Busy... sitting here?"
    darius neutral "Yes."
    vivi angry "Listen, if you don't want to be interviewed, that's fine. But could we not lie about—"
    darius neutral "A question. Do you {i}always{/i} badger other people minding their own business, or is that just for me?"
    vivi neutral "I—I just asked you a simple question!"
    stop music fadeout 1
    darius neutral "And I responded in kind. Nothing else was needed between us."
    darius neutral "But you reporters are never satisfied, are you?"
    darius neutral "{i}Sigh{/i}. If you make it quick, I'll humor you."

    
    menu:
        # OPTION 1
        "(I'm gonna eviscerate this jerk. Every flaw. In print. Forever.)":

            vivithinking angry "I'm gonna eviscerate this jerk. Every flaw. In print. Forever."

            #JUMP TO vivi neutral "Thank you for your patience, um... Well, we never established your name, did we?"
    
    
        # OPTION 2
        "(This guy! No, cool your jets, Vivi. Angry, er, squids tell no tales.)":

            vivithinking neutral "This guy! No, cool your jets, Vivi. Angry, er, squids tell no tales."

            #JUMP TO vivi neutral "Thank you for your patience, um... Well, we never established your name, did we?"
    
    vivi neutral "Thank you for your patience, um... Well, we never established your name, did we?"

    stop music
    play music dariusmusic fadein 5 volume 0.3 #introduce Darius's theme for the first time, slow fade in.
    darius neutral "Just call me Darius."
    vivi neutral "No last name?"
    darius neutral "Does it really matter?"
    vivi neutral "I'd like to have a proper way of referring to you."
    darius neutral "Gods, it never ends. It's Wrecker."
    vivi neutral "Really? That's the best you could come up with?"
    darius neutral "The best my lineage could, apparently. Now, could you please get to the questions?"
    vivithinking neutral "You're that into your cosplay, huh? Fine, I'll play ball."
    vivithinking neutral "That being said, it is a really nice costume. So lifelike..."
    # <CHOICE>
    vivi neutral "Right, let's see."

    menu:
        # OPTION 1
        "What's your costume?":

            vivi neutral "What's your costume?"
            darius neutral "My... costume?"
            vivi neutral "Yeah, you know. The overcoat, tentacles, mask. What're you going for?"
            show darius neutral blush
            darius "I don't... A detective? Yes, a detective."
            vivi neutral "Not quite what I meant, but sure, a squid detective."
            show darius neutral -blush
            darius neutral "You... don't know what I am, do you?"
            vivi neutral "Sorry, I'm a bit out of the loop with current trends so I don't get the reference."
            vivithinking neutral blush "But I can already imagine the fan fiction..."
            vivithinking angry "Get it together, Vivi!"

            # JUMP TO vivi neutral "Okay, next question."

        # OPTION 2
        "Tell me about yourself.":

            vivi neutral "Tell me about yourself."
            darius neutral "I'd... rather not."
            vivi neutral "Come on, can't you give me something? Even the tiniest shred?"
            darius neutral "A detective. I'm a detective."
            vivithinking neutral "Well, then. This suddenly got a lot more interesting."
            vivi neutral "A detective, huh? Here on a case?"
            darius neutral "No. And if I were, you don't really think I'd say so, do you?"
            vivi angry "Just looking to make conversation."
            darius neutral "And we agreed there is no need."
            vivithinking angry "You want to rush this? Fine. I'm sure the other guests will be more talkative."
        
            # JUMP TO vivi neutral "Okay, next question."

    vivi neutral "Okay, next question."

    # <CHOICE>
    darius neutral "Make it a simple one, will you?"

    menu:
        # OPTION 1
        "Where are you from?":

            vivi neutral "Where are you from?"
            darius neutral "Nowhere you're familiar with."
            vivi angry "Do you intend to be so difficult throughout this entire process?"
            darius neutral "I am simply being honest. I come from a rather small garden."
            vivi neutral "A garden? Weird way to refer to back home."
            darius neutral "It's not the name of it, obviously. Like I said, it's small, you wouldn't know it."
            vivithinking neutral ". . .right then."

            # JUMP TO vivi neutral "Forget it. Last question."

        # OPTION 2
        "How'd you find out about the train?":

            vivi neutral "How'd you find out about the train?"
            darius neutral "I don't remember."
            vivi neutral "This is going nowhere."
            darius neutral "How would you have me answer, hmm? Tell me and I'll do just that. We both walk out of here happier."

            # JUMP TO vivi neutral "Forget it. Last question."

    vivi neutral "Forget it. Last question."
    vivi neutral "Why did you decide to take this little excursion?"
    darius neutral "Well I... I..."
    darius sad "Why..."
    vivithinking neutral "His whole demeanor changed. No witty remark this time?"
    darius sad "Sorry, I'm...not feeling very well. Why am I here, you asked?"
    vivi neutral "Essentially, yes."
    
    # <CHOICE>
    darius neutral "Duty... yes."

    menu: 
        # OPTION 1
        "(Duty? You're a detective. What, were you here for wardrobe inspo?)":

            vivithinking neutral "Duty? You're a detective. You just told me you weren't on a case!" 
            vivithinking neutral "What, does the decor match your outfit? Trying to get wardrobe inspiration?"

            # JUMP TO vivi neutral "Very interesting, I—"

        # OPTION 2
        "(Duty, eh? Are they keeping their eye on someone here?)":

            vivithinking neutral "Duty, eh? Are they keeping their eye on someone here?"

            # JUMP TO vivi neutral "Very interesting, I—"
    
    
    play sound [ "<silence 1.6>", "audio/sfx/orex_char_telepathy.ogg" ]
    $ renpy.music.set_audio_filter("ambience", audio_filter.Lowpass(100), replace=True, duration=2.6)
    stop music fadeout 2.6
    vivi neutral "Very interesting, I—"
    $ renpy.music.set_audio_filter("ambience", None, replace=True, duration=5)
    vivithinking sad "It's like a chill just came in. Why is the room so...heavy? Such a sickly atmosphere, like wet clothes sticking to your skin."
    vivi neutral "Thank you, uh...Darius. I'll leave you be."
    vivithinking sad "It's like he doesn't even see me."

    hide darius with dissolve

    # JUMP TO: Figuring it out
    jump interview_choice