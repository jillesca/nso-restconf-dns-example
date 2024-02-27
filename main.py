from dns_restconf import DnsHandler

USERNAME = "admin"
PASSWORD = "admin"
BASE_URL = "http://localhost:8080/restconf"


def main() -> None:
    restconf = DnsHandler(USERNAME, PASSWORD, BASE_URL)
    restconf.list_devices_in_nso()
    restconf.nso_sync_from_single_device(device="ex1")
    restconf.nso_sync_from()
    restconf.add_dns_server(device="ex1", dns_server="1.1.1.1")
    restconf.check_dns_config(device="ex1")
    restconf.dry_run_add_dns_server(device="ex1", dns_server="2.2.2.2")
    restconf.check_dns_config(device="ex1")
    restconf.add_dns_server(device="ex1", dns_server="2.2.2.2")
    restconf.check_dns_config(device="ex1")
    restconf.list_rollback_files()
    restconf.apply_rollback_file(rollback_id=0)
    restconf.check_dns_config(device="ex1")
    restconf.dry_run_add_dns_server(device="ex1", dns_server="3.3.3.3")
    restconf.check_dns_config(device="ex1")
    restconf.add_dns_server(device="ex1", dns_server="3.3.3.3")
    restconf.check_dns_config(device="ex1")


if __name__ == "__main__":
    main()
