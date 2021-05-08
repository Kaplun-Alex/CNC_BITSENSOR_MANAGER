import struct
s = '03 05 00 BF 00 00 00 00 00 00 00 00 00 10 FFFFF FF FF 00 00 00 00 00 00 00 00 00 00'

for i in s.split():
    #print(i)
    print(i, int(i, base=16), chr(int(i, base=16)))

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

print(tohex(-1, 32))
print(tohex(1, 32))

def twos_complement(hexstr,bits):
    value = int(hexstr, 32)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

print(twos_complement('FFFFFFFF', 32))

h = 'FFFFFFFF'
print(struct.unpack('>i', bytes.fromhex(h)))
h = 'FFFFFFFE'
print(struct.unpack('>i', bytes.fromhex(h)))