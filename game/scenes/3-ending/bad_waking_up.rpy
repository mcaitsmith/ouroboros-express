# The scene starts here.

label bad_waking_up:

    #3.1 Acceptance
    #Bad Ending/Waking Up

    play music badendmusic volume 0.5

    #LOCATION: black background
    # over black
    call hide_overlay from _call_hide_overlay_1
    scene black with fade

    # vivi is dreaming

    vivithinking neutral "A gaping maw. Falling. Falling. Desert dunes. Midnight."
    vivithinking neutral "Flash: another perfect picture. It's me. Framed, behind glass. My face, everywhere."
    vivithinking neutral "My name's in every feed. Every post. {i}Vivienne Sanssouci: Truth-Teller. Trendsetter. Lone Wolf.{/i}"
    vivithinking neutral "Everywhere, then nowhere. The tide comes and goes. Goes, mostly."
    vivithinking sad "Everything comes to an end. Talent. Success. Love."
    vivithinking sad "Vivienne Sanssouci. Who is she? Who are we?"
    vivithinking sad "Why are we so alone?"

    # LOCATION: cabin
    call check_overlay from _call_check_overlay_36
    scene cabin with fade

    show vivi surprised at left with dissolve:
        xzoom -1

    vivi surprised "No!"
    vivi surprised "A dream. Only, I was dying. All alone."
    vivi sad "A dream imitating life."
    vivi angry "Ouch! What's in my eye?"
    vivi angry "Gah, it's huge! Where's the mirror..."
    vivi surprised "..."
    vivi surprised "Oh, my God."
    vivi surprised "Tears...made of silver? Glass?"
    vivi angry "What the {i}hell{/i} is happening?"
    vivi angry "My eyes are bleeding! Ow! Why am I crying out shards of a mirror?"
    vivi angry "This is the end of the road. This goddamn train. No more stops. Just the end."
    vivithinking sad "It's all my fault. It's all my {i}fault{/i}!"
    vivi angry "Shut up! Look at you, bleeding from your eyes and still blaming yourself!"
    vivithinking sad "Of course it's my fault. It always is. I never take chances. Never the right chances..."
    vivi sad "But...I tried. I did everything Urshu asked. I tried to connect with all of them! Asha, Susu, Darius...They—"
    vivithinking angry "They didn't try. They let their wounds define them. They, they..."
    vivi neutral "They didn't let me in. They put up their walls and cowered."
    vivi angry "Fuck. Them."
    vivi angry "I'm done with Asha. I'm done with Susu'Rha. I'm done with Darius. And most of all..."
    vivi angry "{i}Fuck Urshu.{/i}"
    vivi angry "If it weren't for them, I'd be alive again. Traveling the world, sipping {i}tinto{/i} in Madrid. Making love to beautiful people. Finding myself."
    vivithinking angry "I want to break something. Anything! Starting with this mirror!"
    vivi neutral "No... I can't even feel it. I feel nothing."
    vivi angry "I'm going to find them. And make them pay."

    # JUMP TO: Bad Ending/Argument
    jump bad_argument