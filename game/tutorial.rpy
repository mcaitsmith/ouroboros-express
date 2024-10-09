define message_tutorial = """Welcome to the Ouroboros Express! As you travel aboard this mysterious train,
you'll have the opportunity to interact with your fellow challenges, uncover
hidden stories and navigate unique challenges.\n
Each day is split in two parts: use the first to gather information and the second
to take action.\n
But remember this rule! Whoever you choose as a companion for your first half
of the day won't be available for the second.
"""
define message_relationship_levels = """Relationship levels indicate how strong Vivi's connection is with each passanger:
interacting and choosing responses wisely can strengthen these bonds.
"""
define message_journal = """From now onward, the journal will reflect the impact of Vivi's actions. You can check
it anytime, allowin you to see your progress as you go. That means: check it often!
"""
define message_choice_selection = """When a dialogue choice appears, select Vivi's response carefully as it may impact
her relationships and her own mental state. As the second part of the day is for
action, your choices there will have a bigger impact on the game.
"""
define message_bottom_navigation = """ The bottom navigation gives access to various options such as manual saving, quick
saving, quick loading, skipping to the next choice, advancing text automatically, 
going back, reviewing the conversation history, and viewing settings.
"""
define message_relationship_meter = """The Decay meter (green) fills as Vivi isolates hersof or masks her thoughts, while the 
Attraction meter (red) grows when Vivi does not hide her true feelings.
"""
define message_vivis_diary = """Vivi's journal entry provides thoughts and reflections on the current day.
It can be accessed anytime in your journal through the menu.
"""

# tutorial screen
label tutorial:
    screen tutorial(tutorial_name):
        modal False
        viewport xalign 0.5 yalign 0.5:
            xysize(1400,740)
            image "tutorial/tutorial_bg.png"
            vbox xalign 0.5:
                null height 100
                if tutorial_name == "tutorial":
                    text "Tutorial" size 48 xalign 0.5
                    null height 50
                    text message_tutorial xalign 0.5 text_align 0.5
                elif tutorial_name == "bottom_navigation":
                    text "Bottom Navigation" size 48 xalign 0.5
                    null height 100
                    image "tutorial/bottom_nav.png"
                    null height 100
                    text message_bottom_navigation xalign 0.5 text_align 0.5
                elif tutorial_name == "choice_selection":
                    text "Choice Selection" size 48 xalign 0.5
                    null height 20
                    image "tutorial/choice_selection.png" xalign 0.5
                    null height 20
                    text message_choice_selection xalign 0.5 text_align 0.5
                elif tutorial_name == "journal":
                    text "Journal" size 48 xalign 0.5
                    null height 40
                    image "tutorial/journal.png" xalign 0.5
                    null height 40
                    text message_journal xalign 0.5 text_align 0.5
                elif tutorial_name == "vivis_diary":
                    text "Vivi's Journal Entry" size 48 xalign 0.5
                    null height 50
                    image "tutorial/vivis_diary.png" xalign 0.5
                    null height 50
                    text message_vivis_diary xalign 0.5 text_align 0.5
                elif tutorial_name == "relationship_meter":
                    text "Relationship Meter" size 48 xalign 0.5
                    null height 50
                    hbox xalign 0.5:
                        image "tutorial/attraction_meter.png"
                        null width 50
                        image "tutorial/decay_meter.png"
                    null height 100
                    text message_relationship_meter xalign 0.5 text_align 0.5
                elif tutorial_name == "relationship_levels":
                    text "Relationship Levels" size 48 xalign 0.5
                    null height 50
                    image "tutorial/relationship_level.png" xalign 0.5
                    null height 30
                    text message_relationship_levels xalign 0.5 text_align 0.5
                
        


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
