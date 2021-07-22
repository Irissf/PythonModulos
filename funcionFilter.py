#aplica una condición a cada elemento de una lista iterable
#devolviendo una lista con los resultados

#una función para ver si el número es par
def numero_par(num):
    if num % 2 == 0:
        return True

#creamos una lista de números
numeros = [1,3,4,65,74,33,43,52]

#imprimimos los pares, filter nos devuelve un objeto que transformamos en lista
print(list(filter(numero_par,numeros)))

#podemos hacerlo mediante lambdas también
print(list(filter(lambda num_par: num_par%2==0,numeros)))

#Se suele usar filter para filtrar objetos
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self) -> str:
        return "{}, tiene un salario de {} en el cargo de {}".format(self.nombre, self.salario, self.cargo)

listaEmpleados = [
    Empleado("Juan", "director", 30000),
    Empleado("Ana", "presidenta", 50000),
    Empleado("Raúl", "prog", 21000),
    Empleado("Marta", "prog", 22300),
    Empleado("Hugo", "prog", 23300)
]

salarios_bajos = filter(lambda empleado:empleado.salario<30000, listaEmpleados)
for empleado_salario in salarios_bajos:
   print(empleado_salario) 