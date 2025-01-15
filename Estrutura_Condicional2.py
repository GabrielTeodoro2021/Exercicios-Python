Maior_Idade = 18
Idade_Especial = 17

idade = int(input("Informe sua idade para tirar a CNH:"))

if idade >= Maior_Idade:
    print("Maior de idade, você pode tirar a CNH")

elif idade == Idade_Especial:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas!")

else: 
    print("Menor de idade, você não pode tirar a CNH!")