def numero_escolhido():
    print ("Coloque um número, até encontrar o que irá encerrar o programa.")
    
    while True:
        try:
            numero = float(input("Digite um número:"))
            
            if numero > 0:
                print(f"O número {numero} é positivo.")
            elif numero <0:
                print(f"O número {numero} é negativo.")
            else:
                print("Você digitou zero. O programa será encerrado.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            
numero_escolhido()