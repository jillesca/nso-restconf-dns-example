import json

PURPLE = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
BOLD = "\033[1m"
ENDC = "\033[0m"


def print_ok_green(msg: str) -> None:
    print(f"\n{OKGREEN}{msg}{ENDC}")


def print_ok_blue(msg: str) -> None:
    print(f"\n{OKBLUE}{msg}{ENDC}")


def print_header(msg: str) -> None:
    print(f"\n{'#'*10} {BOLD}{msg}{ENDC} {'#'*10}")


def print_purple(msg: str) -> None:
    print(f"\n{PURPLE}{msg}{ENDC}")


def print_json(msg: str) -> None:
    if msg:
        print(json.dumps(msg, indent=2))
