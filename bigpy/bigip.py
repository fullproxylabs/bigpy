import requests
import urllib3
from .ltm import Ltm
from .sys import Sys
from .cm import Cm

urllib3.disable_warnings()


class Bigip:

    def __init__(self, address, **kwargs):

        self.address = address
        self.username = kwargs.get("username", "admin")
        self.password = kwargs.get("password", "admin")
        self.token = kwargs.get("token")
        self.verify = kwargs.get("verify", True)
        self.ltm = Ltm(self)
        self.sys = Sys(self)
        self.cm = Cm(self)

        if not self.token:
            self.request_token()
        else:
            self.verify_token()

    def __str__(self) -> str:

        return f"Bigip: {self.address}\nUsername: {self.username}\nPassword: {'*' * len(self.password)}"

    def __repr__(self) -> str:

        return f"Bigip('{self.username}', '{self.password}', '{self.address}', {self.verify}, '{self.token}')"

    def verify_token(self):

        uri = self.__dict__.get(
            "__token_self_link",
            f"/mgmt/shared/authz/tokens/{self.token}")
        response = self.request(uri=uri,
                                method="get")

        if response.status_code == 401:
            self.request_token

    def request_token(self) -> None:

        def _increase_timeout(selfLink: str):

            request_body = str({"timeout": "36000"})
            self.request(uri=selfLink,
                         method="patch",
                         data=request_body)

        request_body = str({"username": self.username,
                            "password": self.password,
                            "loginProviderName": "tmos"})

        response = self.request(uri="/mgmt/shared/authn/login",
                                method="post",
                                data=request_body)

        response_json = response.json()

        self.token = (response_json)["token"]["token"]
        self.__token_self_link = self.extract_uri(
            response_json["token"]["selfLink"])
        _increase_timeout(self.__token_self_link)

    def request(self, uri:str, method:str, data=None, **kwargs) -> requests.Response:

        request_methods = {"get": requests.get,
                           "post": requests.post,
                           "delete": requests.delete,
                           "patch": requests.patch,
                           "put": requests.put}

        if kwargs.get("headers"):
            kwargs["headers"] = {**kwargs["headers"],
                                 **{"X-F5-Auth-Token": self.token}}
        else:
            kwargs["headers"] = {"X-F5-Auth-Token": self.token}

        response = request_methods[method.lower()](
            url=self.address + uri, verify=self.verify, data=data, **kwargs)

        return response

    @staticmethod
    def resource_identifier(path: str) -> str:

        return path.replace("/", "~")

    @staticmethod
    def extract_uri(selfLink: str) -> str:

        return selfLink.split("https://localhost")[1].split("?")[0]
