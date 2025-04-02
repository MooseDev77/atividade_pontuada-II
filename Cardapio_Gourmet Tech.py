import os 
os.system("clear")
subtotal= 0
pedido = 0
forma_pagamento = 0
nome = str ()
preco = ()
soma = 0
#O cardapio das comidas da casa

menu = {     
    1:  ("Acarajé", 8.00),
    2:  ("Moqueca Bahiana", 104.90),
    3:  ("Vatapá", 10.00),
    4:  ("Abará", 8.00),
    5:  ("Caruru", 25.00),
    6:  ("Bobó de Camarão", 89.90),
    7:  ("Xinxim de Galinha", 30.00)
}
    
  
# Processo de escolha dos pratos
while True:
        menu = codigo and nome and preco
        print(f"{codigo} - {nome}: R${preco:.2f}")
        contador = +1
        codigo += preco 
        print("Menu:")
        codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))

        if codigo == 0:
            break
        
        else:
            print("Código invalido. Tente novamente.")
            continue
        # Cáculo do valor total
        subtotal = (preco, preco, pedido)
        opcao_pagamento = int(input("Escolha a forma de pagamento: "))
        print("\nForma de pagamento:")
        print("1 - À vista (10% de desconto)")
        print("2 - Cartão de crédito (10% de acréscimo)")
#Escolha da forma de pagamento
        match opcao_pagamento:
            case 1:
                desconto = subtotal * 0.10
                total = subtotal - desconto
                forma_pagamento = "À vista"
                
            case 2:
                desconto = -subtotal * 0.10 # Acréscimo
                total = subtotal - desconto
                forma_pagamento = "Cartão de Crédito"
                
            case _:
                print("Opção invalida. Escolha novamente.")
# Exixbindo resultados finais
print("\nResumo do pedido:")
for nome, preco in pedido:
    print(f" - {pedido}: R${preco:.2f}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
print(f"Valor do desconto ou acréscimo: R${desconto:.2f}")
print(f"valor final a ser pago: R${total:.2f}")