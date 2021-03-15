from .source_addr import Source_addr

class Persistence:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/persistence"
        self.source_addr = Source_addr(self.bigip)