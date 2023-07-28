import base64

mensaje_codificado = "VGUgZmVsaWNpdG8sIHN1cGVyYXN0ZSBlc3RhIHBydWViYS4gVGUgcGlkbyBxdWUgdG9tZXMgY2FwdHVyYSBkZSBwYW50YWxsYSBkZSBlc3RvIGp1bnRvIGNvbiBsYSBmZWNoYSB5IGhvcmEgeSBub3MgZW52w61lcyBlc3RhIGNhcHR1cmEgZW4gdW4gZW1haWwganVudG8gY29uIGVsIHJlc3RvIGRlIGxvcyBkZXNhZsOtb3MuIFBvciBmYXZvciBleHBsaWNhbm9zIGVuIGVsIG1haWwgY29tbyByZXNvbHZpc3RlIGVsIGFjZXJ0aWpvLg=="

try:
  mensaje_decodificado=base64.b64decode(mensaje_codificado).decode('utf-8') #Intenta decodificar el mensaje si está en formato base64  
  print(mensaje_decodificado)
except:
  print("Lo siento, no pude descifrar el mensaje porque está codificado en un formato diferente") #Si no está en formato base64 manda este mensaje





