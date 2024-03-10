### EXAMPLE OF TEMPLATE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene2:

    ##########################
    # OREX WRITING TEMPLATE #
    ##########################

    # Put your script in this template!
    # Any line starting with a # is a comment - it doesn't get parsed as code.
    # Use comments often to let your programmers know what you want to happen! If you don't know the code for something, just leave a comment describing what you want.
    # adhere to asset naming conventions for all locations, character names and expressions!
    # IMPORTANT: DUPLICATE THIS TEMPLATE (under File -> Make a copy), do not copy/paste!

    # Gameplay notes:
    # changes to attraction/decay meter start in the Anger section
    # DECAY ROUTE (i.e. skipping choices if decay is high) starts in the Bargaining section

    ##################
    # Scene dialogue #
    ##################

    # Start a scene by telling us the location it takes place, which background to show:

    # LOCATION: lounge

    # tell us which characters are visible (you can put them at right, left, or center of screen)
    # for example, to show player char 'vivi' on the left, using the 'happy' expression:

    show vivi happy at left

    # to show NPC char 'asha' on the right, using the 'neutral' expression:

    show ava neutral at right

    # Now start dialogue using this format, which shows the character, their expression, and what they say:

    vivi neutral "Hello, I'm Vivi."
    vivi happy "I'm a hot mess."
    ava neutral "That you are."

    # For narration (Vivi thinking - the narrative perspective is Vivienne's), we will implement in italics. Write like the example below:

    vivithinking neutral "Does she like me?"

    # If you want us to implement an effect, give us a comment like these examples:

    # SOUND: door closes
    vivi surprised "What was that?"

    # VISUAL: the screen shakes
    ava surprised "Earthquake!!"

    # If you want dialogue that only shows up if an attraction or decay meter is high, write like this:

    # ??ATTRACTION
    ava happy "You're so attractive"
    # END

    # ??DECAY
    ava angry "You're so fake"
    # END

    ##################
    # Dialogue Choices #
    ##################

    # In RenPy, every choice has a prompt and options that branch the story.
    # In this project dialogue choices affect the 'attraction' and/or 'decay' meters, which determine what happens later in game.
    # Increasing attraction pushes you toward romance/friendship ending with that character.
    # Increasing decay pushes you away from romance/friendship ending with ANY character.
    # Some choices may only be available if one of your meters is high enough.

    # First give the line of dialogue or 'prompt' that will show up with the list of choices:

    # <CHOICE>
    ava sad "Will you help me?"

    # next add the dialogue that will show if decay meter is too high and the choices are locked.
    # (note that the decay route is only needed for Bargaining and Depression loops)
    # in this case all the choices are skipped so you then jump to the line that comes next in the story.

    # DECAY ROUTE
    ava neutral "Oh...I can see you don't really care."
    # JUMP TO: vivi "So here's the deal"

    # now start listing the choices that will appear if the decay meter is NOT too high.
    # the first line in the branch is the choice option that will appear, and subsequent lines are the dialogue that happens when you select that choice (keep the indent! use TAB not SPACE)
    # in this example option 1 has no effect on the meters, option 2 increases attraction, option 3 increases decay and option 4 increases both attraction and decay (denoted by + symbol)
    # options 5/6 only unlocked if attraction/decay meter high enough (>> symbol) and can also increase attraction and/or decay - same effects as options 2-4 but get bonus story details
    # all these option types can be mixed and matched as needed for the story!
    # at the end of each branch jump to the line that should come next.

    menu:
        # OPTION 1 
        "I don't know":

            vivi neutral "I don't know"
            ava neutral "Uhh okay" 
            # JUMP TO: vivi "So here's the deal"

        # OPTION 2 +ATTRACTION
        "Sure.":

            vivi neutral "Sure."
            ava happy "Thank you!"
            # JUMP TO: vivi "So here's the deal"

        # OPTION 3 +DECAY
        "Nah.":

            vivi neutral "Nah."
            ava sad "Oh. That's sad."
            # JUMP TO: vivi "Let's go to the observatory and talk more..."

        # OPTION 4 +ATTRACTION +DECAY
        "Anything you want babe":

            vivi neutral "Anything you want babe"
            ava happy "Thank you!"
            # JUMP TO: vivi "So here's the deal"

        # OPTION 5 >>ATTRACTION +ATTRACTION
        "Sure-happy to help":

            vivi neutral "Sure-happy to help"
            ava happy "Thank you! (more bonus dialogue)"
            # JUMP TO: vivi "So here's the deal"

        # OPTION 6 >>DECAY +DECAY
        "Nah I'm way too cool to help anyone":

            vivi neutral "Nah I'm way too cool to help anyone"
            ava sad "Oh. That's sad. (more bonus dialogue)"
            # JUMP TO: vivi "Let's go to the observatory and talk more..."

    # at this point the branching dialogue is over and the dialogue continues

    vivi determined "So here's the deal."
    vivi neutral "Let's go to the observatory and talk more..."

    # at the end of your scene add a comment specifying which scene to go to next

    # JUMP TO: observatory scene

    return
