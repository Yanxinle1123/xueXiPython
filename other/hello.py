from colorama import Fore

from comm.common import slow_print


def hello():
    slow_print(Fore.RED + '*        *       *********       *          *            *****', 0.002)
    slow_print(Fore.RED + Fore.YELLOW + '*        *       *               *          *          *       *', 0.002)
    slow_print(Fore.YELLOW + '*        *       *               *          *          *       *', 0.002)
    slow_print(Fore.GREEN + '**********       *********       *          *          *       *', 0.002)
    slow_print(Fore.GREEN + Fore.BLUE + '*        *       *               *          *          *       *', 0.002)
    slow_print(Fore.BLUE + '*        *       *               *          *          *       *', 0.002)
    slow_print(Fore.MAGENTA + '*        *       *********       ******     ******       *****', 0.002)


if __name__ == '__main__':
    hello()
