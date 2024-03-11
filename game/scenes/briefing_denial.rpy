define freeroam1ava = False
define freeroam1darius = False
define freeroam1susu = False
label briefing_denial:

    scene bg cabin
    show urshu neutral at right

    # SOUND: knocking
    #play sound knocking

    vivithinking "Uhhh…"
    vivithinking "Did I faint yesterday?"

    urshu neutral "Miss Sanssouci, the Ouroboros Express waits for no one. Least of all a reporter. Do you have a moment?"

    show vivi angry at left
    vivi "Conductor! Why not? Got nothing but time here, right?"

    # SOUND: laughing & Urshu surprised
    play sound laugh
    show urshu surprised at right
    vivi neutral "What’s so funny?"

    urshu neutral "I apologize, Miss Sanssouci, for not informing you earlier. The cosmic cycle of life and death and life again spirals faster than any of us like to admit."
    urshu "I digress, Miss Sanssouci, I came to check on you. Last night’s excitement did not, ah, sit well with you."
    vivi neutral "To say the least…"
    urshu neutral "I was concerned that yesterday’s revelations, on top of your potential temporal distress, were contributing to a less than ideal mental state."
    vivi angry "You’re talking in circles, Conductor. Temporal distress?"

    # CHOICE
    urshu neutral "Come now, did you not notice your new sets of crow’s feet?"
    menu:
        # OPTION 1
        "Crow’s feet? My skin is perfect. What the hell do you mean?":
            vivithinking "He is pointing at the mirror."
            vivi neutral "What’s wrong? Let me have a look at myself."
            vivithinking "HUH?"
            vivithinking "What are these gross flakes protruding off my skin?!"
            vivithinking "They’re shining like wet scales."
            vivithinking "I think I’m going to throw up."
            vivi surprised "Explain this."

            # CHOICE
            urshu neutral "Would the good lady like a story? I am happy to indulge, if your quickly deteriorating time allotment permits?"
            menu:
                #OPTION 1
                "Go on, already. A story might lift my crow’s feet.":
                    vivi neutral "Go on, already. A story might lift my crow’s feet."
                    urshu happy "Once, long ago, I was in the doldrums of an ordinary immortal career...ferrying souls to and fro. From mortal realms to eternal gardens or places eternal but foul."
                    # SOUND: sighs
                    play sound sigh
                    urshu neutral "One such soul was in great need of me at a time where I was under heightened supervision. My...managers were unhappy with me. This soul begged of me a great favor…"
                    urshu angry "And did so after they ruined something of mine! It was audacious! But this soul only did what they thought was right, for they were in a dire time…"
                    urshu neutral "I was in great conflict about it. I had my own life to keep afloat, and this soul’s request would certainly sink it. I had a choice."
                    # CHOICE
                    urshu neutral "Ah…forgive me. I ramble. Shall I go on, Miss Sanssouci?"
                    menu:
                        # OPTION 1
                        "I gotta know how this vague story ends.":
                            vivi neutral "I gotta know how this vague story ends."
                            urshu happy "Wonderful!"
                            urshu neutral "I acquiesced to the request. I gave this soul what they asked for. And earned trust and recognition. In my dire straits, I had a companion - a lovely one - but I paid an eternal price for it."

                            # CHOICE
                            urshu sad "I could never return home."
                            menu:
                                # OPTION 1
                                "Being here, I feel what you mean…":
                                    vivi sad "Being here, I feel what you mean…"
                                    urshu happy "Thank you for saying so! But not all was lost. That daring soul I aided? They invited me to their domain and I gained a new home. A safe one…"
                                    # CHOICE
                                    urshu neutral "Is that not a wonder? A tribulation transfigured into triumph? Are you not yourself in dire straits, Miss Sanssouci?"
                                    menu:
                                        # OPTION 1
                                        "I might be.":
                                            vivi sad "I might be."
                                            # CHOICE 
                                            urshu neutral "Be sure to share your life with others, before the metaphorical cosmic iceberg capsizes you."
                                            menu:
                                            #OPTION 1
                                                "Urshu, are you being cute?":
                                                    vivi neutral "Urshu, are you being cute?"
                                                    urshu happy blush "Cuteness is next to godliness, as they say."
                                                    hide urshu
                                                    vivi neutral "Share my life boat, eh? Let’s go make some friends before I have a cosmic Titanic on my hands…"
                                                    jump character_selector_1
                                                    #Jump to Character Selector 1

                                            #OPTION 2
                                                "You think you’re funny, don’t you?":
                                                    vivi neutral "You think you’re funny, don’t you? Crow’s feet, vague stories, cryptic metaphors…"
                                                    urshu happy "I think I’m just cosmical. I bid you adieu, Miss Sanssouci."
                                                    hide urshu
                                                    vivi neutral "Cosmical? Com-ic-al? Jesus. I better leave before he comes back."
                                                    jump character_selector_1
                                                    #Jump to Character Selector 1
                                        # OPTION 2
                                        "Your storytelling needs work. For one, you buried the lead. For two, your story is a fluff piece. No meat to it.":
                                            vivi neutral "Your storytelling needs work. For one, you buried the lead. For two, your story is a fluff piece. No meat to it."
                                            jump urshu_kinder
                                            # JUMP to urshu saying "I hope you have a kinder…"
                        # OPTION 2
                        "No. You’re wasting the time I’m apparently running out of!":
                            vivi angry "No. You’re wasting the time I’m apparently running out of!"
                            # JUMP to vivi saying "I’m not dying. It can’t really be the end…"

                    # OPTION 4
                "Fuck you! You just said I’m running out of time!":
                    vivi angry "Fuck you! You just said I’m running out of time!"
                    label urshu_kinder:
                    urshu sad "I hope you have a kinder word for your fellow travelers, Miss Sanssouci. Since time is our master, you should know that you are all on short leashes."
                    vivi neutral "Next you’ll tell me to sit, stay…"
                    urshu neutral "Fetch, rather, fetch the truth of your circumstances here. I’ll even give you a treat, if you do."
                    hide urshu
                    vivi neutral "Sure, I’ll fetch the truth…fetch it right up your ass."
                    jump character_selector_1
                    #JUMP to Character Selector 1
        # OPTION 2
        "I’m not dying. It’s not the fucking end. Come on, why else would we get another chance here?":
            label vivi_not_dying:
            vivi angry "I’m not dying. It can’t really be the end. Come on, why else would we get another chance here?"
            urshu neutral "All mortals resist the end. But it’s the truth, Miss Sanssouci. In life, it was your sole mission to find that indelible substance."

            # CHOICE
            urshu neutral "Might it be time to seek truth before decides to hunt you?"
            menu:

                # OPTION 1
                "I’m done with this, Urshu. Go rain on someone else’s cosmic parade…":
                    vivi angry "I’m done with this, Urshu. Go rain on someone else’s cosmic parade…"
                    jump urshu_kinder
                    # JUMP to Urshu saying "I hope you have a kinder word for your fellow travellers…"

                # OPTION 2
                "The hell does that mean?":
                    vivi neutral "The hell does that mean?"
                    urshu neutral "Tick tock, Miss Sanssouci. If you need me, ever, give a shout."
                    hide urshu
                    vivi neutral "The truth will hunt me? I don’t even want to know what that means. Better get a move on."
                    jump character_selector_1
