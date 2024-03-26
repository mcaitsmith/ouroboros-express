# The scene starts here.

label depression_cs2:

    # Character Selector 2

    # LOCATION: cabin
    scene cabin with fade

    show vivi neutral at left with dissolve

    vivithinking sad "Ugh... I think I might've had a little too much."
    vivithinking neutral "Then again, there's nothing to look toward. Might as well take advantage of the open bar."

    # SOUND: knocking

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
    urshu neutral "Believe it or not, you have had a profound effect on the other passengers. I'm sure one of them would love to spend time with you as we approach our destination."
    # END

    # ??DECAY (ELSE)
    urshu neutral "That is for you to discover. We approach our destination. Now would be a good time for final goodbyes."
    # END
    hide urshu with dissolve

    vivithinking neutral "I suppose there might be something to what he said."

    # <CHOICE>
    # ??ATTRACTION
    #Dialog appears if any of the meters is high
    vivithinking happy "Let's find someone to hold one last time before this thing ends."
    # END

    # ??DECAY (ELSE)
    vivithinking neutral "Time to finally leave this purgatory. I reckon goodbyes are in order."
    # END

    menu:

        # OPTION 1
        "Avatar of Asha" if fr1_depression_choice != "Ava":

            vivithinking neutral "The goddess. I want to spend my last moments with her."
            # JUMP TO: Free roam 2 / Avatar of Asha
            jump depression_fr2_ava

        # OPTION 2
        "Inquisitor Darius Wrecker" if fr1_depression_choice != "Darius":

            vivithinking neutral "Darius. I want to spend my last moments with them."
            # JUMP TO: Free roam 2 / Darius Wrecker
            jump depression_fr2_darius

        # OPTION 3
        "Susu'Rha Balrinn" if fr1_depression_choice != "Susu'Rha":

            vivithinking neutral "Susu'Rha. I want to spend my last moments with them."
            # JUMP TO: Free roam 2 / Susu'Rha Balrinn
            jump depression_fr2_susurha


    # FREE ROAM 2 - Ava
    # # LOCATION: observatory

    # show vivi neutral at right

    # Show asha neutral left

    # vivithinking "Oh, the Sun Goddess, herself. Somehow looking radiant as usual."

    # #??DECAY
    # vivi sad "She's too good for me..."
    # #END

    # #??ATTRACTION
    # vivi happy "I need her in my life, no matter what."
    # #END

    # vivithinking "Okay, Vivi, deep breath, and-"
    # vivi happy blush "Asha, darling, how are you?"
    # ava neutral "..."
    # vivi surprised "Asha?"
    # ava surprised "Oh, sunshine, we are so sorry. We couldn't detach from our memories. They are painful, you must understand. Our life has not been a happy one."

    # # <CHOICE>
    #     #OPTION 1 + ATTRACTION
    #     "Really?"

    #         vivi surprised "Really? Even though the royals treated you poorly you had everything you could have ever wanted. I don't understand."
    #         ava sad "Of course you do not understand. How could you?"
    #         vivi sad "I want to...understand. How can I share your pain if you don't talk about it with me?"
    #         # JUMP TO: ava sad "Vivi..."

    #     #OPTION 2 + DECAY
    #     "You're pretty ungrateful, huh?"

    #         vivi angry "You're pretty ungrateful, huh? It sounds like you had everything you could have ever wanted."
    #     ava sad "How could you ever understand..."
    #     vivi angry "You're right, Asha. I can't and I won't. How could a puny little human peasant like me ever understand what it's like to be a princess in a castle?!"
    #     # JUMP TO: ava sad "Vivi..."

    #     #OPTION 3>>ATTRACTION +ATTRACTION
    #     "I wish I could have been there for you."

    #         vivi sad "I wish I could have been there for you. Our relationship has been the one thing keeping me sane on this journey... I wish we could have spent some time together while we were alive."
    #         ava happy "Really? We feel the same way." 
    #         # JUMP TO: ava sad "Vivi..."


    # ava sad "Vivi..."
    # ava sad "We have never had a friend."
    # vivi angry blush "What about me?! I thought we were friends!"
    # ava surprised "That may be true, but we will soon be separated by fate. There is no heaven awaiting for Asha."
    # vivi surprised blush "Oh? And why's that?"
    # ava neutral "{i}*sigh*{/i} You are aware that I am not the first Avatar of Asha. Every twenty and five years, a new avatar is chosen."
    # ava sad "Soleos was not always the peaceful society it is today. The planet was once split in two, marred by war and terror...until the Avatar arrived."
    # ava sad "She was born from the seed of a Solarian man and the egg of a Lunolian woman. The mixing of cultures was considered taboo, said to bring about the end of the world."
    # vivi sad "Oh, my goodness. I had no idea."
    # ava sad "The woman who gave birth to Asha was my ancestor, far removed. My bloodline is the only one that can act as a vessel for the Avatar."

    # # <CHOICE>
    #     #OPTION 1 + ATTRACTION
    #     "But why do you need her to begin with?"

    #         vivi surprised "But why do you need her to begin with? I wish you could have had a normal life on Earth."
    #         ava sad "Without the Avatar, our world would be doomed. These hands have seen much bloodshed."
    #         vivi surprised "I didn't realize that your life wasn't all sunshine and rainbows."
    #         ava sad "It is not your fault, for we did not share with you. It is not an easy thing to broach lightly."

    #         # JUMP TO: vivi neutral blush "I'm sorry, Asha."


    #     #OPTION 2
    #     "Why are you telling me all this now?"

    #         vivi surprised "Why are you telling me all this now?
    #         ava sad "What better time to share our ways than at the end of the world?"
    #         vivi happy "I guess you make a good point."

    #         #JUMP TO: vivi neutral blush "I'm sorry, Asha."


    #     #OPTION 3>>+ATTRACTION
    #     "If only I had known you in life."

    #         vivi sad "If only I had known you in life, things could have been different."
    #         show ava neutral blush with dissolve
    #         ava "A little bit of love would have gone a long way."
    #         vivi happy blush "Well I'm glad we can spend this time together now."
    #         show ava neutral -blush

    #         # JUMP TO: vivi neutral blush "I'm sorry, Asha."

    # vivi neutral blush "I'm sorry, Asha."

    # show ava neutral blush with dissolve

    # #??ATTRACTION
    # ava "No need. Just be here now."

    # #pause

    # # SOUND heartbeat

    # #END

    # ava "I want to know more about your life on Earth. What can you tell us?"
    # show ava neutral -blush

    # # <CHOICE>

    #     #OPTION 1>>+ATTRACTION
    #     "My family moved around a lot..."

    #         vivi neutral "My family moved around a lot, from country to country."
    #         vivi neutral "I'm luckier than most - seen and experienced so many amazing cultures."
    #         vivi sad "But it's lonely for a kid, you know? As soon as I made friends, started feeling comfortable... We'd uproot again"
    #         ava neutral "Ah, you were a lonely child. We understand this."
    #         vivi sad "Over time, I just felt like it was easier to not make friends... And even when my family stopped moving, I just kept going."
    #         ava neutral "Did you find solace in other things?"
    #         vivi happy "Yes - there were always books... and I guess I retreated into those pages."
    #         vivi happy "I think that's why I wanted to become a writer, you see. When people disappointed me, books were always there."
    #         vivi sad "Unfortunately, needing money meant that I became a reporter instead of a novelist. It's one of my regrets." 
    #         vivi sad "I wish I'd pursued my passions more."
    #         vivi surprised "I'm sorry, I forgot myself. I'm trauma dumping."
    #         ava sad "Please do not apologize. We, too found shelter in the palace library."
    #         ava neutral "Your imagination, it must have grown, no?"

    #         # JUMP TO: vivi happy "Like you wouldn't believe!"



    #     #OPTION 2>>+DECAY
    #     "I wrote this haiku in school once."

    #         vivi happy "I wrote this haiku in school once. Wanna hear it?"
    #         asha surprised "Go on."
    #         vivi happy blush "Tasty soup tasty. Tasty soup tasty soup mmm. Tasty tasty soup."
    #         asha surprised "Wow. You do have a way with words."
    #         # JUMP TO: vivi happy "Like you wouldn't believe!"


    #     #OPTION 3 NEUTRAL
    #     "Earth is beautiful."

    #         vivi happy blush "Earth is beautiful. In its own way. There are thousands of unique cultures and ways of life that thrive in different ecosystems, from deserts and mountains to swamps and snow."
    #         ava happy "We cannot imagine..."
    #         vivi happy "And the people! I've reported on so many stories, interviewed so many strange characters."
    #         vivi neutral "I just wish I could have taken my time in the places I traveled to. Really got to know some people - or someone."
    #         show ava surprised blush with dissolve
    #         ava "Is there really so much diversity on your Earth?"
    #         show ava surprised -blush
    #     # JUMP TO: vivi happy "Like you wouldn't believe!"


    # vivi happy "Like you wouldn't believe!"
    # show ava neutral blush with dissolve
    # ava "Well our conversations have certainly helped us feel better. We enjoy your...perspective."
    # vivi happy blush "Come to Earth sometime! I'll show you around!"

    # #??DECAY
    # show ava sad -blush
    # ava sad "If only we could have..."
    # #END

    # #??ATTRACTION
    # show ava happy blush
    # ava "It's a date. We look forward to it."
    # #END

    # vivi sad blush "I should go... See you soon, Asha."
    # show ava neutral blush
    # ava "Remember, The All is the One."
    # vivi blush "The All is the One..."

    # # JUMP TO: DEBRIEF DEPRESSION





    # FREE ROAM 2 - Darius
    # # LOCATION: observatory

    # show darius sad at right
        
    # show vivi neutral at left

    # darius sad "You're here."
    # vivi neutral "Expecting me?"
    # show darius sad blush with dissolve
    # darius "I don't think I ever expected you."
    # vivi surprised "Honestly, I...don't think I expected you, either."
    # vivi "I can't say I've ever been in an observatory quite like this."
    # show darius happy -blush
    # darius happy "Beautiful, isn't it? The cosmos are alight tonight."
    # darius "I could watch the stars swirl like this forever. I just might."
    # vivi neutral "Surely you'd tire of them eventually. Everything bright burns out after a time."
    # darius sad "Too right. Sometimes even {i}before{/i} their time."
    # darius "I'm surprised you wanted to see me. If Urshu is to be believed, this is it. One last conversation before...well. I guess we'll see."

    # # <CHOICE>

    # menu:
    #     # OPTION 1 +ATTRACTION
    #     "There's so much more I want to learn about you.":

    #         vivi sad "There's so much more I want to learn about you."
    #         show darius surprised blush with dissolve
    #         darius "Surely not. I'm an open book."
    #         vivi happy blush "If you call {i}this{/i} being an open book then I shudder to imagine what closed off looks like."
    #         show darius happy blush
    #         darius "Heh. I suppose there's no harm in being open."
    #         show darius neutral -blush
    #         darius neutral "At least, there won't be any more consequences."

    #         # JUMP TO: vivi surprised "What do you mean by that?"

    #     # OPTION 2 +DECAY
    #     "I won't say it's been nice getting to know you.":

    #         vivi neutral "I won't say it's been nice getting to know you."
    #         darius neutral "You {i}really{/i} don't mince words. I suppose I respect that."
    #         vivi neutral "There isn't a point. May as well say what we mean."
    #         vivi "There's still a lot I don't know about you. I'd like to unearth those truths."
    #         darius sad "You won't like it. Though, as you implied...it doesn't matter anymore."

    #         # JUMP TO: vivi surprised "What do you mean by that?"

    #     # OPTION 3 NEUTRAL
    #     "You think this is it? Really and truly? No más?":
        
    #         vivi surprised "You think this is it? Really and truly? No más?"
    #         darius neutral "No reason to think otherwise. May as well enjoy the void as best we can. 
    #         Maybe even make some amends."

    #         # JUMP TO: vivi surprised "What do you mean by that?"

    #     # OPTION 4 ??ATTRACTION
    #     "If this is the last conversation I'm ever to have, I'm grateful to have it with you.":

    #         vivi neutral blush "If this is the last conversation I'm ever to have, I'm grateful to have it with you."
    #         show darius neutral blush with dissolve
    #         darius "You don't even know me."
    #         vivi happy blush "I know enough. You care deeply."
    #         show darius sad blush
    #         darius "Vivi."
    #         vivi happy blush "You feel deeply."
    #         show darius sad -blush
    #         darius sad "Vivi-"
    #         vivi happy blush "You want to make others happy."
    #         darius angry "VIVI."
    #         darius "Stop. Please... stop. I'm not that person. I'm {i}nothing like{/i} that person."
    
    #         # JUMP TO: vivi surprised "What do you mean by that?"

    #     # OPTION 5 ??DECAY
    #     "Do you see them, Darius?":

    #         vivi neutral "Do you see them, Darius?"
    #         darius surprised "I do. You do, as well?"
    #         vivi neutral "I thought maybe they were nightmares. Something I hallucinated. But I see them clearly now."
    #         darius neutral "I have to ask... What do they look like?"
    #         vivi surprised "Why, don't you see them?"
    #         darius sad "It's different for everyone. Mine are long claws—outstretched fingers. Pointing directly at me."
    #         darius "At my heart."
    #         vivithinking "Terrifying."
    #         vivi neutral "I see... It's difficult to describe. An empty dress. Reflective surface. I see myself in the creases and folds. It draws me in."
    #         vivi "It wants to swallow me."
    #         darius sad "Ah. Guilt. I know it well."

    #         # JUMP TO: vivi surprised "What do you mean by that?"

    # vivi surprised "What do you mean by that?"
    # darius neutral "I'm not who you think I am, Ms. Sanssouci. Vivi."
    # darius "I'm a monster. Worse, even, I'm a coward."
    # vivi happy "Come on, now. You're too hard on yourself. I--"
    # vivithinking "AH. Ah. This energy coming from him... It's like the worst migraine I've ever experienced, all at once."              
    # darius angry "I'm responsible for the deaths of millions of sentient beings. {i}Millions{/i}."
    # darius sad "I deserve to be crushed by those hands. I long for it."
    # vivi surprised "I... I don't know how to respond."
    # darius neutral "I'm not asking you to. I just want you to know who you're choosing to spend your time with."
    # darius "I loved my god. I loved the Inquisition. I would have done anything for them. And I did. Frequently."
    # vivithinking "Is it weird that I'm pulling out my notebook? Who is even going to read this...?"
    # vivi neutral "Who were they?"
    # darius neutral "I don't think a human tongue could say their name without considerable effort. They are ancient."
    # darius sad "Eldritch."
    # darius neutral "You may think of them as That Which Gathers. Or, perhaps-- Za'deeh."
    # vivi neutral blush "Your terrifying ancient eldritch god is a zaddy?"
    # show darius surprised blush with dissolve
    # darius "What? No! Their very gaze would melt your mind, much less your face! Put some respect on Za'deeh's name!"
    # vivi happy blush "Listen, I get it. I'll always respect a zaddy when I see one."
    # show darius happy blush
    # darius happy blush "You... you are..."
    # show darius happy -blush

    # # <CHOICE>

    # menu:
    #     # OPTION 1 +ATTRACTION
    #     "Adorable? Cute? A sassy lil' cupcake who you can't help but open up to?":

    #         vivi happy blush "Adorable? Cute? A sassy lil' cupcake who you can't help but open up to?"
    #         darius happy "You know what? Sure."
    #         vivi surprised blush "FINALLY! You admit it!"

    #         # JUMP TO: vivi neutral "Now. Let's get real."

    #     # OPTION 2 +DECAY
    #     "More open than you'll ever be?":

    #         vivi sad "More open than you'll ever be?"
    #         darius sad "I suppose so. There's just-- the weight. Of everything."
    #         vivi neutral "There you are."
        
    #         # JUMP TO: vivi neutral "Now. Let's get real."

    #     # OPTION 3 NEUTRAL
    #     "Just a gal in need of some company.":

    #         vivi neutral "Just a gal in need of some company."
    #         darius neutral "I'm happy to provide it."
            
    #         # JUMP TO:vivi neutral "Now. Let's get real."

    # vivi neutral "Now. Let's get real."
    # darius sad "Better late than never."
    # vivi neutral "You said you were an Inquisitor?"
    # darius sad "That's what I called myself."
    # darius "My joy was in rooting out the faithless. In bringing them in to face judgment."
    # darius "Across dimensions. Planes. Realities. No one could hide from me."
    # darius "I found them. And brought them before my god. None could withstand their gaze."
    # darius "They died. Or went mad. ...And I relished their fear."
    # vivithinking "..."
    # darius sad "Until one day. There was a couple. Human. Man and woman. No matter; I'd captured couples before."
    # darius "But this one... something about them. Even as their minds broke before Za'deeh's baleful glare, they only thought of each other. Of what they meant to one another."
    # darius surprised "They were unafraid to die. To be reduced to gibbering husks. As long as they were near each other."
    # darius sad "I've been thinking about them for the last 500 years."
    # darius neutral "Is that what you call "love"? That fearlessness? Certitude?"
    # darius "Whatever it is, I knew that I'd never felt it. In any galaxy."
    # vivi neutral "You didn't kill them, Darius. Your god did."
    # darius sad "I appreciate you saying that. But you're wrong. I'm just as responsible."
    # darius "I think that's why I'm here. Torment. It's a fitting punishment."
    # darius neutral "Let's enjoy the stars together. At least one person has been witness to my unburdening. I thank you."
    # vivithinking "Darius is... a monster. But not a remorseless one."

    # ??ATTRACTION
    # vivi neutral blush "You're not beyond redemption, Darius."
    # darius surprised "After all that... You believe so?"
    # vivi happy blush "I know so."

    # ??DECAY
    # vivi sad "Darius...that's horrifying. I don't know that I can look at you the same way."
    # darius sad "I know. I don't expect you to."
    # darius sad "Let the horrors take me. It's what I deserve."

    # # JUMP TO: Debrief Depression

    # FREE ROAM 2 - Susu'Rha (DEPRESSION)

    # # LOCATION: observatory

    # show susurha sad right

    # vivithinking "Susu'Rha looks like they're holding up about as well as me."
    # susurha "The stars are out tonight. As beautiful and endless as the night I left home."

    # show vivi neutral left

    # susurha "Ah. Vivacious Vivi. What brings you to me in these final moments?"

    # ??DECAY
    # vivi "Don't know. You're not boring."
    # #END
    # # <CHOICE>
    # vivi "I wanted to see you because...."
            
    # menu:
    #     #OPTION 1 +ATTRACTION
    #     "I didn't want to be alone."

    #         vivi "I didn't want to be alone."
    #         susurha "I very much hoped you'd come."
    #         vivi "Is it okay if I stay here?"
    #         susurha "Please do."
    #         #JUMP TO: vivithinking "It feels so warm being next to them."
        
    #     #OPTION 2 >>ATTRACTION +ATTRACTION
    #     "I also needed to see a friendly face."
                
    #         vivi "I also needed to see a friendly face."
    #         show susurha happy blush with dissolve
    #         vivi "..."
    #         show susurha neutral -blush
    #         susurha neutral "Please... sit with me."
    #         # JUMP TO: vivithinking "It feels so warm being next to them."

    #     #OPTION 3 >>DECAY +ATTRACTION
    #     "I don't...know why."

    #         vivi "I don't...know why."
    #         susurha "I wish you knew, but I'll take it.
    #         susurha "Thank you for your honesty."
    #         vivi "Is it okay if I stay here?"
    #         susurha "Yes."
    #         # JUMP TO: vivithinking "It feels so warm being next to them."

    # vivithinking "It feels so warm being next to them."
    # vivithinking "I could almost fall asleep right here."

    # ??DECAY
    # vivithinking "Why do I feel this way?"
    # susurha "Even with all the druidic teachings in my life..."
    # susurha "The space out there seems so peaceful in all its chaos."
    # susurha "It feels so welcoming..."
    # susurha "Yet I can't trust it."
    # susurha "Do you think it will hurt..."
    # susurha "...when we merge with the cosmic weave?"
    # #END

    # #<CHOICE>
    # susurha "Will we know when we're gone?"

    # menu:
    #     #OPTION 1 
    #     "We'll never know until it happens."

    #         vivi "We'll never know until it happens."
    #         susurha "That's what I'm afraid of."
    #         # JUMP TO: susurha "So you ARE afraid?"

    #     #OPTION 2 +ATTRATION
    #     "I don't want to go."

    #         vivi "I don't want to go."
    #         susurha sad "Yeah..."
    #         # JUMP TO: susurha "So you ARE afraid?"

    # # <CHOICE>
    # susurha "So you ARE afraid?"

    # menu:
    #     #OPTION 1 +ATTRACTION
    #     "Yes."

    #         vivi "Yes."
    #         vivi "I'm very afraid."
    #         vivi "Who wouldn't be?"
    #         # JUMP TO: susurha "Well, I know I am."

    #     #OPTION +DECAY
    #     "No."

    #         vivi "No."
    #         vivi "What's the point in being afraid?"
    #         vivi "You cease to be, and it's lights out. Poof."
    #         susurha "Your confidence feels as if it is made of glass."
    #         # JUMP TO: susurha "Well, I know I am."

    #     #OPTION 3
    #     "..."

    #         vivi "..."
    #         # JUMP TO: susurha "Well, I know I am."

    # susurha "Well, I know I am."
    # susurha sad "..."
    # susurha neutral "That abomination that stalks me..."
    # susurha "I've tried to talk to it. Reason with it. Understand its motives."
    # susurha "I thought it chose to not speak to me when I begged for it to free me, but I realize now that it never had a voice to begin with."
    # susurha "Its body is chained at the wrists and ankles, making it unable to move."
    # susurha "Its eyes, blinded so that it couldn't see a path ahead."
    # susurha "Its mouth, muzzled so that it can never express thoughts."
    # vivi sad "That sounds awful"
    # susurha sad "I ran away from home because I was afraid I would never get to live the life I wanted to."
    # susurha sad "Now I'm afraid that thing, void of life, is my fate. Ceasing to exist..."
    # susurha sad "I don't want to cease to exist."
    # susurha sad "I want to be ME."

    # # <CHOICE>
    # vivithinking "I want to be me!"

    # menu:
    #     #OPTION 1 +ATTRACTION
    #     "I want to be ME as well."

    #         vivi "I want to be ME as well."
    #         vivi "My whole life... I felt I was living someone else's life."
    #         vivi "Think like someone else. Act like someone else."
    #         vivi "I'm afraid I've missed my chance to be me."
    #         susurha "Right here, right now, you are you."
    #         # JUMP TO: susurha "Thank you for staying with me, if even for a moment."
                

    #     #OPTION 2 >>DECAY +ATTRACTION
    #     "I get what you mean."

    #         vivi "I get what you mean."
    #         susurha "You do?"
    #         vivi "My whole life, everyone has said "Vivi, just be yourself!""
    #         vivi "I don't think I ever understood what that meant."
    #         susurha "Right here, in this moment of vulnerability, you are you."
    #         # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

    #     #OPTION 3 >>ATTRACTION +ATTRACTION
    #     "Nothing can take away who you are."

    #         vivi "Nothing can take away who you are."
    #         vivi "You're one of the most unique creatures I have ever met."
    #         vivi "There aren't many poet-musicians druids that were once heir to a throne, but chose to not take that power so that they could be THEMSELVES."
    #         vivi happy blush "You are truly one of a kind."
    #         show susurha happy blush with dissolve
    #         susurha "STOP... You flatter me, Vivienne."
    #         susurha "Nothing can take away who you are."
    #         show susurha happy -blush
    #         # JUMP TO: susurha "Thank you for staying with me, if even for a moment."

    #     #OPTION 4 >>DECAY +DECAY
    #     "I know who I am."

    #         vivi "I know who I am."
    #         susurha "Are you sure about that?"
    #         susurha "This whole time that I've interacted with you, it has always felt like I was talking to a mirror that bends and flows with the wind."
    #         vivithinking sad "This son of a..."
    #         susurha "I told you the thing that stalks me. Tell me, what does the thing that haunts you appear as?"
    #         vivi sad "It's... I can't tell you. It's personal"
    #         susurha "Oh. As I thought."
    #         #JUMP TO: susurha "Thank you for staying with me, if even for a moment."

    # susurha "Thank you for staying with me, if even for a moment."

    # ??DECAY
    # susurha "I hope I brought some worth to you."
    # #END

    # susurha "The only thing worse than being alone is never being at all."

    # #DECAY ROUTE
    # #SAL'S NOTE: Lines below are supposed to be a DECAY ending of the scene.
    # vivi "Everything will turn out for the best."
    # susurha "You lie to yourself so easily."
    # susurha "I hope there is someone behind that mask."
    # susurha "Even if you don't show them to me."
    # vivithinking "I..."
    # vivithinking "I think I have had enough of this."
    # vivi "Good night."
    # susurha "Rest easy, Vivi."
    # #JUMP to Debrief Depression

    # #SAL'S NOTE: Lines below show if decay is NOT high
    # vivi "We can sit here for a little while longer."
    # vivi "And watch the cosmos fly by."
    # show susurha neutral blush with dissolve
    # susurha "I'd love that."
    # vivithinking "In its own strange way, the view sure is beautiful from here."
    # #JUMP to Debrief Depression





    # Debrief Depression

    # # LOCATION: cabin

    # #??ATTRACTION

    # show vivi neutral at left

    # # SOUND knocking

    # show urshu neutral at right

    # urshu neutral "I trust you had a good evening?"

    # vivi happy "Yeah, it was nice."
    # vivi neutral "About what you said before. Writing my own story... I think I'm starting to understand."
    # urshu happy "I live to serve, Miss Sanssouci."
    # vivi neutral "You know you're a cosmic entity, right? No need to be so formal with me."
    # urshu happy "As you wish."
    # vivi neutral "Hey Urshu, before you go, can I ask you something?"
    # vivi neutral "Why'd you put us four together?"
    # urshu happy "Maybe it was preordained. Maybe it was random. Or maybe, I think you four just fit together. I do love puzzles after all."
    # vivi neutral "You've been quite the conductor, Urshu."
    # urshu neutral "And you have been quite the puzzle."
    # urshu neutral "Enjoy your final night here."
    # vivi sad "It's really ending, huh?"
    # urshu happy "All may not be as lost as you think."
    # vivi happy "Goodnight, Urshu."
    # Urshu happy "Goodnight, Vivienne."
    # vivithinking neutral "My mind is buzzing. I need to write."
    # # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH

    # #Journal entry with attraction meter high
    # Wow. At the beginning of all this, I would've never thought I'd get to know some of the other passengers this well. We're all more similar than I thought. Even Urshu, believe it or not. Time is weird here. I feel like I've been riding this train for ages, but I think I finally understand this place. It's a lot to process, but I'm glad I didn't have to do it alone.


    # #NOTE: SCENE VARIATION IF DECAY IS HIGH
    # show vivi neutral at left

    # # SOUND Knocking on door

    # show urshu neutral at right

    # urshu neutral "I trust you had a good evening?"
    # vivi neutral "It was fine. I am glad this is ending though."
    # urshu surprised "Oh? Do tell."
    # vivi neutral "I was scared at first. Of changing, of the unknown, of leaving my past behind..."
    # vivi neutral "I'm not anymore."
    # urshu neutral "And what changed?"
    # vivi neutral "Nothing. I guess I realized wherever I'm going can't be worse than here."
    # vivi angry "The more I talk to the people on this train the more I realize how much I hate it here. I'm not myself anymore. You took that from me. I've withered away just like this train."
    # vivi angry "I don't even recognize myself in the mirror. I can't tell if I've physically changed or if my perception of self has warped. My thoughts... they're not entirely my own anymore."
    # vivi angry "The only thing I had were my thoughts!"
    # urshu sad "I'm sorry you feel that way."
    # vivi angry "And I'm sorry I wasn't your perfect little plaything to be experimented on!"
    # vivi neutral "I will thank you for one thing: You've pushed me beyond all knowable limits. Now I can guarantee I'll be ready for anything in the next life."
    # urshu neutral "Thank you for the feedback. Goodnight, Miss Sanssouci."

    # hide urshu

    # vivithinking neutral "I should write whatever thoughts I have left. By tomorrow, I'm not sure they'll be mine."

    # # NOTE: JUMP TO RESPECTIVE ACT 3 BRANCH

    # # Journal entry with degradation meter high
    # I can't take this anymore. There's something growing inside me. A hunger I, we can't explain. What is happening to us? This is the conductor's fault. He's behind everything. The other passengers too. They must be working with him. None of them feel the way we do. They're all out to get us. We won't go. Not like this. They'll see.

