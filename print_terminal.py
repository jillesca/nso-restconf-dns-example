import json

PURPLE = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
BOLD = "\033[1m"
ENDC = "\033[0m"


def print_results(data: dict) -> None:
    print_header(data.get("header", ""))
    print(f'Path: {data.get("path", "")}')
    if "data" in data:
        print("Data sent:")
        print_json(data.get("data", ""))
    print("\nResponse:")
    if "body" in data:
        print_blue(data.get("body", ""))
    if "json" in data:
        print_json(data.get("json", ""))
    print_purple(f'HTTP Method: {data.get("method", "").upper()}')
    print_purple(f'HTTP Status Code: {data.get("code", "")}')


def print_green(msg: str) -> None:
    print(f"{OKGREEN}{msg}{ENDC}")


def print_blue(msg: str) -> None:
    print(f"{OKBLUE}{msg}{ENDC}")


def print_header(msg: str) -> None:
    print_bold(f"{'#' * 15} {msg} {'#' * 15}")


def print_bold(msg: str) -> None:
    print(f"{BOLD}{msg}{ENDC}")


def print_purple(msg: str) -> None:
    print(f"{PURPLE}{msg}{ENDC}")


def print_json(msg: str) -> None:
    print_green(json.dumps(msg, indent=2))
