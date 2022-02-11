import os
import tkinter.filedialog
from tkinter import *
import time
from calculatelines import get_all_code_numbers

tag = 0
result = ''

def select_file():
    global file_path
    if button3.cget('state') != 'disabled':
        while True:
            if v.get() == 0:
                file_path = tkinter.filedialog.askdirectory(title=u'选择目录', initialdir=(os.path.expanduser(r"./")))
            else:
                file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(r"./")),
                                                               filetypes=[('*', '*.*')])
            if file_path:
                if v.get():
                    text1.insert(END, '文件导入成功！\n')
                else:
                    text1.insert(END, '目录导入成功！\n')

                text6.insert(END, file_path + '\n')
                button3.configure(state='disable', text='锁定路径')
                button2.configure(state='active', text='开始统计')
                break
            else:
                if v.get():
                    text1.insert(END, '文件没有导入，请选择并确认\n')
                else:
                    text1.insert(END, '目录没有导入，请选择并确认\n')
    else:
        # text1.insert(END, '无效的点击' + '\n')
        pass


def wait_result():
    # button2.configure(state='disable', text='统计中...')
    result = '{} 行数统计数据如下：\n{}\n'.format(time.strftime("%Y-%m-%D %H:%M.%S"), get_all_code_numbers(file_path, v.get()))

    with open(r'log.txt', mode='a+', encoding='utf-8') as f:
        f.write(result)
        f.close()
    text1.insert(END, result)
    text1.see(END)

    if result != '':
        button2.configure(state='disable', text='统计结束')
        return 0



def usart_sent():

    # print(text6.get('0.0', END))
    global result
    if text6.get('0.0', END) != '\n':
        text6.delete('0.0', END)
        text1.insert(END, '码量正在火速计算中...\n')
        button2.configure(state='disable', text='统计中...')
        s = v.get()
        if s:
            button3.configure(state='active', text='选择文件')
        else:
            button3.configure(state='active', text='选择目录')
        text1.after(1000, wait_result)
        # result = '{} 统计数据如下：\n{}\n'.format(time.strftime("%Y-%m-%D %H:%M.%S"), get_all_code_numbers(file_path, s))
        #
        # with open(r'log.txt', mode='w', encoding='utf-8') as f:
        #     f.write(result)
        #     f.close()
        # text1.insert(END, result)
        # text1.see(END)

    else:
        if v.get():
            text1.insert(END, '文件没有导入，请选择并确认\n')
        else:
            text1.insert(END, '目录没有导入，请选择并确认\n')


def unit_resister():
    global tag
    if tag:
        v.set(0)
    else:
        v.set(1)
    if v.get():
        button3.configure(state='active', text='选择文件')
    else:
        button3.configure(state='active', text='选择目录')
    tag = v.get()
    text6.delete('0.0', END)


if __name__ == '__main__':
    init_window = Tk()
    init_window.title('常用码量统计表')
    # init_window.geometry("800x600")

    frame_root = Frame(init_window)
    frame_left = Frame(frame_root)
    frame_right = Frame(frame_root)
    #
    # pw1 = PanedWindow(frame_left, orient=VERTICAL)
    # pw2 = PanedWindow(frame_left, orient=VERTICAL)
    # pw3 = PanedWindow(frame_left, orient=VERTICAL)
    #
    # pw3.pack()

    frame5 = Frame(frame_right)
    frame5.pack(side=TOP)
    frame6 = Frame(frame_right)
    frame6.pack(side=LEFT)
    frame7 = Frame(frame_right)
    frame7.pack(side=RIGHT)

    global text1, button2
    text1 = Text(frame5, width=100, height=30)
    text1.grid(column=0, row=0)

    scroll = tkinter.Scrollbar()
    # 放到窗口的右侧, 填充Y竖直方向
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    # 两个控件关联
    scroll.config(command=text1.yview)
    text1.config(yscrollcommand=scroll.set)

    button2 = Button(frame7, text="开始统计", state='active', width=20, height=1)
    button2.bind("<Button-1>", lambda event: usart_sent())
    button2.grid(column=1, row=0)


    global radio5, v
    v = IntVar()
    radio5 = Radiobutton(frame6, text='切换', width=5, height=1, variable=v, value=0, command=unit_resister)
    radio5.grid(column=2, row=0)


    #
    global text6, button3
    text6 = Text(frame6, width=30, height=2)
    button3 = Button(frame6, text="选择目录", state='active', width=10, height=1)
    button3.bind("<Button-1>", lambda event: select_file())
    button3.grid(column=1, row=0)
    text6.grid(column=0, row=0)

    frame_left.pack(side=LEFT)
    frame_right.pack(side=RIGHT)
    frame_root.pack()
    init_window.mainloop()


