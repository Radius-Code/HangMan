'''hacer que el programa almacene en una variable la _ self.y la sustituya por self.letras cuando al presionar una letra coincida esta
 con otra de la palabra establecida. Esta palabra se establecerá de manera random a partir de un diccionario de palabras. cuando
 la letra seleccionada no coincida con ninguna de la palabra, la imagen cambiará por la siguiente (hang0, por hang1.. self.y así 
 conforme nos equivoquemos al pulsar una letra) 
 segun la ificultad cambiara el numero de self.letras

 	-el programa sugerirá pistas de self.letras (crear funcion pistas self.y un boton al lado para sugerirla, además de una opcion en la 
 	barra de menu)

hacer modo por tematicas
multijugador: que uno se encargue de poner la palabra

que ponga el numero de intentos que quedan
poner que muestre la palabra completa cuando pierdas
 '''



import random
from random import *
from io import open
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk



diccionario=open("diccionario.txt", "r") #abre el diccionario
lineas=diccionario.readlines()
palabrasdic=list(map(str.strip, lineas))


raiz=Tk()
texto=StringVar()
texto.set("Inicia una Nueva Partida")

		


imagenes=[]
misImagenes=[]


global pulsacion

letra = ""

def teclaPulsada(event):
	
	global letra

	letra = event.char

	print("Has pulsado " + letra.upper())

	ahorcado.in_game()
	
		#print(letra)
	
			#------función de pulsar-----
pulsacion = raiz.bind("<Key>", teclaPulsada) #excluir teclas que no sean self.letras #falla en esto

#----------logica---------



