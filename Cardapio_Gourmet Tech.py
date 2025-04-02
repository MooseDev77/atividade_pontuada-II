import os 
os.system("clear")

#O cardapio das comidas da casa
menu = ("""          
   1:  ("Acarajé", 8.00)
   2:  ("Moqueca Bahiana", 104.90 ("seve duas pessoas"))
   3:  ("Vatapá", 10.00" ("Pequena porção"))
   4:  ("Abará", 8.00)
   5:  ("Caruru", 25.00)
   6:  ("Bobó de Camarão", 89.90 ("Serve duas pessoas"))
   7:  ("Xinxim de Galinha", 30.00)
   """)
# Processo de escolha dos pratos
pedido = ()
while True:
      print ("menu:")
      for codigo, (nome, preco) in menu.items():
        print(f"{codigo} - {nome}: R${preco:.2f}")
   
      codigo = int(input("Digite o código do prato escolhido (ou 0 para finalizar): "))
      if codigo == 0:
       break
      elif codigo in menu:
       pedido.append(menu[codigo])
      else:
         print("Código inválido. Tente novamente.")
      continue
#Cáculo do valor total
subtotal = sum(preco for _, preco in pedido)

# Escolha da forma de pagamento
while True:
   print("\nForma de pagamente:")
   print("1 - À vista (10% de desconto)")
   print("2 - Cartão de crédito (10% de acréscimo)")
   opcao_pagamneto = int(input("Qual a forma de pagamento "))

   match opcao_pagamneto:
      case 1:
         desconto = subtotal * 0.10
         total = subtotal - desconto
         forma_pagamento = "À vista"
         break
      case 2:
         desconto = -subtotal * 0.10 #acréscimo
         total = subtotal - desconto
         forma_pagamento = "Cartão de Crédito"
         break
      case _:
         print("Opção inválida. Escolha novamente.")

# Mostrando Resultados Finais
print("\nResumo do pedido: ")
for nome, preco in pedido:
   print(f" - {nome}: R${preco:.2f}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
print(f"Valor do desconto ou acréscimo: R${desconto:.2f}")
print(f"valor final a ser pago: R${total:.2f}")

      