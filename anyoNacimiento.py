anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

import datetime
anio_actual = datetime.datetime.now().year

edad = anio_actual - anio_nacimiento

print("Tienes", edad, "años.")