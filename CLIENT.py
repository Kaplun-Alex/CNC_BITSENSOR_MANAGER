from tkinter import *
import tkinter.font
from decimal import Decimal
import threading
import socket
import struct
import get_speed_profiile
from tkinter import filedialog as fd
from tkinter import ttk
import glob

win = tkinter.Tk()
win.title("CNC BIT SENSOR MANAGER")
win.geometry('950x500+100+100')
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

class CncCorVal():
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

cnc_x_cor_val = CncCorVal(0)
cnc_y_cor_val = CncCorVal(0)
cnc_z_cor_val = CncCorVal(0)
cnc_doz_cor_val = CncCorVal(0)

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
# /////////////////////////////////////////////////////////
x_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
x_cor_system_entry.pack()
x_cor_system_entry.place(x=25, y=15, height=30, width=200)
x_cor_system_entry.delete(0, END)
x_cor_system_entry.insert(0, str(x_cor_system_value))

y_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
y_cor_system_entry.pack()
y_cor_system_entry.place(x=25, y=75, height=30, width=200)
y_cor_system_entry.delete(0, END)
y_cor_system_entry.insert(0, str(y_cor_system_value))

z_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
z_cor_system_entry.pack()
z_cor_system_entry.place(x=25, y=135, height=30, width=200)
z_cor_system_entry.delete(0, END)
z_cor_system_entry.insert(0, str(z_cor_system_value))

doz_cor_system_entry = Entry(win, font=ButtonFont, justify='center')
doz_cor_system_entry.pack()
doz_cor_system_entry.place(x=25, y=195, height=30, width=200)
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
                        data = sock.recv(256)
                    send_cor_mes = mes_dict[1]
                    rez_mes_cor.clear()
                else:
                    sock.send(str(control_mess).encode())
                    data = sock.recv(256)
                    data = data.decode()
                    str_r = data[12:-2].split(', ')
                    r = []
                    for i in str_r:
                        r.append(int(i))
                    print(r)
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

axel_x_minus = Button(win, text='▼', command=key_x_minus)
axel_x_minus.pack()
axel_x_minus.place(x=230, y=30)

axel_x_plus = Button(win, text='▲', command=key_x_plus)
axel_x_plus.pack()
axel_x_plus.place(x=230, y=5)

axel_y_minus = Button(win, text='▼', command=key_y_minus)
axel_y_minus.pack()
axel_y_minus.place(x=230, y=90)

axel_y_plus = Button(win, text='▲', command=key_y_plus)
axel_y_plus.pack()
axel_y_plus.place(x=230, y=65)

axel_z_minus = Button(win, text='▼', command=key_z_minus)
axel_z_minus.pack()
axel_z_minus.place(x=230, y=150)

axel_z_plus = Button(win, text='▲', command=key_z_plus)
axel_z_plus.pack()
axel_z_plus.place(x=230, y=125)

axel_doz_minus = Button(win, text='▼', command=key_doz_minus)
axel_doz_minus.pack()
axel_doz_minus.place(x=230, y=210)

axel_doz_plus = Button(win, text='▲', command=key_doz_plus)
axel_doz_plus.pack()
axel_doz_plus.place(x=230, y=185)

conn_button = Button(win, text='Connecting', command=run_server)
conn_button.pack()
conn_button.place(x=450, y=452)

send_button = Button(win, text='RUN TO', font=BigFont, command=lambda: send_mes(2))
send_button.pack()
send_button.place(x=150, y=300)

manual_device_speed = Entry(win, font=small_font, justify='center')
manual_device_speed.pack()
manual_device_speed.place(x=25, y=240, height=20, width=60)
manual_device_speed.delete(0, END)
manual_device_speed.insert(0, speed_and_acc_dict[1])

manual_device_acc = Entry(win, font=small_font, justify='center')
manual_device_acc.pack()
manual_device_acc.place(x=25, y=270, height=20, width=60)
manual_device_acc.delete(0, END)
manual_device_acc.insert(0, speed_and_acc_dict[2])

get_file_lists = ttk.Combobox(win, values=['choose file'], font=small_font, justify='center')
get_file_lists.pack()
get_file_lists.place(x=450, y=260, height=30, width=200)

entry_run_from_op_file = Entry(win, font=small_font, justify='center')
entry_run_from_op_file.pack()
entry_run_from_op_file.place(x=450, y=310, height=30, width=200)


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
save_manual_speed_and_acc.pack()
save_manual_speed_and_acc.place(x=30, y=300)

def get_cnc_list_files():
    files = glob.glob("*.cnc")
    #print(files)
    get_file_lists.config(values=files)

def save_cor_to_file():     # ['<COR>*100*200*300*400*100*20']
    if get_file_lists.get():
        f = open(get_file_lists.get(), 'a')
        f.write(str(mes_dict[2] + '*' + str(int(Decimal(x_cor_device_entry.get())*10000)) + '*' +
                    str(int(Decimal(y_cor_device_entry.get())*10000)) + '*' +
                    str(int(Decimal(z_cor_device_entry.get())*10000)) + '*' +
                    str(int(Decimal(doz_cor_device_entry.get())*10000)) + '*' +
                    manual_device_speed.get() + '*' +
                    manual_device_acc.get()+'\n'))
        f.close()
    else:
        status_entry.delete(0, END)
        status_entry.insert(0, 'NO FILE TO SAVE')

def manual_cor_saving():
    of = fd.asksaveasfile('a')
    of.close()
    get_cnc_list_files()

choose_file = Button(win, text='ADD FILE FOR MANUAL SAVING', font=small_font, command=manual_cor_saving)
choose_file.pack()
choose_file.place(x=670, y=450)

save_cor_to_file = Button(win, text='SAVE COR TO FILE', font=small_font, command=save_cor_to_file)
save_cor_to_file.pack()
save_cor_to_file.place(x=670, y=260)

def openfileforrun():
    global rez_mes_cor
    prom_list = []
    of = fd.askopenfile()
    entry_run_from_op_file.delete(0, END)
    entry_run_from_op_file.insert(0, of.name)
    t = of.readlines()
    prom_list.append(t[0][:-1])
    for i in range(1, len(t)):
        t_last = t[i-1][:-1].split('*')
        t_next = t[i][:-1].split('*')
        t_list = [mes_dict[2], str(int(t_next[1])-int(t_last[1])), str(int(t_next[2])-int(t_last[2])),
                  str(int(t_next[3])-int(t_last[3])), str(int(t_next[4])-int(t_last[4])), t_next[5], t_next[6]]
        temp = '*'.join(t_list)
        prom_list.append(temp)
    rez_mes_cor = prom_list[:]
    of.close()
    print(prom_list)
    print(rez_mes_cor)

def run_from_opened_file():
    global send_cor_mes
    if rez_mes_cor:
        send_cor_mes = mes_dict[2]
    else:
        status_entry.delete(0, END)
        status_entry.insert(0, 'ADD FILE TO RUN')


openfile_for_running = Button(win, text='OPEN FILE FOR RUNNING', font=small_font, command=openfileforrun)
openfile_for_running.pack()
openfile_for_running.place(x=670, y=310)

run_from_op_file = Button(win, text='RUN FROM THIS FILE', font=small_font, command=run_from_opened_file)
run_from_op_file.pack()
run_from_op_file.place(x=480, y=350)

get_cnc_list_files()

mainloop()
