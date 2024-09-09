# Vamos solicitar como entrada dois números e depois realizaremos uma operação simples entre eles.

# Passo 1: Solicitar dois números (usei dois inteiros para simplificar)
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

# Passo 2: Perguntar qual operação deseja realizar.
operacao = input("Escolha a operação (+, -, *, /): ")

# Passo 3: Mostrar o resultado da operação escolhida.
if operacao == '+':
    print(number1 + number2)
elif operacao == '-':
    print(abs(number1 - number2))
elif operacao == '/':
    print(number1 / number2)
elif operacao == '*':
    print(number1 * number2)
else: 
    print("Operação inválida.")
