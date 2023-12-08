import tkinter as tk
import time
import math

start_time = time.time_ns()

scrn = tk.Tk()

screen_width = scrn.winfo_screenwidth()
screen_height = scrn.winfo_screenheight()

scrn.quit()
scrn.destroy()

def createWindow(color: str) -> tk.Tk:
    window = tk.Tk()
    window.resizable(False, False)
    window.attributes('-topmost', 1)
    window.overrideredirect(True)
    window.title("")
    window.configure(bg=color)
    return window

def gettime() -> float:
    return (time.time_ns() - start_time) / 1000000000

def setpos(win: tk.Tk, x: float, y: float, w: float, h: float):
    string = "{}x{}+{}+{}".format(int(w), int(h), int(x), int(y))
    win.geometry(string) 

windows: list[tk.Tk] = []
avg = 0
avgcount = 0

prevtime = gettime()
while True:
    t = gettime()
    avg += 1 / (t - prevtime)
    avgcount += 1
    print("\r" + str(round(avg / avgcount, 2)) + " " * 20, end="")
    if len(windows) < t / 3:
        avg = 0
        avgcount = 0
        windows.append(createWindow("white"))
        print(str(len(windows)) + " " * 20)

    for i, win in enumerate(windows):
        newt = t - i / 1.2
        w = math.sin(newt * 2 * math.pi * 1) * 50 + 100
        h = math.cos(newt * 2 * math.pi * 1) * 50 + 100
        x = math.cos(newt * 2 * math.pi * 0.25) * 800 + screen_width / 2 - w / 2
        y = math.sin(newt * 2 * math.pi * 0.5) * 400 + screen_height / 2 - h / 2
        setpos(win, x, y, w, h)
        win.update_idletasks()
        win.update()

    time.sleep(0.01)
    prevtime = t
