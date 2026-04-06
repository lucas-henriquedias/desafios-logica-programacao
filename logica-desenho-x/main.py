import sys, os, platform

def clear_screen():
    if platform.system().lower() == "windows":
        os.system('cls')
    
    else:
        os.system('clear')


def repeat_question():
    while True:
        try:
            
            escolha = int(input(f"\n{"-"*40}\nGostaria de fazer de novo:\n1 - Sim\n2 - Não\n\n >> "))
            if (escolha == 1):
                break

            elif (escolha == 2):
                clear_screen()
                print("\nEncerrando programa...")
                sys.exit()

            else:
                clear_screen()
                print("Selecione uma opção válida.")
                input("Enter para continuar...")
                

        except ValueError:
            clear_screen()
            print("\nSelecione uma opção válida!\n")
            input("Enter para continuar...")


def print_line(espacos_fora, espacos_dentro):
    print(f"{' ' * espacos_fora}X{' ' * espacos_dentro}X")


def desenhando_x (valor):

    for i in range(valor // 2):
        espaco_fora = i

        """valor - 2 represent os X's de cada linha, o - (i * 2), a cada linha a 
        formula tem q decrementar n só 1 espaço, o do X, como tbm outro para q ele
        ande para a esquerda."""
        espaco_dentro = valor - 2 - (i * 2) 

        print_line(espaco_fora, espaco_dentro)

    if (valor % 2 != 0):
        print(f"{' ' * (valor // 2)}X")

    """ neste for eu deixo o parametro de range desta forma pois, o primeiro determina
    onde começa, e como estamos no modo ímpar, precisa ser a metade do valor - 1, ele
    precisa ir até -1, já q o range funciona o 0 como um indice valido, e colocamos o
    3 parametro como -1 para q ele faça o processo contrário a parte de cima do X. """
    for i in range((valor // 2) - 1, -1, -1):
        espaco_fora = i
        espaco_dentro = valor - 2 - (i * 2)
        print_line(espaco_fora, espaco_dentro)


####### Função Principal ##########################################

while True:
    try:
        clear_screen()
        print("\n=== Desenhando um X ===")
        print("-"*30)
        valor = int(input("Digite o tamanho que o X terá: "))
        print(" ")

        if valor <= 2:
            clear_screen()
            print("O valor deve ser de 3 em diante.\n")
            input("Enter para continuar...")
            continue

        else:
            #Chamandos a função resposnsável pelos calculos
            desenhando_x(valor)
            repeat_question()

    except ValueError:
        clear_screen()
        print("\nO valor deve ser um número inteiro.\n")
        input("Enter para continuar...")

