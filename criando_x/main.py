

def desenhando_x (valor):
    metade = 0
    cont = valor
                                #revisar variáveis, criar variaveis para espaçamento de dentro e de fora
    i = 0
    j = 0

    if (valor % 2 == 0):            
        metade = (valor // 2) - 1

        for i in range(int(metade)):          #melhor tentar usar while! 
            print(f"X{' '*valor}X")
            valor += 1

        print(f"{' '*cont}X")

        for j in range(int(metade)):
            print(f"X{' '*valor}X")
            valor -= 1
   
    else:
        
        metade = valor // 2

        for i in range(metade):
            print(f"X{' '*valor}X")
            valor -= 1
        
        print(f"X{' '*cont}")

        for j in range(metade):
            print(f"X{' '*valor}X")
            valor += 1



while True:
    try:
        print("\n=== Desenhando um X ===")
        print("-"*30)
        valor = int(input("Digite o tamanho que o X terá: "))

        if valor <= 2:
            print("valor deve ser de 3 em diante.")
            continue

        else:
            desenhando_x(valor)
            escolha = int(input(f"\n{"-"*40}\nGostaria de fazer de novo:\n1 - Sim\n2 - Não\n\n >> "))
            if (escolha == 1):
                continue
            else:
                break

    except ValueError:
        print("\nO valor deve ser um num inteiro.")

