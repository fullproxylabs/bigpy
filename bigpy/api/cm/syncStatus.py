from .api import Api, _ApiObject
import json

class _SyncStatusObject(_ApiObject):

    pass


class SyncStatus(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/cm/sync-status"

    def __call__(self):

        response = self.bigip.send_request(uri=self.uri,
                                           method="GET")
        data = json.loads(response.text)["entries"]["https://localhost" + self.uri + "/0"]["nestedStats"]["entries"]
        data = {"mode": data["mode"]["description"], "status": data["status"]["description"]}
        return _SyncStatusObject(data)