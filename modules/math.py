a = 3//2;
b = 3/2;
c = 3 ** 2;

# eponent begin from right side
d = 2 ** 3 ** 2;

# binary
e = 0b0000 + 0b1;
#octal
f = 0o10 + 0o10;
#hex
g = 0x10 + 0x10;

print(a);
print(b);
print(c);
print(d);
print(e);
print(f);
print(g);

# predifend function
print(abs(-3))
print(float(3))
print(float(3.2))
print(float(3.2e10))
# error: print(float('no es un numero'))
print(int(3.2))
print(str(3.2))
print(bin(3))
print(oct(3))
print(hex(3))
print(round(3.1))
print(round(2.1415, 2)) #2.15 - the second param is for the decimals

# string values
print(ord('a'))
print(ord('A'))
# python3 unicode : print(ord('á'))

from math import sin, cos
from math import *

import math
print(math.sin(0))