class hangman():

	def __init__(self):

		self.palabra = ""
		self.palabraIncompleta = ""
		self.palabra_con_tildes = ""
		self.letrasAdivinadas = []
		self.letrasincorrectas = []
		self.foto = 0
		self.endgame = False
		self.partidaAnterior = False
		self.puntuacion = 0
		self.winlose = False
		self.inicio = True
		self.x = 0
		self.y = 0
		self.longitud_previa = False #inicia la siguiente partida con la misma longitud de palabra si está en True



	def configuracion(self):


		ventana=Toplevel()
		ventana.grid()

		etiqueta=Label(ventana, text="Dificultad")
		etiqueta.grid(row=0, column=0, padx=10, pady=10)


		opciones=["Fácil", "Media", "Difícil"] # hacer que cuando se elija de 3 a 5 sea facil, de 3 a 7 media self.y de 7 a 14 dificil

		variable=StringVar(ventana)
		variable.set("")
		opcion=OptionMenu(ventana, variable, *opciones) #crea el menu desplegable
		opcion.config(width=10)
		opcion.grid(row=1, column=0, padx=10, pady=10)

		
		def boton(): #al pulsarlo, elige una palabra de longitud (* letras) aleatoriamente

			global elegirpalabra

			def elegirpalabra(self):

				global palabrasdic

				if variable.get()==opciones[0]:

					self.x= 2
					self.y = 5
				
					#palabra = lambda palabrasdic, longitud=randint(2,5): choice([i for i in palabrasdic if len(i) == longitud]) #itera en cada elemento de la lista																											#self.y escribe i en una variable si es igual a un numero entero random


				elif variable.get()==opciones[1]:

					self.x= 6
					self.y = 9
					#palabra = lambda palabrasdic, longitud=randint(6,9): choice([i for i in palabrasdic if len(i) == longitud])
				
				elif variable.get()==opciones[2]:

					self.x= 10
					self.y = 20

						#palabra = lambda palabrasdic, longitud=randint(10,20): choice([i for i in palabrasdic if len(i) == longitud])
	
									
				if self.longitud_previa:
					self.x
					self.y

				longitud=randint(self.x, self.y)
				lista_palabras=[]

				for i in palabrasdic:

					if len(i) == longitud:
						lista_palabras.append(i)

					else:

						continue

				print(lista_palabras)

				self.palabra_con_tildes = choice(lista_palabras)
				#self.palabra_con_tildes = "moton"
				print(self.palabra_con_tildes)

				for i in self.palabra_con_tildes:
					if i in 'áéíóúü':
						a,b = 'áéíóúü', 'aeiouu',
						trans = str.maketrans(a,b)
						self.palabra = self.palabra_con_tildes.translate(trans)
					else:
						continue

				print(self.palabra)
				
				if self.palabra == "": # si está vacío, es decir si no se ha cumplido la condición anterior del if rellenando la
										#self.palabra con las de self.palabra_con_tildes
					self.palabra = self.palabra_con_tildes # asigno esto para que se guarde en self.palabra
					print(self.palabra)

						
						

			
						
				#que elija un indice random dentro de uno de los rangos (de 0 a 5, de 6 a 9 self.y de 10 a 14) de la longitud de las palabras
				#self.y lo compare con el indice de la palabra del diccionario self.y devuelva esta palabra

				
					
			#print(texto) #lo imprime correctamente con los guiones
			#miLabel.config(miFrame, textvariable=texto) #da error, se soluciona poniendo .set en la variable global self.y en la de aquí
			ventana.destroy()

			ahorcado.iniciopartida()
			#print(palabra)

		
		botonCrear=Button(ventana, text="Nueva Partida", command=lambda:boton())
		botonCrear.grid(row=2, column=0, padx=10, pady=10)

	
	



	#-----------------------------------------
	#@staticmethod
	def iniciopartida(self):

		global miImagen
		global misImagenes
		global texto


		if (self.inicio or self.partidaAnterior)==True:
			miImagen.config(image=misImagenes[0])
			self.foto=0
			if self.inicio==True:
				self.inicio=False
			elegirpalabra(self)

		
		palabraIncompleta="_ " * len(self.palabra_con_tildes)
		self.palabraIncompleta = palabraIncompleta[:-1]
		texto.set(self.palabraIncompleta)
		print(self.palabraIncompleta)

		#convierte la letra con tilde de la palabra en letra sin tilde y almacena la palabra en otra nueva variable
		#si tiene tildes 
				
		"""for i in self.palabra:
			if i in 'áéíóúü': 
				a,b = 'áéíóúü', 'aeiouu',
				trans = str.maketrans(a,b)
				self.palabra = self.palabra.translate(trans)
			else:
				self.palabra"""

		ahorcado.in_game()
		

	

	#@staticmethod
	def in_game(self):

		global texto
		global letra

		self.intentos=11
		self.palabraAdivinada=False
		#self.palabra = "río"



		print(self.palabra)

		#self.palabra = "toro"

		#print(self.palabra)
		if letra != "":

			"""for i in self.palabra: #para cada letra de la palabra
				if i in 'áéíóúü': # si la letra está en aeiou con tildes
					i.index()
					letra == i"""
				
			"""for f in self.palabra_con_tildes: 
				for s in self.palabra:
				"""

			print(letra)
			indices=[] 
			#[i for i, leter in enumerate(s) if leter == ch]
			for l, letrilla in enumerate(self.palabra):
				if letrilla == letra:
					#if self.palabra.index(l)==self.palabra_con_tildes.index(y):
					indices.append(l) #añade el indice de la letra a indices
				else:
					continue

			print(indices)

			if indices:

				if letra in self.letrasAdivinadas:

					print("Letra ya adivinada, pruebe otra vez")


				if letra not in self.letrasAdivinadas:

					print("Letra adivinada: " + letra)
					
					self.letrasAdivinadas.append(letra)
					print(self.letrasAdivinadas)
					print(self.palabraIncompleta)
					listaOculta=list(self.palabraIncompleta.split(" ")) #hace una lista con cada _ de la palabraIncompleta (palabra con _)
																#self.y quita los espacios
					print(listaOculta) # imprime ____

					"""for i in indices: #mira en los indices de las self.letras adivinadas y almacena la letra adivinada en el indice de la listaOculta
						if 'áéíóúü' in self.palabra_con_tildes:
							for j in self.palabra_con_tildes:
								#print(j)
								if self.palabra_con_tildes.index(j) == i:
									listaOculta[i] == j
						
						#if letra in 'áéíóúü': 
								#a,b = 'áéíóúü', 'aeiouu',
								#trans = str.maketrans(a,b)
								#letra = letra.translate(trans)
						else:"""
					for indice in indices: #itera en la lista de indices para buscar que letra se ha adivinado y la almacena en la lista oculta, sustituyéndola antes por 
										#una tilde
						#print(self.palabra)
						"""for j in self.palabra_con_tildes:
							print(j)
							if i == self.palabra_con_tildes.index(j):
								print(i)
								listaOculta[i] = j
								break
							else:
								continue"""
						
						if letra in self.palabra: #para cada caracter de la palabra
							#for letra2 in self.palabra_con_tildes:
							#letra.replace(self.palabra.index(letra), self.palabra_con_tildes.index(letra)) #PONER ESTO ANTES
							#COGE EL INDICE DE LA LETRA Y LA REEMPLAZA POR LA LETRA DE LA PALABRA CON TILDES
							indice_de_letra = self.palabra.index(letra)
							palabra_con_tildes = self.palabra_con_tildes
							letra = palabra_con_tildes[indice_de_letra]
							#lista_de_palabra = list(self.palabra)
							#lista_de_palabra_con_tildes = list(self.palabra_con_tildes)
							#indice_de_letra = lista_de_palabra.index(letra)
							#lista_de_palabra[indice_de_letra] = lista_de_palabra_con_tildes[indice_de_letra]
							#palabra_con_tilde = ''.join(lista_de_palabra)
							

							listaOculta[indice] = letra #agrega a lista el caracter en su posicion
							
								
						else:
							continue
						
						#yield indice
						
					
						#listaOculta[i]=letra

					print(listaOculta)

					#print(listaOculta)
					self.palabraIncompleta=" ".join(listaOculta) # crea una variable con espacios self.y las self.letras de la listaOculta
					texto.set(self.palabraIncompleta) #cambia el texto por el de esa variable

					if "_" not in self.palabraIncompleta:

						palabraCompleta=self.palabraIncompleta.replace(" ", "")
						print(palabraCompleta)
						
						if palabraCompleta == self.palabra_con_tildes:

							print("¡¡Has ganado!!!")
							print("Tienes " + str(self.puntuacion) + " puntos")
							self.puntuacion+=1
							self.winlose=True
							self.longitud_previa=True
							self.letrasAdivinadas=[]
							self.palabra = ""
							ahorcado.resolucion()


						



			elif not indices:

				print("Letra incorrecta: " + letra)

				if letra not in self.letrasincorrectas:

					self.letrasincorrectas.append(letra)

					for i in range(11):
						self.foto+=1
						miImagen.config(image=misImagenes[self.foto])
						break
					
					if self.foto==11:

						print("¡¡Has perdido!!") #reiniciar la palabra poniendo otra nueva si has perdido self.y reiniciar listas de palabras correctas e incorrectas
						print("Tienes " + str(self.puntuacion) + " puntos")
						self.winlose=False
						self.longitud_previa=True
						self.letrasAdivinadas=[]
						self.palabra = ""
						ahorcado.resolucion()
						

					

				print(self.letrasincorrectas)



			#crear una lista más para los inputs de raiz.bind

				
				

			

			'''for i in indices:
				palabraIncompleta[i]=letra
				texto="".join(palabraIncompleta)

				#texto.set("".join(letra))


				elif letra in palabraIncompleta:
					print("Letra ya adivinada")'''



			

	#@staticmethod
	def resolucion(self):

		global letra
		
		if self.winlose==True:

			valor=messagebox.askquestion("Partida terminada", "Has ganado, \n ¿quieres volver a jugar?")

		else:
			
			valor=messagebox.askquestion("Partida terminada", "Has perdido, \n ¿quieres volver a jugar?")

		if valor=="yes":
			self.partidaAnterior=True
			self.letrasAdivinadas=[]
			self.letrasincorrectas=[]
			letra=""
			ahorcado.iniciopartida()
		else:
			raiz.destroy()


