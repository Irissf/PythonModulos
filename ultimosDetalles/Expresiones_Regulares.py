import re

cadena = "Vamos a aprender expresiones regulares"

#buscar una palabra en un texto, devuelve un objeto, o none si no encuentra la palabra
busquedaPalabra = re.search("aprender", cadena)
print("caracter inicio: "+str(busquedaPalabra.start())+" y el caracter final: "+str(busquedaPalabra.end()))

if re.search("aprender", cadena) is not None:
    print("El texto a buscar ha sido encontrado")
else:
    print("El texto a buscar no ha sido encontrado")

cadenaVeces = "python, ¿cuántas veces se encuentra una palabra en el texto?-> python"
#añadimos len para el núm de veces
print(len(re.findall("python", cadenaVeces)))

#METACACTERES, anclas y clases de caracteres
lista_Nombres=['Ana Góñez',
                'Maria Martín',
                'Sandra Santiago',
                'Santiago Martín']

print("Empieza con San")
for elemento in lista_Nombres:
    #todos tienen San, con '^' tiene en cuenta la mayuscula
    if re.findall('^San',elemento):
        print(elemento)

print("\nAcaba con tín")
for elemento in lista_Nombres:
    #todos los nombres que acaban por tín, con '$'
    if re.findall('tín$',elemento):
        print(elemento)

print("\ncontiene el caracter")
for elemento in lista_Nombres:
    #todos los nombres que contienen ñ, con '[]'
    if re.findall('[ñ]',elemento):
        print(elemento)

lista_palabras=['hombres',
                'mujeres',
                'niños',
                'niñas']

print("\ncontiene el caracter")
for elemento in lista_palabras:
    #lista de los niños y niñas, entre [] los caracteres que puede tener
    if re.findall('niñ[oa]s',elemento):
        print(elemento)

print("\n contiene una letra entre la o y la p")
for elemento in lista_palabras:
    #todos los nombres con letras entre la o y la t
    if re.findall('[o-t]', elemento):
        print(elemento)
        