label character_selector_1:
    scene bg cabin
    show vivi neutral at left
    if freeroam1ava and freeroam1darius and freeroam1susu:
        jump character_selector_2
    vivi neutral "This is all so much to process. I can’t breathe. I need to talk to one of the other passengers. They might know what's going on here."

    #CHOICE
    vivi neutral "But which passenger should I talk to?"
    menu:
    #OPTION 1
        "Avatar of Asha" if not freeroam1ava:
            vivi happy "Who better to help me than a goddess? She’s gotta know where this train is going and how to get off. I think she’s in the observatory."
            jump free_roam_1_ava

    #OPTION 2
        "Inquisitor Darius Wrecker" if not freeroam1darius:
            vivi happy "The inquisitor looks like they would understand what's going on. Maybe they know where this train is going. I think they’re in the lounge."
            #JUMP to Free roam 1 / Darius Wrecker
            jump free_roam_1_darius

    #OPTION 3
        "Susu’Rha Balrinn" if not freeroam1susu:
            vivi happy "The druid seemed easy to talk to. Maybe they can help me figure out what’s going on. I think they’re in the dining car."
    #JUMP to Free roam 1 / Susu’Rha Balrinn
            jump free_roam_1_susu
label free_roam_1_ava:
    $ freeroam1ava = True
    scene bg observatory
    show ava sad at left
    vivithinking "I stroll into the observatory and who do I see staring out the window into darkness but the sun goddess herself"
    show ava surprised at left
    play sound scoff 
    show ava happy
    vivithinking "Oh, she’s noticed me. So imposing~"
    ava happy "Hello, little one. Has our radiance tempted you today? Come, sit with us for a moment." #blush
    vivithinking "When she says it like this. It’s not like I can say no."
    #CHOICE
    ava neutral "Your sandal has a pebble, little one?"
    menu:
        "She’d know where we’re headed and how to escape.":
            vivithinking "She’d know where we’re headed and how to escape."
            vivi surprised "Where do you think we’re really headed? Or how to escape?"
            ava happy "Where are we going? A destination. The train will stop, we will leave.."
            vivi neutral "Not very specific."
            ava happy "Correct. For how can we tell you what we do not yet know?"
            vivithinking "What is wrong with her?"
        "I wonder what she saw in the window.":
            vivithinking "I wonder what she saw in the window."
            vivi happy "I’m a little overwhelmed by everything going on. What are you looking at?"
            ava happy "We exist to spread the light of knowledge. We have looked into the darkness. Above us." #blush
            vivi scared "What’d you see?"
            ava scared "A cold void stares back at us. A sun, black as night. Inescapable emptiness."
            vivi scared "How terrifying!" 
            ava neutral "Perhaps it was just our imagination, hm?"
    vivi neutral "Beats me!"
    #CHOICE
    ava sad "The pebble remains. Speak your mind."
    menu:
        "I should share my worries with her.":
            vivithinking "I should share my worries with her."
            vivi surprised "I don’t even know what to think anymore…this whole journey has thrown me for a loop. I mean, if the conductor was telling the truth, then are we all really dead…?"
            ava neutral "We can understand why you feel that way, but the Avatar shall not perish before twenty and five years! It is as obvious as the sunrise. We can still feel the Goddess’ power surging through us."
            vivi surprised "But maybe we really are gone. You’d think I’d remember dying! Maybe that’s why we’re here…to come to terms with…with this."
            play sound scoff
            ava angry "(scoffs) Silly mortal… But..we know how you feel. We scarcely recall boarding this train; home one moment, here the next. Why has our memory forsaken us?…ugh! Let us speak of other things."
        "I should interview her for more info.":
            "I should interview her for more info."
            vivi neutral "I’ve been tasked by my editor with taking a deep dive into this mysterious Ouroboros Express. How has this luxury liner been for you?"
            ava neutral "Let us bring Light to your darkness. Besides last night, the journey, like so many, has been pleasant."
    vivi neutral "I can’t imagine we’re actually dead… I mean we’re still breathing, eating, and drinking! If that’s not alive, then I don’t know what is."
    ava neutral "Ridiculous. Of course we are alive. Look around you. Breathe. Have a drink and calm those nerves of yours."
    # CHOICE
    ava happy blush "What say you, little one?"
    menu:
        "Drink, yes? Little one? No!":
            "Drink, yes? Little one? No!"
            vivi happy blush "Another time! But please stop calling me \"little one.\" I’m thirty."
            ava sad blush "Ah. Our words have offended. A thousand pardons." 
            ava happy blush "We admire you standing up for yourself. It is…appealing."
            ava happy "May the Goddess guide your travels. The All is the One."
            vivi happy "Thanks, Asha! May the Goddess guide your journey too."
        "More of the cat chasing its tail.":
            "More of the cat chasing its tail."
            vivi neutral "Maybe later. Thank you for listening, Asha. I’ll keep you updated with my investigation as it progresses."
            ava neutral "May the Goddess guide your travels. The All is the One."
            vivi neutral "Sure thing, sunshine. See ya."
    vivithinking "That was interesting. Wonder what’s next…"
    jump character_selector_1 
