import tkinter as tk
from tkinter import messagebox
import subprocess

music = subprocess.Popen(["afplay", "music.mp3"])

def make_key():
    word = entry.get().strip().upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if len(word) != 6:
        messagebox.showerror("Ошибка", "Нужно слово ровно из 6 букв!")
        return

    for letter in word:
        if letter not in alphabet:
            messagebox.showerror("Ошибка", "Можно вводить только английские буквы!")
            return

    b1 = word[3] + word[0] + word[5]
    b3 = word[1] + word[4] + word[2]
    b2 = ""
    for letter in word:
        num = alphabet.find(letter) + 1
        b2 = b2 + str(num % 10)

    key = b1 + "-" + b2 + "-" + b3
    res_label.config(text=key)

def close_win():
    music.terminate()
    win.destroy()

bee_x = 20
step = 5

def move_bee():
    global bee_x, step
    bee_x = bee_x + step

    if bee_x > 530 or bee_x < 20:
        step = -step
    bee_lbl.place(x=bee_x, y=30)
    win.after(40, move_bee)

win = tk.Tk()
win.title("Minecraft Keygen")
win.geometry("600x400")
win.resizable(False, False)

bg = tk.PhotoImage(file="bg.png")
bg_lbl = tk.Label(win, image=bg)
bg_lbl.place(x=0, y=0)

bee_lbl = tk.Label(win, text=" =] ", font=("Courier", 14, "bold"), fg="black", bg="#ffcc00", bd=2, relief="raised")

lbl = tk.Label(win, text="Введите слово из 6 букв:", font=("Courier", 12, "bold"), fg="white", bg="#2e4d14")
lbl.pack(pady=(120, 5))

entry = tk.Entry(win, font=("Courier", 14), justify="center", width=15)
entry.pack(pady=5)

btn = tk.Button(win, text="Сгенерировать", font=("Courier", 12, "bold"), fg="black", command=make_key)
btn.pack(pady=15)

res_label = tk.Label(win, text="XXX-XXXXXX-XXX", font=("Courier", 18, "bold"), fg="#ffcc00", bg="#1a3305", width=18)
res_label.pack(pady=10)

move_bee()

win.protocol("WM_DELETE_WINDOW", close_win)
win.mainloop()


