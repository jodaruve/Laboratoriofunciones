## parte 1
def a_power_b(a,b):
  prod=1
  for i in range (1,b+1):
    prod=prod*a
  
  return prod
  
  
print("Este programa calculara el elevado de los numeros ingresados. Cuando no desee ingresar mas numeros por favor digite 0")  

while True:

  a=int(input("Por favor ingrese un numero "))
  
  if a <= 0:
    break
  
  b=int(input("Por favor ingrese otro numero "))

  
  res = a_power_b(a,b)
  print("El resultado de elevar", a, "entre", b, "es:", res)
