from ...base import _Base


class _Sync_status(_Base):

    pass


class Sync_status:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/cm/sync-status"

    def __call__(self):

        response = self.bigip.request(uri=self.uri, method="get")
        data = response.json()["entries"]["https://localhost" + self.uri + "/0"]["nestedStats"]["entries"]
        data = {"mode": data["mode"]["description"], "status": data["status"]["description"]}
        return _Sync_status(self.bigip, data)