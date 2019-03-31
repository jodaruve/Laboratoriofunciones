def is_prime(a):
  i=0
  for n in range(1,a+1):
    if a%n==0:
     i=i+1
  if i>2:
    print(a, "Is not a prime number")
  else:
    print(a, "Is a prime number")


a=int(input("Por favor ingrese un numero para saber si es primo o no "))
is_prime(a)
