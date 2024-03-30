init -5 python:


    class CreditsCategory:
        def __init__(self, category, credit_list):            
            self.category = category
            self.credit_list = credit_list


define credits_list = [
    CreditsCategory(category = "Director", credit_list = [
        "Director name 1",
        "Director name 2",
    ]),
    CreditsCategory(category = "Writing", credit_list = 
    [
        "Writer name 1 (LEAD)",
        "Writer name 2"
    ]),
    CreditsCategory(category = "Art", credit_list = [
        "Artist name 1"
    ]),
    CreditsCategory(category = "Audio", credit_list = [
        "Audio name 1"
    ]),
    CreditsCategory(category = "Programming", credit_list = [
        "Programming name 1"
    ]),
]
