import tkinter as tk

# ana pencere
root = tk().Tk()
root.title("first-ever66 - HMI test")
root.geometry("400x250")
root.configure(bg="#2c3e50")

# başlık
baslik = tk.Lable(
    root,
    text="first-ever66",
    font=("Arial", 16, "bold"),
    fg="#ecf0f1",
    bg="#2c3e50")
baslik.pack(pady=20)

# durum etiketi
durum = tk.Lable(
    root,
    text="sistem hazır",
    font=("Arial", 12),
    fg="#2ecc71",
    bg="#2c3e50")
durum.pack(pady=10)

# buton fonksiyonu
def buton_tiklandi():
    durum.confige(text="motor çalışıyor", fg="#f1c40f")
    
# test butonu
btn = tk.Button(
    root,
    text="sistem başlat",
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="#black",
    command=buton_tiklandi)
btn.pack(pady=20)

root.mainloop()