from .api import Api, _ApiObject

class _PoolObject(_ApiObject):

    pass

class Pool(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/ltm/pool/"

    def get_pool(self, fullpath: str):

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _PoolObject(response)

    def get_pools(self):

        response = self._api_request(uri=self.uri, method="get")

        for pool in response["items"]:
            yield _PoolObject(pool)