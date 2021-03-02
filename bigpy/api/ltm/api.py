import json


class _ApiObject:

    def __init__(self, response: dict):

        for key in response:
            setattr(self, key, response[key])

    def __str__(self):

        return str(self.__dict__)

    def __repr__(self):

        return repr(self.__dict__)


class Api:

    def __init__(self, bigip):

        self.bigip = bigip

    def _f5_friendly_path(self, fullpath: str) -> str:
        return fullpath.replace("/", "~")

    def _api_request(self, uri: str, method: str) -> dict:
        response = self.bigip.send_request(uri=uri,
                                           method=method)

        response = json.loads(response.text)
        return response