import time as T
import os as O
e=T.localtime()
d='DebagLog(%s_%02d_%02d-%02d.%02d.%02d)'%(e[0], e[1] ,e[2], e[3], e[4], e[5])
e='ErrorLog(%s_%02d_%02d-%02d.%02d.%02d)'%(e[0], e[1] ,e[2], e[3], e[4], e[5])
print(e, d)
O.system('cmdow @ /hid')
O.system(".\\Monitor3.pyw 2>.\\CosechkI\\%s.txt 1>.\\CosechkI\\%s.txt"%(e, d))
#input()