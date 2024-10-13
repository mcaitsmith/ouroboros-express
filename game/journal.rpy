label journal:
    # Journal start
    define journal_array = []
    define max_decay = 100
    define max_affection = 100
    screen journal:
        modal False
        frame xalign 0.5 yalign 0.5: # +0.45
            vbox xalign 0.5:
                # Journal background
                image "journal/journal.png":
                    xalign 0.5
        # nameplates
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.77 # +0.15
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.55
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.33
        # icons
        image "journal/susu_icon.png":
                    xalign 0.54 yalign 0.775
        image "journal/ava_icon.png":
                    xalign 0.54 yalign 0.55
        image "journal/darius_icon.png":
                    xalign 0.54 yalign 0.325
        #bars
        image "journal/bar_empty.png":
            xalign 0.635 yalign 0.69
        image "journal/bar_empty.png":
            xalign 0.635 yalign 0.45
        image "journal/bar_empty.png":
            xalign 0.635 yalign 0.21
        bar value AnimatedValue(dec_meter, max_decay, delay=1.0):
            xalign 0.325 yalign 0.75
            xmaximum 327
            ymaximum 80
            right_bar Frame("images/journal/time_empty.png", 100, 10)
            left_bar Frame("images/journal/time_full.png", 100, 10)
        bar value AnimatedValue(att_meter_susurha, max_affection, delay=1.0):
            xalign 0.625 yalign 0.69
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        bar value AnimatedValue(att_meter_ava, max_affection, delay=1.0):
            xalign 0.625 yalign 0.45
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        bar value AnimatedValue(att_meter_darius, max_affection, delay=1.0):
            xalign 0.625 yalign 0.21
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        # name text
        text "{color=#ffffff}Susu'Rha{/color}" xpos 1155 ypos 796 # +144
        text "{color=#ffffff}Avatar of Asha{/color}" xpos 1115 ypos 567
        text "{color=#ffffff}Darius{/color}" xpos 1170 ypos 340
        # determine diary note
        # note 9/6/24 - 14 lines max, ~42 chars max per line
        # if len(journal_array) >= 1:
        vbox xpos 395 ypos 265:
            text "DAY [cycle]" size 32 font "fonts/Kalam-Bold.ttf" color "#000000" xalign 0.5
            null height 15
            viewport xsize 520 ysize 360:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                text message size 24 kerning 1.5 font "fonts/Kalam-Bold.ttf" color "#000000"

        # if cycle == 0:
        #     text "{font=Kalam-Bold.ttf}{size=32}{k=1.5}{color=#000000}DAY 1{/color}{/k}{/font}{/size}"  xalign 0.33 yalign 0.26
        #     text "{font=Kalam-Bold.ttf}{size=24}{k=1.5}{color=#000000}[message]{/color}{/k}{/font}{/size}" xpos 400 xanchor 0.0 ypos 314 yanchor 0.0
        # # if len(journal_array) >= 2:
        # if cycle == 1:
        #     # text "{color=#000000}DAY 2{/color}"  xalign 0.25 yalign 0.2
        #     text "{font=Kalam-Bold.ttf}{size=32}{k=1.5}{color=#000000}DAY 2{/color}{/k}{/font}{/size}"  xalign 0.33 yalign 0.26
        #     # text "{color=#000000}[journal_array[1]]{/color}" xalign 0.25 yalign 0.23
        #     text "{font=Kalam-Bold.ttf}{size=24}{k=1.5}{color=#000000}[message]{/color}{/k}{/font}{/size}" xpos 400 xanchor 0.0 ypos 314 yanchor 0.0
        # # if len(journal_array) >= 3:
        # if cycle == 2:
        #     # text "{color=#000000}DAY 3{/color}"  xalign 0.25 yalign 0.3
        #     text "{font=Kalam-Bold.ttf}{size=32}{k=1.5}{color=#000000}DAY 3{/color}{/k}{/font}{/size}"  xalign 0.33 yalign 0.26
        #     # text "{color=#000000}[journal_array[2]]{/color}" xalign 0.25 yalign 0.33
        #     text "{font=Kalam-Bold.ttf}{size=24}{k=1.5}{color=#000000}[message]{/color}{/k}{/font}{/size}" xpos 400 xanchor 0.0 ypos 314 yanchor 0.0
        # # if len(journal_array) >= 4:
        # if cycle == 3:
        #     # text "{color=#000000}DAY 4{/color}"  xalign 0.25 yalign 0.4
        #     text "{font=Kalam-Bold.ttf}{size=32}{k=1.5}{color=#000000}DAY 4{/color}{/k}{/font}{/size}"  xalign 0.33 yalign 0.26
        #     # text "{color=#000000}[journal_array[3]]{/color}" xalign 0.25 yalign 0.43
        #     text "{font=Kalam-Bold.ttf}{size=24}{k=1.5}{color=#000000}[message]{/color}{/k}{/font}{/size}" xpos 400 xanchor 0.0 ypos 314 yanchor 0.0
        # if cycle == 4:
        #     # text "{color=#000000}DAY 4{/color}"  xalign 0.25 yalign 0.4
        #     text "{font=Kalam-Bold.ttf}{size=32}{k=1.5}{color=#000000}DAY 5{/color}{/k}{/font}{/size}"  xalign 0.33 yalign 0.26
        #     # text "{color=#000000}[journal_array[3]]{/color}" xalign 0.25 yalign 0.43
        #     text "{font=Kalam-Bold.ttf}{size=24}{k=1.5}{color=#000000}[message]{/color}{/k}{/font}{/size}" xpos 400 xanchor 0.0 ypos 314 yanchor 0.0
        # note as of 9/6/24: 14 chars max per line, 5 lines max
        #determine darius note
        if eldritch == True:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#920000}{i}{s}\nUUUuuUR\nssshhu\nuuUU{/s}{/i}{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 240
        elif att_meter_darius >= 0 and att_meter_darius <= 100 :
            if att_meter_darius == 0:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}\n\n????{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
            elif att_meter_darius <= 20:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Not sure if\nmore surprised\nat their story\nor their\nphysiology.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
            elif att_meter_darius <= 40:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}There's an allure\nto him,\nmust know\nmore.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
            elif att_meter_darius <= 60:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Their baggage \nis wearing\nthem down.\nIt affects\nme...{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
            elif att_meter_darius <= 80:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Tormented by \npast. I can \nsave them.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
            elif att_meter_darius <= 100:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}The end\nchanged them,\nmade them \nanew. I want\nthat too.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 240
        elif att_meter_darius > 100:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}The end\nchanged them,\nmade them \nanew. I want\nthat too.{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 240
        #determine ava note
        if eldritch == True:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#920000}{i}{s}\nyYYyoouuu\nSooon OF {/s}{/i}{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 465
        elif att_meter_ava >= 0 and att_meter_ava <= 100 :
            
            if att_meter_ava == 0:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}\n\n????{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
            elif att_meter_ava <= 20:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Caution:\nComplicated\nbackground.\nPrincess or \ncaptive?{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
            elif att_meter_ava <= 40:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}kinda WOW{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
            elif att_meter_ava <= 60:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}We're more\nalike than I\nthought. Actually\npretty friendly.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
            elif att_meter_ava <= 80:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Can't imagine\nbeing in her\nshoes...hard-\nship made her\nincredible.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
            elif att_meter_ava <= 100:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}A new sun\nrises... \nbrighter than\nany deity.{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 465
        elif att_meter_ava > 100:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}A new sun\nrises... \nbrighter than\nany deity.{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 465
        # determine susurha note
        if eldritch == True:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#920000}{i}{s}\n\na B?TCH{/s}{/i}{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 690
        elif att_meter_susurha >= 0 and att_meter_susurha <= 100 :
            if att_meter_susurha == 0:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}\n\n????{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
            elif att_meter_susurha <= 20:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Are they the \nmost normal of\nthe lot?\nEvasive...{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
            elif att_meter_susurha <= 40:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}kinda cute!{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
            elif att_meter_susurha <= 60:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}Cool hang when\nin the right\nmood. Want to\nadventure\ntogether...{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
            elif att_meter_susurha <= 80:
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}I feel you. I\nalso isolated\nmyself from my\nfamily. \nIs this fate?{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
            elif att_meter_susurha <= 100 :
                text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}I knew this as \na kid--dragons\naren't scary!\nThey're based!{/color}{/k}{/size}{/font}" :
                    xpos 1370 ypos 690
        elif att_meter_susurha > 100:
            text "{font=Kalam-Bold.ttf}{size=20}{k=1.5}{color=#000000}I knew this as \na kid--dragons\naren't scary!\nThey're based!{/color}{/k}{/size}{/font}" :
                xpos 1370 ypos 690
           
    return
# display journal on screen
label display_journal:
    $ journal_array = []
    window hide dissolve
    # show screen journal with dissolve
    # vivithinking "I should write something to the journal."
    # define message = ""
    # python :
    #     message = renpy.input("What should I write:", length = 64)
    #     print(cycle)
    #     if len(journal_array) == 0:
    #         journal_array.insert(cycle,message)
    #     elif len(journal_array)>0 :
    #         if len(journal_array) == cycle+1:
    #             journal_array.pop(cycle)
    #         journal_array.insert(cycle,message)
        # journal_array = ["test"]
        # journal_array.insert(cycle,"test")
            
    show screen journal with dissolve
    $ renpy.pause()
    hide screen journal with dissolve
    return