label free_roam_1_darius:
    $ freeroam1darius = True
    scene bg lounge
    show vivi neutral at left
    show darius neutral at right
    vivi "{i}Darius is doing their best to fill out that loveseat. Even in such a casual position, they’re so graceful. Guess that’s the benefit of that mindflayer physique.{/i}"
    vivi "Excuse me, it’s Darius, right?"
    darius surprised "Yes."
    vivi "{i}They seem surprised. Loner type maybe?{/i}"
    darius neutral "I’m surprised you walked over to me of all people. Surely the goddess or dragon would be more approachable? Not many humans would chat up a mindflayer like you just have."
    vivi "{i}Bingo on the loner call.{/i}"
    vivi "You seem approachable enough. I actually had a question if you don’t mind."
    darius neutral "Go ahead."
    vivi "{i}If anyone has a good idea what the hell is going on here, it has to be the mindflayer, right?{/i}"
    vivi  "Tell me, you must have experience with otherworldly phenomena, right?"
    darius neutral "In a sense. This whole situation is unlike anything I’ve seen however."
    vivi "{i}Crap. Swing and a miss.{/i}"
    vivi  "Interesting. Do you believe him then? That this is some sort of intermission before we all die?"
    vivi "{i}Their… phalanges? Tentacles? Whatever they are. He keeps them hidden from me. Strange.{/i}"
    darius neutral "I’m not entirely sure, but he’s given us no reason to doubt. We should find out soon regardless."
    #vivi angry "{i}Real charmer, this one. Who knows if this is some sort of trap, a messed up fantasy for this conductor? Are we supposed to just take him at his word?.{/i}"
    # CHOICE
    darius neutral "Now that you mention it, I am… curious. What do you make of this \"Urshu’s\" claim that we must come to terms?"
    menu:
        "I’m not sure.":
            vivi  "I’m not sure. The man speaks in riddles, and I can’t make heads or tails of them right now."
            darius neutral "That is understandable. Last night was a shock to be sure."
            vivi "Is that something you’re interested in? Coming to terms?"
            darius neutral "You could say that. The details of my life are still cloudy but they’re coming back slowly. I’m sure the same goes for you?"
            vivi "Yes, some things are coming back slowly."
            vivi "{i}There’s a pain in their voice, it’s almost… melancholic?{/i}"
            vivi "If you don’t mind me asking, what happened—"
            darius neutral "Ahem…"
        "It’s nonsense.":
            vivi  "It’s nonsense. If we’re dead, we’re dead. There is no coming to terms."
            darius sad "Hmm. I suppose so. Apologies for the foolish question."
            # vivi sad blush "{i}Oops. I get the feeling I might’ve offended them somehow.{/i}"
            vivi neutral "Of course, if that’s what you’re looking for, there’s nothing wrong with that!"
            darius sad "No no, you’re right. There’s no chance of redemption if we’ve passed already."
            # vivi surprised "{i}Redemption?{/i}"
        "It’s interesting.":
            vivi "It’s a thinker, that’s for sure. If you’re into that, then I guess there’s some merit to it. I don’t know about you though, but I can’t \"come to terms\" here of all places."
            darius surprised "Interesting. I wouldn’t have expected that answer from you. Thank you for humoring me."
            # vivi surprised "{i}What does THAT mean? You don’t know me. Unless… oh god, are they reading my mind?{/i}"
            darius happy "Wondering if I’m reading your mind are you?"
            #vivi surprised blush "So you ARE then!"
            darius happy "Hah, I don’t rely on such cheap tricks. I’m naturally quite skilled at reading people you see."
            vivi "{i}Is that a hint of annoyance I sense?{/i}"
            vivi "So then, what do you see when you look at me?"
            darius blush "I— uhh, erm… my detective skills are a bit off today, you see. Try asking me again tomorrow, I’m sure I’ll have a better answer for you."
            # vivi happy "{i}Who knew mindflayers could get flustered. And even a little cute?{/i}"
    darius neutral "Enough about that for now. Don’t you find this train strange?"
    vivi "I suppose so. In what way exactly?"
    darius neutral "The way it bends, twists, almost shifts to the eye, as if it isn’t entirely there. Have you noticed it too?"
    vivi "I’ve noticed some oddities yes, but I chalked that up to the conductor pulling some tricks. Do you think there’s something more to it?"
    darius neutral "Possibly, yes. It’s just as much a mystery to me as that conductor is."
    vivi "{i}Their words are somber yet curious. It’s soothing to listen to.{/i}"
    vivi "Where do you think we’re going?"
    darius "In my… religion, we believed that oblivion was at the end of it all. Maybe this train is leading us to that."
    vivi "{i}Do mindflayers have religions? No, that’s probably a dumb question.{/i}"
    vivi "You seemed interested in making amends before. What’s the point if you’re headed for oblivion regardless?"
    darius "That’s… a little too complex a topic for me to get into right now. I apologize."
    # CHOICE
    darius "That being said though, which would you prefer awaits us at the end of this little trip? Oblivion, or some sort of rebirth?"
    menu:
        "Oblivion.":
            vivi  "I kind of like the idea that we just fade away into the ether when everything’s said and done. It’s like finally being able to rest after a long day’s work."
            darius sad "It’s a very appealing option to many. It was for me as well, long ago."
            darius sad "But doesn’t it bother you? The idea that things are left unsaid, apologies left unmade?"
            vivi "Not entirely. The same fate awaits us all, and we can’t make every wrong right again."
            vivi "Besides, that’s assuming that this place is really what that conductor claims it is. Which I’m not that sure of, personally."
            darius neutral "I see."
        "Rebirth.":
            vivi  "I like the idea that we are reborn in some way. It’s a comforting thought that life never truly leaves, it just renews itself."
            darius happy "I feel much the same way. The opportunity to take what you’ve learned with you in some form, to grow and try again? It’s a welcome fate."
            vivi "Interesting that you assume that we could take our past experiences with us. What if we couldn’t? Would you still be so interested?"
            vivi "{i}Were they always fidgeting with their hands like that?{/i}"
            darius sad "You’re right, that was rather optimistic of me." 
            darius neutral "I would still be interested, even if it meant losing the experiences I’ve had. I suppose in some cases, that would even be a better outcome."
            vivi "That’s assuming that this place is really what that conductor claims it is. Which I’m not that sure of, personally."
            darius neutral "I see."
        "Something Else.":
            vivi "I don’t think either of those are really true. I think whatever comes after is just another form of life. We might not know what it is exactly, but it doesn’t make it any less than this stage."
            darius surprised "Fascinating. I’ve never considered that perspective."
            darius neutral "A clean slate, a new experience… that doesn’t sound terrible."
            vivi "That’s assuming that this place is really what that conductor claims it is. Which I’m not that sure of, personally."
            darius neutral "I see."
        "Doesn’t Matter.":
            vivi "It’s pointless to prefer one or the other. If it is the case that the conductor is telling the truth, then we’ll find out soon."
            vivi "Why place assumptions and hopes on something we have no control over? It’ll only hurt you in the long run."
            darius sad "Hmm. I suppose you’re right. My apologies."
            vivi "No need to apologize. It’s just that in my experience, hope can keep you going but it can just as easily end you. I’d rather focus on what I can do now."
            darius sad "A very wise statement."
    darius neutral "Thank you for this conversation. If you don’t mind, I’d like some time to think to myself."
    vivi "Sure. Thank you for being open to my questions."
    darius "Anytime, Ms. Sanssouci."
    jump character_selector_1
