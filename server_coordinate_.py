import socket
import time
from multiprocessing import Process
import usb.core
import usb.util


VENDOR_ID = 0xA720
PRODUCT_ID = 0xF803

dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
dev.set_configuration()
dev.set_interface_altsetting(interface=0, alternate_setting=0)
dev.write(0x01, [3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 15, 99, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 2, 0, 5, 0, 0, 0, 0, 0], 10)
dev.write(0x01, [2, 10, 0, 36, 1, 0, 0, 0, 0], 10)
dev.write(0x01, [3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], 10)


sock = socket.socket()
sock.bind(('', 6060))
sock.listen(10)
conn, addr = sock.accept()

while True:                 #for i in range(count):
    r = str(dev.read(0x81, 49, 64))
    print(r)


def client_sock_processing():
    while True:
        data = (conn.recv(254).decode()).split('*')
        print(data)
        if not data:
            break
        conn.send('server ECHOE'.encode() + r.encode())

def get_list_cor(self):
    cor_list = (((r.encode()).decode())[1:-1]).split(', ')
    x_cor = [cor_list[10], cor_list[11], cor_list[12], cor_list[13]]
    y_cor = [cor_list[18], cor_list[19], cor_list[20], cor_list[21]]
    z_cor = [cor_list[26], cor_list[27], cor_list[28], cor_list[29]]
    a_cor = [cor_list[34], cor_list[35], cor_list[36], cor_list[37]]
    print(x_cor, y_cor, z_cor, a_cor,)

def send_board_runner(self, mes, count: int):
    for i in range(count):
        self.dev.write(0x1, mes, 10)


mes = ([3, 5, 0, 2, 0, 0, 0, 0, 0, 100, 0, 0, 0, 50, 0, 0, 0, 25, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0], 1)
if __name__ == '__main__':
    p2 = Process(target=start_read_cor)
    p2.start()
    p1 = Process(target=client_sock_processing)
    p1.start()


sock = socket.socket()
sock.bind(('', 6060))
sock.listen(10)


def client_sock_processing(self):  # шлет на клиента преобразованый пакет координат полученный от клиента
    conn, addr = self.sock.accept()
    while True:
        data = (conn.recv(254).decode()).split('*')
        if data[0] == '0.0000':
            print(data)
        if not data:
            break
        conn.send('server ECHOE'.encode() + self.r.encode())
        
usb_board_reader_thread = threading.Thread(target=board.start_read_cor(), daemon=True)
usb_board_reader_thread.start()
board_open_client_stream = threading.Thread(target=board.client_sock_processing(), daemon=True)
board_open_client_stream.start()
