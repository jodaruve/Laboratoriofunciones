## parte 1
def a_power_b(a,b):
  prod=1
  
  for i in range (1,b+1):
    
    if i>1000:
      raise( Exception('TOOOO BIG') )
    
    prod=prod*a
  
  return prod
  
  
print("Este programa calculara el elevado de los numeros ingresados. Cuando no desee ingresar mas numeros por favor digite 0")  
pot=0
par=0
impar=0
error=0

while True:
  try:
      
    a=int(input("Por favor ingrese un numero "))
    
    if a <= 0:
      break
    
    b=int(input("Por favor ingrese otro numero "))

    res = a_power_b(a,b)
    print("El resultado de elevar", a, "entre", b, "es:", res)
    pot=pot+1
    if res % 2 ==0:
      par=par+1
    else:
      impar=impar+1

  except: 
    print("Ha ocurrido un error. :(")
    error=error+1

print("El total de potencias mostradas fue de:", pot)
print("El total de errores fue de:", error)
print("El total de potencias pares fue de:", par)
print("El total de potencias impares fue de:", impar)

