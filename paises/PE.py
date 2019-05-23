import os, webbrowser,sys
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def Peru():
	limpiar()
	print '''
 {0}Aqui podras obtener datos de Peru 
  {3}1.{1}{2}  Usersherlock
  {3}2.{1}{2}  Usersearch
  {3}3.{1}{2}  Namechk
  {3}4.{1}{2}  linkedin
  {3}5.{1}{2}  Pipl
  {3}6.{1}{2}  GoogleProfile
  {3}7.{1}{2}  Twitter
  {3}8.{1}{2}  Facebook
  {3}9.{1}{2}  Instagram
  {3}10.{1}{2} Informacion de Padron Electoral
  {3}11.{1}{2} SIS Datos de filiacion
  {3}12.{1}{2} Operadora Movil
  {3}13.{1}{2} Multas Electorales
  {3}14.{1}{2} Informacion Vehicular
  {3}15.{1}{2} Informacion Vehiular II
  {3}16.{1}{2} Constas informacionde RUC
  {3}17.{1}{2} Administracion Tributaria SAT
  {3}18.{1}{2} Sistemas de Licencia de Conducir SCLP
  {3}19.{1}{2} Migraciones 
  {3}20.{1}{2} Salir
	'''.format(GREEN, END, CYAN, RED)
	p = raw_input('\033[1;32m PERU ERROR404 > \033[0m')
	if p == "1":
		webbrowser.open('http://usersherlock.com')
        if p == "2":
		webbrowser.open('https://usersearch.org/')
	if p == "3":
 		webbrowser.open('http://namechk.com/')
	if p == "4":
 		webbrowser.open('http://www.linkedin.com/')
	if p == "5":
 		webbrowser.open('https://pipl.com/')
	if p == "6":
 		webbrowser.open('https://profiles.google.com/')
	if p == "7":
	    	webbrowser.open('https://twitter.com/')
	if p == "8":
   		webbrowser.open('http://www.facebook.com/')
	if p == "9":
    		webbrowser.open('https://www.instagram.com/instagram/?hl=es-la')
        if p == "10":
   		webbrowser.open('http://www.midis.gob.pe/padron/')
        if p == "11":
   		webbrowser.open('http://afiliacion.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx')
        if p == "12":
   		webbrowser.open('https://www.deperu.com/celulares/')
        if p == "13":
   		webbrowser.open('https://multas.jne.gob.pe/')
        if p == "14":
   		webbrowser.open('http://www.pit.gob.pe/pit2007/EstadoCuenta.aspx')
        if p == "15":
   		webbrowser.open('https://www.sunarp.gob.pe/ConsultaVehicular/')
        if p == "16":
   		webbrowser.open('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias')
        if p == "17":
   		webbrowser.open('https://www.sat.gob.pe/Websitev9')
        if p == "18":
   		webbrowser.open('https://slcp.mtc.gob.pe/')
        if p == "19":
   		webbrowser.open('https://sel.migraciones.gob.pe/servmig-valreg/VerificarCE')
	if p == "20":
                limpiar()
		sys.exit()
while True:
	Peru()
