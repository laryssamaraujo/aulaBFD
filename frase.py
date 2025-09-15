def gerar_frase():
    
    frase_escolhida = input("Olá. Digite uma frase que você goste:")
    
    palavras = frase_escolhida.split()
    
    numero_de_palavras = len(palavras)
    
    palavras_invertidas = palavras[::-1]
    
    frase_escolhida = ''.join(palavras_invertidas)
    
    print(f"\n A frase possui {numero_de_palavras} palavras.")
    print(f"Frase invertida: {frase_escolhida}")
    
gerar_frase()