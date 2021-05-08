import usb.core
import usb.util

#HidUsb (v10.0.19041.1)

VENDOR_ID = 0xA720
PRODUCT_ID = 0xF803
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
dev.set_configuration()
dev.set_interface_altsetting(interface=0, alternate_setting=0)
#print(dir(dev))
#print(dev)


def read_port():
    count = 1
    tm = 1
    while count != 0:
        try:
            r = dev.read(0x81, 49, 64)
            print(len(r), r)
            count -= 1

        except usb.core.USBTimeoutError:
            print('Error')
            print(tm)

def write_port(f):

    wrt = dev.write(0x1, f, 10)
    print(wrt)


write_port([3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 15, 99, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0])
write_port([2, 2, 0, 5, 0, 0, 0, 0, 0])
write_port([2, 10, 0, 36, 1, 0, 0, 0, 0])
write_port([3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0])
#write_port('000000')
#write_port('0000A')
#write_port('000000')



count = 10
while count != 1:
    mes = [3, 5, 0, 2, 0, 0, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0]
    print(len(mes))
    write_port(mes)
    count -= 1
read_port()
