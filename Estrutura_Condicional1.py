salario = float(input("Informe seu salario:"))

if salario <= 4000:
    print("Programador Junior")

elif salario >4000 and salario <=7000:
    print("Programador Pleno")

elif salario >7000 and salario <=12000:
    print("Programador Senior")

else:
    print("Especialista")