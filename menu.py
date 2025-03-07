def menu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def calculadora():
    while True:
        menu()
        escolha = int(input("Digite a opção: "))
        
        if escolha == 0:
            print("Saindo...")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == 1:
            print(f"Resultado: {somar(num1, num2)}")
        elif escolha == 2:
            print(f"Resultado: {subtrair(num1, num2)}")
        elif escolha == 3:
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif escolha == 4:
            print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")

# Chamar a função para iniciar a calculadora
calculadora() 