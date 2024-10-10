#=============================================== ERRORES Y EXCEPCIONES ===============================================================

x = 5
y = "2"


# Intentamos sumar un entero con una cadena lo que genera un TypeError
result = x + y

try:
  result = x + y
  print(f"el valor de x:{x}, el valor de y:{y}")
except TypeError:
  print("El valor de los sumandos deben ser numericos")

# try except anidados
try:
  print("Ingrese los valores a dividir")
  num1 = int (input("ingrese el primer valor = "))
  num2 = int (input("ingrese el segundo valor = "))
  resultado = num1 / num2
except ZeroDivisionError:
  print("El valor de los dividendos deben ser mayor a cero")

# try except anidados

try:
	# Bloque Externo
    
    try:
		# Bloque Interno
        numero1 = int(input("Digite el primer número: "))
        numero2 = int(input("Digite el segundo número: "))
        resultado = numero1 / numero2
        print("El resultado de la division es:", resultado)
    except ValueError:
        print("Algun número tiene valor incorrecto")
    except ZeroDivisionError:
         print("No se puede dividir por cero")
except Exception as e:
     print(e)
#====================== El bloque else =======================
try:
    numero1 = int(input("Digite el primer número: "))
    numero2 = int(input("Digite el segundo número: "))
    resultado = numero1 / numero2
except ValueError:
    print("Algun número tiene valor incorrecto")
except ZeroDivisionError:
        print("No se puede dividir por cero")
else:
     print("El resultado de la division es:", resultado)

#====================== el bloque finally =======================

try:
 
 file = open("archivoFinaly.txt", "r")
	# Código que puede generar una excepción
except FileNotFoundError:
	# Manejo de la excepción
  print("No se enctro el archivo")

finally: 
	# Código que se ejecuta si no se genera ninguna excepcion
    if file:
        file.close()