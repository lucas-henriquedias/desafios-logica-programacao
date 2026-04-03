import sys

def repeat_question():
    while True:
        try:
            escolha = int(input(f"\n{"-"*40}\nGostaria de fazer de novo:\n1 - Sim\n2 - Não\n\n >> "))
            if (escolha == 1):
                break

            elif (escolha == 2):
                print("\nEncerrando programa...")
                sys.exit()

            else:
                print("Selecione uma opção válida.")
                

        except ValueError:
            print("\nSelecione uma opção válida")


def desenhando_x (valor):
    metade = 0
    i = 0           #contador para a parte de cima do X.
    j = 0           #cont para a parte de baixo.

    """ eu preciso pensar em alguma forma de primeiro, imprimir o X, dar uma série de espaços
    na qual pode ter algum calculo que faça valor -2, enquanto dar espaços antes o segunda
    linha em diante. """


    metade = (valor // 2)

    for i in range(metade):
        print(f"{' '*i}")

        for j in range(metade):
            print(f"X{' '*valor}X")
            valor -= 1

    for i in range(metade, 0):
        print(f"{' '*i}")

        for j in range(metade):
            print(f"X{' '*valor}X")
            valor += 1


#################################################

while True:
    try:
        print("\n=== Desenhando um X ===")
        print("-"*30)
        valor = int(input("Digite o tamanho que o X terá: "))
        print(" ")

        if valor <= 2:
            print("valor deve ser de 3 em diante.")
            continue

        else:
            #Chamandos a função resposnsável pelos calculos
            desenhando_x(valor)
            repeat_question()

    except ValueError:
        print("\nO valor deve ser um num inteiro.")



