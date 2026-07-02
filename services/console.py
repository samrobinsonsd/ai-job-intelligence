from colorama import Fore, Style, init

init(autoreset=True)


def success(message):
    print(f"{Fore.GREEN}[✓] {message}{Style.RESET_ALL}")


def step(message):
    print(f"{Fore.CYAN}[ ] {message}{Style.RESET_ALL}")


def warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")


def error(message):
    print(f"{Fore.RED}[x] {message}{Style.RESET_ALL}")


def decision_color(decision):
    if decision == "Jobs High-Value":
        return Fore.GREEN
    if decision == "Jobs Review":
        return Fore.YELLOW
    if decision == "Jobs Reject":
        return Fore.RED
    return Fore.WHITE