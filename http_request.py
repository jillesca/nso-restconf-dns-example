import requests
from requests.auth import HTTPBasicAuth


class session_handler:
    def __init__(self, username: str, password: str, base_url: str):
        self._username = username
        self._password = password
        self._base_url = base_url
        self._create_restconf_session()

    def _create_restconf_session(self):
        session = requests.session()
        session.auth = HTTPBasicAuth(self._username, self._password)
        session.headers.update({"Content-Type": "application/yang-data+json"})
        session.verify = False
        self.session = session

    def get(self, endpoint: str) -> str:
        try:
            response = self.session.get(self._base_url + endpoint)
            response.raise_for_status()
            return response.text
        except Exception as err:
            print(f"An unexpected error happened: {err=}")

    def post(self, endpoint: str, data: dict = None) -> str:
        try:
            response = self.session.post(self._base_url + endpoint, json=data)
            response.raise_for_status()
            return response.status_code
        except Exception as err:
            print(f"An unexpected error happened: {err=}")

    def patch(self, endpoint: str, data: dict = None) -> str:
        try:
            response = self.session.patch(self._base_url + endpoint, json=data)
            response.raise_for_status()
            return response.status_code
        except Exception as err:
            print(f"An unexpected error happened: {err=}")
