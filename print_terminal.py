import json

PURPLE = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
BOLD = "\033[1m"
ENDC = "\033[0m"


def print_results(data: dict) -> None:
    print(format_data(data))


def format_data(data: dict) -> str:
    result = ""
    result += add_header(data.get("header", ""))
    result += f'Path: {data.get("path", "")}\n'
    if "data" in data:
        result += "Data sent:\n"
        result += format_json(data.get("data", ""))
    result += "\nResponse:\n"
    if "body" in data:
        result += colour_blue(data.get("body", ""))
    if "json" in data:
        result += format_json(data.get("json", ""))
    result += colour_purple(f'HTTP Method: {data.get("method", "").upper()}')
    result += colour_purple(f'HTTP Status Code: {data.get("code", "")}')
    return result


def colour_green(msg: str) -> str:
    return f"{OKGREEN}{msg}{ENDC}\n"


def colour_blue(msg: str) -> str:
    return f"{OKBLUE}{msg}{ENDC}\n"


def add_header(msg: str) -> str:
    return f"{BOLD}{'#' * 15} {msg} {'#' * 15}{ENDC}\n"


def colour_purple(msg: str) -> str:
    return f"{PURPLE}{msg}{ENDC}\n"


def format_json(msg: str) -> str:
    return colour_green(json.dumps(msg, indent=2))
