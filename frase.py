def gerar_frase():
    
    frase_escolhida = input("Olá. Digite uma frase que você goste:")
    
    palavras = frase_escolhida.slip()
    
    numero_de_palavras = len(palavras)
    
    palavras_invertidas = palavras[::-1]
    
    frase_escolhida = ''.join(palavras_invertidas)
    
gerar_frase()

print(f )