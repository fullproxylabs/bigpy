from ...base import _Base
from .members import Member

class _Pool(_Base):

    def stats(self):

        uri = self.bigip.extract_uri(self.selfLink) + "/members/stats"
        response = self.bigip.request(uri=uri, method="get")

        data = response.json()["entries"]
        return data


class Pool:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/pool/"
        self.members = Member(bigip)
    
    def __call__(self, **kwargs):

        if kwargs.get("pool"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("pool"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))
        else:
            uri = self.uri

        response = self.bigip.request(uri=uri, method="get")

        if "items" in response.json():
            for pool in response.json()["items"]:
                yield _Pool(self.bigip, pool)
        else:
            yield _Pool(self.bigip, response.json())