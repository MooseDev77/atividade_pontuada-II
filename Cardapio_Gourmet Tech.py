import os 
os.system("cls")
#O cardapio das comidas da casa
contador = 0

Escolha = int(input(""""
        Cardapio
                    
   1 \t Acarajé R$ 8,00
   2 \t Moqueca Bahiana R$ 104,90 ("seve duas pessoas")
   3 \t Vatapá R$ 10,00 ("Pequena porção")
   4 \t Abará R$ 8,00
   5 \t Caruru R$ 25,00
   6 \t Bobó de Camarão R$ 89,90 ("Serve duas pessoas")
   7 \t Xinxim de Galinha R$ 30,00
   Digite sua escolha: 
""""))

forma_de_pagamento = str(input("Vista | prazo : "))
desconto_v = {* 0.10}
acrescimo_p = {+ 0.10}

match Escolha: 
    case 1:
       desconto = valor * 0.10
        print("Prato escolhido {1} Acarajé R$ 8,00")
        print("")
                       