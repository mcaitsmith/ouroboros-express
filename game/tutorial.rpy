label tutorial:
    screen tutorial(tutorial_name):
        modal False
        vbox xalign 0.5 yalign 0.5:
            image "tutorial/[tutorial_name].png":
                xalign 0.5

        


label display_tutorial:
    show screen tutorial("tutorial") with dissolve
    $ renpy.pause()
    show screen tutorial("bottom_navigation") with dissolve
    $ renpy.pause()
    show screen tutorial("choice_selection") with dissolve
    $ renpy.pause()
    if has_journal:
        show screen tutorial("journal") with dissolve
        $ renpy.pause()
        show screen tutorial("vivis_diary") with dissolve
        $ renpy.pause()
        show screen tutorial("relationship_meter") with dissolve
        $ renpy.pause()
        show screen tutorial("relationship_levels") with dissolve
        $ renpy.pause()
    hide screen tutorial with dissolve
    return
