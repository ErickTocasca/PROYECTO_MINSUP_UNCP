try:    
    n1 = input("Digite un numero: ")
    
    resultado = 15 + n1
    
    print(resultado)
except Exception as e:
    print(type(e).__name__)
except TypeError:
    print("Ha ocurrido un error al digitar")
