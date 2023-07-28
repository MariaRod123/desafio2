import base64

mensaje_codificado = "VGUgZmVsaWNpdG8sIHN1cGVyYXN0ZSBlc3RhIHBydWViYS4gVGUgcGlkbyBxdWUgdG9tZXMgY2FwdHVyYSBkZSBwYW50YWxsYSBkZSBlc3RvIGp1bnRvIGNvbiBsYSBmZWNoYSB5IGhvcmEgeSBub3MgZW52w61lcyBlc3RhIGNhcHR1cmEgZW4gdW4gZW1haWwganVudG8gY29uIGVsIHJlc3RvIGRlIGxvcyBkZXNhZsOtb3MuIFBvciBmYXZvciBleHBsaWNhbm9zIGVuIGVsIG1haWwgY29tbyByZXNvbHZpc3RlIGVsIGFjZXJ0aWpvLg=="
verificador_formato= base64.b64decode(mensaje_codificado, validate=True) #Comprueba si mi string está codificado en base64

if verificador_formato:
  mensaje_decodificado=base64.b64decode(mensaje_codificado).decode('utf-8') #Decodifica el mensaje utilizando los método b64decode() y decode()  
  print(mensaje_decodificado)
else:
  print("Lo siento, no pude descifrar el mensaje porque está codificado en un formato diferente")





