from tkinter import *
import tkinter.font
from decimal import Decimal
import threading
import socket
import time
import struct
import array
import get_speed_profiile

win = tkinter.Tk()
win.title("DOPROS")
win.geometry('800x500+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=10, weight='bold')
small_font = tkinter.font.Font(family='Hervetica', size=10, weight='bold')


class SystemCorVal():
    def __init__(self, val):
        self.coordinate_obj = val
        self.fl_val = 1

    def __str__(self):
        return f'{self.coordinate_obj}'

    def increase_value(self):
        self.coordinate_obj += self.fl_val

    def decrease_value(self):
        self.coordinate_obj -= self.fl_val

    def get_value(self):
        return self.coordinate_obj


x_cor_system_value = SystemCorVal(0)
y_cor_system_value = SystemCorVal(0)
z_cor_system_value = SystemCorVal(0)
doz_cor_system_value = SystemCorVal(0)


def save_cor():
    x_cor = get_speed_profiile.list_creator(100, 20, int(x_cor_system_entry.get()))
    y_cor = get_speed_profiile.list_creator(100, 20, int(y_cor_system_entry.get()))
    z_cor = get_speed_profiile.list_creator(100, 20, int(z_cor_system_entry.get()))
    doz_cor = get_speed_profiile.list_creator(100, 20, int(doz_cor_system_entry.get()))
    return x_cor, y_cor, z_cor, doz_cor


status_entry = Entry(win, font=BigFont, justify='left')
status_entry.pack()
status_entry.place(x=10, y=450, height=30, width=400)
status_entry.delete(0, END)
status_entry.insert(0, 'TAP CONNECT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')

# Считаные координаты////////////////////////////////////////////////
x_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
x_cor_device_entry.pack()
x_cor_device_entry.place(x=450, y=15, height=30, width=200)
x_cor_device_entry.delete(0, END)
x_cor_device_entry.insert(0, str(x_cor_system_value))

y_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
y_cor_device_entry.pack()
y_cor_device_entry.place(x=450, y=75, height=30, width=200)
y_cor_device_entry.delete(0, END)
y_cor_device_entry.insert(0, str(y_cor_system_value))

z_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
z_cor_device_entry.pack()
z_cor_device_entry.place(x=450, y=135, height=30, width=200)
z_cor_device_entry.delete(0, END)
z_cor_device_entry.insert(0, str(z_cor_system_value))

doz_cor_device_entry = Entry(win, font=ButtonFont, justify='center')
doz_cor_device_entry.pack()
doz_cor_device_entry.place(x=450, y=195, height=30, width=200)
doz_cor_device_entry.delete(0, END)
doz_cor_device_entry.insert(0, str(doz_cor_system_value))
# Координаты на отправку в сервер/////////////////////////////////////////////////////////
x_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
x_cor_system_entry.pack()
x_cor_system_entry.place(x=150, y=15, height=30, width=200)
x_cor_system_entry.delete(0, END)
x_cor_system_entry.insert(0, str(x_cor_system_value))

y_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
y_cor_system_entry.pack()
y_cor_system_entry.place(x=150, y=75, height=30, width=200)
y_cor_system_entry.delete(0, END)
y_cor_system_entry.insert(0, str(y_cor_system_value))

z_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
z_cor_system_entry.pack()
z_cor_system_entry.place(x=150, y=135, height=30, width=200)
z_cor_system_entry.delete(0, END)
z_cor_system_entry.insert(0, str(z_cor_system_value))

doz_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
doz_cor_system_entry.pack()
doz_cor_system_entry.place(x=150, y=195, height=30, width=200)
doz_cor_system_entry.delete(0, END)
doz_cor_system_entry.insert(0, str(doz_cor_system_value))


# Кнопки
def key_x_minus():
    x_cor_system_value.decrease_value()
    x_cor_system_entry.delete(0, END)
    x_cor_system_entry.insert(0, x_cor_system_value.get_value())
def key_x_plus():
    x_cor_system_value.increase_value()
    x_cor_system_entry.delete(0, END)
    x_cor_system_entry.insert(0, x_cor_system_value.get_value())
def key_y_minus():
    y_cor_system_value.decrease_value()
    y_cor_system_entry.delete(0, END)
    y_cor_system_entry.insert(0, y_cor_system_value.get_value())
def key_y_plus():
    y_cor_system_value.increase_value()
    y_cor_system_entry.delete(0, END)
    y_cor_system_entry.insert(0, y_cor_system_value.get_value())
def key_z_minus():
    z_cor_system_value.decrease_value()
    z_cor_system_entry.delete(0, END)
    z_cor_system_entry.insert(0, z_cor_system_value.get_value())
def key_z_plus():
    z_cor_system_value.increase_value()
    z_cor_system_entry.delete(0, END)
    z_cor_system_entry.insert(0, z_cor_system_value.get_value())
def key_doz_minus():
    doz_cor_system_value.decrease_value()
    doz_cor_system_entry.delete(0, END)
    doz_cor_system_entry.insert(0, doz_cor_system_value.get_value())
def key_doz_plus():
    doz_cor_system_value.increase_value()
    doz_cor_system_entry.delete(0, END)
    doz_cor_system_entry.insert(0, doz_cor_system_value.get_value())


def all_cor_device_inserter(x, y, z, doz, mm_count=10000):
    x_cor_device_entry.delete(0, END)
    x_cor_device_entry.insert(0, Decimal(str(x / mm_count)))
    y_cor_device_entry.delete(0, END)
    y_cor_device_entry.insert(0, Decimal(str(y / mm_count)))
    z_cor_device_entry.delete(0, END)
    z_cor_device_entry.insert(0, Decimal(str(z / mm_count)))
    doz_cor_device_entry.delete(0, END)
    doz_cor_device_entry.insert(0, Decimal(str(doz / mm_count)))


connection = False
socket_close = False
send_cor_mes = 0
rez_mes_cor = []
mes_dict = {1: '<ОК!>', 2: '<COR>', 3: '<MOW!>'}
speed_and_acc_dict = {1: '100', 2: '20'}


def send_mes(mes):
    global send_cor_mes
    global rez_mes_cor
    send_cor_mes = mes_dict[mes]
    x_run_to_cor = x_cor_system_entry.get()
    y_run_to_cor = y_cor_system_entry.get()
    z_run_to_cor = z_cor_system_entry.get()
    doz_run_to_cor = doz_cor_system_entry.get()
    rez_mes_cor.append(send_cor_mes
                       + '*' + x_run_to_cor
                       + '*' + y_run_to_cor
                       + '*' + z_run_to_cor
                       + '*' + doz_run_to_cor
                       + '*' + speed_and_acc_dict[1]
                       + '*' + speed_and_acc_dict[2])
    print(rez_mes_cor)


def go_run():
    global server_thread_live
    global send_cor_mes
    control_mess = mes_dict[1]
    try:
        sock = socket.socket()
        sock.connect(('localhost', 5150))
        while True:
            try:
                if send_cor_mes == '<COR>':
                    for i in range(len(rez_mes_cor)):
                        print(i)
                        sock.send((str(rez_mes_cor[i]).encode()))
                    send_cor_mes = mes_dict[1]
                    rez_mes_cor.clear()
                else:
                    sock.send(str(control_mess).encode())
                    data = sock.recv(256)
                    data = data.decode()
                    print(data)
                    str_r = data[12:-2].split(', ')
                    r = []
                    for i in str_r:
                        r.append(int(i))
                    print(r, type(r))
                    x_cor = [r[12], r[11], r[10], r[9]]
                    y_cor = [r[20], r[19], r[18], r[17]]
                    z_cor = [r[28], r[27], r[26], r[25]]
                    doz_cor = [r[36], r[35], r[34], r[33]]
                    # print(x_cor, y_cor, z_cor, doz_cor)
                    hex_x_cor = bytes(x_cor).hex()
                    dec_x_cor = struct.unpack('>i', bytes.fromhex(hex_x_cor))
                    hex_y_cor = bytes(y_cor).hex()
                    dec_y_cor = struct.unpack('>i', bytes.fromhex(hex_y_cor))
                    hex_z_cor = bytes(z_cor).hex()
                    dec_z_cor = struct.unpack('>i', bytes.fromhex(hex_z_cor))
                    hex_doz_cor = bytes(doz_cor).hex()
                    dec_doz_cor = struct.unpack('>i', bytes.fromhex(hex_doz_cor))
                    all_cor_device_inserter(dec_x_cor[0], dec_y_cor[0], dec_z_cor[0], dec_doz_cor[0])  # struct->tuple
                    control_mess = mes_dict[1]

            except ConnectionResetError:
                status_entry.delete(0, END)
                status_entry.insert(0, 'No connection to server')
                server_thread_live = False
                break
    except ConnectionRefusedError:
        status_entry.delete(0, END)
        status_entry.insert(0, 'No connection to server')
        server_thread_live = False


server_thread_live = False


def run_server():
    global server_thread_live
    if not server_thread_live:
        sender_thread = threading.Thread(target=go_run, name='Server thread')
        sender_thread.start()
        server_thread_live = True
        status_entry.delete(0, END)
        status_entry.insert(0, 'Connecting...')
    else:
        status_entry.delete(0, END)
        status_entry.insert(0, 'Is connect')


def close_conn():
    global socket_close
    socket_close = True


doprosbot = Label(win, text='', font=BigFont)
doprosbot.pack()
doprosbot.place(x=120, y=5)

axel_x_minus = Button(win, text='▼', command=key_x_minus)
axel_x_minus.pack()
axel_x_minus.place(x=355, y=30)

axel_x_plus = Button(win, text='▲', command=key_x_plus)
axel_x_plus.pack()
axel_x_plus.place(x=355, y=5)

axel_y_minus = Button(win, text='▼', command=key_y_minus)
axel_y_minus.pack()
axel_y_minus.place(x=355, y=90)

axel_y_plus = Button(win, text='▲', command=key_y_plus)
axel_y_plus.pack()
axel_y_plus.place(x=355, y=65)

axel_z_minus = Button(win, text='▼', command=key_z_minus)
axel_z_minus.pack()
axel_z_minus.place(x=355, y=150)

axel_z_plus = Button(win, text='▲', command=key_z_plus)
axel_z_plus.pack()
axel_z_plus.place(x=355, y=125)

axel_doz_minus = Button(win, text='▼', command=key_doz_minus)
axel_doz_minus.pack()
axel_doz_minus.place(x=355, y=210)

axel_doz_plus = Button(win, text='▲', command=key_doz_plus)
axel_doz_plus.pack()
axel_doz_plus.place(x=355, y=185)

conn_button = Button(win, text='Connecting', command=run_server)
conn_button.pack()
conn_button.place(x=450, y=452)

send_button = Button(win, text='RUN TO', font=BigFont, command=lambda: send_mes(2))
send_button.pack()
send_button.place(x=80, y=105)

send_button = Button(win, text='Close connection', command=close_conn)
send_button.pack()
send_button.place(x=5, y=65)

manual_device_speed = Entry(win, font=small_font, justify='center')
manual_device_speed.pack()
manual_device_speed.place(x=700, y=5, height=20, width=60)
manual_device_speed.delete(0, END)
manual_device_speed.insert(0, speed_and_acc_dict[1])

manual_device_acc = Entry(win, font=small_font, justify='center')
manual_device_acc.pack()
manual_device_acc.place(x=700, y=30, height=20, width=60)
manual_device_acc.delete(0, END)
manual_device_acc.insert(0, speed_and_acc_dict[2])

def save_speed_and_acc():
    global speed_and_acc_dict
    speed = manual_device_speed.get()
    acc = manual_device_acc.get()
    eroor_mes = 'Error, value SP-> 1-255, ACC->1-100'
    error_mes_colision = 'SPEED MUST BE MORE THAN ACCELERATION'
    if 0 < int(speed) <= 255:
        speed_and_acc_dict[1] = str(speed)
        status_entry.delete(0, END)
        status_entry.insert(0, f'Speeed > {speed_and_acc_dict[1]} | | Acceleration > {speed_and_acc_dict[2]}')
    else:
        status_entry.delete(0, END)
        status_entry.insert(0, eroor_mes)
        manual_device_speed.delete(0, END)
        manual_device_speed.insert(0, speed_and_acc_dict[1])
    if 0 < int(acc) <= 100:
        speed_and_acc_dict[2] = str(acc)
        status_entry.delete(0, END)
        status_entry.insert(0, f'Speeed > {speed_and_acc_dict[1]} | | Acceleration > {speed_and_acc_dict[2]}')
    else:
        status_entry.delete(0, END)
        status_entry.insert(0, eroor_mes)
        manual_device_acc.delete(0, END)
        manual_device_acc.insert(0, speed_and_acc_dict[2])
    if int(speed) < int(acc):
        speed_and_acc_dict[1], speed_and_acc_dict[2] = 100, 20
        status_entry.delete(0, END)
        status_entry.insert(0, error_mes_colision)
        manual_device_speed.delete(0, END)
        manual_device_speed.insert(0, speed_and_acc_dict[1])
        manual_device_acc.delete(0, END)
        manual_device_acc.insert(0, speed_and_acc_dict[2])
        speed_and_acc_dict[1],  speed_and_acc_dict[2] = 100, 20
    print(speed_and_acc_dict)

save_manual_speed_and_acc = Button(win, text='SAVE', font=small_font, command=save_speed_and_acc)
# win.bind('4', key_x_minus)
save_manual_speed_and_acc.pack()
save_manual_speed_and_acc.place(x=706, y=60)

mainloop()
