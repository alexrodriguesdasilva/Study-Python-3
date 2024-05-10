def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Exemplo de uso
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
print("Seu IMC é:", imc)