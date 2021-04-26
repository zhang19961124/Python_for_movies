import requests  #pip install requests
import re
import tkinter as tk
from tkinter import messagebox #消息框
from lxml import etree
import webbrowser

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
resp = requests.get("https://v.cnv3.com/", headers=headers)
resp.encoding = resp.apparent_encoding
response = resp.text
#print(response)
#使用正则表达式获取数据
html = etree.HTML(response)
data = html.xpath('.//select[@id="jk"]/option/@value')
reg = data
print(reg)

one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]

#写界面
root = tk.Tk()
root.title('Vip电影播放')
root.geometry('500x250+1000+500')

l1 = tk.Label(root, text='播放接口：', font=('Arial', 12))  #内容
l1.grid()

l2 = tk.Label(root, text='播放链接：', font=('Arial', 12))  #内容
l2.grid(row=6, column=0) #row是行 column是列

t1 = tk.Entry(root, text='', width=50)  #设置一个文本框
t1.grid(row=6, column=1)

var = tk.StringVar()  #设置单选框
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one)
r1.grid(row=0, column=1)   #播放接口选择  单选框

r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two)
r2.grid(row=1, column=1)

r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three)
r3.grid(row=2, column=1)

r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four)
r4.grid(row=3, column=1)


def bf():
    webbrowser.open(var.get() + t1.get())

b1 = tk.Button(root, text='播放',font=('Arial', 12),width=8, command=bf)
b1.grid(row=7, column=1)

def del_text():
    t1.delete(0, 'end')

b2 = tk.Button(root, text='清除',font=('Arial', 12),width=8, command=del_text)
b2.grid(row=8, column=1)


#消息循环
root.mainloop()
