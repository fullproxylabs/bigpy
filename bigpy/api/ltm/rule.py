from .api import Api, _ApiObject
import json


class _RuleObject(_ApiObject):

    pass


class Rule(Api):

    def __init__(self, bigip):

        super().__init__(bigip)
        self.uri = "/mgmt/tm/ltm/rule/"

    def get_rule(self, fullpath: str) -> _RuleObject:

        uri = self.uri + self._f5_friendly_path(fullpath)
        response = self._api_request(uri=uri, method="get")

        return _RuleObject(response)

    def get_rules(self) -> _RuleObject:

        response = self._api_request(uri=self.uri, method="get")

        for rule in response["items"]:
            yield _RuleObject(rule)
