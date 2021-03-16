from ....base import _Base


class _Member(_Base):

    def stats(self):

        uri = self.bigip.extract_uri(self.selfLink) + "/stats"
        response = self.bigip.request(uri=uri, method="get")

        return response.json()

    def enable(self):

        uri = self.bigip.extract_uri(self.selfLink)
        data = '{"session": "user-enabled"}'

        response = self.bigip.request(uri=uri, method="put", data=data)

        return response.status_code == 200

    def disable(self):

        uri = self.bigip.extract_uri(self.selfLink)
        data = '{"session": "user-disabled"}'

        response = self.bigip.request(uri=uri, method="put", data=data)

        return response.status_code == 200

    def force(self):

        uri = self.bigip.extract_uri(self.selfLink)
        data = '{"session": "user-disabled", "state": "user-down"}'

        response = self.bigip.request(uri=uri, method="put", data=data)

        return response.status_code == 200




class Member:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/pool/"

    def __call__(self, **kwargs):

        try:
            pool = self.bigip.resource_identifier(kwargs["pool"])
        except KeyError:
            raise NoPoolSpecified

        if kwargs.get("member"):
            uri = self.uri + pool + "/members/" + self.bigip.resource_identifier(kwargs.get("member"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))
        else:
            uri = self.uri + pool + "/members/"

        response = self.bigip.request(uri=uri, method="get")

        if "items" in response.json():
            for member in response.json()["items"]:
                yield _Member(self.bigip, member)
        else:
            yield _Member(self.bigip, response.json())


class NoPoolSpecified(Exception):

    pass