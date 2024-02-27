from calculadora import * 

option = input("""
Seleccione una operación
1: Suma 
2: Resta
3: Division
4: Multiplicación
""")

try:
    option = int(option)
    
    if option not in [1,2,3,4]:
        exit()
    
    a = int(input("Digite el primer numero: "))
    b = int(input("Digite el segundo numero: "))
    
    if option == 1:
        print("Suma: " + str(suma(a,b)))
        
    elif option == 2:
        print("Resta: " + str(resta()))
        
    elif option == 3:
        print("Division: " + str(division(a,b)))
        
    elif option == 4:
        print("Multiplicación: " + str(multiplicacion(a,b)))
              
    else:
        print ("Valor no válido")
except:
    print ("valor no válido")
    


