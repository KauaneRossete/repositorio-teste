# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que multiplica-los.

# Passo 1: Solicitar uma string
string = input("Digite uma string: ")

# Passo 2: Solicitar um número inteiro
# Note que usamos int() para converter a entrada
numero = int(input("Digite um número inteiro: "))

# Passo 3: Multiplicar a string pelo número e mostrar o resultado
print((string + ' ') * numero) # Adicionamos um espaço para separar as repetições da string
