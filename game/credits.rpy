# adapted from https://lemmasoft.renai.us/forums/viewtopic.php?t=42667
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

# to call credits screen use commented code below at end of final game scene:
# $ quick_menu = False # hide quick menu
# call screen credits ## Show credits screen.
# return ## return to main menu

transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -2950

## Credits screen.

screen credits():
    style_prefix "credits"

    add "#000000"

    # timer 10.0 action Return()
    timer 40.0 action Return()

    # frame at credits_scroll(10.0):
    frame at credits_scroll(30.0):
        background None
        xalign 0.5

        vbox:

            label "Credits"

            null height 20
            spacing 60

            for credit in credits_list:

                vbox:
                    add "images/logo.png"

                vbox:
                    spacing 4
                    text "{b}" + credit.category + "{/b}"
                    for name in credit.credit_list:
                        text name

            null height 200
            # spacing 60

            vbox:
                add "images/logo.png"

            vbox:
                text "{b}SMALL LOAN STUDIO{/b}"
                text "https://smallloanstudio.wordpress.com"
                text "Thanks for playing!"

style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    spacing 40
    ysize 30

style credits_vbox_logo:
    xalign 0.5
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_label_text:
    size gui.title_text_size*0.5

style credits_text:
    xalign 0.5
    color "#FFF"