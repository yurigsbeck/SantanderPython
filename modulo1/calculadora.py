def calculadora():
    while True:
        print('escolha a operação \n [1] ADIÇÃO \n [2] SUBTRAÇÃO \n [3] MULTIPLICAÇÃO \n [4] DIVISÃO \n [5] FECHAR PROGRAMA')
        escolha = input('digite sua escolha!')
        
        if escolha == '5':
            print("Encerrando a calculadora.")
            break
        22
        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro! Divisão por zero não permitida.")
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n")

calculadora()


