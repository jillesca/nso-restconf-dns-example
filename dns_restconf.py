from print_terminal import (
    print_ok_green,
    print_ok_blue,
    print_header,
    print_purple,
    print_json,
)
from http_request import Session_handler


class Dns_handler:
    def __init__(self, username: str, password: str, base_url: str):
        self.http_session = Session_handler(username, password, base_url)

    def list_devices_in_nso(self) -> None:
        path = "/data?fields=tailf-ncs:devices/device(name;address)"
        response = self.http_session.get(path)

        print_header("Devices present in NSO:")
        print(f"{response.text}\nSTATUS_CODE: {response.status_code}")

    def nso_sync_from(self) -> None:
        path = "/operations/tailf-ncs:devices/sync-from"
        response = self.http_session.post(path)

        print_header("Sync-from result:")
        print_ok_green(f"{response.text}\nSTATUS_CODE: {response.status_code}")

    def add_dns_server(self, device: str, dns_server: str) -> None:
        """
        To get the data payload, add first an example manually,
        commit it and then use 'display json' as below

        show running-config dns-config ex1 | display json
        """

        data = {
            "data": {
                "dns-config:dns-config": [
                    {"device": device, "dns-server": [{"address": dns_server}]}
                ]
            }
        }
        path = "/data"
        response = self.http_session.patch(path, data)

        print_header("add_dns_server result:")
        print(f"Added DNS server {dns_server} on {device}")
        print_json(response.json)
        print_ok_green(f"{response.text}\nSTATUS_CODE: {response.status_code}")

    def list_rollback_files(self) -> None:
        path = "/data/tailf-rollback:rollback-files"
        response = self.http_session.get(path)

        print_header("list_rollback_files result:")
        print_json(response.json)
        print_ok_green(f"STATUS_CODE: {response.status_code}")

    def apply_rollback_file(self, rollback_id: int) -> None:
        data = {"input": {"id": rollback_id}}
        path = "/data/tailf-rollback:rollback-files/apply-rollback-file"
        response = self.http_session.post(path, data)

        print_header("apply_rollback_file result:")
        print(f"Rolled back ID: {rollback_id}")
        print_json(response.json)
        print_ok_green(f"STATUS_CODE: {response.status_code}")

    def check_dns_config(self, device: str) -> None:
        """
        To get the restconf path
        show running-config devices device ex1 config ip name-server | display restconf
        """

        path = f"/data/tailf-ncs:devices/device={device}/config/tailf-ned-cisco-ios:ip/name-server/"
        response = self.http_session.get(path)

        print_header("check_dns_config result:")
        print_json(response.json)
        print_ok_green(f"STATUS_CODE: {response.status_code}")

    def dry_run_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        path = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server?dry-run"
        response = self.http_session.patch(path, data)
        print(response)
