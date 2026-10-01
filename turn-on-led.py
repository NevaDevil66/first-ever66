# ampullllllll

import tkinter as tk

root = tk().Tk()
root.title("Zamanlı Ampul")
root.geometry("500x320")
root.configure(bg="#2c3e50")

root.columnconfigure(0, weight=1)

led = tk.Lable(
    root,
    text="💡",
    font=("Arial", 60),
    fg="#7f8d8c",
    bg="#2c3e50")
led.grid(row=0, column=0, pady=(20, 10))

status_lable = tk.Lable(
    root,
    text="zamanlayıcı",
    fg="#ecf0f1",
    bg="#2c3e50")
status_lable.grid(row=1, column=0, pady=(0, 20))

# turn off
def turn_off_led():
    led.config(fg="#7f8c8d")
    status_lable.config(text=f"zaman doldu")

# turn on
def turn_on_led(seconds):
    
    led.config(fg="#f1c40f")
    status_lable.config(text=f"led {seconds} sn boyunca açık")
    
    milliseconds = seconds * 1000
    root.after(milliseconds, turn_off_led)
    
# buton
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.grid(row=2, column=0, padx=10, pady=10)

for col_idx in range(5):
    button_frame.columnconfigure(col_idx, weight=1, uniform="equal_cols")
    
button_data = [
    ("1sn", 1, "#e74c3c", "black", 0),
    ("2sn", 2, "#e67e22", "black", 1),
    ("3sn", 3, "#f1c40f", "black", 2),
    ("4sn", 4, "#2ecc71", "black", 3),
    ("5sn", 5, "#1abc9c", "black", 4)]

for text, sec, bg_color, fg_color, col_idx in buttons_data:
    btn = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 12, "bold"),
        bg=bg_color,
        fg=fg_color,
        width=5,
        heigth=2,
        command=lambda s=sec: turn_on_led(s))
    btn.grid(row=0, column=col_idx, padx=6, pady=5)
    
root.mainloop()