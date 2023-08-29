from tkinter import *

root = Tk()
root.title("AppA GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)  # Text는 여러줄 입력받을때 사용
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)    # Entry는 한줄만 입력받을때 사용
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END))   # 1 : 첫번째 라인, 0 : 0번쨰 column 위치
    print(e.get())      # Entry는 그냥 get()만 쓰면 된다.
 
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)   #클릭하면 내용은 터미널에 출력되고,  txt와 e에 있던 내용은 삭제된다

btn =Button(root, text="클릭", command=btncmd)
btn.pack()    



root.mainloop()