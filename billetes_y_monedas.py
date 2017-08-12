money = float(input("Cantidad de dinero: "))

def billetes_y_monedas(money):
	# notas
	cien = int(money // 100)
	cincuenta = int((money-100*cien) // 50)
	veinte = int((money-(cien*100+cincuenta*50)) // 20)
	diez = int((money-(cien*100+cincuenta*50+veinte*20)) // 10)
	cinco = int((money-(cien*100+cincuenta*50+veinte*20+diez*10)) // 5)
	dos = int((money-(cien*100+cincuenta*50+veinte*20+diez*10+cinco*5)) // 2)
	# monedas
	uno = int((money-(cien*100+cincuenta*50+veinte*20+diez*10+cinco*5+dos*2)) // 1)
	restante = money-(cien*100+cincuenta*50+veinte*20+diez*10+cinco*5+dos*2+uno)
	un_medio = int(restante // 0.5)
	un_cuarto = int((restante-(un_medio*0.5)) // 0.25)
	un_decimo = int((restante-(un_medio*0.5+un_cuarto*0.25)) // 0.1)
	un_quinto = int((restante-(un_medio*0.5+un_cuarto*0.25+un_decimo*0.1)) // 0.05)
	un_centimo = int((restante-(un_medio*0.5+un_cuarto*0.25+un_decimo*0.1+un_quinto*0.05)) // 0.01)
	return [cien, cincuenta, veinte, diez, cinco, dos, uno, un_medio, un_cuarto, un_decimo, un_quinto, un_centimo]

print(billetes_y_monedas(money))

map(lambda x: x*x, billetes_y_monedas(money))
# print(elements)