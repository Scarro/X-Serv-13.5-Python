"""
Script que introduce en un diccionario
los usuarios y su shell, tomados del archivo /etc/passwd
"""
#!/usr/bin/python


fichero = open('/etc/passwd','r')
lectura = fichero.readlines();
fichero.close()
diccionario = {}                        ## Diccionario vacio

for linea in lectura
    shell = linea.split(":")[-1]
    usuario = linea.split(":")[0]
    dicc[usuario] = shell
    print "Usuario: " + usuario + ", Shell: " + dicc[usuario]

print "Hay " + str(len(dicc)) + " usuarios"
