# The scene starts here.

label confrontation:

    # Confrontation
    # LOCATION: lounge
    scene lounge with fade
    play ambience amb_lounge fadein 1.0

    show urshu happy at right with dissolve
    show vivi angry at left with dissolve:
        xzoom -1

    urshu happy "Doo doo doo, dee dee dee, dum dum dum!"
    vivithinking angry "There he is. Humming a jaunty tune. Polishing his little cap, er... badge... thing! The audacity!"
    vivithinking angry "Just look at his smug face, his perfectly tailored suit with  golden details... his tight caboose in those sharp black pants—"
    urshu neutral "Miss Sanssouci?"
    vivithinking surprised blush "Shit! How long have I been staring?"
    urshu neutral "I am flattered by your gaze, my dear, but do take care. In some lands, the victim of such a gaze is entitled to divorce your head from your shoulders."
    vivi angry "I'd love nothing more than that for {i}you{/i} right now."
    urshu neutral "Oh? Is there no bread? Shall you eat cake?"
    vivithinking angry "Oh, the {i}gall{/i}."
    vivi angry "I {i}know{/i}, Urshu."
    urshu happy "You know? Know what? Recipes for cake? My waist size?"
    play music confrontationmusic loop fadein 10.0
    vivi angry "Quit the deflections. I said I {i}know.{/i}"
    urshu neutral "..."
    urshu neutral "Ah, so you have followed your investigative proclivities. Tell me, what is it you {i}know{/i}?"
    vivi angry "For starters, this train exists on some sort of cosmic plane heading nowhere good, and—"
    vivi surprised "Why are you getting excited?"
    urshu happy "No reason, Miss Sanssouci! Do go on."
    vivi angry "Well, uh, okay. Oh, and I'm one of four passengers, all of us from different worlds."
    vivi angry "And you, or someone, or {i}something{/i} has taken our memories of boarding the train!"
    urshu happy "How delightful you've learned so much about your peers!"
    vivi angry "Don't interrupt me. I'm furious with you!"
    show urshu happy blush with dissolve
    urshu "My apologies."
    vivi neutral "Which means one of three things: One, I'm having a delusion my therapist is just {i}loving{/i} because she knows her findings are going to get her a Nobel Prize."
    show urshu neutral -blush
    urshu neutral "Interesting."
    vivi neutral "Two: I'm projecting my spirit into this astral plane while lying butt naked in a yurt in Cuzco."
    show urshu happy blush with dissolve
    urshu "What a sight that would be!"
    vivi angry "This isn't a game, Urshunabi!"
    show urshu neutral -blush
    urshu neutral "No, indeed. Not yet, anyhow."
    vivi angry "What?"
    urshu happy "What is your final theory, Miss Sanssouci?"
    vivi angry "..."
    urshu neutral "Cosmic cat got your tongue?"
    vivi sad "If I tell you, I'll know it's true."
    urshu neutral "Truth swallowed sickens the soul, my dear. Please, share what you have discovered."
    vivi sad "I..."
    vivi sad "We're..."
    urshu angry "Say it!"
    stop music fadeout 0.5
    vivi sad "Dead! We're all dead! Except for you."
    urshu happy "Well done, Miss Sanssouci. Well done."

    # SOUND: teleport
    play sound teleport_enter
    stop ambience fadeout 1.0
    # VISUAL: screen shakes
    show lounge with hpunch


    # VISUAL: fade out
    # TRANSITION TO DINING CAR
    # JUMP TO: REVEAL
    jump reveal