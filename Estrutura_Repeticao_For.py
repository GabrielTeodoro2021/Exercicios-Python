# o laço for percorre a lista “frutas” e imprime cada elemento até que encontremos a palavra "laranja".
# Nesse momento, interrompemos o laço.

frutas = ['maça', 'banana', 'laranja', 'melancia']

for fruta in frutas:
    if fruta == 'laranja':
        break
    print(fruta)


#Se quisermos iterar sobre os números de 1 a 10 com um incremento de 2, podemos usar a função range(1, 10, 2)

for i in range(1,10,2):
    print(i)



#Utilizamos o método items() para obter uma lista de pares chave-valor do dicionário “pessoa”.
# O laço for itera sobre cada par chave-valor e, a cada iteração, atribuímos o valor da chave à
# variável “chave” e o valor correspondente à variável “valor”. Em seguida, imprimimos os valores de “chave” e
# “valor” na tela.

pessoa = {'nome': 'Gabriel', 'idade': '23', 'cidade': 'Santos'}
for chave, valor in pessoa.items():
    print(chave, valor)


#verificar se um número é primo usando um loop for aninhado.
#encerra-se o loop quando o número for divisível pelo valor de i.

numero = 17

for i in range(2, numero):
    if numero % i == 0:
        break

print("O número", numero, "é primo.")