import tkinter as tk
import time
import math

start_time = time.time_ns()

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.resizable(False, False)
window.attributes('-topmost', 1)
window.overrideredirect(True)
window.title("Anim")
window.configure(bg="white")

def gettime() -> float:
    return (time.time_ns() - start_time) / 1000000000

def setpos(win: tk.Tk, x: float, y: float, w: float, h: float):
    string = "{}x{}+{}+{}".format(int(w), int(h), int(x), int(y))
    win.geometry(string) 

while True:
    t = gettime()
    w = math.sin(t * 2 * math.pi * 1) * 50 + 100
    h = math.cos(t * 2 * math.pi * 1) * 50 + 100
    x = math.cos(t * 2 * math.pi * 0.25) * 400 + screen_width / 2 - w / 2
    y = math.sin(t * 2 * math.pi * 0.5) * 200 + screen_height / 2 - h / 2
    setpos(window, x, y, w, h)
    window.update_idletasks()
    window.update()
