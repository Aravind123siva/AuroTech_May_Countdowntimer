import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Application")
        
        self.mode = tk.StringVar(value="stopwatch")
        
        self.create_widgets()
        self.running = False
        self.time_left = 0
        
    def create_widgets(self):
        tk.Radiobutton(self.root, text="Countdown Timer", variable=self.mode, value="countdown", command=self.reset).pack(anchor="w")
        tk.Radiobutton(self.root, text="Stopwatch", variable=self.mode, value="stopwatch", command=self.reset).pack(anchor="w")
        
        self.time_entry = tk.Entry(self.root, width=10)
        self.time_entry.pack(pady=10)
        
        self.label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=10)
        
    def start(self):
        if self.running:
            return
        self.running = True
        if self.mode.get() == "countdown":
            try:
                self.time_left = int(self.time_entry.get())
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter an integer value for the countdown timer.")
                self.running = False
                return
        self.update_timer()
    
    def stop(self):
        self.running = False
    
    def reset(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00:00")
        self.time_entry.delete(0, tk.END)
    
    def update_timer(self):
        if self.running:
            if self.mode.get() == "countdown":
                if self.time_left > 0:
                    self.time_left -= 1
                    self.label.config(text=self.format_time(self.time_left))
                    self.root.after(1000, self.update_timer)
                else:
                    self.running = False
                    messagebox.showinfo("Time's up!", "Countdown finished.")
            else:
                self.time_left += 1
                self.label.config(text=self.format_time(self.time_left))
                self.root.after(1000, self.update_timer)
    
    @staticmethod
    def format_time(seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
