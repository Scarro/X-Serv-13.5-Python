"""
Script que introduce en un diccionario
los usuarios y su shell, tomados del archivo /etc/passwd
"""
#!/usr/bin/python

fichero = open('/etc/passwd','r')
lectura = fichero.readlines()
fichero.close()

diccionario = {}

for linea in lectura:
	shell = linea.split(":")[-1]
	usuario = linea.split(":")[0]
	diccionario[usuario] = shell

print "root: " + diccionario['root']

try:
	print "imaginario: " + diccionario['imaginario']
except:
	print "No existe ese usuario."

