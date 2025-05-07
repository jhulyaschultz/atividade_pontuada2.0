import os
os.system("clear")

valor = 0
total = 0
lista_pratos = []

while True:
    menu = int(input(""" 
olá, escolha seu prato: \n 
 CÓDIGO |  DESCRIÇÃO  |  VALOR 
    1   |  SUSHI      | 38,00
    2   |  HOTDOG    | 15,00
    3   |  BATATA FRITA | 20,00
    4   |  MOUSSE      |  12,00
    5   |   TRUFA    |  3,00
    6   |   SALADA  |   46,00
    7   |   BOLO DE POTE    |   15,00
    0   |   ENCERRAR PEDIDO
"""))

    match menu:
        case 1:
            print("VOCE ESCOLHEU SUSHI")
            valor = 38.00
            prato = "SUSHI"
        case 2:
            print("VOCE ESCOLHEU HOTDOG")
            valor = 15.00
            prato = "HOTDOG"
        case 3:
            print("VOCE ESCOLHEU BATATA FRITA")
            valor = 20.00
            prato = "BATATA FRITA"
        case 4:
            print("VOCE ESCOLHEU MOUSSE")
            valor = 12.00
            prato = "MOUSSE"
        case 5:
            print("VOCE ESCOLHEU TRUFA")
            valor = 3.00
            prato = "TRUFA"
        case 6:
            print("VOCE ESCOLHEU SALADA")
            valor = 46.00
            prato = "SALADA"
        case 7:
            print("VOCE ESCOLHEU BOLO DE POTE")
            valor = 15.00
            prato = "BOLO DE POTE"
        case 0:
            print(f"\nTOTAL DO PEDIDO: {total:.2f}")
            break
        case _:
            print("\nDesculpe, não tem essa opção.")

    lista_pratos.append(prato)
    total += valor

    continuar = input("\nDeseja adicionar mais um pedido? (s/n): ").strip().lower()

    if continuar == "s":
        continue
    elif continuar == "n":
        print(f"\nTotal do pedido: {total:.2f}")
        break
    else:
        print(f"\nOpção inválida, digite 's' ou 'n'.")
        break

forma_pagamento = int(input("\nDIGITE A FORMA DE PAGAMENTO:\n 1 | À vista (desconto de 10%).\n 2 | Parcelado (juros de 10%).\n"))

if forma_pagamento == 2:
    acrescimo = total * 0.10
    valor_acrescimo = acrescimo + total
    print(f"\nVocê teve um acréscimo de R$ {acrescimo:.2f} no seu pedido.")
    print(f"\nTotal com acréscimo: R$ {valor_acrescimo:.2f}")
elif forma_pagamento == 1:
    desconto = total * 0.10
    valor_desconto = total - desconto
    print(f"\nVocê teve um desconto de R$ {desconto:.2f} no seu pedido.")
    print(f"\nTotal com desconto: R$ {valor_desconto:.2f}")
else:
    print("\nOpção inválida.")

for prato in lista_pratos:
    print(f"SEU PRATO ESCOLHIDO FOI: {prato}")

print("\nPEDIDO FINALIZADO, MUITO OBRIGADA!")