label free_roam_1_susu:
    $ freeroam1susu = True
    scene bg diningcar
    # play sound footsteps
    show susurha happy at right
    vivithinking "Wait."
    vivithinking "Susu’Rha? What are they doing?"
    vivithinking "Are they literally feasting on a slice of cake?"
    vivithinking "Okay, that’s cute."
    # play sound traindoor
    # screen shake transition
    show susurha surprised at right
    # play sound forkdrop
    susurha neutral "Oh my… are you as hungry as I? I too get flustered when I haven’t eaten all day."
    show vivi neutral at left
    #SOUND: Vivi sighs.
    vivi neutral "I’m not hungry. I’m…"
    menu:
        "I’m fine.":
            vivi "I’m fine."
            susurha "Are you positive?"
            vivi "Yes, I’m positive. There is just a lot on my mind at the moment."
            susurha "Mmmhmm… That much I can glean."
        "Honestly, I don’t know.":
            vivi "Honestly, I don’t know."
            show susurha sad
            susurha sad "Yeah, I get that too. I’m…"
            show susurha happy
            susurha happy "Well, I’m here doing what I know can lift the spirits."
        "Are you eating cake right now?":
            vivi "Are you eating cake right now?"
            susurha "Ah yes, I am and this angel food cake is quite delectable. I wonder if that angel beauty had anything to do with this being here."
            susurha "..."
            susurha "I do hope that you aren’t judging me."
            vivi "I’m not."
            susurha "Good."
    susurha happy "Here. Join me and enjoy a slice."     
    vivithinking "Deep breaths."
    #SOUND: Vivi inhales and exhales.
    vivithinking "Alright, let’s just sit down and chill."
    vivithinking "What’s the worst that can happen?"
    #SOUND: Vivi takes a seat at the table.
    vivithinking "They gracefully cut a slice of cake and nudge it my way. I take a fork and take a bite."
    vivi happy "Oh my goodness, this is amazing."
    susurha happy "I told you. The Archdruids back in the living forest can’t even dream of conjuring such savoury delights. This angel food cake is to die for."
    show susurha neutral
    show vivi neutral
    vivithinking "..."
    vivithinking "..."
    vivithinking "Oh no…"
    vivithinking "Awkward silence alert…"
    susurha "Please tell me you weren’t paying attention to that Urshu fellow the other day when he was spouting off about…"
    menu:
        "Urshu has no idea what he was rambling about.":
            vivi "Urshu has no idea what he was rambling about."
            susurha happy "Ah… music to my ears. So clearly I haven’t found myself entirely surrounded by those more insane than I."
            vivi "No, I am very much sane, but this place is testing that."
            susurha happy "I couldn’t agree anymore."
            susurha happy "Hehe."
            susurha happy "Dead…"
            susurha happy "My father could have told better crafted jokes than that back home."
            susurha sad "Hmm."
            show vivi sad
        "How could I not? I can’t stop thinking about it.":
            vivi "How could I not? I can’t stop thinking about it."
            susurha angry "Uh…. Wrong answer. Not quite what I was looking to hear. Thank you very much. Now please tell me that the next thing that you utter isn’t just echoing…"
            vivi "I don’t know. What if we are truly dead?"
            susurha neutral "That."
            susurha "Great, everyone has gone mad and I’m soon to join them."
            vivi "Are you telling me that you haven’t thought about the possibility?"
            susurha "No ma’am, I haven’t. I would very much be aware if I was dead. I’d either be roasting in an abyss of flames with like-minded individuals or be experiencing the sweet void of nothingness."
            susurha "NOT some poorly designed metallic tube flying to who knows where."
            Susurha sad "I… I don’t know."
            vivithinking "Oh wow. They’re breaking."
            show susurha neutral
    susurha sad "I’m sorry…"
    susurha sad "I really know how to go and spoil a mood, don’t I?"
    "Susu’Rha slides the entire cake dish to my side of the table."
    susurha sad "I’ve lost my appetite."
    susurha neutral "Please do enjoy what you can of it. I’d hate to see it waste away."
    susurha "...I think I’m going to go lay my head down and not think."
    menu:
        "Are you okay?":
            vivi "Are you okay?"
            show susurha happy
        "Alright.":
            vivi "Alright."
            show susurha sad
    hide susurha
    vivithinking "Hey! Oh no, they’re leaving!"
    vivithinking "Well…"
    #SOUND: Door closes.
    #SOUND: A headache inducing ringing echoes.
    vivithinking "Ugh… my head feels like something is crawling at the walls of my skull."
    vivi "I think that was enough for me too."
    vivi "I better head back to my cabin and collect myself."
    jump character_selector_1


define freeroam2ava = False
define freeroam2darius = False
define freeroam2susu = False
label character_selector_2:
    if freeroam2ava and freeroam2darius and freeroam2susu:
        jump denial
    scene bg cabin
    show vivi neutral at left
    vivi neutral "That was… interesting. Looks like I wasn’t the only one blindsided by this train. I need some time to gather my thoughts."
    # Fade to blur if possible.
    "Outside the window, surreal landscapes blend into a swirl of colors and the train's breathtaking speed blurs known realities. The view slowly darkens as time passes."
    # Fade back in.
    vivi sad "This can’t be happening."
    vivi sad "Are we all dead for real?"
    vivi angry "It can’t end like this. I want out."
    vivi neutral "How can I escape this train?"
    #CHOICE
    vivi neutral "I should go talk to someone else. I can’t be the only one who wants off this ride."
    # Note that whoever you talked to in free roam 1 should be unavailable as an option.
    menu:
        "Avatar of Asha" if not freeroam2ava:
            vivi happy "That’s right. I should try the ‘goddess’!Who better to help me than a goddess? I think they’re in the lounge."
            jump free_roam_2_ava
    
        "Inquisitor Darius Wrecker" if not freeroam2darius:
            vivi neutral "The inquisitor is probably the best brain here.The inquisitor looks like they would understand what's going on. I think they’re in the lounge.Now, where are they? Let’s try over here..."
            jump free_roam_2_darius
    
        "Susu’Rha Balrinn" if not freeroam2susu:
            vivi neutral "I feel like the druid wants out tooThe druid seemed easy to talk to. Maybe they can help me figure this all out. I think they’re in the lounge."
            jump free_roam_2_susu
