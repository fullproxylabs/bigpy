from .api import Api, _ApiObject


class _UcsObject(_ApiObject):

    pass


class Ucs(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/sys/ucs/"

    def get_ucs(self, fullpath: str) -> _UcsObject:

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _UcsObject(response)

    def get_all_ucs(self) -> _UcsObject:

        response = self._api_request(uri=self.uri, method="get")

        for rule in response["items"]:
            yield _UcsObject(rule)
