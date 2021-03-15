from .device import Device
from .sync_status import Sync_status

class Cm:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/cm"
        self.device = Device(self.bigip)
        self.sync_status = Sync_status(self.bigip)
