import os 
os.system("clear")

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
print ("""
1 Acarajé         | R$ 8,00
2 Moqueca Bahiana | R$ 104,90
3 Vatapá          | R$ 10,00 
4 Abará           | R$ 8,00
5 Caruru          | R$ 25,00 
6 Bobó de Camarão | R$ 89,90
7 Xinxim de Galinha| R$ 30,00)""")
contador = 0
pedido = []
subtotal = 0
# Processo de escolha dos pratos
while True:
    codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))
    contador +1
    match codigo:
        case 0:
            break
        case _ if codigo in menu:
            pedido.append(menu[codigo])
            subtotal += menu[codigo][1]
            print(f"Adicionado:{0} {codigo}- R${menu}{1}:")  
        case _:
            print("Código inválido. Tente Novamente.")
print(f"\nSubtotal: R${subtotal:.2f}")
while True:
    print("\nFormas de pagamento:")
    print("1 - Dinheiro (10 porcento de Desconto)")
    print("2 - Cartão de Crédito (acréscimo de 10 porcento)")

    opcao = int(input("Escolha a forma de pagamento: "))

    match opcao:
        case 1:
            total = subtotal * 0.10
            print(f"Total com desconto: R$ {total:.2f}")
        case 2:
            total = subtotal * 1.10
            print(f"Total com acréscimo: R${total:2.f}")
        case _:
            print("Opção inválida. tente novamente.")                                                        




