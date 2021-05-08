from multiprocessing import Process
from time import sleep
import usb.util
import usb.core
import socket


class DNO:

    def __init__(self):
        self.r = ''
        self.dev = 'device obj'

    def init_board(self):
        VENDOR_ID = 0xA720
        PRODUCT_ID = 0xF803
        self.dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        self.dev.set_configuration()
        self.dev.set_interface_altsetting(interface=0, alternate_setting=0)
        self.dev.write(0x01, [3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 15, 99, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)
        self.dev.write(0x01, [2, 2, 0, 5, 0, 0, 0, 0, 0], 10)
        self.dev.write(0x01, [2, 10, 0, 36, 1, 0, 0, 0, 0], 10)
        self.dev.write(0x01, [3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], 10)
        return self.dev

    def func1(self):
        s = self.init_board()
        print("func1 up and running")
        board_sock = socket.socket()
        board_sock.bind(('', 5150))
        board_sock.listen(1)
        conn, addr = board_sock.accept()
        while True:
            self.r = str(s.read(0x81, 49, 64))
            board_data = []
            cor_list = (((self.r.encode()).decode())[1:-1]).split(', ')
            x_cor = [cor_list[10], cor_list[11], cor_list[12], cor_list[13]]
            y_cor = [cor_list[18], cor_list[19], cor_list[20], cor_list[21]]
            z_cor = [cor_list[26], cor_list[27], cor_list[28], cor_list[29]]
            a_cor = [cor_list[34], cor_list[35], cor_list[36], cor_list[37]]
            conn.send('server ECHOE'.encode() + self.r.encode())
            print(x_cor, y_cor, z_cor, a_cor)
            sleep(0.5)

    def func2(self):
        print("func2 up and running")
        sock = socket.socket()
        sock.bind(('', 6160))
        sock.listen(10)
        conn, addr = sock.accept()
        while True:
            data = (conn.recv(254).decode()).split('*')
            mes = [3, 5, 0, 2, 0, 0, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0]
            print(data)
            if not data:
                break
            conn.send('run_cor'.encode() + self.r.encode())
            sleep(1)

    def run(self):
        proc1 = Process(target=self.func1)
        proc1.start()
        proc2 = Process(target=self.func2)
        proc2.start()

if __name__ == '__main__':
    b = DNO()
    b.run()











