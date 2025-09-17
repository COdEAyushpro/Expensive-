import tkinter as tk
import time



def update_time():
    current_time = time.strftime("%H:%M:%S")   
    current_date = time.strftime("%A, %d %B %Y") 
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)  


root = tk.Tk()
root.title("Digital Clock ⏰")
root.geometry("400x200")
root.config(bg="black")

time_label = tk.Label(root, font=("Arial", 40, "bold"), fg="cyan", bg="black")
time_label.pack(pady=20)

date_label = tk.Label(root, font=("Arial", 16), fg="white", bg="black")
date_label.pack()


update_time()

root.mainloop()
