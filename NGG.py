import tkinter as tk
import random

class UnlimitedGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sayı Tahmin Oyunu")
        self.root.geometry("440x680")
        
        # Renk Paleti
        self.BG_DARK = "#1e272e"
        self.BG_WRONG = "#e74c3c"
        self.BG_RIGHT = "#2ecc71"
        self.BTN_RED = "#ff3f34"
        
        self.root.configure(bg=self.BG_DARK)
        
        # Ana Hizalama
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_container = tk.Frame(self.root, bg=self.BG_DARK)
        self.main_container.grid(row=0, column=0)

        # Oyun Değişkenleri
        self.target_number = 0
        self.guess_count = 0
        self.current_input = ""
        self.game_started = False
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        # Durum Bilgisi Etiketi
        self.status_label = tk.Label(
            self.main_container,
            text="OYUNA BAŞLAMAK İÇİN BUTONA BASIN",
            font=("Arial", 12, "bold"),
            fg="#ecf0f1",
            bg=self.BG_DARK
        )
        self.status_label.grid(row=0, column=0, pady=(15, 5))

        # Tahmin Sayacı Göstergesi (Sınırsız Hak)
        self.attempts_label = tk.Label(
            self.main_container,
            text="",
            font=("Arial", 11),
            fg="#f1c40f",
            bg=self.BG_DARK
        )
        self.attempts_label.grid(row=1, column=0, pady=(0, 10))

        # Çerçevesiz Koyu Ekran
        self.display_var = tk.StringVar(value="")
        self.display_screen = tk.Label(
            self.main_container,
            textvariable=self.display_var,
            font=("Courier", 36, "bold"),
            fg="#ffffff",
            bg=self.BG_DARK,
            width=6,
            height=1,
            bd=0,
            highlightthickness=0
        )

        # Numpad Frame (3x3 Grid)
        self.pad_frame = tk.Frame(self.main_container, bg=self.BG_DARK)
        for col in range(3):
            self.pad_frame.columnconfigure(col, weight=1, uniform="pad_cols")

        buttons = [
            (1, 0, 0), (2, 0, 1), (3, 0, 2),
            (4, 1, 0), (5, 1, 1), (6, 1, 2),
            (7, 2, 0), (8, 2, 1), (9, 2, 2)
        ]

        for num, r, c in buttons:
            btn = tk.Button(
                self.pad_frame,
                text=str(num),
                font=("Arial", 16, "bold"),
                bg="#3d3d3d",
                fg="black",
                highlightbackground="#3d3d3d",
                width=4,
                height=2,
                command=lambda n=num: self.press_num(n)
            )
            btn.grid(row=r, column=c, padx=5, pady=5)

        # 0 ve C Satırı
        self.zero_frame = tk.Frame(self.main_container, bg=self.BG_DARK)

        btn_clear = tk.Button(
            self.zero_frame,
            text="C",
            font=("Arial", 14, "bold"),
            bg="#e67e22",
            fg="black",
            highlightbackground="#e67e22",
            width=4,
            height=2,
            command=self.clear_input
        )
        btn_clear.grid(row=0, column=0, padx=5)

        btn_zero = tk.Button(
            self.zero_frame,
            text="0",
            font=("Arial", 16, "bold"),
            bg="#3d3d3d",
            fg="black",
            highlightbackground="#3d3d3d",
            width=4,
            height=2,
            command=lambda: self.press_num(0)
        )
        btn_zero.grid(row=0, column=1, padx=5)

        # Tahmin Et (Enter) Butonu
        self.btn_enter = tk.Button(
            self.main_container,
            text="T A H M İ N   E T",
            font=("Arial", 12, "bold"),
            bg="#2ecc71",
            fg="black",
            highlightbackground="#2ecc71",
            width=20,
            height=2,
            command=self.check_guess
        )

        # BÜYÜK YUVARLAK KIRMIZI BUTON (Canvas)
        self.red_btn_canvas = tk.Canvas(
            self.main_container,
            width=140,
            height=140,
            bg=self.BG_DARK,
            highlightthickness=0
        )
        self.draw_round_button("BAŞLAT", 140)
        self.red_btn_canvas.bind("", lambda e: self.start_or_reset_game())
        self.red_btn_canvas.grid(row=2, column=0, pady=40)

    def draw_round_button(self, text, size):
        self.red_btn_canvas.delete("all")
        self.red_btn_canvas.config(width=size, height=size)
        
        # Tam Yuvarlak Çizimi
        self.red_btn_canvas.create_oval(
            5, 5, size - 5, size - 5,
            fill=self.BTN_RED,
            outline="#b32b24",
            width=3
        )
        # Yuvarlak Buton Yazısı
        font_size = 13 if size > 100 else 10
        self.red_btn_canvas.create_text(
            size // 2, size // 2,
            text=text,
            fill="black",
            font=("Arial", font_size, "bold")
        )

    def start_or_reset_game(self):
        self.target_number = random.randint(0, 99)
        self.guess_count = 0
        self.current_input = ""
        self.game_started = True
        self.game_over = False

        self.set_background_color(self.BG_DARK)
        self.status_label.config(text="0 - 99 Arası Sayı Tutuldu")
        self.attempts_label.config(text="Tahmin Sayısı: 0")
        self.display_var.set("--")

        # Elemanları Arayüze Diz
        self.display_screen.grid(row=2, column=0, pady=(0, 10))
        self.pad_frame.grid(row=3, column=0, pady=5)
        self.zero_frame.grid(row=4, column=0, pady=5)
        self.btn_enter.grid(row=5, column=0, pady=10)
        
        # Kırmızı Yuvarlak Butonu En Alta Kaydırıp Küçült
        self.draw_round_button("YENİDEN", 80)
        self.red_btn_canvas.grid(row=6, column=0, pady=(5, 10))

    def press_num(self, num):
        if not self.game_started or self.game_over:
            return
        if len(self.current_input) < 2:
            self.current_input += str(num)
            self.display_var.set(self.current_input)

    def clear_input(self):
        if not self.game_started or self.game_over:
            return
        self.current_input = ""
        self.display_var.set("--")

    def flash_red(self):
        self.set_background_color(self.BG_WRONG)
        self.root.after(1000, lambda: self.set_background_color(self.BG_DARK))

    def set_background_color(self, color):
        self.root.configure(bg=color)
        self.main_container.configure(bg=color)
        self.pad_frame.configure(bg=color)
        self.zero_frame.configure(bg=color)
        self.status_label.configure(bg=color)
        self.attempts_label.configure(bg=color)
        self.display_screen.configure(bg=color)
        self.red_btn_canvas.configure(bg=color)

    def check_guess(self):
        if not self.game_started or self.game_over or not self.current_input:
            return

        guess = int(self.current_input)
        self.guess_count += 1
        self.attempts_label.config(text=f"Tahmin Sayısı: {self.guess_count}")

        if guess == self.target_number:
            self.status_label.config(text=f"🎉 TEBRİKLER! {self.guess_count}. denemede buldun!")
            self.set_background_color(self.BG_RIGHT)
            self.game_over = True
        else:
            if guess < self.target_number:
                self.status_label.config(text=f"Daha BÜYÜK bir sayı! (🔼 {guess}'den fazla)")
            else:
                self.status_label.config(text=f"Daha KÜÇÜK bir sayı! (🔽 {guess}'den az)")
            
            self.flash_red()
            self.clear_input()

if __name__ == "__main__":
    root = tk.Tk()
    app = UnlimitedGuessGame(root)
    root.mainloop()