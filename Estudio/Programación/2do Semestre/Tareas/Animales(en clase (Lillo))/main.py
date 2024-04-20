from canguro import Canguro
from delfin import Delfin

x = 0
c = Canguro()
c.nombre = "Tayson"
c.edad = 5

d = Delfin()
d.nombre = "Neptuno"
d.edad = 4

print(f"Canguro: {c.nombre}, Edad: {c.edad}")
print(f"Delfín: {d.nombre}, Edad: {d.edad}")

c1 = Canguro()
c2 = Canguro()
c3 = Canguro()

print(f"Edad canguro 1: {c1.edad}")
print(f"Edad canguro 2: {c2.edad}")
print(f"Edad canguro 3: {c3.edad}")