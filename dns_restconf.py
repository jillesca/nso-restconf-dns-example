#!/usr/bin/env python3

import sys
import itertools
import json
import requests

# import ncs

AUTH = ("admin", "admin")
BASE_URL = "http://localhost:8080/restconf"

session = requests.Session()
session.auth = AUTH
headers = {"Content-Type": "application/yang-data+json"}


PATH = "/data?fields=tailf-ncs:devices/device(name;address)"
r = session.get(BASE_URL + PATH, headers=headers)
print(r.text)

PATH = "/operations/tailf-ncs:devices/sync-from"
r = session.post(BASE_URL + PATH, headers=headers)
print(r.text)

SERVER_DATA = {"server": [{"address": "198.51.100.1"}]}
SYS_DATA = {"router:sys": {"dns": SERVER_DATA}}
DEV_DATA = {"device": [{"name": "ex1", "config": SYS_DATA}]}
INPUT_DATA = {"data": {"tailf-ncs:devices": DEV_DATA}}
PATH = "/data"
r = session.patch(BASE_URL + PATH, json=INPUT_DATA, headers=headers)
print("Status code: {}\n".format(r.status_code))

PATH = "/data/tailf-rollback:rollback-files"
r = session.get(BASE_URL + PATH, headers=headers)
print(r.text)

INPUT_DATA = {"input": {"id": "0"}}
PATH = "/data/tailf-rollback:rollback-files/apply-rollback-file"
r = session.post(BASE_URL + PATH, json=INPUT_DATA, headers=headers)
print("Status code: {}\n".format(r.status_code))

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

PATH = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
r = session.get(BASE_URL + PATH, headers=headers)
print(r.text)

INPUT_DATA = {"router:server": [{"address": "192.0.2.2"}]}
PATH = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server?dry-run"
r = session.patch(BASE_URL + PATH, json=INPUT_DATA, headers=headers)
print(json.dumps(r.json(), indent=2))

PATH = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
r = session.patch(BASE_URL + PATH, json=INPUT_DATA, headers=headers)
print("Status code: {}\n".format(r.status_code))

PATH = "/data/tailf-ncs:devices/device=ex1/config/router:sys/dns/server"
r = session.get(BASE_URL + PATH, headers=headers)
print(r.text)
