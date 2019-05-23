import os, webbrowser,sys
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Argentina():
	limpiar()
	print '''
 {0}Aqui podras obtener datos de Argentina 
  {3}1.{1}{2}  Usersherlock
  {3}2.{1}{2}  Usersearch
  {3}3.{1}{2}  Namechk
  {3}4.{1}{2}  linkedin
  {3}5.{1}{2}  Pipl
  {3}6.{1}{2}  GoogleProfile
  {3}7.{1}{2}  Twitter
  {3}8.{1}{2}  Facebook
  {3}9.{1}{2}  Instagram
  {3}10.{1}{2} Consulta Numero o Chip
  {3}11.{1}{2} Buscar mediante telefono
  {3}12.{1}{2} Buscar cualquier persona
  {3}13.{1}{2} Buscar Nombre y Apellido en Patron
  {3}14.{1}{2} Guias Telefonicas
  {3}15.{1}{2} Buscar DNI en el Patron
  {3}16.{1}{2} Buscar Direccion en el Patron
  {3}17.{1}{2} Buscar Lineas Telefonicas
  {3}18.{1}{2} Buscar Telefonos en el Patron
  {3}19.{1}{2} Buscar Historico por Telefonico
  {3}20.{1}{2} Salir
	'''.format(GREEN, END, CYAN, RED)
        a = raw_input('\033[1;32m ARGENTINA ERROR404 > \033[0m')
	if a == "1":
                #os.system('firefox http://usersherlock.com > /dev/null 2>&1 &')
		webbrowser.open('http://usersherlock.com') 
        if a == "2":
		webbrowser.open('https://usersearch.org/')
	if a == "3":
 		webbrowser.open('http://namechk.com/')
	if a == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if a == "5":
 		webbrowser.open('https://pipl.com/')
	if a == "6":
 		webbrowser.open('https://profiles.google.com/')
	if a == "7":
	    	webbrowser.open('https://twitter.com/')
	if a == "8":
   		webbrowser.open('http://www.facebook.com/')
        if a == "9":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
	if a == "10":
    		webbrowser.open('https://www.datacels.com/mobile/detectar-empresa.php')
        if a == "11":
    		webbrowser.open('http://www.webdedatos.com/ZIPs/telefonos/')
        if a == "12":
    		webbrowser.open('http://buscardatos.com/Empresas')
        if a == "13":
    		webbrowser.open('http://www.buscardatos.com/Personas/Apellido/')
        if a == "14":
    		webbrowser.open('http://www.webdedatos.com/ZIPs/telefonos/?start=1')
        if a == "15":
    		webbrowser.open('http://www.buscardatos.com/Personas/DNI/')
        if a == "16":
    		webbrowser.open('http://www.buscardatos.com/Personas/Direccion/')
        if a == "17":
    		webbrowser.open('http://www.webdedatos.com/ZIPs/telefonos/?start=2')
        if a == "18":
    		webbrowser.open('http://www.webdedatos.com/ZIPs/telefonos/?start=0')
        if a == "19":
    		webbrowser.open('http://www.webdedatos.com/Personas/DHT/')
	if a == "20":
                limpiar()
		sys.exit()
while True:
	Argentina()
