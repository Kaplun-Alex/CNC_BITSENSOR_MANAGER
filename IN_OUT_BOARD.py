from threading import Thread
import queue
import usb.util
import usb.core
import socket
import keyboard
import interpolator
import full_mes_creator


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

mes_dict = {1: '<ОК!>', 2: '<COR>', 3: '<MOW!>'}

def read_board_cor(q):
    global mes_dict
    board_sock = socket.socket()
    board_sock.bind(('', 5150))
    board_sock.listen(1)
    conn, addr = board_sock.accept()
    print(conn, addr)
    while True:
        data = (conn.recv(128).decode())
        r = dev.read(0x81, 49, 64)
        conn.send(str(r).encode())
        if data != mes_dict[1]:
            coordinate_worker(data)
        q.put(r)

def coordinate_worker(data):
    main_mes = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cort_of_mes = ()
    c = data[:-5].split('*')
    print('C - ', c)    # C -  ['<COR>', '09937', '03331', '0333317', '033971', '<COR>']
    if int(c[1]) == 0 and int(c[2]) == 0 and int(c[3]) == 0 and int(c[4]) == 0:
        print('No cor')
    else:
        interpolator_dict = interpolator.speed_x_y_z_a_interpolator(int(c[5]), int(c[6]), int(c[1]), int(c[2]), int(c[3]), int(c[4]))
        #print(interpolator_dict)    # like - {0: [5, 10, 10, 10, 10, 5], 1: [10, 20, 20, 20, 20, 10], 2: [7, 15, 15, 15, 15, 8], 3: [2, 5, 5, 5, 5, 3]}
        main_list_mes = full_mes_creator.full_mes(interpolator_dict, c)
        #print(main_list_mes)
        for i in main_list_mes:
            dev.write(0x1, i, 20)

def serv_process():
    pass

def keyboard_realese():
    x_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 10, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_plus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0]
    a_mes_minus = [3, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 245, 255, 255, 255, 0, 0, 0, 0, 0]

    while True:
        if keyboard.is_pressed('w'):  # if key 'q' is pressed
            dev.write(0x1, x_mes_plus, 10)
        if keyboard.is_pressed('x'):  # if key 'q' is pressed
            dev.write(0x1, x_mes_minus, 10)
        if keyboard.is_pressed('d'):  # if key 'q' is pressed
            dev.write(0x1, y_mes_plus, 10)
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            dev.write(0x1, y_mes_minus, 10)
        if keyboard.is_pressed('e'):  # if key 'q' is pressed
            dev.write(0x1, z_mes_plus, 10)
        if keyboard.is_pressed('c'):  # if key 'q' is pressed
            dev.write(0x1, z_mes_minus, 10)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            dev.write(0x1, a_mes_plus, 10)
        if keyboard.is_pressed('z'):  # if key 'q' is pressed
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




