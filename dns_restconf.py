#!/usr/bin/env python3

# import ncs
# import json
import requests
from http_request import session_handler


class dns_handler:
    def __init__(self, http_session: requests.session) -> None:
        self.http_session = http_session

    def list_devices_in_nso(self) -> None:
        endpoint = "/data?fields=tailf-ncs:devices/device(name;address)"
        response = self.http_session.get(endpoint)
        print(response)

    def nso_sync_from(self) -> None:
        endpoint = "/operations/tailf-ncs:devices/sync-from"
        response = self.http_session.post(endpoint)
        print(response)

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
        response = self.http_session.patch(endpoint, data)
        print(response)

    def list_rollback_files(self) -> None:
        endpoint = "/data/tailf-rollback:rollback-files"
        response = self.http_session.get(endpoint)
        print(response)

    def apply_rollback_file(self) -> None:
        data = {"input": {"id": "0"}}
        endpoint = "/data/tailf-rollback:rollback-files/apply-rollback-file"
        response = self.http_session.post(endpoint, data)
        print(response)

    # with open("packages/router/src/yang/router-dns.yang", "r", encoding="utf-8") as f:
    #     for line in f:
    #         if "list server" in line:
    #             sys.stdout.write(line)
    #             sys.stdout.writelines(itertools.islice(f, 7))
    #             break

    # with ncs.maapi.single_write_trans("admin", "python") as t:
    #     root = ncs.maagic.get_root(t)
    #     dns_server_list = root.devices.device["ex1"].config.sys.dns.server
    #     dns_server_list.create("192.0.2.1")
    #     params = t.get_params()
    #     params.dry_run_native()
    #     result = t.apply_params(True, params)
    #     print(result["device"]["ex1"])
    #     t.apply_params(True, t.get_params())
    #     print("Done!")

    def check_dns_config(self) -> None:
        endpoint = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response = self.http_session.get(endpoint)
        print(response)

    def dry_run_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        endpoint = (
            "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server?dry-run"
        )
        response = self.http_session.patch(endpoint, data)
        print(response)

    def commit_dns_config(self) -> None:
        data = {"router:server": [{"address": "192.0.2.2"}]}
        endpoint = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
        response = self.http_session.patch(endpoint, data)
        print(response)


def main() -> None:
    USERNAME = "admin"
    PASSWORD = "admin"
    BASE_URL = "http://localhost:8080/restconf"

    http_session = session_handler(
        username=USERNAME, password=PASSWORD, base_url=BASE_URL
    )
    restconf = dns_handler(http_session)
    restconf.list_devices_in_nso()
    restconf.nso_sync_from()
    restconf.update_dns_server()
    restconf.list_rollback_files()
    restconf.apply_rollback_file()
    restconf.check_dns_config()
    restconf.dry_run_dns_config()
    restconf.commit_dns_config()
    restconf.check_dns_config()


if __name__ == "__main__":
    main()
