# from tkinter import *

# root = Tk()
# root.title("AppA GUI")
# root.geometry("640x480") # 가로 * 세로
# #root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표



# root.mainloop()




from tkinter import *

root = Tk()
root.title("AppA GUI")
root.geometry("640x480") # 가로 * 세로






def btncmd():
    pass


btn =Button(root, text="클릭", command=btncmd)
btn.pack()    



root.mainloop()