import random, os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

table = Table()
console = Console()
table.add_column("No", style="green", justify="center")
table.add_column("Peraturan", style="green", justify="center")
table.add_column("Item", style="green", justify="center")
table.add_row("1", "kalah dengan batu ", " gunting")
table.add_row("2", "kalah dengan gunting ", " kertas")
table.add_row("3", "kalah dengan kertas ", " batu")
console.print(table, justify="center")

komputer = lambda: random.choice(["kertas", "batu", "gunting"])


def vs():
    while True:
        com = komputer()
        user = input("pilih jagoanmu : ")
        console.print(Panel(validasi(com, user)), justify="center")
        lagi = input(f"\n lagi? Y/N :")
        os.system("clear")
        if lagi.upper() != "Y":
            break


def validasi(komputer, user):
    komputer.lower()
    user.lower()
    mess = f"komputer : {komputer}\n you : {user}"
    message = {"win": "YOU WIN", "lose": " YOU LOSE "}
    if komputer == user:
        return f" Seri\n {mess}"
    elif (komputer, user) in [
        ("batu", "kertas"),
        ("gunting", "batu"),
        ("kertas", "gunting"),
    ]:
        return f" {message["win"]} , \n\n {mess}"
    else:

        return f"{message["lose"]}\n\n {mess}"


vs()
