#Python ronbuun.py
import tkinter as tk
import tkinter.ttk as ttk
import random

x=[0]*500#ざっくりの問題数を入れる
y=[0]*500
for i in range(500):
    x[i],y[i]= list(input("単語/答えを入力してください。X/Xまで読み込み").split("/"))#問題/答えの形式で認識する
    if(x[i]=="X"):#X/Xまで読み込んだら終わり
        break
x=[i for i in x if i!=0]
y=[i for i in y if i!=0]
x=[i for i in x if i!="X"]
y=[i for i in y if i!="X"]
print(x)
print(y)
kosuu=len(x)

root = tk.Tk()
#フレーム
root.title('ankiban')
root.geometry("600x266")

#画像
img = "img.png"#同フォルダ内に好きな画像を入れて大きさ調節してね、デフォルトでは380*256ピクセルの画像で丁度いい
img1 = tk.PhotoImage(file=img,master=root)
label1 = ttk.Label(root,image=img1)
label1.place(relx=0, rely=0)

#単語のテキスト
txt1 = tk.Text(width=25, height=2)
txt1.place(relx=0.65, rely=0)

#答えのテキスト
txt2 = tk.Text(width=25, height=2)
txt2.place(relx=0.65, rely=0.12)

#メインエンジン
def tango(event):
    global ran
    ran=random.randint(1,kosuu)
    tango1=x[ran]
    txt1.delete(1.0,tk.END)
    txt2.delete(1.0,tk.END)
    txt1.insert(1.0,tango1)

def kotae(event):
    kotae=y[ran]
    txt2.delete(1.0,tk.END)
    txt2.insert(1.0,kotae)

#次の単語表示ボタン
Button = tk.Button(text='次の単語',width=20, height=2)
Button.bind("<Button-1>",tango)
Button.place(relx=0.67, rely=0.4)

#答え表示ボタン
Button2 = tk.Button(text='答えを表示',width=20, height=2)
Button2.bind("<Button-1>",kotae)
Button2.place(relx=0.67, rely=0.55)

root.mainloop()