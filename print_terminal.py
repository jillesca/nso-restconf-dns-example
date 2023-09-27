HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
ENDC = "\033[0m"
BOLD = "\033[1m"


def print_ok_green(msg: str) -> None:
    print(f"\n{OKGREEN}{msg}\n{ENDC}")


def print_ok_blue(msg: str) -> None:
    print(f"{OKBLUE}{msg}{ENDC}")


def print_bold(msg: str) -> None:
    print(f"{BOLD}{msg}{ENDC}")


def print_header(msg: str) -> None:
    print(f"{HEADER}{msg}{ENDC}")
