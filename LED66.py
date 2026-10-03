import customtkinter as ctk

ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.title("LED")
root.geometry("600x600")
root.resizable(False, False)

siyah_bg = "#000000"
beyaz_bg = "#f0f0f0"

root.configure(fg_color=siyah_bg)

# 3 sütunu da eşit genişlikte esnetiyoruz
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(0, weight=1)

def siyaha_don():
    root.configure(fg_color=siyah_bg)

def arkaplan_degistir(saniye):
    root.configure(fg_color=beyaz_bg)
    root.after(int(saniye * 1000), siyaha_don)

btn1 = ctk.CTkButton(
    root,
    text="1sn",
    font=("Arial", 12, "bold"),
    fg_color="#34495e",
    hover_color="#2c3e50",
    command=lambda: arkaplan_degistir(1))
btn1.grid(row=0, column=0, padx=10, pady=30, ipady=10)

btn2 = ctk.CTkButton(
    root,
    text="2sn",
    font=("Arial", 12, "bold"),
    fg_color="#34495e",
    hover_color="#2c3e50",
    command=lambda: arkaplan_degistir(2))
btn2.grid(row=0, column=1, padx=10, pady=30, ipady=10)

btn3 = ctk.CTkButton(
    root,
    text="3sn",
    font=("Arial", 12, "bold"),
    fg_color="#34495e",
    hover_color="#2c3e50",
    command=lambda: arkaplan_degistir(3))
btn3.grid(row=0, column=2, padx=10, pady=30, ipady=10)

root.mainloop()