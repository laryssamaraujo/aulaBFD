print("Vamos começar a Caça ao Queijo.")
rato = int(input("Você tem 5 etapas. Digite 1 para começar:"))

if rato == 1:
       print("Você chegou na sala. HUUMM - não está aqui, siga adiante.")
       
quarto = int(input("Escolha mais um número da sequência. Cuidado o rato está por perto!"))
if quarto == 2 or 3:
       print("Você avançou e chegou no quarto. SIGA...")
       
cozinha = int(input("Estamos mais próximos, escolha 4 ou 5."))
if cozinha == 4:
       print("XIII, paramos na cozinha e você perdeu. O RATO COMEU O QUEIJO.")
if cozinha == 5:
       print("EBAAA, ABRI O ARMÁRIO E ACHEI O QUEIJO. PARABÉNS!! O RATO PERDEU.")