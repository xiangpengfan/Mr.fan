'''
python的绘图模块，速度较慢,不过一般的中小型绘图任务没有问题
并且一次编写多平台运行，简洁且优雅
'''

__author__="伟大的小熊猫"

from tkinter import *
import tkinter.messagebox as msgbox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)           #master是父窗口,在调用这个类的时候可以传入父窗口对象
        self.pack(padx=20, pady=20)
        self.creatWidgets()

    def creatWidgets(self):
        self.nameInput=Entry(self,width=30)
        self.nameInput.pack()
        self.alterButton=Button(self,text='点击开始',command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'word'    
        msgbox.showinfo('Message',f'骐骥一跃，不能十步；驽马十驾，功在不舍\n\n{' '*56}---{name}')

if __name__=='__main__':
    app=Application()
    app.master.title('和生活作斗争')
    app.mainloop()