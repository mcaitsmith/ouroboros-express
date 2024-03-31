init -5 python:


    class CreditsCategory:
        def __init__(self, category, credit_list, image):            
            self.category = category
            self.credit_list = credit_list
            self.image = image


define credits_list = [
    CreditsCategory(category = "Writing", credit_list = 
    [
        "Writer name 1",
        "Writer name 2"
    ], image = "images/vivi in the train being all mysterious and such.png"),
    CreditsCategory(category = "Art", credit_list = [
        "Artist name 1"
    ], image = "images/vivi and urshu.png"),
    CreditsCategory(category = "Sound", credit_list = [
        "Audio name 1"
    ], image = "images/vivi expressions.png"),
    CreditsCategory(category = "Programming", credit_list = [
        "Programming name 1"
    ], image = "images/vivi and ava.png"),
    CreditsCategory(category = "LEADS", credit_list = [
        "Lead name 1"
    ], image = "images/vivi bruh.png"),
    CreditsCategory(category = "DIRECTOR", credit_list = [
        "Director name"
    ], image = "images/thumbnail concept.png"),
]
