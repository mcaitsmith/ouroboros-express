init -5 python:


    class CreditsCategory:
        def __init__(self, category, credit_list):            
            self.category = category
            self.credit_list = credit_list


define credits_list = [
    CreditsCategory(category = "Writing", credit_list = 
    [
        "Writer name 1",
        "Writer name 2"
    ]),
    CreditsCategory(category = "Art", credit_list = [
        "Artist name 1"
    ]),
    CreditsCategory(category = "Sound", credit_list = [
        "Audio name 1"
    ]),
    CreditsCategory(category = "Programming", credit_list = [
        "Programming name 1"
    ]),
    CreditsCategory(category = "LEADS", credit_list = [
        "Lead name 1"
    ]),
    CreditsCategory(category = "DIRECTOR", credit_list = [
        "Director name"
    ]),
]
