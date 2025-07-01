# main.py

import tkinter as tk
from ui.ui_main import SchedulerUI

def main():
    root = tk.Tk()
    app = SchedulerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
