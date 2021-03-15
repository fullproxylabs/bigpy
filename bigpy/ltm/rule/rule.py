from ...base import _Base


class _Rule(_Base):

    pass


class Rule:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/rule/"

    def __call__(self, **kwargs):

        rule_path = self.bigip.resource_path(kwargs.get("rule", ""))
        response = self.bigip.request(uri=self.uri + rule_path, method="get")
        
        return _Rule(response)
