import base64

mensaje = "VGUgZmVsaWNpdG8sIHN1cGVyYXN0ZSBlc3RhIHBydWViYS4gVGUgcGlkbyBxdWUgdG9tZXMgY2FwdHVyYSBkZSBwYW50YWxsYSBkZSBlc3RvIGp1bnRvIGNvbiBsYSBmZWNoYSB5IGhvcmEgeSBub3MgZW52w61lcyBlc3RhIGNhcHR1cmEgZW4gdW4gZW1haWwganVudG8gY29uIGVsIHJlc3RvIGRlIGxvcyBkZXNhZsOtb3MuIFBvciBmYXZvciBleHBsaWNhbm9zIGVuIGVsIG1haWwgY29tbyByZXNvbHZpc3RlIGVsIGFjZXJ0aWpvLg== "
print(base64.b64decode(mensaje).decode('utf-8'))





