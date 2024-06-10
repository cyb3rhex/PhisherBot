import subprocess
from sys import exit
import os

def StartBot(Name):
    Script_Locations = {
        "Знакомства": "Modules\\Bots\\Acquaintance.py",
        "ГлазБога": "Modules\\Bots\\EyeGod.py",
        "Хамстер": "Modules\\Bots\\Hamster.py"
    }
    result = ""

    if Name == "ГлазБога":
        result = Script_Locations["ГлазБога"]

    elif Name == "Хамстер":
        result = Script_Locations["Хамстер"]

    elif Name == "Знакомства":
        result = Script_Locations["Знакомства"]

    else:
        print("[!] An error occurred!")
        exit(0)

    Starter(result)

def Starter(Path):
    process = subprocess.Popen(["venv\\Scripts\\python.exe", Path], stdout=subprocess.PIPE)

    for line in process.stdout:
        print(line.decode().strip())

    process.wait()

