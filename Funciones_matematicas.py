def sumar(op1,op2):
    print("El resultado de la suma: ", op1+op2)

def restar(op1,op2):
    print("El resultado de la resta: ", op1-op2)

def multiplicar(op1,op2):
    print("El resultado de la multiplicación: ", op1*op2)

def dividir(op1,op2):
    if (op2 > 0):
        print("El resultado de la división: ", op1/op2)
        print("El resto es: ", op1%op2)
    else:
        print("Divisor debe ser mayor de 0")

    