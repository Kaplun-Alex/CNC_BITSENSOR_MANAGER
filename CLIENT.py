from tkinter import *
import tkinter.font
from decimal import Decimal
import threading
import socket
import time

win = tkinter.Tk()
win.title("DOPROS")
win.geometry('600x450+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')


doprosbot = Label(win, text='Положення приладу', font=BigFont)
doprosbot.pack()
doprosbot.place(x=120, y=50)

class SystemCorVal():
    def __init__(self, val):
        self.coordinate_obj = val
        self.fl_val = Decimal('0.001')
    def __str__(self):
        return f'{self.coordinate_obj}'
    def increase_value(self):
        self.coordinate_obj += self.fl_val
    def decrease_value(self):
        self.coordinate_obj -= self.fl_val
    def get_value(self):
        return self.coordinate_obj

x_cor_system_value = SystemCorVal(Decimal('0.0000'))
y_cor_system_value = SystemCorVal(Decimal('0.0000'))
z_cor_system_value = SystemCorVal(Decimal('0.0000'))
doz_cor_system_value = SystemCorVal(Decimal('0.0000'))

# Считаные координаты////////////////////////////////////////////////
x_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
x_cor_device_entry.pack()
x_cor_device_entry.place(x=300, y=100, height=30, width=200)
x_cor_device_entry.delete(0, END)
x_cor_device_entry.insert(0, x_cor_system_value)

y_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
y_cor_device_entry.pack()
y_cor_device_entry.place(x=300, y=150, height=30, width=200)
y_cor_device_entry.delete(0, END)
y_cor_device_entry.insert(0, y_cor_system_value)

z_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
z_cor_device_entry.pack()
z_cor_device_entry.place(x=300, y=200, height=30, width=200)
z_cor_device_entry.delete(0, END)
z_cor_device_entry.insert(0, z_cor_system_value)

doz_cor_device_entry = Entry(win, font=BigFont, justify='center')
doz_cor_device_entry.pack()
doz_cor_device_entry.place(x=300, y=250, height=30, width=200)
doz_cor_device_entry.delete(0, END)
doz_cor_device_entry.insert(0, doz_cor_system_value)
# Координаты по системе/////////////////////////////////////////////////////////
x_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
x_cor_system_entry.pack()
x_cor_system_entry.place(x=50, y=100, height=30, width=200)
x_cor_system_entry.delete(0, END)
x_cor_system_entry.insert(0, x_cor_system_value)

y_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
y_cor_system_entry.pack()
y_cor_system_entry.place(x=50, y=150, height=30, width=200)
y_cor_system_entry.delete(0, END)
y_cor_system_entry.insert(0, y_cor_system_value)

z_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
z_cor_system_entry.pack()
z_cor_system_entry.place(x=50, y=200, height=30, width=200)
z_cor_system_entry.delete(0, END)
z_cor_system_entry.insert(0, z_cor_system_value)

doz_cor_system_entry = Entry(win, font=BigFont, justify='center')
doz_cor_system_entry.pack()
doz_cor_system_entry.place(x=50, y=250, height=30, width=200)
doz_cor_system_entry.delete(0, END)
doz_cor_system_entry.insert(0, doz_cor_system_value)

# Кнопки


def key_x_minus(event=None):
    x_cor_system_value.decrease_value()
    x_cor_system_entry.delete(0, END)
    x_cor_system_entry.insert(0, x_cor_system_value.get_value())
    print(x_cor_system_value.get_value())
def key_x_plus(event=None):
    x_cor_system_value.increase_value()
    x_cor_system_entry.delete(0, END)
    x_cor_system_entry.insert(0, x_cor_system_value.get_value())
    print(x_cor_system_value.get_value())
def key_y_minus(event=None):
    y_cor_system_value.decrease_value()
    y_cor_system_entry.delete(0, END)
    y_cor_system_entry.insert(0, y_cor_system_value.get_value())
    print(y_cor_system_value.get_value())
def key_y_plus(event=None):
    y_cor_system_value.increase_value()
    y_cor_system_entry.delete(0, END)
    y_cor_system_entry.insert(0, y_cor_system_value.get_value())
    print(y_cor_system_value.get_value())


sock = socket.socket()
sock.connect(('localhost', 5150))

def go_run():
    print('go_run')
    while True:
        mess = str(x_cor_system_value.get_value()).replace('.', '') + '*' + str(y_cor_system_value.get_value()).replace('.', '')
        print(mess)
        sock.send(mess.encode())
        data = sock.recv(256)

        #sock.close()
        print(data)
        time.sleep(0.001)

sender_thread = threading.Thread(target=go_run)
sender_thread.start()
# Кнопки

axel_x_minus = Button(win, text='X-- ', command=key_x_minus)
win.bind('4', key_x_minus)
axel_x_minus.pack()
axel_x_minus.place(x=150, y=350)

axel_x_plus = Button(win, text='X++',  command=key_x_plus)
win.bind('6', key_x_plus)
axel_x_plus.pack()
axel_x_plus.place(x=250, y=350)

axel_y_minus = Button(win, text='Y-- ', command=key_y_minus)
win.bind('2', key_y_minus)
axel_y_minus.pack()
axel_y_minus.place(x=200, y=400)

axel_y_plus = Button(win, text='Y++', command=key_y_plus)
win.bind('8', key_y_plus)
axel_y_plus.pack()
axel_y_plus.place(x=200, y=300)


mainloop()