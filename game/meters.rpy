# Declare attraction and meter variables used by this game.

# define meter variables
label meters:
    # initialize meters
    $ att_meter_ava = 0
    $ att_meter_darius = 0
    $ att_meter_susurha = 0
    $ dec_meter = 0

    # define total meter increase for Anger FR1
    $ att_max_anger_fr1 = 15
    # define total meter increase for Anger FR2
    $ att_max_anger_fr2 = 40
    # define total decay increase for Anger
    $ dec_max_anger = 20

    # define total meter increase for Bargaining FR1
    $ att_max_bargaining_fr1 = 20
    # define total meter increase for Bargaining FR2
    $ att_max_bargaining_fr2 = 55
    # define total decay increase for Bargaining
    $ dec_max_bargaining = 35

    # define total meter increase for Depression FR1
    $ att_max_depression_fr1 = 30
    # define total meter increase for Depression FR2
    $ att_max_depression_fr2 = 65
    # define total decay increase for Depression
    $ dec_max_depression = 45

    # define threshold for romance
    $ romance_threshold = 70

    # define choice number lists for each character
    # guide: [anger_FR1, anger_FR2, bargaining_FR1, bargaining_FR2, depression_FR1, depression_FR2]
    $ att_num_list_ava = [3,4,5,4,4,5]
    $ dec_num_list_ava = [4,5,2,4,3,2]
    $ att_num_list_darius = [2,2,2,2,2,2]
    $ dec_num_list_darius = [2,2,2,3,2,2]
    $ att_num_list_susurha = [1,2,5,5,2,8]
    $ dec_num_list_susurha = [2,4,5,4,1,2]

    # define variable for NPC-dependent meal reveal choice number (just one currently)
    $ att_num_meal_reveal = 1

    return