def is_prime(a):
  i=0
  primo=0
  for n in range(1,a+1):
    if a%n==0:
     i=i+1
  if i>2:
    no="0"
    print(no)
  else:
    si="1"
    print(si)
    primo=primo+1
    print("El total de primos fue:", primo)
    

print("-Este programa calculara si el numero ingresado es primo o no. Si el mensaje devuelto es 1 significa que el numero es primo, si devuelve 0 significa que el numero no es primo, si devuelve -1 significa que ha ocurrido un error. Del mismo modo cuando no desee ingresar mas numeros digite -00")
print("")
try:
  a=int(input("Por favor ingrese un numero "))
  while a!=-00:
      if a !=0 and a >1:
        is_prime(a)
        a=int(input("Por favor ingrese un numero "))
      else:
        break 
      
except:
  error="-1"
  print(error)
