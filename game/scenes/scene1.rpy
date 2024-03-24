### PLACEHOLDER SCENE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lounge

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show urshu angry at right

    # These display lines of dialogue.

    ava ""

    urshu happy "You've created a new {b}Ren'Py game{/b}. Once you {i}add a story, pictures, and music,{/i} you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can"

    # show screen diary

    urshu sad "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "You've created a new Ren'Py game. Once you add a story, pictures and music, you can":

            urshu surprised "Test!"

    hide ava

    jump scene2
