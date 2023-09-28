#!/usr/bin/env python3

# import ncs
# import json
import requests
from print_terminal import print_ok_green, print_ok_blue, print_bold, print_purple


class dns_handler:
    def __init__(self, http_session: requests.session):
        self.http_session = http_session

    def list_devices_in_nso(self) -> None:
        endpoint = "/data?fields=tailf-ncs:devices/device(name;address)"
        response, status_code = self.http_session.get(endpoint)
        print_purple(f"{'#'*10} Devices present in NSO: {'#'*10}")
        print(f"{response}\nSTATUS_CODE: {status_code}")

    def nso_sync_from(self) -> None:
        endpoint = "/operations/tailf-ncs:devices/sync-from"
        response, status_code = self.http_session.post(endpoint)
        print_bold(f"{'#'*10} Sync-from result: {'#'*10}")
        print_ok_green(f"{response}\nSTATUS_CODE: {status_code}")

    def update_dns_server(self) -> None:
        data = {
            "data": {
                "tailf-ncs:devices": {
                    "device": [
                        {
                            "name": "ex1",
                            "config": {
                                "router:sys": {
                                    "dns": {"server": [{"address": "198.51.100.1"}]}
                                }
                            },
                        }
                    ]
                }
            }
        }
        endpoint = "/data"
        response, status_code = self.http_session.patch(endpoint, data)
        print(response)

    def list_rollback_files(self) -> None:
        endpoint = "/data/tailf-rollback:rollback-files"
        response, status_code = self.http_session.get(endpoint)
        print(response)

    def apply_rollback_file(self) -> None:
        data = {"input": {"id": "0"}}
        endpoint = "/data/tailf-rollback:rollback-files/apply-rollback-file"
        response, status_code = self.http_session.post(endpoint, data)
        print(response)

    def check_dns_config(self) -> None:
        endpoint = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response, status_code = self.http_session.get(endpoint)
        print(response)

    def dry_run_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        endpoint = (
            "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server?dry-run"
        )
        response, status_code = self.http_session.patch(endpoint, data)
        print(response)

    def commit_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        endpoint = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response, status_code = self.http_session.patch(endpoint, data)
        print(response)
