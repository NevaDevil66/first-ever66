import tkinter as tk

# Main Window Setup
root = tk.Tk()
root.title("Zamanlı Ampul")
root.geometry("500x320")
root.configure(bg="#2c3e50")

root.columnconfigure(0, weight=1)

# LED Status Label
led = tk.Label(
    root,
    text="💡",
    font=("Arial", 60),
    fg="#7f8c8d",
    bg="#2c3e50"
)
led.grid(row=0, column=0, pady=(20, 10))

# Status Label
status_label = tk.Label(
    root,
    text="Zamanlayıcı Seçin",
    font=("Arial", 12, "bold"),
    fg="#ecf0f1",
    bg="#2c3e50"
)
status_label.grid(row=1, column=0, pady=(0, 20))

# Function to turn off
def turn_off_led():
    led.config(fg="#7f8c8d")
    status_label.config(text="Zaman doldu")

# Function to turn on
def turn_on_led(seconds):
    led.config(fg="#f1c40f")
    status_label.config(text=f"LED {seconds} sn boyunca açık")
    
    milliseconds = seconds * 1000
    root.after(milliseconds, turn_off_led)

# Button Frame
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.grid(row=2, column=0, padx=10, pady=10)

# Symmetric Grid Configuration
for col_idx in range(5):
    button_frame.columnconfigure(col_idx, weight=1, uniform="equal_cols")

# Button Data
buttons_data = [
    ("1sn", 1, "#e74c3c", "black", 0),
    ("2sn", 2, "#e67e22", "black", 1),
    ("3sn", 3, "#f1c40f", "black", 2),
    ("4sn", 4, "#2ecc71", "black", 3),
    ("5sn", 5, "#1abc9c", "black", 4)
]

# Create Buttons in Loop
for text, sec, bg_color, fg_color, col_idx in buttons_data:
    btn = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 12, "bold"),
        bg=bg_color,
        fg=fg_color,
        width=5,
        height=2,
        command=lambda s=sec: turn_on_led(s)
    )
    btn.grid(row=0, column=col_idx, padx=6, pady=5)

root.mainloop()