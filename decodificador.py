import base64

mensaje_codificado = input("Ingrese el código a descifrar: ")

try:
  mensaje_decodificado=base64.b64decode(mensaje_codificado).decode('utf-8') #Intenta decodificar el mensaje si está en formato base64  
  print(mensaje_decodificado)
except:
  print("Lo siento, no pude descifrar el mensaje porque está codificado en un formato diferente") #Si no está en formato base64 manda este mensaje





