# The scene starts here.

label denial_fr1_darius:

    #FREE ROAM 1 - Darius
    #LOCATION: lounge
    scene lounge with fade
    play ambience amb_lounge fadein 1.0
    play music mainmusic if_changed fadein 1.0

    show vivi neutral at left with dissolve:
        xzoom-1

    show darius neutral at right with dissolve

    vivithinking "Darius is doing their best to fill out that loveseat. Even in such a casual position, they're so graceful."

    vivi "Excuse me, it's Darius, right?"

    darius surprised "Yes."

    vivithinking "They seem surprised. Loner type maybe?"

    darius neutral "Intriguing. You approaching me like this. Especially after my rude behavior yesterday."

    vivithinking "Bingo on the loner call."

    vivi "You seem approachable enough. I actually had a question if you don't mind."

    darius neutral "Go ahead."

    vivithinking "If anyone has a good idea what the hell is going on here, I'm guessing the mystical squid detective might have a decent shot at it."

    vivi  "Tell me, you must have experience with otherworldly phenomena, right?"

    darius neutral "In a sense. This whole situation is unlike anything I've seen, however."

    vivithinking "Crap. Swing and a miss."

    vivi  "Interesting. Do you believe him then? That this is some sort of intermission before we all die?"

    vivithinking "Their... phalanges? Tentacles? Whatever they are. They keep them hidden from me. Strange."

    # <CHOICE>
    darius neutral "I'm not entirely sure, but he's given us no reason to doubt. We should find out soon regardless."

    menu:

        # OPTION 1
            "(Real charmer, this one.)":

                vivithinking angry "Real charmer, this one."
                vivithinking angry "Who knows if this is some sort of trap, a messed up fantasy for this conductor? Are we supposed to just take him at his word?"
    
                # JUMP TO darius neutral "Now that you mention it, I am... curious...

        # OPTION 2
            "(Damn. I was banking on them knowing.)":

                vivithinking neutral "Damn. I was banking on them knowing."
                vivithinking neutral "I hope this won't be a total bust."

                # JUMP TO darius neutral "Now that you mention it, I am... curious...


    # <CHOICE>

    darius neutral "Now that you mention it, I am... curious. What do you make of this "Urshu's" claim that we must come to terms?"

    menu:

    # OPTION 1 
        "I'm not sure.":

            vivi  "I'm not sure." 
            vivi "The man speaks in riddles, and I can't make heads or tails of them right now."

            darius neutral "That is understandable. Last night was a shock to be sure."

            vivi "Is that something you're interested in? Coming to terms?"

            darius neutral "You could say that. The details of my life are still cloudy but they're coming back slowly. I'm sure the same goes for you?"

            vivi "Yes, some things are coming back slowly."

            vivithinking "There's a pain in their voice, it's almost... melancholic?"

            vivi "If you don't mind me asking, what happened—"

            darius neutral "Ahem..."

            # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"

    # OPTION 2 
        "It's nonsense.":

            vivi "It's nonsense." 
            vivi "If we're dead, we're dead. There is no coming to terms."

            darius sad "Hmm. I suppose so. Apologies for the foolish question."

            show vivi sad blush 
            vivithinking "Oops. I get the feeling I might've offended them somehow."

            vivi neutral "Of course, if that's what you're looking for, there's nothing wrong with that!"

            darius sad "No no, you're right. There's no chance of redemption if we've passed already."

            show vivi surprised 
            vivithinking "Redemption?"

            # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"

    # OPTION 3 
        "It's interesting.":

            vivi  "It's interesting. If you're into that, then I guess there's some merit to it. I don't know about you though, but I can't \"come to terms\" here of all places."

            darius surprised "Interesting. I wouldn't have expected that answer from you. Thank you for humoring me."

            vivithinking surprised "What does THAT mean? You don't know me. Unless... oh god, are they reading my mind?"

            darius happy "Wondering if I'm reading your mind, are you?"

            vivi surprised blush "So you ARE then!"

            darius happy "Hah, I don't rely on such cheap tricks. Other mindflayers might, but I'm naturally quite skilled at reading people."

            vivithinking "Is that a hint of annoyance I sense?"

            vivi "So then, what do you see when you look at me?"

            show darius happy blush

            darius "I— uhh, erm... my detective skills are a bit off today, you see. Try asking me again tomorrow, I'm sure I'll have a better answer for you."

            show vivi happy 
            vivithinking "Who knew mindflayers could get flustered. And even a little cute?"

            # JUMP TO: darius neutral "Enough about that for now. Don't you find this train strange?"

    show darius neutral -blush
    darius "Enough about that for now. Don't you find this train strange?"

    vivithinking "That deflection was about as subtle as their outfit."

    vivi "I suppose so. In what way exactly?"

    darius neutral "The way it bends, twists, almost shifts to the eye, as if it isn't entirely there. Have you noticed it too?"

    vivi "I've noticed some oddities yes, but I chalked that up to the conductor pulling some tricks. Do you think there's something more to it?"

    darius neutral "Possibly, yes. It's just as much a mystery to me as that conductor is."

    vivithinking "Their words are somber but curious. It's soothing to listen to."

    vivi "Where do you think we're going?"

    darius "In my...religion, we believed that oblivion was at the end of it all. Many mindflayers believe in a similar idea. Maybe this train is leading us to that."
 
    vivi "Mindflayer? Is that what you are?"

    vivi "You seemed interested in making amends before. What's the point if you're headed for oblivion regardless?"

    darius "That's... a little too complex a topic for me to get into right now. I apologize."

    # <CHOICE>

    darius "That being said though, which would you prefer awaits us at the end of this little trip? Oblivion, or some sort of rebirth?"

    menu:

    # OPTION 1 

        "Oblivion.":

            vivi  "Oblivion. I kind of like the idea that we just fade away into the ether when everything's said and done. It's like finally being able to rest after a long day's work."

            darius sad "It's a very appealing option to many. It was for me as well, long ago."

            darius sad "But doesn't it bother you? The idea that things are left unsaid, apologies left unmade?"

            vivi "Not entirely. The same fate awaits us all, and we can't make every wrong right again."

            vivi "Besides, that's assuming this place is really what that conductor claims it is. Which I'm not that sure of, personally."

            darius neutral "I see."

            # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."


    # OPTION 2 

        "Rebirth.":

            vivi "Rebirth."
            vivi  "I like the idea that we are reborn in some way. It's a comforting thought that life never truly leaves, it just renews itself."

            darius happy "I feel much the same way. The opportunity to take what you've learned with you in some form, to grow and try again? It's a welcome fate."

            vivi "Interesting that you assume that we could take our past experiences with us. What if we couldn't? Would you still be so interested?"

            vivithinking "Were they always fidgeting with their hands like that?"

            darius sad "You're right, that was rather optimistic of me." 

            darius neutral "I would still be interested, even if it meant losing the experiences I've had. I suppose in some cases, that would even be a better outcome."

            vivi "That's assuming that this place is really what the conductor claims it is. Which I'm not that sure of, personally."

            darius neutral "I see."

            # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."


    # OPTION 3

        "Something else.":

            vivi "Something else."
            vivi "I don't think either of those are really true. I think whatever comes after is just another form of life. We might not know what it is exactly, but it doesn't make it any less than this stage."

            darius surprised "Fascinating. I've never considered that perspective."

            darius neutral "A clean slate, a new experience... that doesn't sound terrible."

            vivi "That's assuming that this place is really what the conductor claims it is. Which I'm not that sure of, personally."

            darius neutral "I see."

            # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    # OPTION 4 

        "Doesn't matter.":

            vivi "Doesn't matter."
            vivi "It's pointless to prefer one or the other. If it is the case that the conductor is telling the truth, then we'll find out soon."

            vivi "Why place assumptions and hopes on something we have no control over? It'll only hurt you in the long run."

            darius sad "Hmm. I suppose you're right. My apologies."

            vivi "No need to apologize. It's just that in my experience, hope can keep you going but it can just as easily end you. I'd rather focus on what I can do now."

            darius sad "A very wise statement."

            # JUMP TO: darius "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    darius neutral "Thank you for this conversation. If you don't mind, I'd like some time to think to myself."

    vivi "Sure. Thank you for being open to my questions."

    darius "Anytime, Ms. Sanssouci."
    # JUMP TO: Denial 2.1 NPC scene Ava and Darius
    stop music fadeout 1.0
    jump denial_fr1_ava_darius