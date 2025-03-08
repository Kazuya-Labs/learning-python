import time, os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table

table = Table()
console = Console()


def loading(text: str, color: str = "[red]", totall: int = 100):
    with Progress() as progress:
        texts = progress.add_task(f"{color} {text}", total=totall)

        while not progress.finished:
            progress.update(texts, advance=1.5)
            time.sleep(0.2)


class Ttc:
    def __init__(self) -> None:
        self.player = "X"
        self.box = [None] * 9
        self.acces = True

    def validasi_box(self, player, posisi):
        try:
            #            self.validasi_win(self.player)
            if self.box[posisi] != None:
                return {"repeat": True, "message": "posisi sudah terisi"}
            elif posisi > 9 or posisi < 0:
                return {"repeat": True, "message": "masukan angka 1-9"}
            else:
                self.box[posisi] = player

                return {"repeat": False}
        except ValueError as e:
            print(e)

    def validasi_win(self, player):
        list = [
            [0, 1, 2],
            [0, 3, 6],
            [0, 4, 8],
            [1, 4, 7],
            [2, 5, 8],
            [3, 4, 5],
            [4, 2, 6],
            [6, 7, 8],
        ]
        for i in list:
            #         print(list)
            if self.box[i[0]] == self.box[i[1]] == self.box[i[2]] != None:
                self.acces = False
                return True
        return loading("LOADING", "[green]", 5)

    def vs(self):
        try:
            while self.acces:
                x_p = int(input(f"[{self.player}] masukan angka : ")) - 1
                cek = self.validasi_box(self.player, x_p)
                if self.validasi_win(self.player):
                    return console.print(
                        Panel(f"Winer {self.player}"), justify="center"
                    )
                for i in range(0, len(self.box), 3):
                    console.print(
                        f"{self.box[i]} | {self.box[i + 1]} | {self.box[i+2]} | "
                    )
                if cek.get("repeat"):
                    console.print(
                        Panel(
                            f"{cek.get("message")}",
                            title="message",
                            title_align="center",
                            highlight=True,
                        )
                    )
                    continue
                if self.player == "X":
                    self.player = "O"
                else:
                    self.player = "X"

        except ValueError as e:
            self.vs()


main = Ttc()
main.vs()
