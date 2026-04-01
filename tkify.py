import sys
import tkinter as tk


class TKInput:
    def __init__(self) -> None:
        self.entries = []
        self.root = tk.Tk()
        self.tkUseCheck()

    def tkinput(self, prompt):
        self.entries.append(tk.Entry(self.root, name=prompt))

    def tkUseCheck(self):
        with open(__file__, "r") as f:
            cur = f.read()

        if cur.find("input(") == cur.find("tkinput("):
            return

        else:
            print("replacing input() with tkinput(). You will need to restart the program.")
            with open(__file__, "w") as f:
                f.write(cur.replace("input(", "tkinput("))

            sys.exit()

    def render(self):
        for entry in self.entries:
            entry.pack()

        self.root.mainloop()


if __name__ == "__main__":
    inp = TKInput()
    inp.tkinput("test")
    inp.render()
