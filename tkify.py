import atexit
import builtins
import tkinter as tk

objects = []



root = tk.Tk()
root.geometry("500x500")
def add_object(obj: str):
    objects.append((obj, tk.Entry(root, textvariable=tk.StringVar(root, value=obj))))

def run_code():
    global objects
    for i in objects:
        tk.Label(root, text=i[0]).pack(justify="right")
        tk.Entry(root, textvariable=i[1]).pack(justify="left")

    root.mainloop()

atexit.register(run_code)
