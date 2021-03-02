import requests
import urllib3
import json
from .api import ltm

urllib3.disable_warnings()

class Bigip:

    def __init__(self, address: str, username="admin", password="admin", key=None):

        self.address = self._parse_address(address)
        self.username = username
        self.password = password
        self.key = key
        self.status = 0
        self.ltm = ltm

        if not self.key:
            self.get_auth_key()
        else:
            self.verify_key()

    def _parse_address(self, address: str) -> str:

        if "https://" in address:
            return address
        else:
            return "https://" + address

    def verify_key(self):

        response = self.send_request(method="GET",
                                     uri=f"/mgmt/shared/authz/tokens/{self.key}",
                                     status=[200, 401])

        if response.status_code == 401:
            self.key = None
            self.get_auth_key()

    def get_auth_key(self):

        def generate_key():

            data = str({"username": self.username, "password": self.password, "loginProviderName": "tmos"})

            response = self.send_request(method="POST",
                                         uri="/mgmt/shared/authn/login",
                                         data=data,
                                         status=[200, 401, 444])


            if self.status == 200:
                self.key = json.loads(response.text)["token"]["token"]

        def increase_timeout():

            data = str({"timeout": "36000"})

            self.send_request(method="PATCH",
                              uri=f"/mgmt/shared/authz/tokens/{self.key}",
                              data=data,
                              status=[200, 401])

        generate_key()
        if self.key:
            increase_timeout()

    def send_request(self, uri: str, method: str, data=None, status=[200]) -> requests.Response:

        headers = {"Content-Type": "application/json"}
        url = self.address + uri

        if data:
            data = str(data)

        if self.key:
            headers["X-F5-Auth-Token"] = self.key

        request_dict = {"GET": requests.get,
                        "POST": requests.post,
                        "DELETE": requests.delete,
                        "PATCH": requests.patch,
                        "PUT": requests.put}

        request_object = request_dict[method.upper()]

        try:
            response = request_object(url=url,
                                      headers=headers,
                                      data=data,
                                      verify=False)
        except requests.exceptions.ConnectionError:
            self.status = 522

        if response.status_code not in status:
            self.error_handler(response)
        else:
            self.status = response.status_code

        return response

    def error_handler(self, response):

        raise Exception(response.text)
