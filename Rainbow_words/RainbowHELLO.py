import colorama

colorama.init()


def rainbowHELLO():
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
              colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
    text = '*        *       *********       *          *            *****\n' \
           '*        *       *               *          *          *       *\n' \
           '*        *       *               *          *          *       *\n' \
           '**********       *********       *          *          *       *\n' \
           '*        *       *               *          *          *       *\n' \
           '*        *       *               *          *          *       *\n' \
           '*        *       *********       ******     ******       *****'
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(color + char, end='')
    print()


if __name__ == '__main__':
    rainbowHELLO()
