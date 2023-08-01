import base64
import binascii

mensaje_codificado = input("Ingrese el código a descifrar: ")

try:
  mensaje_decodificado=base64.b64decode(mensaje_codificado).decode('utf-8') #Intenta decodificar el mensaje si está en formato base64  
  print(mensaje_decodificado)
except binascii.Error:
  print("Lo siento, no pude descifrar el mensaje") #Si no está en formato base64 imprime este mensaje





