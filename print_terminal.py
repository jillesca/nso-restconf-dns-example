import json

PURPLE = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
BOLD = "\033[1m"
ENDC = "\033[0m"


def print_results(data: dict) -> None:
    result = ""
    result += print_header(data.get("header", ""))
    result += f'Path: {data.get("path", "")}\n'
    if "data" in data:
        result += "Data sent:\n"
        result += print_json(data.get("data", ""))
    result += "\nResponse:\n"
    if "body" in data:
        result += print_blue(data.get("body", ""))
    if "json" in data:
        result += print_json(data.get("json", ""))
    result += print_purple(f'HTTP Method: {data.get("method", "").upper()}')
    result += print_purple(f'HTTP Status Code: {data.get("code", "")}')
    print(result)


def print_green(msg: str) -> str:
    return f"{OKGREEN}{msg}{ENDC}\n"


def print_blue(msg: str) -> str:
    return f"{OKBLUE}{msg}{ENDC}\n"


def print_header(msg: str) -> str:
    return f"{BOLD}{'#' * 15} {msg} {'#' * 15}{ENDC}\n"


def print_purple(msg: str) -> str:
    return f"{PURPLE}{msg}{ENDC}\n"


def print_json(msg: str) -> str:
    return print_green(json.dumps(msg, indent=2))
