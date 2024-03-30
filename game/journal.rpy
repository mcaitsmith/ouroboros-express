label journal:
    # Journal start
    define journal_array = []
    define max_decay = 100
    define max_affection = 100
    screen journal:
        modal False
        frame xalign 0.5 yalign 0.05:
            vbox xalign 0.5:
                # Journal background
                image "journal/journal.png":
                    xalign 0.5
        # nameplates
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.63
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.41
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.19
        # icons
        image "journal/susu_icon.png":
                    xalign 0.54 yalign 0.635
        image "journal/ava_icon.png":
                    xalign 0.54 yalign 0.41
        image "journal/darius_icon.png":
                    xalign 0.54 yalign 0.185
        #bars
        image "journal/bar_empty.png":
            xalign 0.64 yalign 0.54
        image "journal/bar_empty.png":
            xalign 0.64 yalign 0.3
        image "journal/bar_empty.png":
            xalign 0.64 yalign 0.06
        bar value AnimatedValue(dec_meter, max_decay, delay=1.0):
            xalign 0.33 yalign 0.6
            xmaximum 327
            ymaximum 80
            right_bar Frame("images/journal/time_empty.png", 100, 10)
            left_bar Frame("images/journal/time_full.png", 100, 10)
        bar value AnimatedValue(att_meter_susurha, max_affection, delay=1.0):
            xalign 0.63 yalign 0.54
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        bar value AnimatedValue(att_meter_ava, max_affection, delay=1.0):
            xalign 0.63 yalign 0.3
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        bar value AnimatedValue(att_meter_darius, max_affection, delay=1.0):
            xalign 0.63 yalign 0.06
            xmaximum 251
            ymaximum 120
            right_bar Frame("images/journal/bar_empty2.png", 100, 10)
            left_bar Frame("images/journal/bar_full2.png", 100, 10)
        # name text
        text "{color=#ffffff}Susu'Rha{/color}" xalign 0.64 yalign 0.625
        text "{color=#ffffff}Avatar of Asha{/color}" xalign 0.64 yalign 0.41
        text "{color=#ffffff}Darius{/color}" xalign 0.64 yalign 0.195
        # determine diary note
        # if len(journal_array) >= 1:
        if cycle == 0:
            text "{font=Slimamif.ttf}{size=20}{color=#000000}{b}DAY 1{/b}{/color}{/font}{/size}"  xalign 0.33 yalign 0.1
            text "{font=Slimamif.ttf}{size=20}{color=#000000}[message]{/color}{/font}{/size}" xalign 0.28 yalign 0.20
        # if len(journal_array) >= 2:
        if cycle == 1:
            # text "{color=#000000}DAY 2{/color}"  xalign 0.25 yalign 0.2
            text "{font=Slimamif.ttf}{size=20}{color=#000000}{b}DAY 2{/b}{/color}{/font}{/size}"  xalign 0.33 yalign 0.1
            # text "{color=#000000}[journal_array[1]]{/color}" xalign 0.25 yalign 0.23
            text "{font=Slimamif.ttf}{size=20}{color=#000000}[message]{/color}{/font}{/size}" xalign 0.28 yalign 0.20
        # if len(journal_array) >= 3:
        if cycle == 2:
            # text "{color=#000000}DAY 3{/color}"  xalign 0.25 yalign 0.3
            text "{font=Slimamif.ttf}{size=20}{color=#000000}{b}DAY 3{/b}{/color}{/font}{/size}"  xalign 0.33 yalign 0.1
            # text "{color=#000000}[journal_array[2]]{/color}" xalign 0.25 yalign 0.33
            text "{font=Slimamif.ttf}{size=20}{color=#000000}[message]{/color}{/font}{/size}" xalign 0.28 yalign 0.20
        # if len(journal_array) >= 4:
        if cycle == 3:
            # text "{color=#000000}DAY 4{/color}"  xalign 0.25 yalign 0.4
            text "{font=Slimamif.ttf}{size=20}{color=#000000}{b}DAY 4{/b}{/color}{/font}{/size}"  xalign 0.33 yalign 0.1
            # text "{color=#000000}[journal_array[3]]{/color}" xalign 0.25 yalign 0.43
            text "{font=Slimamif.ttf}{size=20}{color=#000000}[message]{/color}{/font}{/size}" xalign 0.28 yalign 0.20
        if cycle == 4:
            # text "{color=#000000}DAY 4{/color}"  xalign 0.25 yalign 0.4
            text "{font=Slimamif.ttf}{size=20}{color=#000000}{b}DAY 5{/b}{/color}{/font}{/size}"  xalign 0.33 yalign 0.1
            # text "{color=#000000}[journal_array[3]]{/color}" xalign 0.25 yalign 0.43
            text "{font=Slimamif.ttf}{size=20}{color=#000000}[message]{/color}{/font}{/size}" xalign 0.28 yalign 0.20
        #determine darius note
        if eldritch == True:
            text "{font=Slimamif.ttf}{size=16}{color=#920000}{i}{s}UUUuuURssshhuuuUU{/s}{/i}{/color}{/size}{/font}" :
                xalign 0.785 yalign 0.08
        elif att_meter_darius >= 0 and att_meter_darius <= 100 :
            if att_meter_darius == 0:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}????{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
            elif att_meter_darius <= 20:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}What a specimen! \nNot sure if more \nsurprised at their stor-\ny or their physiology.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
            elif att_meter_darius <= 40:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}kinda...hot{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
            elif att_meter_darius <= 60:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Their baggage \nis wearing them \ndown. It affects\n me...{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
            elif att_meter_darius <= 80:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Tormented by \npast. I can \nsave them.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
            elif att_meter_darius <= 100:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}The end changed \nthem, made them \nanew.I want that too.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.08
        elif att_meter_darius > 100:
            text "{font=Slimamif.ttf}{size=16}{color=#000000}The end changed \nthem, made them \nanew.I want that too.{/color}{/size}{/font}" :
                xalign 0.785 yalign 0.08
        #determine ava note
        if eldritch == True:
            text "{font=Slimamif.ttf}{size=16}{color=#920000}{i}{s}yYYyoouuu Sooon OF {/s}{/i}{/color}{/size}{/font}" :
                xalign 0.785 yalign 0.315
        elif att_meter_ava >= 0 and att_meter_ava <= 100 :
            
            if att_meter_ava == 0:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}????{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
            elif att_meter_ava <= 20:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Caution: Compli-\ncated background. \nPrincess or \ncaptive?{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
            elif att_meter_ava <= 40:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}kinda WOW{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
            elif att_meter_ava <= 60:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}We're more alike\nthan I thought. \nActually pretty friendly.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
            elif att_meter_ava <= 80:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Can't imagine being \nin her shoes... \nBut hardship has \nmade her an\nincredible person.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
            elif att_meter_ava <= 100:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}A new sun rises... \nbrighter than any \ndeity.(did I just \nwrite that? so tacky){/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.315
        elif att_meter_ava > 100:
            text "{font=Slimamif.ttf}{size=16}{color=#000000}A new sun rises... \nbrighter than any \ndeity.(did I just \nwrite that? so tacky){/color}{/size}{/font}" :
                xalign 0.785 yalign 0.315
        # determine susurha note
        if eldritch == True:
            text "{font=Slimamif.ttf}{size=16}{color=#920000}{i}{s}a B?TCH{/s}{/i}{/color}{/size}{/font}" :
                xalign 0.785 yalign 0.55
        elif att_meter_susurha >= 0 and att_meter_susurha <= 100 :
            if att_meter_susurha == 0:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}????{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
            elif att_meter_susurha <= 20:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Are they the \nmost normal of the \nlot? Evasive; must \ncrack that juice.{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
            elif att_meter_susurha <= 40:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}kinda cute!{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
            elif att_meter_susurha <= 60:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}Cool hang when \nin the right mood. \nKinda want to \nadventure together...{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
            elif att_meter_susurha <= 80:
                text "{font=Slimamif.ttf}{size=16}{color=#000000}I feel you, Susu'Rha. \nI also isolated myself \nfrom my family. \nIs this fate?{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
            elif att_meter_susurha <= 100 :
                text "{font=Slimamif.ttf}{size=16}{color=#000000}I knew this as \na kid--dragons aren't \nscary! They're based!{/color}{/size}{/font}" :
                    xalign 0.785 yalign 0.55
        elif att_meter_susurha > 100:
            text "{font=Slimamif.ttf}{size=16}{color=#000000}I knew this as \na kid--dragons aren't \nscary! They're based!{/color}{/size}{/font}" :
                xalign 0.785 yalign 0.55
           
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