#aplica una función a cada elemento de una lista iterable
#devolviendo una lista con los resultados

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self) -> str:
        return "{}, tiene un salario de {} en el cargo de {}".format(self.nombre, self.salario, self.cargo)

listaEmpleados = [
    Empleado("Juan", "director", 3000),
    Empleado("Ana", "presidenta", 4500),
    Empleado("Raúl", "prog", 1900),
    Empleado("Marta", "prog", 1900),
    Empleado("Hugo", "prog", 1900)
]

def calculo_comision(empleado):
    if empleado.salario < 3000:
        empleado.salario = empleado.salario * 1.50
    else:    
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleados = map(calculo_comision,listaEmpleados)
for empleado in listaEmpleados:
    print(empleado)
    