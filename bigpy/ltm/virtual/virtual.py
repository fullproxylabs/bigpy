from ...base import _Base

class _Virtual(_Base):

    pass

    def enable(self):

        uri = self.bigip.extract_uri(self.selfLink)
        data = '{"enabled": true}'

        response = self.bigip.request(uri=uri, method="patch", data=data)
        return response.status_code == 200

    def disable(self):

        uri = self.bigip.extract_uri(self.selfLink)
        data = '{"disabled": true}'

        response = self.bigip.request(uri=uri, method="patch", data=data)
        return response.status_code == 200

    def stats(self):

        uri = self.bigip.extract_uri(self.selfLink) + "/stats"
        response = self.bigip.request(uri=uri, method="get")

        data = response.json()["entries"]["https://localhost" + uri]["nestedStats"]["entries"]
        return data


class Virtual:

    def __init__(self, bigip):

        self.bigip = bigip
        self.uri = "/mgmt/tm/ltm/virtual/"

    def __call__(self, **kwargs):

        if kwargs.get("virtual"):
            uri = self.uri + self.bigip.resource_identifier(kwargs.get("virtual"))
        elif kwargs.get("selfLink"):
            uri = self.bigip.extract_uri(kwargs.get("selfLink"))
        else:
            uri = self.uri

        response = self.bigip.request(uri=uri, method="get")

        if "items" in response.json():
            for virtual in response.json()["items"]:
                yield _Virtual(self.bigip, virtual)
        else:
            yield _Virtual(self.bigip, response.json())