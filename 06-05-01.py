# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
  b = exitboxl.get()
  tmsg.showinfo("入力されたテキスト",b)

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

labell = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
labell.place(x = 20, y = 20)

exitboxl = tk.Entry(width = 4, font=("Helvetica", 28))
exitboxl.place(x = 120, y = 60)

buttonl = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
buttonl.place(x = 220, y = 60)

root.mainloop()