import sys
import tkinter as tk


class TKInput:
    def __init__(self, runCheck=True, windowSize=(1000, 1000)) -> None:
        self.entries = []
        self.root = tk.Tk()
        self.root.geometry(f"{windowSize[0]}x{windowSize[1]}")
        self.tkUseCheck() if runCheck else None

    def tkinput(self, prompt):
        self.entries.append(tk.Entry(self.root, textvariable=tk.StringVar(self.root, prompt)))

    def tkUseCheck(self):
        with open(__file__, "r") as f:
            cur = f.read()

        if cur.find("input(") == cur.find("tkinput("):
            return

        else:
            print("replacing tkinput() with tkinput(). You will need to restart the program.")
            with open(__file__, "w") as f:
                f.write(cur.replace("tkinput(", "tkinput("))

            sys.exit()

    def render(self):
        for entry in self.entries:
            entry.pack()

        self.root.mainloop()


if __name__ == "__main__":
    inp = TKInput(False)
    inp.tkinput("test")
    inp.tkinput("test2")
    inp.tkinput("test3")
    inp.tkinput("test4")
    inp.render()
