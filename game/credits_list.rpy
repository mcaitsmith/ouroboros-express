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
    CreditsCategory(category = "{b}{i}DIRECTOR{/i}{/b}\n", credit_list = [
        "Najmah Salam"
    ], image = "images/thumbnail concept.png"),
    CreditsCategory(category = "{b}{i}Special Thanks{/i}{/b}\n", credit_list = [
        "Daniel Westfall"
    ], image = None),
]
