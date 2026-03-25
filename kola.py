import tkinter as tk

# Tuşa basılınca gerçekleşen olay
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Eşittir butonuna basıldığında hesaplama
def calculate():
    try:
        result = eval(entry.get())  # İşlemi değerlendirir
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hata!")

# Giriş alanını temizleme fonksiyonu
def clear():
    entry.delete(0, tk.END)

# Pencere oluşturma
window = tk.Tk()
window.title("Apple Tarzı Hesap Makinesi")

# Giriş alanı
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Butonları tanımlama
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Butonları yerleştirme
row = 1
col = 0
for button in buttons:
    action = lambda x=button: button_click(x) if x != '=' else calculate()
    tk.Button(window, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Temizleme butonu
tk.Button(window, text='C', width=5, height=2, font=('Arial', 18), command=clear).grid(row=row, column=0, columnspan=4)

# Pencereyi çalıştırma
window.mainloop()
