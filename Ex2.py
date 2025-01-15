def calcula_desconto(total):
    if total >= 500:
        desconto = total * 0.20
    elif total >= 300:
        desconto = total * 0.15
    elif total >= 100:
        desconto = total * 0.10
    else:
        desconto = 0.0
    
    return (desconto)

print(calcula_desconto(50))
