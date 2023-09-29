from print_terminal import print_results
from http_request import SessionHandler


class DnsHandler:
    def __init__(self, username: str, password: str, base_url: str) -> None:
        self._http_session = SessionHandler(username, password, base_url)

    def list_devices_in_nso(self) -> None:
        path = "/data?fields=tailf-ncs:devices/device(name;address)"
        response = self._http_session.get(path)
        print_results(
            {
                "header": "list_devices_in_nso",
                "body": response.text,
                "path": path,
                "method": "GET",
                "code": response.status_code,
            }
        )

    def nso_sync_from(self) -> None:
        path = "/operations/tailf-ncs:devices/sync-from"
        response = self._http_session.post(path)
        print_results(
            {
                "header": "nso_sync_from",
                "body": response.text,
                "path": path,
                "method": "POST",
                "code": response.status_code,
            }
        )

    def dry_run_add_dns_server(self, device: str, dns_server: str) -> None:
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
        path = "/data?dry-run=native"
        response = self._http_session.patch(path, data)
        print_results(
            {
                "header": "DRY-RUN add_dns_server",
                "data": data,
                "body": f"DRY-RUN DNS server {dns_server} on {device}",
                "json": response.json,
                "method": "PATCH",
                "path": path,
                "code": response.status_code,
            }
        )

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
        response = self._http_session.patch(path, data)
        print_results(
            {
                "header": "add_dns_server",
                "data": data,
                "body": f"Added DNS server {dns_server} on {device}",
                "json": response.json,
                "method": "PATCH",
                "path": path,
                "code": response.status_code,
            }
        )

    def list_rollback_files(self) -> None:
        path = "/data/tailf-rollback:rollback-files"
        response = self._http_session.get(path)
        print_results(
            {
                "header": "list_rollback_files",
                "json": response.json,
                "path": path,
                "method": "GET",
                "code": response.status_code,
            }
        )

    def apply_rollback_file(self, rollback_id: int) -> None:
        data = {"input": {"id": rollback_id}}
        path = "/data/tailf-rollback:rollback-files/apply-rollback-file"
        response = self._http_session.post(path, data)
        print_results(
            {
                "header": "apply_rollback_file",
                "data": data,
                "body": f"Rolled back ID: {rollback_id}",
                "json": response.json,
                "path": path,
                "method": "POST",
                "code": response.status_code,
            }
        )

    def check_dns_config(self, device: str) -> None:
        """
        To get the restconf path
        show running-config devices device ex1 config ip name-server | display restconf
        """

        path = f"/data/tailf-ncs:devices/device={device}/config/tailf-ned-cisco-ios:ip/name-server/"
        response = self._http_session.get(path)
        print_results(
            {
                "header": "check_dns_config",
                "json": response.json,
                "path": path,
                "method": "GET",
                "code": response.status_code,
            }
        )
