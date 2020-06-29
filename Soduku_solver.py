# Sudoku solver

sudoku = [
		[0,6,3,0,8,0,4,0,0],
		[0,9,0,0,0,4,0,0,7],
		[4,0,0,0,2,0,0,0,0],
		[0,0,7,2,0,3,0,5,8],
		[0,5,0,0,4,0,0,0,0],
		[0,0,8,0,0,0,2,0,4],
		[6,0,0,0,0,0,7,0,0],
		[0,0,5,0,3,6,0,0,0],
		[0,3,0,8,7,0,0,2,6]
			]


def regla_1(sudoku,fila, num):
	#Chequea numeros por fila
	if num in sudoku[fila]:
		return False
	return True

def regla_2(sudoku,fila,columna,num):
	#Chequea numeros por columna
	for numero in range(len(sudoku)):
		if sudoku[numero][columna] == num:
			return False

	return True


def regla_3(sudoku,fila,columna,num):
	# Chequea recuadro 3x3
	box_x = fila // 3  
	box_y = columna // 3
	for i in range(box_x*3, box_x*3 + 3):
		for j in range(box_y*3, box_y*3 + 3):
			if sudoku[i][j] == num and (i,j) != (fila,columna):
				return False
	return True

def funciona(sudoku, fila, columna):
	# Chequeando condiciones

	for numero in range(1,10):
		condicion1 = regla_1(sudoku,fila, numero)
		condicion2 = regla_2(sudoku,fila,columna,numero)
		condicion3 = regla_3(sudoku,fila,columna,numero)
		if condicion1==True and condicion2==True and condicion3==True:
			sudoku[fila][columna] = numero
			
			if main(sudoku):
				return True
		
			sudoku[fila][columna]= 0
	return False



def vacio(sudoku):
	# Chequeando si el numero esta vacio
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # fila, columna

    return None




def main(sudoku):
	esvacio = vacio(sudoku)
	if not esvacio:
		return True
	else:
		fila,columna = esvacio
	
	if funciona(sudoku,fila,columna):
		return True

	return False

print("Sudoku antes de resolver: ")
for col in sudoku:
	print (col)
print(" ")
main(sudoku)
print("Sudoku despues de resolver: ")
for col in sudoku:
	print(col)
