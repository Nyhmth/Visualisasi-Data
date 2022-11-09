import matplotlib.pyplot as plt
from math import sin
from math import pi
from math import cos

a=[]
b=[]

t = 0.1
v = 1.4*10**-3
#s= v*t
s=t*v
sdt = (s/180)*pi
n = sin(sdt)
g = 9.8
# x = v^2sin2a /g

jarak = (v**2)* sin(2*n)/g
print("jawab : ")
print("jarak = ", jarak,"m")

#menghitung jarak vertikal (y)
o = n**2
puncak = (v**2)*o/(2*g)
print("ketinggian = ", puncak , "m")

for x in range(-10,10,1):
    y=x**2+2*x+2
    a.append(x)
    b.append(y)
    #x= x+1

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()