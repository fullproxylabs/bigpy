from ...base import _Base


class _Device(_Base):

    pass


class Device:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/cm/device"

    def __call__(self):

        response = self.bigip.request(uri=self.uri, method="get")
        return _Device(response.json())