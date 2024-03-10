### PLACEHOLDER SCENE ###

# The script of the scene goes in this file.

# The scene starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    play sound blip # example of playing sound 'blip'

    e "Once you add a story, pictures, and music, you can release it to the world!"

    hide eileen

    jump scene2
