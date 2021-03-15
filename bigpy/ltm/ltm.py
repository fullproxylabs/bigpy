from .virtual import Virtual
from .pool import Pool
from .rule import Rule
from .persistence import Persistence

class Ltm:

    def __init__(self, bigip):

        self.bigip = bigip
        self.virtual = Virtual(self.bigip)
        self.pool = Pool(self.bigip)
        self.rule = Rule(self.bigip)
        self.persistence = Persistence(self.bigip)
        self.uri = "/mgmt/tm/ltm"
