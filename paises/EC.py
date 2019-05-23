# -*- coding: utf-8 -*-
import sys,webbrowser,os
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Ecuador():
	limpiar()
    	print '''
 {0}Aqui podras obtener datos de Ecuador
  {3}1.{1}{2}  Datos de Interes
  {3}2.{1}{2}  Gestion Fiscalias
  {3}3.{1}{2}  Paginas Amarillas
  {3}4.{1}{2}  SRI
  {3}5.{1}{2}  Usersherlock
  {3}6.{1}{2}  Usersearch
  {3}7.{1}{2}  Namechk
  {3}8.{1}{2}  linkedin
  {3}9.{1}{2}  Pipl
  {3}10.{1}{2} GoogleProfile
  {3}11.{1}{2} Twitter
  {3}12.{1}{2} Facebook
  {3}13.{1}{2} Instagram
  {3}14.{1}{2} Salir
    '''.format(GREEN, END, CYAN, RED)
	d = raw_input("\033[1;32m ECUADOR ERROR404 > ") 
	if d == "1":
    		print ('\033[1;33m Llena el campo para obtener la informacion')
    		ID=raw_input('\033[1;32m Ingrese su Cedula: \033[0m')
    		num = "http://si.secap.gob.ec/sisecap/servicioObtieneDatosRegistroCivil.php?num_doc="
    		ID=str(ID)
     		if len(ID) != 10:
			print ('La cedula debe tener 10 digitos')
			wait = raw_input("PRESIONA ENTER PARA CONTINUAR.")
     		else: 
        		print ('Estamos buscando la info requerida')
			output=os.system('curl '+num+ID)
    	   		print ('')
        		print ('')
			print ('Busqueda Finalizada')
			print ('')
			wait = raw_input("PRESIONA ENTER PARA CONTINUAR.")
        if d == "2":
              webbrowser.open('https://www.gestiondefiscalias.gob.ec/siaf/informacion/web/noticiasdelito/index.php')
        if d == "3":
              webbrowser.open('https://www.edina.com.ec/guia-telefonica/guia_telefonica_blancas.html')
        if d == "4":
              webbrowser.open('https://www.edina.com.ec/guia-telefonica/guia_telefonica_blancas.html')
        if d == "5":
		webbrowser.open('http://usersherlock.com')
        if d == "6":
		webbrowser.open('https://usersearch.org/')
	if d == "7":
 		webbrowser.open('http://namechk.com/')
	if d == "8":
 		webbrowser.open('http://www.linkedin.com/')
	if d == "9":
 		webbrowser.open('https://pipl.com/')
	if d == "10":
 		webbrowser.open('https://profiles.google.com/')
	if d == "11":
	    	webbrowser.open('https://twitter.com/')
	if d == "12":
   		webbrowser.open('http://www.facebook.com/')
	if d == "13":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
        if d == "14":  
             sys.exit()     
while True:
	Ecuador()
