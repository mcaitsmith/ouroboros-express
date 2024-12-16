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
    CreditsCategory(category = "{b}{i}ACCESSIBILITY{/i}{/b}\n", credit_list = [
        "Alice Cross",
        "Stephanie Terrero"
    ], image = "images/fanart_vivi.png"),
    CreditsCategory(category = "{b}{i}ART{/i}{/b}\n", credit_list = [
        "Vinny Konawalik - Art Lead, Artist",
        "Cleo Weeks - Artist",
        "Deniz Dilek - Artist",
        "Dylan Chambore - Artist",
        "Perri Polyviou - Artist",
        "Rachel Lee - Artist"
    ], image = None),
    CreditsCategory(category = "{b}{i}AUDIO{/i}{/b}\n", credit_list = [
        "Noah Campodonico - Audio Lead",
        "{b}Sound{/b}",
        "Noah Campodonico - Sound Designer",
        "Alec Viera - Additional Audio Support",
        "{b}Music{/b}",
        "Armoni Boone - Composer",
        "Charlie Armour - Composer",
        "Noah Campodonico - Composer",
        "Scott Stinson - Composer",
        "{b}Voiceover Cast{/b}",
        "Allyson Frazier - Vivienne Sanssouci",
        "Preston Yeung - Susu’Rha Balrinn",
        "Rydberg Delta - Darius Wrecker",
        "Sean Baxendale - Urshunabi",
        "Sera Milano - Avatar of Asha",
        "{b}Voiceover Production Team{/b}",
        "Lindsay Howard - Voiceover Producer, Casting Director, Voiceover Editor",
        "Alan Moore - Voiceover Director",
        "Jonathan Rhee - Voiceover Production Assistant",
        "Kyle Smith-Laird - Voiceover Production Assistant",
        "Logan Grimes - Casting Assistant, Voiceover Production Assistant",
        "Noah Campodonico - Voiceover Editor, Voiceover Designer",
        "Scott Stinson - Voiceover Editor",
        "Sisi Peng - Voiceover Production Assistant",
        "Stephanie Terrero - Voiceover Production Assistant"
    ], image = "images/fanart_susurha.png"),
    CreditsCategory(category = "{b}{i}MARKETING{/i}{/b}\n", credit_list = [
        "Armoni Boone - Marketing Lead",
        "Alice Cross",
        "Dylan Sands",
        "Kelsey Phelan",
        "Kshitij Khandare",
        "Sisi Peng"
    ], image = "images/fanart_darius.png"),
    CreditsCategory(category = "{b}{i}NARRATIVE{/i}{/b}\n", credit_list = [
        "Tiago Da Cunha - Narrative Lead",
        "Alan Moore - Editor, Voiceover Expert",
        "Cameron Daxon - Writer, Editor, Darius Expert",
        "Carrie Talbot - Writer, Narrative Designer, Vivi/Urshu Expert",
        "Dylan Sands - Avatar of Asha Expert",
        "Salvador Bas Folch - Writer, Editor, Narrative Designer",
        "Kyle Smith-Laird - Writer, Avatar of Asha Expert",
        "Logan Grimes - Writer, Susu’Rha Expert",
        "Sera Milano - Writer, Narrative Designer, Vivi/Urshu Expert",
        "Sisi Peng - Writer, Editor, Darius Expert"
    ], image = None),
    CreditsCategory(category = "{b}{i}PROGRAMMING{/i}{/b}\n", credit_list = [
        "Mica Smith - Programming Lead, Game Designer",
        "Deniz Dilek - Programmer",
        "Special thanks to Daniel Westfall"
    ], image = "images/fanart_ava.png"),
    CreditsCategory(category = "{b}{i}QA{/i}{/b}\n", credit_list = [
        "Rafael Campbell - QA Lead",
        "Carrie Talbot",
        "Damon Day",
        "Jonathan Rhee",
        "Kyle Smith-Laird",
        "Rachel Lee",
        "Salvador Bas Folch"
    ], image = None),
    CreditsCategory(category = "{b}{i}UI/UX{/i}{/b}\n", credit_list = [
        "Stephanie Terrero - UI/UX Lead"
    ], image = None),
    CreditsCategory(category = "{b}{i}PRODUCTION{/i}{/b}\n", credit_list = [
        "Rachel Lee - Lead Producer"
    ], image = None),
    CreditsCategory(category = "{b}{i}DIRECTOR{/i}{/b}\n", credit_list = [
        "Najmah Salam"
    ], image = None),
    CreditsCategory(category = "Use of the terms “mindflayer” and “illithid” in The Ouroboros Express\nis unofficial Fan Content permitted under the Fan Content Policy.\nNot approved/endorsed by Wizards.\nThese portions of the materials used are property of Wizards of the Coast.\n©Wizards of the Coast LLC.", credit_list = [
    ], image = "images/fanart_urshu.png"),
]