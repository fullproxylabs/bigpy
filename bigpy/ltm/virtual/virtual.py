from ...base import _Base

class _Virtual(_Base):

    pass


class Virtual:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/virtual/"

    def __call__(self, **kwargs):

        if kwargs.get("virtual"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("virtual"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))

        response = self.bigip.request(uri=uri, method="get")
        return _Virtual(response.json())