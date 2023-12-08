import tkinter as tk
import time
import math

class animatedWindow(tk.Tk):
    def createWindow(self, color: str) -> tk.Toplevel:
        window = tk.Toplevel(self)
        window.resizable(False, False)
        window.attributes('-topmost', 1)
        window.overrideredirect(True)
        window.title("")
        window.configure(bg=color)
        return window

    def __init__(self, window_count: int) -> None:
        self.startcount = window_count
        super().__init__()
        self.geometry("0x0")
        self.start_time = time.time_ns()
        self.avg = 0
        self.avgcount = 0
        self.prevtime = self.start_time - 0.001
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.windows: list[tk.Toplevel] = []
        for _ in range(self.startcount):
            self.windows.append(self.createWindow("white"))

    def gettime(self) -> float:
        return (time.time_ns() - self.start_time) / 1000000000

    def setpos(self, win: tk.Toplevel, x: float, y: float, w: float, h: float):
        string = "{}x{}+{}+{}".format(int(w), int(h), int(x), int(y))
        win.geometry(string) 

    def frame(self):
        t = self.gettime()
        self.avg += 1 / (t - self.prevtime)
        self.avgcount += 1
        print("\r" + str(round(self.avg / self.avgcount, 2)) + " " * 20, end="")
        if len(self.windows) - self.startcount < t / 3:
            self.avg = 0
            self.avgcount = 0
            self.windows.append(self.createWindow("white"))
            print(str(len(self.windows)) + " " * 20)

        for i, win in enumerate(self.windows):
            newt = t - i / 1.2
            w = math.sin(newt * 2 * math.pi * 1) * 50 + 100
            h = math.cos(newt * 2 * math.pi * 1) * 50 + 100
            x = math.cos(newt * 2 * math.pi * 0.25) * 800 + self.screen_width / 2 - w / 2
            y = math.sin(newt * 2 * math.pi * 0.5) * 400 + self.screen_height / 2 - h / 2
            self.setpos(win, x, y, w, h)
            win.update()
        
        # self.update()
        self.prevtime = t

anim = animatedWindow(10)

while True:
    anim.frame()
    time.sleep(0.01)
