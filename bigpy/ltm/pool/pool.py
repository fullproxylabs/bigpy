from ...base import _Base


class _Pool(_Base):

    pass


class Pool:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/pool/"
    
    def __call__(self, **kwargs):

        if kwargs.get("pool"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("pool"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))

        response = self.bigip.request(uri=uri, method="get")
        return _Pool(response.json())