label free_roam_2_ava:
    $ freeroam2ava = True
    scene observatory
    show vivi neutral at right
    vivithinking "Pondering an escape route, I stroll into the observatory and who do I see staring out into the darkness but the Sun Goddess herself!"
    vivi happy "Hey Ash, I think I found us a way out of this bi-"
    ava angry "You may refer to us as Asha or Avatar of the Eternal Light,…but your proposition has intrigued us. Proceed."
    vivithinking "Jeez! Stick up your ass much?!"
    vivi neutral "I’ll go grab the others!"
    ava surprised "Those poor creatures? Pay them no mind. Their only worry is their own insignificance."
    vivithinking "What a self-important $@#*& this Avatar of Ass is!"
    ava sad "Like sand in the wind."
    vivithinking "Who does she think she is?"
    menu:
        "Asha! Or Avatar! Whatever! How dare you!":
            vivi angry "Asha! Or Avatar! Whatever! How dare you!" 
            vivi angry "If you feel that way, why are we even speaking? I’m one of them, you know!"
            ava sad "Our humblest apologies, Vivi. We never intended to offend you. We have led vastly different lives, you see." #blush 
            vivi neutral "Well you’ve managed to offend me regardless." 
            ava neutral "Why don’t we talk about something else…you were saying earlier?"
        "Maybe we all matter, Asha.":
            vivi neutral "Maybe we all matter, Asha,"
            vivi sad "Maybe we're all just like specks of sand on a cosmic beach."
            vivi sad "Our lives only have the value we give it. Yours. Mine. Theirs."
            ava sad "There are times we wished for a simpler life. Family. Friends. Love, perhaps? All forbidden. Even tears."
            vivithinking "Damn! Even tears? Here I thought I was a hot mess."
            vivi sad "That must’ve been awful. Well, I’m here now, so dry those eyes."
            ava sad "Your heart speaks strangely, but with truth. Tears do not come easily to us. Thank you, Vivi." #blush
        "Asha, respectfully, I disagree with you.":
            vivi neutral "Asha, respectfully, I disagree with you."
            vivi neutral "Humans have identities, lives, and belief systems. Like you. We’re complex. Like you. And you’re no goddess. You’re just a woman calling herself one."
            ava happy "Really? In our world, humans are simple creatures incapable of conscious thought."
            vivithinking "Lord forgive me I’m about to destroy this woman."
            vivi happy  "Well you’re speaking with me right now, are you not? I’m human. Would you say I’m incapable of conscious thought?" #blush
            ava surprised  "Well, when you put it as such…who are we to argue? We apologize." #blush
            vivithinking "About time, for chrissakes!"
    vivi happy "Yeah, so about that exit I mentioned…"
    vivi neutral "I spotted an emergency hatch in the glass above you. We can pop it open and escape. Look here at the window…"
    vivi surprised "What the hell is THAT…monster? It’s like the Morton’s Salt girl covered in tin foil and roasted under a jet engine?!"
    vivithinking "Like in my worst nightmares; I can’t move, I can’t breathe."
    ava neutral "Do you…jest? We see a cold abyss, pulsing with hunger and emptiness."
    show urshu happy at right
    urshu happy "You are both correct! Those are the spirits of passengers lost to the fabric of space-time. Or perhaps how you see them.. hard to say sometimes."
    vivi sad "Those poor souls…is there no help for them?" 
    ava sad "Is there no help for us?"
    urshu sad "None for them, I fear."
    menu:
        "Nightmarish. That’s the only word for it.":
            vivi surprised "Nightmarish. That’s the only word for it."
            vivi angry "And I want nothing to do with whatever that is."
            ava surprised "Were you not lamenting those same souls?"
            vivi angry "Since when do you care? There’s no point to all of this."
            urshu happy "Ah, but there is. That could be you one day."
            urshu neutral "So…"
        "Terrifying. I can’t imagine how it feels.":
            vivi sad "Terrifying. I can’t imagine how it feels."
            ava sad "A circular void haunts my every thought. We fear it."
            urshu happy "Best not to think too hard about it."
            urshu neutral "So instead…"
    urshu neutral "Do you..have any questions?"
    urshu happy " Anything about the Ouroboros Express you want to know..?"
    ava surprised "So are we truly dead? Our service to the Goddess has ended?"
    urshu neutral "‘All quite true. All of it. I wish I could offer better news, but on the Ouroboros Express your soul is bound for the afterlife."
    ava sad "But..this cannot be!"
    vivi sad "Oh, Asha! I’m so sorry. I would say I couldn’t imagine, but given the circumstances…"
    vivithinking "Oh my God, c’mon, Vivi, shut up, summon your inner reporter, and ask the Conductor something clever!"
    menu:
        "Can we get out of here?":
            vivi surprised "Can we get out of here?"
            urshu neutral "No, Vivi. Your lives belong to the cosmic fabric now. Tomorrow you will see, should any lingering doubt remain."
            vivi surprised "But how did I…?"
            urshu "Not important. The destination is."
            vivithinking "Maybe it’s not important to you, but why can’t I remember how I died?"
            vivi angry "Mind divulging our destination then?"
            urshu "The destination? Why, that is up to you, is it not?"
            vivithinking "Like getting blood from a turnip, this guy!"
            urshu neutral "Vivi, Asha, the universe does not decide your fate here; fate has placed the compass in your hands. Here and now."
        "So am I going to Hell, then?":
            vivi surprised "So am I going to Hell then?"
            urshu neutral "Depends. Were you good, deserving of reward, or a villain,destined to rot eternally in Hell? Hell! A silly tale to frighten ill-mannered children, at best."
            vivi surprised "So…Heaven?"
            urshu surprised "Heaven - what a noble concept. The word boring also comes to mind…"
            vivi angry "Fine, it’s not either one."
            vivithinking "Just like pulling teeth…"
        "Why do you do this job?":
            vivi sad "Why do you do this job?"
            urshu surprised "That is the first time anybody has asked me that! Well to be honest, the tale is long, so perhaps another time?" #blush 
            vivi sad "Oh…"
            urshu happy "In short, my destiny is to be on this train, one way or another."
    vivi sad "We all die, one way or another, so what’s the point of all this?"
    ava happy "The answer to that lies within you, Vivi."
    vivi neutral "Well, I cannot thank you both enough for this wonderful chat. Time to head back to my room, now."
    ava happy "See you soon, Vivi. The All is the One."
    ava sad "We have much to ponder. May your dreams be peaceful and warm."
    vivi neutral "Yeah yeah…you too, Asha."
