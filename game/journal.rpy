label journal:
    
    image journal = "images/journal/journal.png"
    define journal_array = []
    define time =1
    define max_time = 4
    define affection = 52
    define max_affection = 100
    screen journal:
        modal False
        frame xalign 0.5 yalign 0.05:
            vbox xalign 0.5:
                image "journal/journal.png":
                    xalign 0.5
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.63
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.41
        image "journal/name_plate.png":
                    xalign 0.65 yalign 0.19
        image "journal/susu_icon.png":
                    xalign 0.54 yalign 0.635
        image "journal/ava_icon.png":
                    xalign 0.54 yalign 0.41
        image "journal/darius_icon.png":
                    xalign 0.54 yalign 0.185
        
        bar value AnimatedValue(time, max_time, delay=1.0):
            xalign 0.33 yalign 0.6
            xmaximum 327
            ymaximum 80
            right_bar Frame("images/journal/time_empty.png", 100, 10)
            left_bar Frame("images/journal/time_full.png", 100, 10)
        bar value AnimatedValue(affection, max_affection, delay=1.0):
            xalign 0.63 yalign 0.54
            xmaximum 327
            ymaximum 120
            right_bar Frame("images/journal/bar_empty.png", 100, 10)
            left_bar Frame("images/journal/bar_full.png", 100, 10)
        bar value AnimatedValue(affection, max_affection, delay=1.0):
            xalign 0.63 yalign 0.3
            xmaximum 327
            ymaximum 120
            right_bar Frame("images/journal/bar_empty.png", 100, 10)
            left_bar Frame("images/journal/bar_full.png", 100, 10)
        bar value AnimatedValue(affection, max_affection, delay=1.0):
            xalign 0.63 yalign 0.06
            xmaximum 327
            ymaximum 120
            right_bar Frame("images/journal/bar_empty.png", 100, 10)
            left_bar Frame("images/journal/bar_full.png", 100, 10)
        text "{color=#ffffff}Susu'Rha{/color}" xalign 0.64 yalign 0.625
        text "{color=#ffffff}Avatar of Asha{/color}" xalign 0.64 yalign 0.41
        text "{color=#ffffff}Darius{/color}" xalign 0.64 yalign 0.195
            
        if len(journal_array) >= 1:
            text "{color=#000000}DAY 1{/color}"  xalign 0.25 yalign 0.1
            text "{color=#000000}[journal_array[0]]{/color}" xalign 0.25 yalign 0.13
        if len(journal_array) >= 2:
            text "{color=#000000}DAY 2{/color}"  xalign 0.25 yalign 0.2
            text "{color=#000000}[journal_array[1]]{/color}" xalign 0.25 yalign 0.23
        if len(journal_array) >= 3:
            text "{color=#000000}DAY 3{/color}"  xalign 0.25 yalign 0.3
            text "{color=#000000}[journal_array[2]]{/color}" xalign 0.25 yalign 0.33
        if len(journal_array) >= 4:
            text "{color=#000000}DAY 4{/color}"  xalign 0.25 yalign 0.4
            text "{color=#000000}[journal_array[3]]{/color}" xalign 0.25 yalign 0.43
        