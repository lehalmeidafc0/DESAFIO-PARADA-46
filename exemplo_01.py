# Função para calcular a média
def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Lista para armazenar os números
numeros = []

# Solicitar ao usuário que insira números
print("Digite os números para calcular a média. Digite 'sair' para finalizar.")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

# Verifica se a lista não está vazia
if numeros:
    media = calcular_media(numeros)
    print(f"A média dos números fornecidos é: {media}")
else:
    print("Nenhum número foi fornecido.")
