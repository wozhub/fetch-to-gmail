#!/usr/bin/python

# Para ocultar el password, que no se vea a simple vista
# Nota: Sigue siendo inseguro dejar el password en un script!

usuario = "usuario"  # Editar segun corresponda
passwd = ""  # Correr este script y completar este campo

if __name__ == "__main__":
    from base64 import b64encode
    passwd = raw_input("Ingrese clave para convertir a base64: ")
    print "Su clave en base64 es: '%s'" % b64encode(passwd)
