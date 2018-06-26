import tkinter
import tkinter.messagebox

#创建应用程序窗口
root = tkinter.Tk()
#在窗口上创建标签组件
labelName= tkinter.Label(root,text='User_name: ',
                         justify=tkinter.RIGHT,
                         width=80
                         )
labelName.place(x=10,y=5,width=80,height=20)
#创建字符串变量和文本框组件,同时设置关联的变量
varName = tkinter.StringVar(root,value='')
entryName = tkinter.Entry(root,width=80,textvariable=varName)
entryName.place(x=100,y=5,width=80,height=20)

#创建密码文本框
laberPwd = tkinter.Label(root,text='User Pwd: ',justify=tkinter.RIGHT,
                         width=80)
laberPwd.place(x=10,y=30,width=80,height=20)
varPwd = tkinter.StringVar(root,value='')
entryPwd = tkinter.Entry(root,show='.',width=80,textvariable=varPwd)
entryPwd.place(x=100,y=30,width=80,height=20)
def login():
    name = entryName.get()
    pwd = entryPwd.get()
    if name == 'admin' and pwd == '12345'.strip():
        tkinter.messagebox.showinfo(title='恭喜',message='登录成功')
    else:
        tkinter.messagebox.showinfo(title='错误',message='输入错误')
def cancel():
    varName.set('')
    varPwd.set('')

button_login = tkinter.Button(root,text='登入',command=login)
button_login.place(x=30,y=70,width=50,height=20)

button_cancel =tkinter.Button(root,text='取消',command=cancel)
button_cancel.place(x=90,y=70,width=50,height=20)

root.mainloop()