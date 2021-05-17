from threading import Thread
from time import time, sleep
import queue
import usb.util
import usb.core
import socket
import keyboard
import get_speed_profiile


VENDOR_ID = 0xA720
PRODUCT_ID = 0xF803
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
dev.set_configuration()
dev.set_interface_altsetting(interface=0, alternate_setting=0)
dev.write(0x01, [3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 15, 99, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 2, 0, 5, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 10, 0, 36, 1, 0, 0, 0, 0], 10)
dev.write(0x01, [3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)


def read_board_cor(q):
    mes_dict = {1: '<ОК>', 2: '<COR>'}
    board_sock = socket.socket()
    board_sock.bind(('', 5150))
    board_sock.listen(1)
    conn, addr = board_sock.accept()
    print(conn, addr)
    while True:
        data = (conn.recv(128).decode())
        if data != mes_dict[1]:
            coordinate_worker(data)
        r = dev.read(0x81, 49, 64)
        conn.send(str(r).encode())
        q.put(r)

def coordinate_worker(data):
    c = data.split('*')
    print('C - ', c)    # C -  ['<COR>', '09937', '03331', '0333317', '033971', '<COR>']
    x_cor = get_speed_profiile.list_creator(255, 10, int(c[1]))
    y_cor = get_speed_profiile.list_creator(255, 10, int(c[2]))
    z_cor = get_speed_profiile.list_creator(255, 10, int(c[3]))
    doz_cor = get_speed_profiile.list_creator(255, 10, int(c[4]))
    print(x_cor, y_cor, z_cor, doz_cor)
    x_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if int(c[1]) == 0:
        pass
    elif int(c[1]) > 0:
        print('pluss')
        for i in x_cor:
            x_mes_plus[9] = i
            dev.write(0x1, x_mes_plus, 10)
    else:
        print('minus')
        for i in x_cor:
            x_mes_minus[9] = 256-i
            dev.write(0x1, x_mes_minus, 10)



def serv_process():
    pass

def keyboard_realese():
    max_speeed = 100
    dynamic_speed = 25
    count = 0
    x_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 10, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0]
    x_buffer = 0
    y_buffer = 0
    z_buffer = 0
    a_buffer = 0
    while True:
        if keyboard.is_pressed('6'):  # if key 'q' is pressed
            dev.write(0x1, x_mes_plus, 10)
        if keyboard.is_pressed('4'):  # if key 'q' is pressed
            dev.write(0x1, x_mes_minus, 10)
        if keyboard.is_pressed('8'):  # if key 'q' is pressed
            dev.write(0x1, y_mes_plus, 10)
        if keyboard.is_pressed('2'):  # if key 'q' is pressed
            dev.write(0x1, y_mes_minus, 10)
        if keyboard.is_pressed('+'):  # if key 'q' is pressed
            dev.write(0x1, z_mes_plus, 10)
        if keyboard.is_pressed('-'):  # if key 'q' is pressed
            dev.write(0x1, z_mes_minus, 10)
        if keyboard.is_pressed('0'):  # if key 'q' is pressed
            dev.write(0x1, a_mes_plus, 10)
        if keyboard.is_pressed('.'):  # if key 'q' is pressed
            dev.write(0x1, a_mes_minus, 10)


q = queue.Queue()
data_reading_sending = Thread(target=read_board_cor, args=(q,), name='Read cor')
key = Thread(target=keyboard_realese, name='Keyboard')
def run():
    #server_process = Thread(target=serv_process)
    data_reading_sending.start()
    key.start()
    #server_process.start()
    data_reading_sending.join()
    #server_process.join()
    key.join()


if __name__ == '__main__':
    run()




