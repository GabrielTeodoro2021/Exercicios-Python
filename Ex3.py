def verifica_palindromo(palavra):
    # Verifica se a palavra é igual à sua versão invertida
    eh_palindromo = palavra == palavra[::-1]
    return eh_palindromo

print(verifica_palindromo('radares'))