label free_roam_2_darius:
    scene diningcar
    show vivi neutral at left
    show darius neutral at right
    vivi "{i}Darius is… drinking? Guess mindflayers need a break every now and then too.{/i}"
    vivi "Enjoying a drink?"
    darius surprised "Hmm? Oh, yes. Would you like one? I’m a bit of a lightweight."
    menu:
        "Sure.":
            # SOUND: glassclink
            darius neutral "There you are."
            vivi "Thank you."
            vivi surprised "{i}Is this… pina colada?{/i}"
            vivi happy "Didn’t think you had a sweet tooth."
            darius happy "It’s actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."
            darius sad "Mindflayers and hard alcohol… don’t mix."
            vivi "{i}They shudder at this, it ripples through their sleek frame like a gentle breeze. Gotta be  a story there.{/i}"
        "I’m okay, thank you.":
            darius neutral "Not a fan? That’s fine.I can make you a non-alcoholic version."
            # SOUND: glassclink
            vivi surprised "Fruits? I didn’t think you had a sweet tooth."
            darius happy "It’s actually one of the few drinks I can consume. Something about the sweetness helps dull the alcohol."
            darius sad "Mindflayers and hard alcohol… don’t mix."
            vivi "{i}They shudder at this, it ripples through their sleek frame like a gentle breeze. Gotta be  a story there.{/i}"
    vivi sad "{i}Why is the air here so… heavy?{/i}"
    darius neutral "Are you ok, Ms. Sanssouci? You look a little… sickly."
    darius surprised "Ahh! My apologies."
    vivi surprised "{i}A quick flick of the wrist, graceful as ever. Did he do something..? Things feel a lot lighter.{/i}"
    darius neutral "A mindflayer’s brain is a powerful thing. Sometimes emotions and thoughts can leak out into the atmosphere. I believe you may have been feeling my… malaise, so to speak."
    darius neutral "I don’t speak with humans often, so I’ve developed a bit of a bad habit of letting my emotions wander."
    vivi neutral "It’s alright, I figured you didn’t get to speak with humans much. You can just call me Vivi by the way, no need for formalities."
    darius neutral "Very well."
    vivi neutral "What had you so bothered?"
    darius sad "Well aside from some unpleasant memories... I’ve been thinking."
    darius sad "I have many questions about this place and this conductor. But I don’t believe asking him will get me any of them…"
    darius neutral "I’ve let myself fall into passivity too often, simply allowing the current to wash over me. This time, I’ll act."
    vivi neutral "{i}They want to act huh? Looks like we’re on the same page.{/i}"
    vivi neutral  "Listen, I was thinking about looking for a way off of this damnable train. What do you think?"
    darius neutral "Hmm. I’m not interested in leaving just yet, but I think there is a way our needs could both be met."
    darius neutral "I am going to trail the conductor. Should you wish, you could join me and look for any sign of an exit strategy."
    vivi surprised "Trail? Are you some sort of detective?"
    darius surprised "What? Ahem I’m— something like that, yes. I have the skills needed for the job, don’t you worry."
    vivi neutral "{i}What a weirdo. They seem pretty confident though, so I’ll take their lead on this. Nice to be able to rely on someone for once.{/i}"
    vivi happy "Sounds good to me. When did you want to start?"
    darius neutral "Well… now is as good a time as any, don’t you think?"
    vivi surprised "Straight to business then? Lead on."
    scene lounge
    show darius neutral at left
    show vivi neutral at right
    darius neutral "Stay behind me and follow my motions."
    vivi neutral "{i}Where is he?{/i}"
    hide darius
    hide vivi
    show urshu happy at left
    show vivi angry at right 
    #SOUND: whistling
    vivi angry "{i}Is he… whistling? This asshole has us captive here and he’s whistling?{/i}"
    hide urshu 
    hide vivi
    show darius neutral at left
    show vivi angry at right
    darius neutral "Calm yourself."
    vivi angry "Can’t you just ask your questions now and I’ll go off to look for an exit while he’s distracted?"
    darius angry "That isn’t what we agreed on. Besides, you’ve spoken to him. Do you really think he’d just give up his secrets so easily?"
    darius neutral "This is the best way to find out more. So please, it may be human nature to be quick to anger but calm yourself."
    vivi "{i}Those last words held an undercurrent to them. Like the rumble of an oncoming storm.{/i}"
    vivi angry "{i}Where the hell did that come from? They were pretty agreeable up until now.{/i}"
    darius neutral "Vivi, look."
    hide darius
    hide vivi
    show urshu happy at left
    urshu happy "Suppose it’s time to retire for the evening. Should do the rounds, ensure nothing is out of order."
    hide urshu
    show darius surprised at left
    show vivi surprised at right
    # SOUND: teleport
    darius surprised "Is that…"
    vivi surprised "Magic. Yeah I think so."
    darius happy "This is exactly what I wanted to see. Come, let’s pursue him."
    vivi happy "{i}Aww, their little mouth tentacles curl up when they’re happy.{/i}" #blush
    vivi angry "{i}What am I thinking? This isn’t the time Vivi!{/i}" #blush
    scene observatory
    show darius surprised at left
    show vivi surprised at right
    darius surprised "Been a while since I had to track a mage. Hopefully my senses are somewhat intact here."
    vivi neutral "{i}They’re a natural at this. I’m kinda curious to know more. Should I ask them?{/i}"
    menu:
        "Ask Darius":
            vivi neutral "Hey, how did you develop these skills anyways?"
            darius neutral "Oh, I was trained in observation since I was young. Making myself scarce, learning my target’s habits and routines. As for reading people, that comes rather naturally to mindflayers."
            vivi neutral "Cause of the whole mind reading thing?"
            darius neutral "Yes, there’s always that to fall back on. But we’re also very good at sensing emotional shifts, lapses in thought, lies."
            vivi neutral "Must come in handy as a detective."
            darius surprised "Yes, it’s uhh… very useful." # blush
        "Leave it be":
            darius neutral "You seem rather quiet back there."
            vivi neutral "Just looking out for any sign of an escape route."
    darius neutral "Found any sign of an escape yet?"
    vivi angry "No. It’s like nothing makes sense on this train, the doors just lead to more doors. There's no final car either. It’s almost like it just… keeps going."
    darius neutral "Hmm. If my hunch is correct, then there’s a good chance there is no escape from this train."
    vivi angry "What? So you think that Urshu is telling the truth?"
    darius neutral "Maybe part of it. There are things he’s keeping from us, of that I’m sure."
    vivi neutral "Hold on."
    vivi "{i}Speaking of hunches, I’ve got one of my own.{/i}"
    #I’d like Vivi to move to the right here and Darius to move to the left. Is that possible without making them disappear and reappear?
    darius surprised "Ms. Sanssouci, I didn’t take you to be one for stargazing, but this hardly seems the time for it."
    vivi neutral "Shut up. Haven’t you noticed that we can’t look out of any of the windows? They’re all fogged up, like we’re going through a snowstorm or something."
    darius neutral "Now that you mention it… that is strange."
    vivi happy "Exactly! But a telescope should be able to focus much farther. I want to see if I can…"
    # SOUND: crash
    vivi surprised "{i}What… what the fuck is that?{/i}"
    darius surprised "Vivi? You look like you’ve seen a ghost."
    vivi surprised "Just… just take a look for me will you? Do you see it? The weird… figure out there?"
    darius neutral "Very well. What kind of figure?"
    vivi angry "Just look! It’s in a dress but it’s like it has no torso or anything! It has some sort of mirror thing for a head!"
    darius surprised "I don’t see this figure you’re speaking of, but… oh my."
    vivi surprised "What? What do you see?"
    darius surprised "I… I knew it. This place… it is his."
    vivi surprised "{i}There's awe in those words but also something else. Fear?{/i}"
    show urshu neutral at center
    urshu neutral "Interesting! What do you see out there?"
    vivi surprised "Where the hell did you come from?"
    urshu neutral "I appear when I am needed my dear! Now Mr. Wrecker, I believe from your tailing of me tonight that you have something you desire. May it be related to what you see out there, I wonder?"
    darius surprised "You… are you not an ambassador of the Eternal Rest?"
    urshu surprised "Oh? And what would make you think that?"
    darius surprised "Out there… I could’ve sworn I saw its tendrils grasping out for me."
    urshu neutral "Ahh, now I see. I’m afraid to disappoint you Mr. Wrecker, but unfortunately that is not the case."
    urshu neutral "The cosmos holds many things, not all of them friendly. Some may draw themselves to you, while others may find another passenger more appealing. What you saw is simply one of those entities."
    vivi angry "{i}Are they really going to act like I’m not here? I have questions too you know!{/i}"
    menu:
        "Interrupt them":
            vivi angry "Excuse me? You’re going to answer my questions now."
            urshu neutral "I know asking questions is in a reporter’s nature, but is decorum not? Mr. Wrecker is clearly \"going through something\" as it were, so I’d appreciate your silence."
            vivi angry "I–" #blush
            vivi angry "{i}Scolded like a schoolgirl. I hate that he’s right.{/i}" #blush 
        "Remind Darius of his questions":
            vivi neutral "Darius, compose yourself. Didn’t you have some questions you wanted to ask him?"
            darius surprised "You’re right, Vivi. Thank you."
    darius neutral "I’ve been having… visions."
    darius sad "A loving couple, screams, confusion… I can’t make sense of it all."
    urshu neutral "I see. Tell me, how much of your… end, do you remember?"
    darius sad "My end?"
    urshu sad "I wasn’t lying to you. Any of you. All of you here have well and truly passed on from the world of the living."
    vivi neutral "{i}That sounded… honest. He can’t be serious, right? He can’t be…{/i}"
    urshu sad "As for you Mr. Wrecker, hmm. I promised I wouldn’t get involved in any of your journeys, but I believe showing you this will help."
    vivi neutral "{i}The conductor holds out his hand. Darius takes it.{/i}"
    #SOUND: twinkle
    #SOUND: horror
    darius surprised "What… WHAT IS THIS?"
    urshu sad "I understand this must be hard. But nothing I’ve shown you is an illusion. These were your choices, your actions."
    vivi sad "{i}I’ve never seen Darius like this before.{/i}"
    urshu sad "And as for you Ms. Sanssouci, I know this must’ve been hard for you as well. You may not believe it, but I am here to help you, you know."
    vivi sad "So it’s true then? We’re really gone?"
    vivi "{i}He simply nods.{/i}"
    vivi "{i}I… I don’t know what to say.{/i}"
    urshu neutral "Some advice, if I may? Many passengers find journaling to be a therapeutic experience. Have you started doing so? The supplies are all in your cabin."
    darius anger "Urshu. What was it all for then? Who am I anymore?"
    urshu sad "Unfortunately, I can’t answer that for you my friend. I'm sure you'll learn the answer yourself, in time."
    vivi "{i}The tension hangs in the air. It’s like a miasma, cutting the oxygen and making my heart pace.{/i}"
    urshu happy "...On a lighter note, we will be serving brunch tomorrow! Do come… well I'd say \"early\" but time has no meaning here anyways. Ta-ta!" 
    vivi "{i}The conductor begins to walk away.{/i}"
    hide urshu
    darius surprised "What?"
    vivi "{i}The air is getting thin, heated even. It’s just like before in the dining car. Darius is…{/i}"
    darius angry "Don't toy with me! COME BACK!"
    darius angry "I AM AN INQUISITOR OF THE LORD–"
    #They stop.
    darius sad "I… I suppose I'm not anymore." #blush
    darius sad "I'm sorry you had to see that. Thank you for joining me but I think I'll be going to bed now." #blush
    vivi "{i}Are they muttering to themselves?{/i}"
    darius sad "It was all pointless…"
    hide darius
    vivi sad "This is all too much… I need to sleep."

