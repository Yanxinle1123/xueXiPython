import colorama

colorama.init()

colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
          colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
text = 'Rainbow Text!'
for i, char in enumerate(text):
    color = colors[i % len(colors)]
    print(color + char, end='')
print()
