
import array
import binascii

a = array.array('i',[1,2,3,4,5,6])
bytes_array = a.tobytes()
print(binascii.hexlify(bytes_array))






