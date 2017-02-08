from struct import *

packed_data = pack('iif',1,2,3.9)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))

original_data = unpack('iif',packed_data)
print(original_data)