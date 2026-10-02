import tkinter as tk

root = tk.Tk()
root.title("RED")
root.geometry("480x480")
root.configure(bg="#000000")
root.resizable(False, False)

canvas = tk.Canvas(root, width=480, height=480, bg="#000000", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# 1. Gölge katmanı (sabit durur)
golge = canvas.create_oval(150, 155, 330, 335, fill="#880000", outline="")

# 2. Ana kırmızı buton nesnesi (silinmeyecek, rengi/konumu güncellenecek)
btn = canvas.create_oval(
    150, 150, 330, 330, 
    fill="#ff0000", 
    outline="#ff6666", 
    width=3, 
    tags="red_button"
)

def buton_bastiginda(event):
    """Basıldığında butonu 3px içeri çeker ve rengini açar."""
    canvas.coords(btn, 153, 153, 327, 327)
    canvas.itemconfig(btn, fill="#ff4d4d", outline="#ff9999")

def buton_biraktiginda(event):
    """Parmağı çekince eski boyut ve rengine döndürür."""
    canvas.coords(btn, 150, 150, 330, 330)
    canvas.itemconfig(btn, fill="#ff0000", outline="#ff6666")
    print("Kırmızı butona basıldı!")

# Tıklama olaylarını bağlama
canvas.tag_bind("red_button", "", buton_bastiginda)
canvas.tag_bind("red_button", "", buton_biraktiginda)
canvas.tag_bind("red_button", "", lambda e: canvas.config(cursor="hand2"))
canvas.tag_bind("red_button", "", lambda e: canvas.config(cursor=""))

root.mainloop()