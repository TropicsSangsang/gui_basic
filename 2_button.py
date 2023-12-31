from tkinter import *

root = Tk()
root.title("AppA GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # padx는 여백이므로 글자가 많아지면 길어진다
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 고정값
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")  # fg 는 글자색 + 글자가 많->길어진다
btn5.pack()

photo = PhotoImage(file="gui_project\\image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()