from .api import Api, _ApiObject


class _PoolObject(_ApiObject):

    pass


class _PoolMemberObject(_ApiObject):

    pass


class PoolMembers(Api):

    def __init__(self, bigip, pool):

        super().__init__(bigip)
        self.pool = pool
        self.uri = "/mgmt/tm/ltm/pool" + self._f5_friendly_path(pool.fullPath) + "/members/"

    def get_pool_members(self):

        response = self._api_request(uri=self.uri, method="get")

        for pool_member in response["items"]:
            yield _PoolMemberObject(pool_member)

    def get_pool_member(self, fullpath: str):

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _PoolMemberObject(response)


class Pool(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/ltm/pool/"

    def get_pool(self, fullpath: str) -> _PoolObject:

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        pool_object = _PoolObject(response)
        pool_object.members = self._get_pool_members(pool_object.fullPath)
        return pool_object

    def get_pools(self) -> _PoolObject:

        response = self._api_request(uri=self.uri, method="get")

        for pool in response["items"]:
            pool_object = _PoolObject(pool)
            pool_object.members = self._get_pool_members(pool_object.fullPath)
            yield pool_object

    def _get_pool_members(self, fullpath: str) -> list:

        members = list()
        uri = self.uri + self._f5_friendly_path(fullpath) + "/members"
        response = self._api_request(uri=uri, method="get")

        for pool_member in response["items"]:
            members.append(_PoolMemberObject(pool_member))

        return members
