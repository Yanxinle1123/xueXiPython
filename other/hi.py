from colored import Fore

from comm.common import slow_print


def hi():
    slow_print(Fore.RED + '*        *       *****', 0.01)
    slow_print(Fore.RED + Fore.YELLOW + '*        *         *', 0.01)
    slow_print(Fore.YELLOW + '*        *         *', 0.01)
    slow_print(Fore.GREEN + '**********         *', 0.01)
    slow_print(Fore.BLUE + '*        *         *', 0.01)
    slow_print(Fore.CYAN + '*        *         *', 0.01)
    slow_print(Fore.MAGENTA + '*        *       *****', 0.01)


if __name__ == '__main__':
    hi()
