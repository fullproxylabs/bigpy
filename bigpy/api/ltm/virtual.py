from .api import Api, _ApiObject
import json


class _VirtualObject(_ApiObject):

    def disable(self, bigip) -> bool:

        uri = f"/mgmt/tm/ltm/virtual/{self._f5_friendly_path(self.fullPath)}"
        data = '{"disabled": true}'

        response = bigip.send_request(uri=uri,
                           method="PATCH",
                           data=data)

        return response.status_code == 200

    def enable(self, bigip) -> bool:

        uri = f"/mgmt/tm/ltm/virtual/{self._f5_friendly_path(self.fullPath)}"
        data = '{"enabled": true}'

        response = bigip.send_request(uri=uri,
                                      method="PATCH",
                                      data=data)

        return response.status_code == 200

    def stats(self, bigip) -> dict:

        uri = f"/mgmt/tm/ltm/virtual/{self._f5_friendly_path(self.fullPath)}/stats"

        response = bigip.send_request(uri=uri,
                                      method="GET")

        response = json.loads(response.text);

        data = response["entries"]["https://localhost"+uri]["nestedStats"]["entries"]

        return data


class Virtual(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/ltm/virtual/"

    def get_virtual_server(self, fullpath: str) -> _VirtualObject:

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _VirtualObject(response)

    def get_virtual_servers(self) -> _VirtualObject:

        response = self._api_request(uri=self.uri, method="get")

        for virtual in response["items"]:
            yield _VirtualObject(virtual)
