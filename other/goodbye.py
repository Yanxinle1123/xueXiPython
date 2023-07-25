from colorama import Fore

from comm.common import slow_print


def goodbye():
    slow_print(
        Fore.RED + '  *******        ****         ****       ******             *****       *       *     *********',
        0.001)
    slow_print(
        Fore.GREEN + Fore.YELLOW + '*              *      *     *      *     *      *           *    *        *   *       *',
        0.001)
    slow_print(
        Fore.YELLOW + '*              *      *     *      *     *       *          *    *          *         *',
        0.001)
    slow_print(
        Fore.GREEN + '*   *******    *      *     *      *     *       *          *****           *         *********',
        0.001)
    slow_print(
        Fore.CYAN + '*       *      *      *     *      *     *       *          *    *          *         *',
        0.001)
    slow_print(
        Fore.BLUE + '*       *      *      *     *      *     *      *           *    *          *         *',
        0.001)
    slow_print(
        Fore.MAGENTA + '  *******        ****         ****       ******             *****           *         *********',
        0.001)


if __name__ == '__main__':
    goodbye()
