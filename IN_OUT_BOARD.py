from threading import Thread
from time import time, sleep
import queue
import usb.util
import usb.core
import socket
import struct
import keyboard


VENDOR_ID = 0xA720
PRODUCT_ID = 0xF803
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
dev.set_configuration()
dev.set_interface_altsetting(interface=0, alternate_setting=0)
dev.write(0x01, [3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 15, 99, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 2, 0, 5, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 10, 0, 36, 1, 0, 0, 0, 0], 10)
dev.write(0x01, [3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], 10)
dev.write(0x1, [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)
board_sock = socket.socket()
board_sock.bind(('', 5150))
board_sock.listen(1)
conn, addr = board_sock.accept()

data = []

def read_board_cor(q):
    global data
    while True:
        data = (conn.recv(128).decode()).split('*')
        #print(data)
        r = dev.read(0x81, 49, 64)
        conn.send('server ECHOES'.encode() + str(r).encode())
        q.put(r)

        #print(data)
        #print(r)

def serv_process():
    mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        r = q.get()
        #print(r)
        #data = (conn.recv(254).decode()).split('*')
        #r = dev.read(0x81, 49, 64)
        x_cor = [r[12], r[11], r[10], r[9]]
        y_cor = [r[20], r[19], r[18], r[17]]
        z_cor = [r[28], r[27], r[26], r[25]]
        a_cor = [r[36], r[35], r[34], r[33]]
        hex_x_cor = bytes(x_cor).hex()
        dec_x_cor = struct.unpack('>i', bytes.fromhex(hex_x_cor))
        hex_y_cor = bytes(y_cor).hex()
        dec_y_cor = struct.unpack('>i', bytes.fromhex(hex_y_cor))
        #hex_z_cor = bytes(z_cor).hex()
        #hex_a_cor = bytes(a_cor).hex()
        #print('координати x:', hex_x_cor)
        #print('координати y:', hex_y_cor)
        #print(x_cor, y_cor, z_cor, a_cor)
        client_cor_x = int(data[0])
        client_cor_y = int(data[1])
        #print('координати кдієнта х', dec_x_cor)
        #print('координати клієнта y:', dec_y_cor)

'''        
        if dec_x_cor[0] == client_cor_x:
            print('Same')
        elif dec_x_cor[0] < client_cor_x:
            dev.write(0x1, mes_plus, 10)
        else:
            dev.write(0x1, mes_minus, 10)
        #conn.send('server ECHOE'.encode() + str(r).encode())
        '''
def keyboard_realese():
    max_speeed = 100
    dynamic_speed = 25
    count = 0
    x_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 155, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 155, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 155, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 155, 255, 255, 255, 0, 0, 0, 0, 0]
    x_buffer = 0
    y_buffer = 0
    z_buffer = 0
    a_buffer = 0
    while True:
        if keyboard.is_pressed('6'):  # if key 'q' is pressed
            x_buffer += 1
            dev.write(0x1, x_mes_plus, 10)
        if keyboard.is_pressed('4'):  # if key 'q' is pressed
            x_buffer -= 1
            dev.write(0x1, x_mes_minus, 10)
        if keyboard.is_pressed('8'):  # if key 'q' is pressed
            y_buffer += 1
            dev.write(0x1, y_mes_plus, 10)
        if keyboard.is_pressed('2'):  # if key 'q' is pressed
            y_buffer -= 1
            dev.write(0x1, y_mes_minus, 10)
        if keyboard.is_pressed('+'):  # if key 'q' is pressed
            z_buffer += 1
            dev.write(0x1, z_mes_plus, 10)
        if keyboard.is_pressed('-'):  # if key 'q' is pressed
            z_buffer -= 1
            dev.write(0x1, z_mes_minus, 10)
        if keyboard.is_pressed('0'):  # if key 'q' is pressed
            a_buffer += 1
            dev.write(0x1, a_mes_plus, 10)
        if keyboard.is_pressed('.'):  # if key 'q' is pressed
            a_buffer -= 1
            dev.write(0x1, a_mes_minus, 10)
        sleep(0.0001)
        print(count, x_buffer, y_buffer, z_buffer, a_buffer)

q = queue.Queue()
def run():
    data_reading_sending = Thread(target=read_board_cor, args=(q,))
    server_process = Thread(target=serv_process)
    key = Thread(target=keyboard_realese)
    data_reading_sending.start()
    key.start()
    server_process.start()
    data_reading_sending.join()
    server_process.join()
    key.join()
if __name__ == '__main__':
    run()



