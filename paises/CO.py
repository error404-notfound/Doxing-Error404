import os, webbrowser,sys
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Colombia():
	limpiar()
	print '''
 {0}Aqui podras obtener datos de Colombia 
  {3}1.{1}{2}  Usersherlock
  {3}2.{1}{2}  Usersearch
  {3}3.{1}{2}  Namechk
  {3}4.{1}{2}  linkedin
  {3}5.{1}{2}  Pipl
  {3}6.{1}{2}  GoogleProfile
  {3}7.{1}{2}  Twitter
  {3}8.{1}{2}  Facebook
  {3}9.{1}{2}  Instagram
  {3}10.{1}{2} EPS
  {3}11.{1}{2} Libreta militar
  {3}12.{1}{2} Comparendos
  {3}13.{1}{2} Antecedentes
  {3}14.{1}{2} RUNT
  {3}15.{1}{2} Sisben
  {3}16.{1}{2} Salir
	'''.format(GREEN, END, CYAN, RED)
	k = raw_input('\033[1;32m COLOMBIA ERROR404 > \033[0m')
	if k == "1":
		webbrowser.open('http://usersherlock.com')
        if k == "2":
		webbrowser.open('https://usersearch.org/')
	if k == "3":
 		webbrowser.open('http://namechk.com/')
	if k == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if k == "5":
 		webbrowser.open('https://pipl.com/')
	if k == "6":
 		webbrowser.open('https://profiles.google.com/')
	if k == "7":
	    	webbrowser.open('https://twitter.com/')
	if k == "8":
   		webbrowser.open('http://www.facebook.com/')
	if k == "9":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
	if k == "10":
    		webbrowser.open('http://www.fosyga.in/fosyga/')
	if k == "11":
    		webbrowser.open('https://www.libretamilitar.mil.co/modules/consult/militarysituation')
	if k == "12":
   		webbrowser.open('https://www.simbogota.com.co/index.php?option=com_content&view=article&id=419&Itemid=376')
	if k == "13":
		webbrowser.open('https://antecedentes.policia.gov.co:7005/WebJudicial/formAntecedentes.xhtml')
	if k == "14":
  		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
	if k == "15":
		 webbrowser.open('http://www.sisben.gov.co/atencion-al-ciudadano/Paginas/consulta-del-puntaje.aspx')
	if k == "16":
                limpiar()
		sys.exit()
while True:
	Colombia()
