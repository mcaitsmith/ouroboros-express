# The scene starts here.

label interview_susurha:

    #Interviews/Susu'Rha Balrinn

    # LOCATION: lounge
    # scene diningcar with fade

    show susurha neutral with dissolve

    show vivi at left with dissolve:
        xzoom -1
    vivithinking surprised "Wait a minute..."
    vivithinking surprised "A humanoid...lizard? Seriously, whoa."
    vivithinking neutral "And so relaxed." 
    vivithinking neutral "A literal lounge lizard."
    vivithinking surprised "What is happening on this train?"
    susurha neutral "May I help you?"
    vivithinking neutral "Well, damn. It speaks."
    vivi neutral "Hello."
    susurha neutral "Hello yourself."
    vivi neutral "You seem quite relaxed."
    susurha neutral "I'm proud to say I've developed relaxation into an art form."
    vivi neutral "Damn! The only art form I've ever developed is pimple-popping." 
    susurha neutral "...Pimple...popping?"
    vivi neutral "...Nevermind!" 
    vivi neutral "What should I call you?"
    susurha neutral "I am the druid, Susu'Rha of Balrinn. Balrinn is my surname."
    vivi neutral "I'm Vivienne Sanssouci, but everyone calls me Vivi."
    susurha neutral "Vivi...Vivi..."
    susurha happy "Like Bon Vivant!"
    vivithinking neutral "Bon vivant - one fond of good living eh? I like that."
    vivithinking sad "Even if it hasn't always been true..."
    susurha neutral "So...What inspired you to approach me, Vivi?"


    # <CHOICE>
    vivi neutral "I'm a journalist. I'm writing a piece on the Ouroboros Express."

    menu:
        # OPTION 1
        "Can you tell me a little about yourself?":

            vivi neutral "Can you tell me a little about yourself?"
            susurha happy "My favorite topic!"
            susurha neutral "I'm heir to the throne of Balrinn. Or was."
            vivi surprised "Was?" 
            susurha neutral "I abdicated my position because I found that life stultifying."
            susurha happy "I then became a druid, which means I embarked upon a life of mirth, art, expression, and pleasure."
            susurha sad "This had...consequences."
            vivi neutral "Like what?"
            susurha sad "..." 
            susurha sad "I don't know if I'm quite comfortable talking about that."

            # JUMP TO: vivithinking neutral "Seriously?"

        # OPTION 2
        "Where are you from?!":

            susurha neutral "Balrinn. The capital city of my home country." 
            susurha neutral "Which is also my family name."
            vivi neutral "So...you're royalty."
            susurha neutral "I was, until I became a druid and dedicated my life to pleasure."
            vivi neutral "You seem very nonchalant about that."
            susurha neutral "If you say so..."
            
            # JUMP TO: vivithinking neutral "Seriously?"

    # <CHOICE>
    vivithinking neutral "Seriously?"
    
    menu:
        # OPTION 1
        "(Ugh, all these deflections are driving me nuts!)":

            vivithinking angry "Ugh, all these deflections are driving me nuts!"
            vivithinking angry "And why are they looking at me like I'M the freak?! THEY'RE the talking wellness-guru gecko!"
            vivithinking angry "The attitude on this one."

            # JUMP TO susurha neutral "Your face right now...You're judging me."

        # OPTION 2
        "(Bury the lede, why don't you?)":
    
            vivithinking neutral "Bury the lede, why don't you?"
            vivithinking neutral "There's gotta be something there. People don't put up walls to protect nothing."
            vivithinking neutral "Maybe I should try something else... something to get ol' wellness-guru gecko here on board..."

            # JUMP TO susurha neutral "Your face right now...You're judging me."
    

    susurha neutral "Your face right now...You're judging me."
    vivi neutral "No, I..."
    susurha neutral "I'd say stay awhile and relax with me, but I don't think you'd know how."

    # <CHOICE>
    vivithinking angry "Oooh! This one is getting on my nerves."

    menu:
        # OPTION 1
        "I know how to relax!":

            vivi angry "I know how to relax!"
            susurha neutral "Oh, really? Take a seat then."
            vivi neutral "I will."
            vivithinking neutral "The seat cushions are warm."
            vivithinking neutral "Oh man. I could fall asleep."
            susurha happy "There you go."
            vivi happy "This is actually kind of nice."
            susurha happy "You see? That's why I practice it so often."     

            # JUMP TO: "So enough about me. Who are you, Vivienne?"

        # OPTION 2
        "I can relax! This just isn't the time.":

            vivi neutral "I can relax! This just isn't the time."
            susurha happy "There is always time to lay back and relax."
            susurha neutral "If you let the stress of everything get to you, you'll age like milk in the blistering sun."
            vivi angry "Look, my skin's already screwed up by an all-American cocktail of pollution and overpriced creams. I don't care what it looks like anymore."
            vivithinking neutral "Well, except when I'm popping a zit..."     
            vivi angry "I just came here to get this assignment done, not get a self-care lecture from a talking lizard."
            susurha angry "Ss-uit yourself."
            susurha neutral "Alright, then. I've spoken enough about myself for one conversation."
            vivi neutral "I mean, not really. You kinda avoided my--"

            # JUMP TO: "So enough about me. Who are you, Vivienne?"

    susurha neutral "So enough about me. Who are you, Vivienne?"
    susurha neutral "Let's see if I can get there. You're a writer. Which means you're an artist, of sorts."
    susurha neutral "But also a pragmatist. With an allergy to art for art's sake."
    susurha neutral "I could see how journalism suits you."
    vivithinking angry "Get out of my head, lizard...gecko...whatever you are!" 
    susurha neutral "But have you ever indulged in poetry? Or songwriting?"
    vivi neutral "I...not seriously."
    susurha sad "You're missing out."
    susurha neutral "What else should I know about you, Vivi?"
    vivi neutral "I'm here to talk about you. Not the other way around."
    susurha happy "Hm. Whatever you say."
    

    # <CHOICE>
    vivithinking neutral "This is taking too long. I just have to ask the right question..."

    menu:
        # OPTION 1
        "Where are you heading?":

            vivi neutral "Where are you heading?"
            susurha neutral "On this train? Home..."
            susurha sad "I hope."
            vivi neutral "You hope?"
            susurha sad "That's where I was heading before I found myself in this bizarre, yet well-appointed cabin."
            vivi neutral "Found yourself?"
            vivi neutral "You don't remember boarding?"
            susurha neutral "I sure don't."
            vivithinking neutral "Funny...Neither do I."

            # JUMP TO: "Where are you headed?"

        # OPTION 2
        "Why are you on this train?":

            vivi neutral "Why are you on this train?"
            susurha neutral "..."
            susurha neutral  "I don't...know."
            susurha neutral "I don't remember boarding."
            vivi surprised "Really?"
            susurha neutral "I was in the woods, running toward my ancestral home..."
            susurha sad "And then I found myself here."
            vivithinking neutral "Something is clearly bothering them."
            vivithinking sad "I can't say that I blame them."
            vivithinking surprised "If I woke up here without knowing I got here..."
            vivithinking "..."
            vivithinking neutral "Something must be going on."

            # JUMP TO: "Where are you headed?"

    susurha neutral "Where are you headed?"
    susurha neutral "Or are you just going to leave as soon as you get your story?"
    vivi neutral "I haven't decided yet."
    susurha neutral "Ah, well, please try to enjoy the trip while it lasts."
    vivithinking surprised "Wait, that's it?"
    vivithinking neutral "All that talk and nothing was actually said!"
    susurha neutral "Perhaps we'll chat again. I'd love to know more about the person behind that disarming smile."
    vivithinking neutral blush "Now, they're charming me?!"
    vivithinking neutral blush "And did I even smile? How is it disarming?"
    vivithinking neutral blush "Crap, is it getting warm in here?"
    vivithinking neutral blush "No! Don't fall for it, Vivi. Keep it together."
    susurha happy "Talk soon, Vivienne."
    vivi happy "See you later."

    hide susurha with dissolve

    # JUMP TO: Figuring it out
    jump interview_choice