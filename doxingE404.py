# -*- coding: utf-8 -*-
import sys, os, webbrowser, platform
from time import sleep
from sys import stdout, exit
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
##Def funciones
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def logo():
      print '''        
       {0}    ``      {2}D O X I N G{0}      ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-          
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/          
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+          
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+          
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/          
          `dMm/::hmNMMNMMMMMMNmho-../hm`          
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `         
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-     
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+` 
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-  
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds     
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.      
       .mMMMdy/.   {2}ERROR 404{1}{0}   `-ohNMMMs`       
       `+y+.           ```           `-sy:                             
       {3}Dedicado para el grupo de Error404 
  Este script esta hecho con fines eduacativos{2} '''.format(GREEN, END, CYAN, RED)

logo()
sleep(0.7)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(1.5)
for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{3}*{0}]{2} Preparando el Script... %d%%".format(GREEN, END, CYAN, RED, WHITE) % i)
        stdout.flush()
limpiar()

def menuc():
    print '''
{3}*{1}{0} Este Script esta hecho con la Colaboracion de Varios Programadores
                Esperamos que les sea util{1} {3}Error404{0}'''.format(GREEN, END, CYAN, RED, WHITE)

def menu():
    print '''
      {3}1.{1} {2} Argentina
      {3}2.{1} {2} Bolivia						
      {3}3.{1} {2} Chile						
      {3}4.{1} {2} Colombia						
      {3}5.{1} {2} Ecuador						
      {3}6.{1} {2} Mexico						
      {3}7.{1} {2} Peru								
      {3}8.{1} {2} Facebook Error404	
      {3}9.{1} {2} Youtube Error404
      {3}10.{1}{2} Twitter Error404
      {3}11.{1}{2} Instagram Error404					
      {3}12.{1}{2} Salir						
				'''.format(GREEN, END, CYAN, RED)
limpiar()
menuc()
menu()
d = raw_input('\033[1;32m DOXING ERROR404 > \033[0m')

if d == "1":
	execfile("paises/AR.py")
elif d == "2":
	execfile("paises/BO.py")
elif d == "3":
	execfile("paises/CH.py")
elif d == "4":
	execfile("paises/CO.py")
elif d == "5":
	execfile("paises/EC.py")
elif d == "6":
	execfile("paises/ME.py")
elif d == "7":
	execfile("paises/PE.py")	
elif d == "8":
	webbrowser.open('https://www.facebook.com/error4o4.org')
elif d == "9":
	webbrowser.open('https://www.youtube.com/channel/UC9ZtujTcMuBcKsV4-4G9Zxg')  
elif d == "10":
	webbrowser.open('https://twitter.com/Error404origen')
elif d == "11":
	webbrowser.open('https://www.instagram.com/error404origen/?hl=de ')  
elif d == "12":
        limpiar()
	sys.exit()
