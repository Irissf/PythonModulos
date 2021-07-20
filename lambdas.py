#para funciones simples como esta, con una sola instrucción
#lo podemos resumir en una función(expresión)lambda
def area_triangulo(base, altura):
    return (base*altura)/2

#con lambdas lo hariamos de la siguiente manera
area_triangulo_lambda = lambda base,altura:(base*altura)/2

#para la función normal
print("Uso función normal")
print(area_triangulo(2,4))
print(area_triangulo(5,7))
print(area_triangulo(4,6))

#para la lambda
print("Uso de las lambda")
print(area_triangulo_lambda(2,4))
print(area_triangulo_lambda(5,7))
print(area_triangulo_lambda(4,6))

#otros ejemplos de lambdas
al_cubo = lambda numero:numero**3
cubo = al_cubo(3)
print("potencia de 3 = "+str(cubo))

destacar_valor = lambda comision:"¡{}!€".format(comision)
print("comisión empresa: "+destacar_valor(1500))