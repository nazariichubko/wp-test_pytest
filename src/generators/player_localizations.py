from faker import Faker

fake = Faker()

class PlayerLocalization:
    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        self.result['number'] = number
        return self



    def build(self):
        return self.result
