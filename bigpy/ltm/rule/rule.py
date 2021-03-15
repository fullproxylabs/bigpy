from ...base import _Base


class _Rule(_Base):

    pass


class Rule:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/rule/"

    def __call__(self, **kwargs):

        if kwargs.get("rule"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("rule"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))
        else:
            uri = self.uri

        response = self.bigip.request(uri=uri, method="get")

        if "items" in response.json():
            for rule in response.json()["items"]:
                yield _Rule(self.bigip, rule)
        else:
            yield _Rule(self.bigip, response.json())
