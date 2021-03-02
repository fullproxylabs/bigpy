import json
import requests


class _VirtualObject:

    def __init__(self, response: dict):

        for key in response:
            setattr(self, key, response[key])

    def __str__(self):

        return str(self.__dict__)


class Virtual:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/virtual/"

    def get_virtual_server(self, fullpath: str):

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _VirtualObject(response)

    def get_virtual_servers(self):

        response = self._api_request(uri=self.uri, method="get")

        for virtual in response["items"]:
            yield _VirtualObject(virtual)

    def _f5_friendly_path(self, fullpath: str) -> str:

        return fullpath.replace("/", "~")

    def _api_request(self, uri: str, method: str) -> dict:

        response = self.bigip.send_request(uri=uri,
                                           method=method)

        response = json.loads(response.text)
        return response
