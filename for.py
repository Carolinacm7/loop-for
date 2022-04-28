# range(10) 0,1,2,3,4,5,6,7,8,9
# range (2,10)  2,3,4,5,6,7,8,9
# range(2,12,2) 2,4,6,8,10

mostrar = ""
for r1 in range(10):
    mostrar = mostrar + str(r1) + ","
print("range(10) -> ",mostrar)

mostrar = ""
for r2 in range(2,10):
    mostrar = mostrar + str(r2) + ","
print("range(2,10) -> ",mostrar)

mostrar = ""
for r3 in range(2,12,2):
    mostrar = mostrar + str(r3) + ","
print("range(2,12,2) -> ",mostrar)

mostrar = ""
for r4 in range(12,1,-2):
    mostrar = mostrar + str(r4) + ","
print("range(12,1,-2) ->",mostrar)
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
word = input("Introduce una palabra: ")
for i in range(10):
print(word)
#parametro end de tipo string como va a terminar no funciona como concatenar 
#print ("hola", end = ",")

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
""" 
invertir, interes , anios = int(input ("digite cantidad a invertir")), float(input("interes")),int(input("anios"))""" 
capitalInicial = invertir
for periodo in range (1,anios+1):
    capital = invertir 
    invertir = invertir*(1+(interes/100))
    print(interes/100)
    print (f"has invertido {round(capital,0)} y has obtenido {round(invertir,0)} en el año {periodo}.")
    print ("invertiste:", capitalInicial,"y obtuviste un total de ",invertir,"para una ganacia neta de",(capitalInicial+invertir)) """ """

  #  Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#     num=int(input("ingrese un numero entero"))
#     triangulo=""
#     for linea in range(num):
#     triangulo = triangulo + "*"
#     print(triangulo)
#     n=int(input("ingrese un numero positivo"))+1

# for i in range(1,n):
#     print("*"*i)
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#  pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = "contraseña"
bandera= True
while bandera:
    clave =input("ingrese contraseña: ")
    if clave == password:
        bandera=False
        print("bienvenido")
    else:
        print("contraseña errada empiece de nuevo ")
    