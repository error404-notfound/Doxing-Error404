import os, webbrowser,sys
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Mexico():
	limpiar()
	print '''
 {0}Aqui podras obtener datos de Mexico 
  {3}1.{1}{2}  Usersherlock
  {3}2.{1}{2}  Usersearch
  {3}3.{1}{2}  Namechk
  {3}4.{1}{2}  linkedin
  {3}5.{1}{2}  Pipl
  {3}6.{1}{2}  GoogleProfile
  {3}7.{1}{2}  Twitter
  {3}8.{1}{2}  Facebook
  {3}9.{1}{2}  Instagram
  {3}10.{1}{2} Buholegal
  {3}11.{1}{2} Registro de Profesionistas
  {3}12.{1}{2} Salir
	'''.format(GREEN, END, CYAN, RED)
	m = raw_input('\033[1;32m DOXING ERROR404 > \033[0m')
	if m == "1":
		webbrowser.open('http://usersherlock.com')
        if m == "2":
		webbrowser.open('https://usersearch.org/')
	if m == "3":
 		webbrowser.open('http://namechk.com/')
	if m == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if m == "5":
 		webbrowser.open('https://pipl.com/')
	if m == "6":
 		webbrowser.open('https://profiles.google.com/')
	if m == "7":
	    	webbrowser.open('https://twitter.com/')
	if m == "8":
   		webbrowser.open('http://www.facebook.com/')
	if m == "9":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
	if m == "10":
    		webbrowser.open('https://www.buholegal.com/consultasep/')
	if m == "11":
    		webbrowser.open('https://www.cedulaprofesional.sep.gob.mx/cedula/presidencia/indexAvanzada.action')
	if m == "12":
                limpiar()
		sys.exit()
while True:
	Mexico()
