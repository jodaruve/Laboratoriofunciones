## parte 1
def a_power_b():
  prod=1
  for i in range (1,b+1):
    prod=prod*a
  print(prod)
  
  
print("Este programa calculara el elevado de los numeros ingresados.")  
a=int(input("Por favor ingrese un numero "))
b=int(input("Por favor ingrese otro numero "))
print("El resultado de elevar", a, "estre", b, "es:")
a_power_b()
