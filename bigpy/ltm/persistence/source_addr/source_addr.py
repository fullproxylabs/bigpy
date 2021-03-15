from ....base import _Base


class _Source_addr(_Base):

    pass


class Source_addr:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/persistence/source-addr"

    def __call__(self, **kwargs):

        if kwargs.get("source_addr"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("source_addr"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))

        response = self.bigip.request(uri=uri, method="get")
        return _Source_addr(self.bigip, response.json())