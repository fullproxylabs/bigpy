from .api import Api, _ApiObject


class _VirtualObject(_ApiObject):

    pass


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
