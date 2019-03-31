def casi_perfecto(a):
	sum=0
	for i in range(1,a):
		if a%i==0:
			sum=sum+i
	if sum<=a-3:
		print("El numero", a, "no es casi perfecto")
	else:
		print("El numero", a, "es casi perfecto")

print("Este programa calculara si el numero ingresado es casi perfecto o no")
a=int(input("Por favor ingrese un numero "))
casi_perfecto(a)
