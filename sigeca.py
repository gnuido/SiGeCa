###     Pre-entrega proyecto integrador final   ###
###     Talento Tech - Segundo semeste 2024     ###
###################################################

#Inicio %-------------------------------------------------------------------------------------------------------
print(f'%'*5, '-'*5, 'Te damos la bienvenida al sistema de gestión de cátedras (SiGeCa)'.title(), '-'*5, '%'*5)
catedras = []
catedra = []
nombre = []
codigo = []
cargaHoraria = []
opcion = 1

#Opciones %------------------------------------------------------------------------------------------------------
while opcion != 6:
	print('Por favor, elija una de las siguientes opciones ingresando el dígito correspondiente: ')
	print('1> Ver lista completa de cátedras')
	print('2> Añadir cátedra a la lista')
	print('3> Editar detalles de una cátedra')
	print('4> Eliminar cátedra de la lista')
	print('5> Ayuda/FAQ')
	print('6> Finalizar')
	opcion = int(input())
#----------------
	if opcion == 1:
		if len(catedras) > 0:
			indice = 0	#indice de recorrida para listas
			while indice <= len(catedras) - 1:
				print('\n%' + '-' * 50)
				print(f'Cátedra: {catedras[indice][0]}')	#acceso a elemento en lista de lista
				print(f'Código de cátedra: {catedras[indice][1]}')
				print(f'Carga horaria semanal: {catedras[indice][2]} hs')
				indice += 1
			print('\n' + '*' * 20 + 'Fin de la lista' + '*' * 20)
			print('\n')
		else:
			print('\n' + '-' * 80)
			print('La lista de cátedras se encuentra vacía')
			print('-' * 80 + '\n')
#----------------
	elif opcion == 2:
		nombre = str(input('Nombre completo de la cátedra: '))
		codigo = str(input('Código de cátedra: '))
		#disponibilidadCarreras = str(input('Carreras para las que está disponible: '))	#no implementado
		cargaHoraria = input('Carga horaria semanal (en horas): ')
		#correlatividades = str(input('Códigos de cátedras correlativas: '))
		#catedra = [nombre, codigo, disponibilidadCarreras, cargaHoraria, correlatividades]
		while cargaHoraria.isnumeric() == False:	#se verifica y fuerza a que la carga horaria sea un integer
			print('Valor inválido, por favor, ingrese la carga horaria empleando números únicamente.')
			cargaHoraria = str(input('Carga horaria semanal, en horas: '))
		catedra = [nombre, codigo, cargaHoraria]
		catedras.append(catedra)
		print('\n' + '-' * 80)
		print(f'Se añadió la cátedra {nombre} a la lista con éxito')
		print('-' * 80 + '\n')
#-----------------
	elif opcion == 3:
		if len(catedras) == 0:
			print('\n' + '-' * 80)
			print('La lista de cátedras se encuentra vacía.')
			print('-' * 80 + '\n')
			continue
		print('Seleccione la cátedra que desea editar: ')
		for j in range(0, len(catedras)):
			print(f'{j}> {catedras[j][0]}')
		catedraModificar = input()
		while catedraModificar.isnumeric() == False or (0 <= int(catedraModificar) <= len(catedras) - 1) == False:
			print('Valor inválido, intente nuevamente.')
			catedraModificar = input('Seleccione la cátedra que desea editar: ')
		catedraModificar = int(catedraModificar)
		print('\nSeleccione el campo a modificar: ')
		print('0> Nombre.')
		print('1> Código de cátedra.')
		print('2> Carga horaria semanal.')
		campoModificar = input()
		while campoModificar.isnumeric() == False or (0 <= int(campoModificar) <= 2) == False:
			print('Valor inválido, intente nuevamente.')
			campoModificar = input('Seleccione el campo a modificar: ')
			print('0> Nombre.')
			print('1> Código de cátedra.')
			print('2> Carga horaria semanal.')
		campoModificar = int(campoModificar)
		nombreModificar = catedras[catedraModificar][0]
		codigoModificar = catedras[catedraModificar][1]
		cargaHorariaModificar = catedras[catedraModificar][2]
		if campoModificar == 0:
			catedras[catedraModificar][0] = str(input('Ingrese nuevo nombre de cátedra: '))
			print('\n' + '-' * 80)
			print(f'El nombre de la cátedra {nombreModificar} se ha modificado a {catedras[catedraModificar][0]} con éxito.')
			print('-' * 80 + '\n')
		elif campoModificar == 1:
			catedras[catedraModificar][1] = str(input('Ingrese nuevo código de cátedra: '))
			print('\n' + '-' * 80)
			print(f'El código de cátedra {codigoModificar} se ha modificado a {catedras[catedraModificar][1]} con éxito.')
			print('-' * 80 + '\n')
		elif campoModificar == 2:
			catedras[catedraModificar][2] = input('Ingrese nuevo valor de carga horaria semanal: ')
			while catedras[catedraModificar][2].isnumeric() == False:
				print('Valor inválido, debe cargar un valor numérico.')
				catedras[catedraModificar][2] = input('Ingrese nuevo valor de carga horaria semanal: ')
			print('\n' + '-' * 80)
			print(f'La carga horaria semanal se ha modificado de {cargaHorariaModificar} a {catedras[catedraModificar][2]} con éxito.')
			print('-' * 80 + '\n')
#-----------------
	elif opcion == 4:
		if len(catedras) == 0:
			print('\n' + '-' * 80)
			print('La lista de cátedras se encuentra vacía.')
			print('-' * 80 + '\n')
			continue
		print('Seleccione la cátedra a remover de la lista: ')
		for j in range(0, len(catedras)):
			print(f'{j}> {catedras[j][0]}')
		catedraEliminar = input()
		while catedraEliminar.isnumeric() == False or (0 <= int(catedraEliminar) <= len(catedras) - 1) == False:
			print('Valor inválido, por favor, intente nuevamente.')
			catedraEliminar = input('Seleccione la cátedra a eliminar: ')
		catedraEliminar = int(catedraEliminar)
		nombreEliminar = catedras[catedraEliminar][0]
		catedras.pop(catedraEliminar)	#método .pop() para eliminar elemento de lista por posición
		print('\n' + '-' * 80)
		print(f'Se ha eliminado la cátedra {nombreEliminar} con éxito.')
		print('-' * 80 + '\n')
#-----------------
	elif opcion == 5:
		print('\n' + '-' * 80)
		print('Para recibir asistencia consulte con su administrador o complete un reporte en https://github.com/gnuido/SiGeCa/issues')
		print('-' * 80 +'\n')
#-----------------
	else:
		indiceError = 0		#contador de intentos inválidos
		if indiceError < 3:
			print('Opción inválida, por favor, intente nuevamente')
			indiceError += 1
		else:
			print('El valor que ingresado no es válido. Por favor, elija la opción a la que desea acceder e ingrese únicamente el número correspondiente')
			indiceError = 0

#Cierre	%------------------------------------------------------------------------------------------------------------
for k in range(1, 4): 	#k oficia como acumulador
    print('Finalizando' + '.' * k)
    
print('Gracias por utilizar el SiGeCa.\n')
print('%' + '-' * 82)


###############################
###     Fin del script      ###
###############################

