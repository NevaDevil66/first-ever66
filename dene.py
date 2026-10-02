import customtkinter as ctk
import random

# Tema ve renk ayarları
ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.title("Sayı Tahmin Oyunu")
root.geometry("380x600")
root.resizable(False, False)

varsayilan_bg = root.cget("fg_color")  # Orijinal koyu arka plan rengi

# Oyundaki değişkenler
hedef_sayi = None
oyun_basladi = False

# 1. Numpad Paneli (Başlangıçta Gizli)
numpad_frame = ctk.CTkFrame(root, fg_color="transparent")

# İpucu Alanı (Yukarı / Aşağı Ok)
ipucu_label = ctk.CTkLabel(
    numpad_frame, 
    text="?", 
    font=("Helvetica", 36, "bold"), 
    text_color="#f39c12"
)
ipucu_label.pack(pady=(0, 5))

# Gösterge Ekranı (Girilen Sayı)
ekran_label = ctk.CTkLabel(
    numpad_frame, 
    text="", 
    font=("Helvetica", 28, "bold"), 
    fg_color="#2c3e50", 
    text_color="#ecf0f1", 
    anchor="center", 
    corner_radius=10, 
    height=50,
    width=260
)
ekran_label.pack(pady=(0, 15))

# Numpad Tuşlar Paneli
tuslar_frame = ctk.CTkFrame(numpad_frame, fg_color="transparent")
tuslar_frame.pack()

def rakam_basildi(r):
    mevcut = ekran_label.cget("text")
    if len(mevcut) < 2:  # En fazla 2 basamaklı sayı girişi
        ekran_label.configure(text=mevcut + str(r))

def temizle():
    ekran_label.configure(text="")

# Rakam Tuşları Düzeni
tuslar = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('C', 3, 0), ('0', 3, 1)
]

for deger, r, c in tuslar:
    if deger == 'C':
        btn = ctk.CTkButton(
            tuslar_frame, 
            text=deger, 
            font=("Helvetica", 16, "bold"), 
            fg_color="#e74c3c", 
            hover_color="#c0392b", 
            command=temizle, 
            width=70, 
            height=50, 
            corner_radius=12
        )
    else:
        btn = ctk.CTkButton(
            tuslar_frame, 
            text=deger, 
            font=("Helvetica", 16, "bold"), 
            fg_color="#34495e", 
            hover_color="#2c3e50", 
            command=lambda d=deger: rakam_basildi(d), 
            width=70, 
            height=50, 
            corner_radius=12
        )
    btn.grid(row=r, column=c, padx=6, pady=6)

# Arka Plan Rengini 1 Saniye Değiştirip Sıfırlayan Fonksiyon
def arka_plan_renklendir(renk):
    root.configure(fg_color=renk)
    root.after(1000, lambda: root.configure(fg_color=varsayilan_bg))

# Tahmin Kontrol Mekanizması
def tahmin_et():
    global hedef_sayi, oyun_basladi
    
    tahmin_str = ekran_label.cget("text")
    if not tahmin_str:
        return
    
    tahmin = int(tahmin_str)
    
    if tahmin == hedef_sayi:
        # Doğru tahmin
        arka_plan_renklendir("#27ae60")  # Yeşil
        ipucu_label.configure(text="🎯", text_color="#2ecc71")
        # Oyun bitti, yeni oyuna hazırla
        oyun_basladi = False
        kirmizi_btn.configure(text="YENİDEN", font=("Helvetica", 12, "bold"))
    else:
        # Yanlış tahmin
        arka_plan_renklendir("#c0392b")  # Kırmızı
        if tahmin < hedef_sayi:
            ipucu_label.configure(text="▲", text_color="#3498db")  # Yukarı ok
        else:
            ipucu_label.configure(text="▼", text_color="#e67e22")  # Aşağı ok
    
    temizle()

# 2. Alt Kısım (Kırmızı Buton)
alt_frame = ctk.CTkFrame(root, fg_color="transparent")
alt_frame.pack(side="bottom", fill="x", pady=25)

def kirmizi_buton_islem():
    global oyun_basladi, hedef_sayi
    
    if not oyun_basladi:
        # Oyunu başlat / sıfırla
        hedef_sayi = random.randint(0, 99)
        oyun_basladi = True
        
        # Numpad'i ekrana yerleştir
        numpad_frame.pack(side="top", pady=15)
        
        # İpucu ve ekranı sıfırla
        ipucu_label.configure(text="?", text_color="#f39c12")
        temizle()
        
        # Kırmızı butonu küçült ve alt kısma al
        kirmizi_btn.configure(
            text="TAHMİN ET", 
            font=("Helvetica", 14, "bold"), 
            width=160, 
            height=45, 
            corner_radius=22
        )
    else:
        # Oyundayken butona basılırsa tahmin yap
        tahmin_et()

# Kırmızı Buton (Başlangıçta ortada, üzerinde yazı yok)
kirmizi_btn = ctk.CTkButton(
    alt_frame, 
    text="", 
    fg_color="#e74c3c", 
    hover_color="#c0392b", 
    command=kirmizi_buton_islem, 
    width=140, 
    height=140, 
    corner_radius=70
)
kirmizi_btn.pack()

root.mainloop()
