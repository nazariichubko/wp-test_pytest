from src.generators.player_localizations import PlayerLocalization
from src.Classes.builder import BuilderBaseClass
from src.enums.user_enums import Statuses
from random import randrange
from src.Classes.fake_data import FakeData as fd
id_key = randrange(1, 800, 3)

class Player(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.reset()

    def set_id(self, id=""):
        self.result['id'] = id
        return self

    def set_status(self, status = Statuses.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar = "https://google.com/"):
        self.result['avatar'] = avatar

    def reset(self):
        self.set_id()
        self.set_avatar()
        self.set_status()
        self.set_balance()
        self.result['localize'] = {
                "en": PlayerLocalization('en_US').build(),
                "ua": PlayerLocalization('uk_UA').build()
            }
        return self



y = Player().set_balance(20).set_status('test_atatus').build()
print(y)