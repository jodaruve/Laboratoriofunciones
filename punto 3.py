def perfect_number(a):
	sum=0

	for i in range(1,a):
		if a%i==0:
			sum=sum+i
	if sum==a:
		print("El numero", a, "es un perfecto")

	else:
		print("El numero", a, "no es un perfecto")

print("Este programa calculara si el numero ingresado es perfecto o no")
a=int(input("Por favor ingrese un numero "))
perfect_number(a)
