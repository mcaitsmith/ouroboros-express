init -5 python:


    class CreditsCategory:
        def __init__(self, category, credit_list, image):            
            self.category = category
            self.credit_list = credit_list
            self.image = image


define credits_list = [
    CreditsCategory(category = "{b}{i}NARRATIVE{/i}{/b}\n", credit_list = 
    [
        "{b}Writing{/b}",
        "Haley Bulen",
        "Patrick Christell",
        "Robert Corra",
        "Tiago Da Cunha",
        "Cameron Daxon",
        "Gideon Devendra",
        "Logan Grimes",
        "Zachary Roush",
        "Dylan Sands",
        "Kyle Smith-Laird",
        "{b}Editing{/b}",
        "Allison Bryant",
        "Haley Bulen",
        "hosomeowa",
        "Megan Fleming",
        "Lindsay Howard"
    ], image = "images/snakelogo.png"),
    CreditsCategory(category = "{b}{i}ART{/i}{/b}\n", credit_list = [
        "Onashabay Daniyar",
        "Denochi_",
        "gleamiarts",
        "Stephanie Terrero"
    ], image = "images/vivi and urshu.png"),
    CreditsCategory(category = "{b}{i}SOUND{/i}{/b}\n", credit_list = [
        "Armoni Boone",
        "Max Lincoln",
        "Scott Stinson"
    ], image = "images/vivi expressions.png"),
    CreditsCategory(category = "{b}{i}PROGRAMMING{/i}{/b}\n", credit_list = [
        "Amorphous",
        "Denochi_"
    ], image = "images/vivi and ava.png"),
    CreditsCategory(category = "{b}{i}QA/PLAYTESTING{/i}{/b}\n", credit_list = [
        "{b}QA{/b}",
        "Keumars Afifi-Sabet",
        "Rafael Campbell",
        "Patrick Christell",
        "Robert Corra",
        "Jonathan Rhee",
        "Cameryn Tuliao",
        "{b}Playtesting{/b}",
        "Keumars Afifi-Sabet",
        "Mohammad Al Hadiansyah Suwandhy",
        "Rafael Campbell",
        "Marcelo Domingues",
        "Megan Fleming",
        "Patrick Knisely",
        "Anika Konkati",
        "Aaron Mesnard",
        "Jonathan Rhee",
        "Thomasina Rogers",
        "Kyle Smith-Laird",
        "Ines Souquett",
        "Cameryn Tuliao"
    ], image = "images/vivi bruh.png"),
    CreditsCategory(category = "{b}{i}LEADS{/i}{/b}\n", credit_list = [
        "{b}Narrative Lead{/b}",
        "Salvador Bas Folch",
        "{b}Narrative Producer{/b}",
        "Anivette Wong",
        "{b}Art Lead{/b}",
        "fruitsicaljams",
        "{b}Sound Lead{/b}",
        "Andrea Saravia Pérez",
        "{b}Programming Lead{/b}",
        "Mica Smith"
    ], image = "images/vivi in the train being all mysterious and such.png"),
    # CreditsCategory(category = "{b}{i}DIRECTOR{/i}{/b}\n", credit_list = [
    #     "Najmah Salam"
    # ], image = "images/thumbnail concept.png"),
]

define credits_list2 = [
    CreditsCategory(category = "{b}{i}VOICEOVER{/i}{/b}\n", credit_list = 
    [
        "{b}VO Cast{/b}",
        "Allyson Frazier - Vivi",
        "Preston Yeung - Susu'Rha",
        "Rydberg Delta - Darius",
        "Sean Baxendale - Urshu",
        "Sera Milano - Avatar of Asha",
        "Stephanie Terrero",
        "{b}VO Production{/b}",
        "Lindsay Howard",
        "Alan Moore",
        "Jonathan Rhee",
        "Kyle Smith-Laird",
        "Logan Grimes",
        "Noah Campodonico",
        "Sisi Peng",
        "Stephanie Terrero",
        "Alec Viera"
    ], image = "images/fanart_vivi.png"),
    CreditsCategory(category = "{b}{i}NARRATIVE{/i}{/b}\n", credit_list = [
        "Salvador Bas Folch",
        "Cameron Daxon",
        "Carrie Talbot",
        "Dylan Sands",
        "Alan Moore",
        "Kyle Smith-Laird",
        "Logan Grimes",
        "Sera Milano",
        "Sisi Peng"
    ], image = "images/fanart_susurha.png"),
    CreditsCategory(category = "{b}{i}ART{/i}{/b}\n", credit_list = [
        "Vinny Konawalik",
        "Stephanie Terrero",
        "Cleo Weeks",
        "Dylan Chambore",
        "Den",
        "Perri Polyviou",
        "Rachel Lee"
    ], image = "images/fanart_darius.png"),
    CreditsCategory(category = "{b}{i}SOUND{/i}{/b}\n", credit_list = [
        "Armoni Boone",
        "Scott Stinson",
        "Charlie Armour"
    ], image = None),
    CreditsCategory(category = "{b}{i}PROGRAMMING{/i}{/b}\n", credit_list = [
        "Mica Smith",
        "Den",
        "Special thanks to Daniel Westfall"
    ], image = "images/fanart_ava.png"),
    CreditsCategory(category = "{b}{i}ACCESSIBILITY{/i}{/b}\n", credit_list = [
        "Alice",
        "Stephanie Terrero"
    ], image = None),
    CreditsCategory(category = "{b}{i}QA{/i}{/b}\n", credit_list = [
        "Rafael Campbell",
        "Rachel Lee",
        "Carrie Talbot",
        "Damon Day",
        "Jonathan Rhee"
    ], image = None),
    CreditsCategory(category = "{b}{i}LEADS{/i}{/b}\n", credit_list = [
        "{b}Narrative Lead{/b}",
        "Tiago Da Cunha",
        "{b}Art Lead{/b}",
        "Vinny Konawalik",
        "{b}QA Lead{/b}",
        "Rafael Campbell",
        "{b}Sound Lead{/b}",
        "Noah Campodonico",
        "{b}Programming Lead{/b}",
        "Mica Smith",
        "{b}Voiceover Producer{/b}",
        "Lindsay Howard",
        "{b}Casting Director{/b}",
        "Lindsay Howard",
        "{b}Voiceover Director{/b}",
        "Alan Moore",
        "{b}Lead Producer{/b}",
        "Rachel Lee",
    ], image = "images/fanart_urshu.png"),
    CreditsCategory(category = "{b}{i}MARKETING{/i}{/b}\n", credit_list = [
        "Alice Cross",
        "Armoni Boone",
        "Dylan Sands",
        "Kelsey Phelan",
        "Kshitij Khandare",
        "Sisi Peng"
    ], image = None),
    CreditsCategory(category = "{b}{i}DIRECTOR{/i}{/b}\n", credit_list = [
        "Najmah Salam"
    ], image = None),
    # CreditsCategory(category = "{b}{i}Special Thanks{/i}{/b}\n", credit_list = [
    #     "Daniel Westfall"
    # ], image = None),
    CreditsCategory(category = "Use of the terms “mindflayer” and “illithid” in The Ouroboros Express\nis unofficial Fan Content permitted under the Fan Content Policy.\nNot approved/endorsed by Wizards.\nThese portions of the materials used are property of Wizards of the Coast.\n©Wizards of the Coast LLC.", credit_list = [
    ], image = None),
]

# define credits_list3 = [
    # CreditsCategory(category = "{b}{i}DIRECTOR{/i}{/b}\n", credit_list = [
    #     "Najmah Salam"
    # ], image = None),
# ]