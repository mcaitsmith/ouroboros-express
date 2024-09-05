# The scene starts here.

label welcome_meal:

    #The Welcome Meal

    #Naj's Note: The other passengers are in silhouette and then revealed.

    # fade in

    # LOCATION: diningcar
    play sound train loop
    scene diningcar with fade

    show vivi neutral at left with dissolve :
        xzoom -1

    show urshu neutral at right with dissolve

    urshu neutral "Welcome to the dining car. The food will be out shortly."
    vivi neutral "It all smells del--"

    show vivi surprised at left

    # VISUAL: the screen shakes
    show diningcar with hpunch

    vivithinking surprised "WHAT THE—"

    hide urshu with dissolve
    hide vivi with dissolve

    show ava silhouette at left with dissolve:
        xzoom -1.0

    show darius silhouette at center with dissolve

    show susurha silhouette at right with dissolve

    vivi neutral "..."

    # hide ava silhouette with dissolve

    # hide darius silhouette with dissolve

    # hide susurha silhouette with dissolve

    show vivi surprised at left with dissolve:
        xzoom -1

    vivi surprised "Umm...Urshu?"

    show urshu neutral at right with dissolve

    urshu neutral "Yes, Miss Sanssouci?"
    vivi surprised "Was I supposed to show up in costume?"
    urshu neutral "What do you mean?"
    vivi surprised "Everyone here's wearing a mask..."
    urshu happy "Ha! I suppose you're right. Everyone IS wearing some sort of mask of their own making. You most of all, Miss Sanssouci."
    vivi angry blush "What the hell is that supposed to mean?!"
    urshu happy "You'll see soon enough."
    urshu neutral "I hope..."
    urshu neutral "In the meantime, I suggest you begin interviewing your fellow passengers while it is still early in your stay. That {i}is{/i} what you came here for, is it not?"
    vivithinking neutral "I just came here so I could pay my rent."
    vivi neutral "Okay. I guess I can start. Though I wish I had a little more time to get acclimated."
    urshu neutral "There's never enough time, Miss Sanssouci. Though there is always enough to seek companionship, I daresay!" 

    # urshu exits
    hide urshu with dissolve

    vivithinking neutral "What's his deal?"
    vivithinking neutral "Whatever. The sooner I start, the sooner I can get outta here."

    #NOTE all options will be explored before continuing.

    $ interview1 = False
    $ interview2 = False
    $ interview3 = False

    label interview_choice:
        hide vivi with dissolve
        if interview1 == True and interview2 == True and interview3 == True:
            stop sound fadeout 2.0
            jump figuring_it_out
        else:
            if not interview1:
                show ava silhouette at left with dissolve:
                    xzoom -1.0
            else:
                show ava neutral at left with dissolve:
                    xzoom -1.0
            if not interview2:
                show darius silhouette at center with dissolve
            else:
                show darius neutral at center with dissolve
            if not interview3:
                show susurha silhouette at right with dissolve
            else:
                show susurha neutral at right with dissolve

            # <CHOICE>
            if interview1 == False and interview2 == False and interview3 == False:
                vivithinking neutral "Let's see. Who should I interview first?"
            else:
                vivithinking neutral "Who should I interview next?"

            menu:
                # OPTION 1 
                "The lady in the fine dress" if interview1 == False:

                    $ interview1 = True

                    hide darius silhouette with dissolve

                    hide susurha silhouette with dissolve

                    vivithinking neutral "Let's talk to the lady in the fine dress and... Is that a crown? She seems interesting."

                    show ava silhouette at right with moveinright
                    show ava silhouette at right:
                        xzoom 1.0

                    # JUMP TO: Interviews / Avatar of Asha
                    jump interview_ava

                # OPTION 2
                "The squid person" if interview2 == False:

                    $ interview2 = True

                    hide ava silhouette with dissolve

                    hide susurha silhouette with dissolve

                    vivithinking neutral "That person went all out with their costume. Those tentacles look so lifelike. I've gotta interview them."

                    show darius silhouette at right with moveinright

                    # JUMP TO: Interviews / Darius Wrecker
                    jump interview_darius

                # OPTION 3
                "The gecko" if interview3 == False:

                    $ interview3 = True

                    hide ava silhouette with dissolve

                    hide darius silhouette with dissolve

                    vivithinking neutral "Let's interview whoever's dressed as a giant gecko, shall we? I really don't understand the theme of this costume party."

                    show susurha silhouette at right with moveinright

                    # JUMP TO: Interviews / Susu'Rha Balrinn
                    jump interview_susurha