from http_request import session_handler
from dns_restconf import dns_handler

USERNAME = "admin"
PASSWORD = "admin"
BASE_URL = "http://localhost:8080/restconf"


def main() -> None:
    http_session = session_handler(
        username=USERNAME, password=PASSWORD, base_url=BASE_URL
    )
    restconf = dns_handler(http_session)
    restconf.list_devices_in_nso()
    restconf.nso_sync_from()
    # restconf.update_dns_server()
    # restconf.list_rollback_files()
    # restconf.apply_rollback_file()
    # restconf.check_dns_config()
    # restconf.dry_run_dns_config()
    # restconf.commit_dns_config()
    # restconf.check_dns_config()


if __name__ == "__main__":
    main()