ahorcado = hangman()	


#--------menu------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

menuArchivo=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Iniciar juego")
menuArchivo.add_command(label="Configurar partida", command=ahorcado.configuracion)
menuArchivo.add_command(label="Salir", command=lambda:raiz.destroy())


#-------frame----------
miFrame=Frame(raiz, width=300, height=400)
miFrame.pack()


imagen="hang0.png"
lista=[]

for i in range(12):
	reemplazo=imagen.replace("0", str(i)) #reemplaza 0 por i (el número del for) en la string imagen
	lista.append(reemplazo) #lo añade a la lista

#se ejecuta despues el for, hay que hacer por que se ejecute antes. este self.y el de arriba
for i in range(12):
	imagenes.append(Image.open(lista[i]).resize((200,200))) #abre la imagen de la lista
	misImagenes.append(ImageTk.PhotoImage(imagenes[i])) #la muestra


miImagen=Label(miFrame, image=misImagenes[11])
miImagen.grid(row=0, column=0, padx=10, pady=10)

miLabel=Label(miFrame, textvariable=texto)
miLabel.grid(row=1, column=0, padx=10, pady=10)

#print(lista)

#imagenes=["hang0.png", "hang1.png", "hang2.png", "hang3.png", ...]



#print(imagenes)
#print(misImagenes)
'''
imagenes=[
(Image.open("hang0.png").resize((200,200))),
(Image.open("hang1.png").resize((200,200))),
(Image.open("hang2.png").resize((200,200))),
(Image.open("hang3.png").resize((200,200))),
(Image.open("hang4.png").resize((200,200))),
(Image.open("hang5.png").resize((200,200))),
(Image.open("hang6.png").resize((200,200))),
(Image.open("hang7.png").resize((200,200))),
(Image.open("hang8.png").resize((200,200))),
(Image.open("hang9.png").resize((200,200))),
(Image.open("hang10.png").resize((200,200))),
(Image.open("hang11.png").resize((200,200)))]

misImagenes=[
(ImageTk.PhotoImage(imagenes[0])),
(ImageTk.PhotoImage(imagenes[1])),
(ImageTk.PhotoImage(imagenes[2])),
(ImageTk.PhotoImage(imagenes[3])),
(ImageTk.PhotoImage(imagenes[4])),
(ImageTk.PhotoImage(imagenes[5])),
(ImageTk.PhotoImage(imagenes[6])),
(ImageTk.PhotoImage(imagenes[7])),
(ImageTk.PhotoImage(imagenes[8])),
(ImageTk.PhotoImage(imagenes[9])),
(ImageTk.PhotoImage(imagenes[10])),
(ImageTk.PhotoImage(imagenes[11]))]

'''





raiz.mainloop()
