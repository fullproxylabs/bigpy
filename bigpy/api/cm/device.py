from .api import Api, _ApiObject
import json

class _DeviceObject(_ApiObject):

    pass


class Device(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/cm/device"

    def __call__(self):

        response = self.bigip.send_request(uri=self.uri,
                                           method="GET")
        return _DeviceObject(json.loads(response.text)["items"][0])