# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
  b = exitboxl.get()
  tmsg.showinfo("入力されたテキスト",b)


  isok = False
  if len(b) !=4:
      tmsg.showerror("エラー""4桁の数字を入力してください")
  else:
      kazuok = True
      for i in range(4):
        if(b[i]<"0")or(b[i]>"9"):
          print("エラー""数字ではありません")
          kazuok = False
          break

      if kazuok:  
        isok = True
  if isok:  
    hit=0
    for i in range(4):
      if a[i]==int(b[i]):
        hit=hit+1

  blow=0
  for j in range(4):
    for i in range(4):
      if (int(b[j])==a[i]) and (a[i]!=int(b[i])) and (a[j]!=int(b[j])):
        blow=blow+1
        break

  if hit ==4:
    print("当たり!")
    root.destroy()
  else:
    tmsg.showinfo("ヒント""ヒット"+str(hit)+"/"+"ブロー"+str(blow))  


a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

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