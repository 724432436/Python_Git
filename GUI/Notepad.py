import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.simpledialog
#创建应用程序窗口
app = tkinter.Tk()
app.title('Notepad++ for 王丹丹')
app['width'] = 900
app['height'] = 600
#标记当前内容是否发生改变,是否需要保存
textChanged = tkinter.IntVar(app,value=0)
#当前的文件名
filename = ''
#创建菜单
menu = tkinter.Menu(app)
submenu = tkinter.Menu(menu,tearoff=0,bg= '#CDCDC1') #tearoff=1说明可以独立，会有虚线
def Open():
    global filename
    #如果内容改变就先保存
    if textChanged.get():
        yesno = tkinter.messagebox.askyesno(title='保存还是取消？',message='你想要保存吗')
        if yesno == tkinter.YES:
            Save()
        else:
            pass
    filename = tkinter.filedialog.askopenfilename(title='Open file',filetypes=[('Text files','*.txt')])
    if filename:
        #清空内容
        txtContent.delete(0.0,tkinter.END)
        with open(filename,'r+') as fp:
            txtContent.insert(tkinter.INSERT,''.join(fp.read()))
        #标记为无修改
        textChanged.set(0)
submenu.add_command(label='Open',command=Open)
def Save():
    global filename
    #如果是不是第一次保存文件，则新建文件
    if not filename:
        SaveAs()
    #如果是改变内容,保存
    elif textChanged.get():
        with open(filename,'w') as fp:
            fp.write(txtContent.get(0.0,tkinter.END))
        textChanged.set(0)
submenu.add_command(label='Save',command=Save)

def SaveAs():
    global filename
    #打开另存为的窗口
    newfilename = tkinter.filedialog.asksaveasfilename(title='Save as',initialdir=r'c:\\',initialfile=r'新建文件.txt')
    if newfilename:
        with open(newfilename,'w') as fp:
            fp.write(txtContent.get(0.0,tkinter.END))
        filename = newfilename
        textChanged.set(0)
submenu.add_command(label='Save as',command=SaveAs)
#分割线
menu.add_separator()

def Close():
    global filename
    if textChanged.get():
        Save()
    app.quit()
    #txtContent.delete(0.0,tkinter.END)
    #置空文件名
    #filename = ''
submenu.add_command(label='Close',command=Close)
#将子菜单关联到主菜单上
menu.add_cascade(label='File',menu=submenu)
#Edit子菜单
submenu = tkinter.Menu(menu,tearoff=0,bg= '#CDCDC1')
def Undo():
    #启用undo标志
    txtContent['undo'] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        print(e)
submenu.add_command(label="Undo",command=Undo)
def Redo():
    txtContent['undo'] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        print(e)
submenu.add_command(label='Redo',command=Redo)
#添加分割线
submenu.add_separator()
def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())

submenu.add_command(label='Copy',command=Copy)
def Cut():
    Copy()
    #删除所选内容
    txtContent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
submenu.add_command(label='Cut',command=Cut)

def Paste():
    #如果没有选择内容,则之间粘贴到鼠标文件中,如果有选择则先删除任何粘贴
    try:
        txtContent.insert(tkinter.SEL_FIRST,txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
        return
    except Exception as e:
        print(e)
    txtContent.insert(tkinter.INSERT,txtContent.clipboard_get())
submenu.add_command(label='Paste',command=Paste)
submenu.add_separator()
def Search():
    textToSearch = tkinter.simpledialog.askstring(title='Search',
                                                  prompt='What to search?')
    start = txtContent.search(textToSearch, 0.0, tkinter.END)
    print(start)

    #找到弹回行或者列
    if start:
        tkinter.messagebox.showinfo(title='Found',message="Ok")
    else:
        tkinter.messagebox.showinfo(title='No found',message='Fail')
submenu.add_command(label="Search",command=Search)
menu.add_cascade(label='Edit',menu=submenu)
submenu = tkinter.Menu(menu,tearoff=0,bg= '#CDCDC1')
def About():
    tkinter.messagebox.showinfo(title='About',message='作者:王丹丹')
submenu.add_command(label='About',command=About)
menu.add_cascade(label='Help',menu=submenu)
#将创建的菜单关联到程序窗口
app.config(menu=menu)
txtContent = tkinter.scrolledtext.ScrolledText(app,wrap=tkinter.WORD,bg='#D1D1D1')
txtContent.pack(fill=tkinter.BOTH,expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>',KeyPress)

app.mainloop()
























