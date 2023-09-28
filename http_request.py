import requests
from requests.auth import HTTPBasicAuth


class Response:
    def __init__(self, text: str, status_code: int, json: dict):
        self.text = text
        self.status_code = status_code
        self.json = json


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

    def _handle_204(self, response: requests.Response) -> tuple[str, str]:
        if response.status_code == 204:
            return ("Empty body, good for '204 No Content'", "No Content Response")
        return (response.text, response.json())

    def _send_request(self, method: str, path: str, data: dict = None) -> Response:
        try:
            url = self._base_url + path
            response = getattr(self.session, method)(url, json=data)
            response.raise_for_status()
            text, json = self._handle_204(response)
            return Response(text, response.status_code, json)
        except Exception as err:
            print(f"{err=}")

    def get(self, path: str) -> Response:
        return self._send_request("get", path)

    def post(self, path: str, data: dict = None) -> Response:
        return self._send_request("post", path, data)

    def patch(self, path: str, data: dict = None) -> Response:
        return self._send_request("patch", path, data)