label free_roam_2_susu:
    scene lounge
    vivithinking "This train is driving me insane. I refuse to play into the conductor’s games."
    vivithinking "Yep. It seems Susu’Rha is lounging on one of the recliners."
    show vivi neutral at left
    vivi "What are you doing?"
    show susurha neutral at right
    susurha "What does it look like I’m doing at the moment? I’m deep in the meditative process of trying not to think about the circumstances that surround me."
    susurha "And girl… let me tell you that the cushions this contraption houses are just soooo…. Welcoming."
    susurha "You should give it a try."
    menu:
        "I’ll stand.":
            vivi "I’ll stand."
            susurha "Suit yourself but I see you weak at the knees. Eyes drawn to where I lay. The cushions calling your name."
            susurha "Vivi…"
            vivi "What?"
            susurha "I’m saying you look exhausted, but to each their own."
            vivithinking "Susu’Rha goes silent as they sink into their chair."
            vivithinking "Ouch. The headache is only getting worse."
            vivithinking "Perhaps this was a mistake."
        "I’d love to.":
            vivi "I’d love to."
            vivithinking "They reach out and slide a chair my way with ease."
            #SOUND: Vivi sits down in a super comfortable recliner.
            vivithinking "Holy shit…"
            susurha happy "Feels like a dream, don’t it?"
            vivi "Feels like I’m sinking."
            vivithinking "We sit in silence, enjoying the simple comforts."
            vivithinking "The headache eases off, only somewhat."
    susurha "This place is a prison."
    susurha "The Archdruids warned of daemons that kidnap their prey and treat them to endless luxuries."
    susurha "Perhaps this is that. We are being fed lies and comfort just so that we can become sooo relaxed and THAT is when they’ll strike…to feast on our satisfied souls."
    susurha "To be frank with you, I always believed such tales to be nothing more than a bunch of creative nonsense to make the less fortunate in the clan okay with their shitty life conditions."
    susurha "But…"
    susurha "I’m beginning to think that those sad old sods that lived in a forest their entire lives weren’t completely high as the stars above."
    menu:
        "This place freaks me out.":
            vivi "This place freaks me out."
            susurha "I feel that in my bones. Oh, this place worms its way down my spine like a spider in the night."
            susurha "Makes me feel like burning the whole place down."
            susurha "Imagine…"
            susurha "You’re walking in the woods one day, lost in the spiraling storm of every possible thought you’ve ever had bouncing around in your head, and then… "
            susurha "Suddenly finding yourself trapped with a bunch of odd looking individuals, no offense, in a metal tube speeding to an unknown locale."
            susurha "All the while you’re being told that…"
            susurha sad "You are dead."
            vivi "Is that how you died? I mean ended up here."
            susurha "How you’d figure that?"
        "That’s absurd. That can’t be the case.":
            vivi "That’s absurd. That can’t be the case."
            vivithinking "..."
            vivithinking "He’s glaring at me. Looking me up and down."
            susurha angry "Let me tell you what is absurd." 
            susurha angry "You’re walking in the woods one day, lost in the spiraling storm of every possible thought you’ve ever had bouncing around in your head, and then…"
            susurha "Suddenly finding yourself trapped with a bunch of odd looking individuals in a metal tube speeding to an unknown locale."
            susurha angry "All the while you’re being told that YOU ARE DEAD."
    susurha neutral "We will be dead if we stay here any longer."
    vivi "We need to get out of here."
    vivithinking "He raises a nonexistent eyebrow. Now I’ve got their attention."
    susurha happy "Now that is something I absolutely LOVE hearing. Please tell me you have some sort of idea of getting off this thing."
    vivithinking "..."
    vivi "I do not."
    susurha neutral "Hmm…"
    susurha happy "Well, lucky for you, I have been indulging in some… sightseeing around this fine place and I think I know just the perfect spot for us to run away together."
    vivi happy "Where?"
    susurha happy "The observatory with a venue that only holds glass windows from the outside world."
    susurha happy "Oh, I do so very much love gazing up at the stars above like I did when I was a young prince."
    vivi happy "Now?"
    susurha happy "Why wait?"
    vivi happy "Are we really doing this?"
    susurha happy "Sweetie, It’s a date."
    vivithinking "They take me by the hand and drag me along through the various train cars to the observatory."
    scene observatory
    show susurha surprised at right
    show vivi surprised at left
    vivithinking "Golden fiery flashes shine through the glass windows of the cabin, and in-between those sparkles of light…"
    vivithinking "Darkness."
    vivithinking "Where are we?"
    show vivi neutral
    susurha surprised "So strange, when I was just here I saw the night sky riddled with an ocean of stars, but now… it’s just nothing."
    menu:
        "Worried?":
            vivi "Worried?"
            show susurha neutral
            #SOUND: Susu’Rha scoffs.
            play sound scoff
            susurha "Me, worried? Never. I make sure to go out of my way to avoid feeling worried, but this…"
            susurha "It just doesn’t make sense.  I was so sure I knew what I saw. It had the same constellations burned into my mind from that night and…"
            susurha "It hasn’t even been an hour since I scouted the place."
            susurha "Where are we?"
            vivi "I was thinking the same thing."
            susurha happy "I suppose there is only one way to find out."

        "Where is this exit you sold me?":
            vivi "Where is this exit you sold me?"
            susurha neutral "Forgive me."
            vivithinking "..."
            susurha "Doesn’t matter."
    susurha "This way."
    susurha "Help me stack these chairs up under that central window on the ceiling."
    #SOUND: Vivi and Susu’Rha exert themselves stacking chairs on top of each other.
    vivithinking "..."
    vivithinking "This seems incredibly unplanned, but I don’t really have a choice."
    vivithinking "I need to get off this train."
    vivithinking "And this one is my best chance."
    susurha happy "This reminds me of back when I was younger and I’d sneak out of my tower bedroom to wander on top of the surrounding castle walls."
    vivithinking "Susu’Rha climbs the tower of stacked chairs and wrestles with the loose screws of the ceiling window. The golden light is glistening off his scaly skin."
    vivithinking "I wonder how it is, living in a castle…"
    vivithinking "All I can see upon his face is the biggest smile I’ve ever seen."
    menu:
        "Can we please hurry this up?":
            vivi "Can we please hurry this up?"
            #SOUND Susu’Rha scoffs.
            play sound scoff
            susurha neutral "You know you remind me a lot of the nobility that I grew up around."
            susurha "They too found my voice to be annoying."
            vivi "That’s not what I meant."
            susurha "Nevertheless, they listened as I slowly found my way out of that hell."
            vivithinking "Aha… Susu’Rha appears soft, but they actually have a nerve…"
        "It sounds like you lived a fairy tale.":
            #SOUND: Susu’Rha laughs.
            play sound laugh
            susurha "I suppose from the outside it could come across with that poetic fantasy allure."
            susurha neutral "Apologies, I believe you were cracking a joke at me."
            menu:
                "I wasn’t. Tell me more.":
                    vivi "I wasn’t. Tell me more."
                    susurha happy "Perhaps I shall at another time."
                "It’s okay.":
                    vivi "It's okay."
    susurha happy "Voila."
    #SOUND: The window clicks open.
    susurha happy "We are homeward bound."
    hide vivi
    hide susurha
    vivithinking "I climb up the tower of chairs and we both peak our heads out of the opened window."
    vivithinking "..."
    vivithinking "This is…"
    vivithinking "Unimaginable."
    vivithinking "Spiraling celestial bodies swirl all around as the train speeds faster than anything I’ve ever seen."
    vivithinking "Flames burst from the train’s tracks and were sucked into the void."
    vivithinking "My hair flaps in my face. I really wanna scream. But I can’t."
    vivithinking "Susu’Rha stares out into the visual abyss of…wherever we are. They mumble to themselves but I can’t hear anything."
    vivithinking "All I could get was the sight of a tear rolling down their cheek."
    vivithinking "I turn to see what they are staring at and I see…"
    vivithinking "That thing."
    vivithinking "A reflective dress floating in the wind, but it slowly inches closer to us."
    vivithinking "It moves with purpose. It moves like it’s alive."
    vivithinking "Dangling like a puppet as it comes closer and I can see its face."
    vivithinking "My face."
    vivithinking "Reflecting on the concave mirror plate it has on its shoulders."
    vivithinking "It crawls closer to us, inches away from my own face."
    vivithinking "I feel the wind stroking my face like cold hands, pulling me closer to it."
    vivithinking "I cannot breathe."
    vivithinking "I cannot breathe."
    vivithinking "I cannot breathe!"
    vivithinking "It reaches out to me…"
    urshu angry "Get down from there!"
    #SOUND: The sounds of chairs clashing and Vivi and Susu’Rha hitting the floor.
    #VISUAL: The screen shakes.
    #SOUND: The window slams shut.
    show urshu angry at right
    vivithinking "I can breathe again!"
    show vivi surprised at left
    vivi surprised "What the hell was that?"
    urshu angry "When I told you to go seek the truth I didn’t quite mean to go and make us all something’s meal."
    vivi surprised "What the hell was that?!"
    urshu neutral "The truth, Miss Sanssouci. The truth of the matter whether you choose to accept it or not is that you and Druid Balrinn here have passed in life and there is no getting off this ride."
    urshu "Please, don’t try to get off this train again. I may not be there next time to save you."
    show susurha neutral at left
    susurha "What was that thing I saw out there?"
    urshu "What you and Miss Sanssouci witnessed depends entirely on yourselves."
    urshu "May I suggest returning to your cabins and getting some rest?"
    vivithinking "Oh baby. Caught between hell and a better place."
    vivithinking "Ugh… I need a drink."
    jump character_selector_2

label denial:
    scene cabin
    show vivi angry at left
    show urshu neutral at right
    vivi neutral "Outside this train… the void… it’s too much. I thought I was living a nightmare before, but that outside…  That was chilling to my core."
    vivi angry "Do you get off in seeing all of us in pain? Giving us all an existential dread that we can’t fix?"
    urshu neutral "Seeing the outside is sobering for many. I’m glad you’re no longer denying the gravity of the situation. I understand that this is a lot to process." 
    urshu happy "I am glad to see you have already started writing in the journal we’ve left for you. I thought a reporter such as yourself would like the ability to write down your thoughts."
    urshu neutral "I hope you continue to utilize it. Please know that nobody else, including myself, can ever read what's inside. Everyone deserves a private place to think."
    hide urshu
    vivi angry "He’s so infuriating! I don’t know why I even bother asking him anything."
    vivi neutral "But, he might be right. Might as well use the journal."
    return