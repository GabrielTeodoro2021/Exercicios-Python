#função para calcular o imposto baseado nas aliquotas
def calcular_imposto(valor_salario):
    aliquota = 0.00
    if (valor_salario >= 0 and valor_salario <=1100):
        aliquota = 0.05
    elif (valor_salario >= 1100.01 and valor_salario <= 2500.00):
        aliquota = 0.10
    else:
        aliquota = 0.15
        return aliquota * valor_salario

#lê os valores de entrada   
valor_salario = float(input("Informe seu salario: "))
valor_beneficios = float(input("Informe seu beneficio: "))

#calcular o imposto através da função "calcular_imposto"
valor_imposto = calcular_imposto(valor_salario)

#calcular e imprimir a saida com 2 caracteres
saida = valor_salario - valor_imposto + valor_beneficios
print(f'{saida:.2f}')