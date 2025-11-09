import tkinter as tk

class ColorAppBMZ:
    def __init__(self, root):
        self.root = root
        self.root.title("ColorMix - BMZ")
        self.root.geometry("500x500")
        self.r = tk.IntVar()
        self.g = tk.IntVar()
        self.b = tk.IntVar()
        self.canvas = tk.Canvas(self.root, width=300, height=200)
        self.canvas.pack(pady=20)
        self.scale_r = tk.Scale(self.root, from_=0, to=255, orient="horizontal", label="Piros", variable=self.r, command=self.szinvaltoztat_bmz)
        self.scale_r.pack()
        self.scale_g = tk.Scale(self.root, from_=0, to=255, orient="horizontal", label="Zöld", variable=self.g, command=self.szinvaltoztat_bmz)
        self.scale_g.pack()
        self.scale_b = tk.Scale(self.root, from_=0, to=255, orient="horizontal", label="Kék", variable=self.b, command=self.szinvaltoztat_bmz)
        self.scale_b.pack()
        self.save_button = tk.Button(self.root, text="Szín mentése", command=self.fajlmentes_bmz)
        self.save_button.pack(pady=10)
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.szinvaltoztat_bmz()

    def szinvaltoztat_bmz(self, *args):
        r, g, b = self.r.get(), self.g.get(), self.b.get()
        color = f"#{r:02x}{g:02x}{b:02x}"
        self.canvas.configure(bg=color)
        self.label.configure(text=color)

    def fajlmentes_bmz(self):
        color = self.label.cget("text")
        with open("kedvenc_szinek.txt", "a", encoding="utf-8") as f:
            f.write(color + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorAppBMZ(root)
    root.mainloop()