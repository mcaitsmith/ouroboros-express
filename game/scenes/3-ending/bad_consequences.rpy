# The scene starts here.

label bad_consequences:

    # Bad Ending/Consequences
    # LOCATION: eldritch landscape
    # call hide_overlay from _call_hide_overlay
    scene black with Fade(3.0,0.0,1.0)

    show vivi neutral at right with dissolve

    vivithinking neutral "I am...more. I am..."
    vivi neutral "I'm outside the train, now. I'm...free!"
    vivi happy "I'm free! I did it! I'm..."
    vivi neutral "But what...what is that? A mirror?"

    # SOUND: horror
    play music horrormusic loop

    vivi sad "No! It's her. The monster. The—"
    vivi sad "No, don't come out of the mirror! Stop! No!"
    vivithinking surprised "She's...embracing me!!"
    vivi "..."
    vivithinking neutral "I don't feel here anymore. I'm going to open my eyes now."
    vivi surprised "She's gone? But?"
    vivithinking neutral "My...arms are shimmering."
    vivithinking neutral "My legs..."
    vivithinking neutral "Even my face...I can see my own reflection in my palms."
    vivithinking neutral "Is all of me...a mirror?"
    vivi angry "No! This can't be what Urshu meant! No!"
    vivi sad "I'm not...I'm not me anymore. I'm..."
    vivi sad "..."
    vivi neutral "I'm..."
    vivi neutral "..."
    show vivi happy
    pause 0.5
    hide vivi happy
    with { "master" : Dissolve(3.0) }
    pause 0.5
    vivi happy "I'm a god, now."

    # $ message = "{i}...Illegible garble...{/i}"
    $ message = "xxxxxxxxxxxxxxxxxxxxxx \nxxxxxxxxx xxxxxxxx \nxxxxxxxx xxxxx xxxxxx xxxxxxxx\nxxxxxx xxxxxxxxxx xxxxxxxxxx \nxxx xxxxx xxxx xxxx xxxxx \nxxxxx \nxxxx \nxxx \nXXX XXX"
    # $ message = "{=strikethrough}{color=#FF0000}{b}starving \n one by one they will be devoured \n give me their light \n starving{/b}{/color}"
    $ message = "{s}{color=#920000}{b}xxxxxxxxxxxxxxxxxxxxxx \nxxxxxxxxx xxxxxxxx \nxxxxxxxx xxxxx xxxxxx xxxxxxxx\nxxxxxx xxxxxxxxxx xxxxxxxxxx \nxxx xxxxx xxxx xxxx xxxxx \nxxxxx \nxxxx \nxxx \nXXX XXX{/b}{/color}{/s}"
    $ eldritch = True

    call display_journal from _call_display_journal_7

    # JUMP to: Epilogue/Eldritch/Vivi
    jump epi_eldritch_vivi