from colorama import Fore, Style, init

# Инициализируем colorama
init(autoreset=True)

# Определяем цвета
Black = Style.BRIGHT + Fore.BLACK
Red = Style.BRIGHT + Fore.RED
Green = Style.BRIGHT + Fore.GREEN
Yellow = Style.BRIGHT + Fore.YELLOW
Blue = Style.BRIGHT + Fore.BLUE
Purple = Style.BRIGHT + Fore.MAGENTA
Cyan = Style.BRIGHT + Fore.CYAN
White = Style.BRIGHT + Fore.WHITE

# Определяем стиль для сброса (если нужно сбрасывать вручную)
Reset = Style.RESET_ALL
