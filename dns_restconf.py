#!/usr/bin/env python3

# import ncs
# import json
import requests
from print_terminal import (
    print_ok_green,
    print_ok_blue,
    print_bold,
    print_purple,
    print_json,
)


class dns_handler:
    def __init__(self, http_session: requests.session):
        self.http_session = http_session

    def list_devices_in_nso(self) -> None:
        path = "/data?fields=tailf-ncs:devices/device(name;address)"
        response = self.http_session.get(path)
        print_purple(f"{'#'*10} Devices present in NSO: {'#'*10}")
        print(f"{response.text}\nSTATUS_CODE: {response.status_code}")

    def nso_sync_from(self) -> None:
        path = "/operations/tailf-ncs:devices/sync-from"
        response = self.http_session.post(path)
        print_bold(f"{'#'*10} Sync-from result: {'#'*10}")
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
        print_bold(f"{'#'*10} add_dns_server result: {'#'*10}")
        print_json(response.json)
        print_ok_green(f"{response.text}\nSTATUS_CODE: {response.status_code}")

    def list_rollback_files(self) -> None:
        path = "/data/tailf-rollback:rollback-files"
        response, status_code = self.http_session.get(path)
        print(response)

    def apply_rollback_file(self) -> None:
        data = {"input": {"id": "0"}}
        path = "/data/tailf-rollback:rollback-files/apply-rollback-file"
        response, status_code = self.http_session.post(path, data)
        print(response)

    def check_dns_config(self) -> None:
        path = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response, status_code = self.http_session.get(path)
        print(response)

    def dry_run_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        path = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server?dry-run"
        response, status_code = self.http_session.patch(path, data)
        print(response)

    def commit_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        path = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response, status_code = self.http_session.patch(path, data)
        print(response)
