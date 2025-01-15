import re

from typing import List, Optional

def valida_cartao_credito(lista_entrada: List[Optional[str]]) -> List[str]:
    resultados = []
    
    for cartao in lista_entrada:
        # Verifica se o cartão é vazio ou se contém outros caracteres que não números ou hífens
        if not cartao or not re.match(r'^[0-9-]+$', cartao):
            resultados.append("Invalido")
            continue
        
        # Verifica se o formato do cartão está correto (exato 16 caracteres, com ou sem hífens)
        if len(cartao.replace('-', '')) != 16 or (cartao.count('-') != 3 and cartao.count('-') != 0):
            resultados.append("Invalido")
            continue
        
        # Verifica se o cartão começa com 4, 5 ou 6
        if not cartao[0] in '456':
            resultados.append("Invalido")
            continue
        
        # Verifica se o cartão tem 4 ou mais dígitos repetidos
        if re.search(r'(\d)\1{3,}', cartao.replace('-', '')):  # Busca por 4 ou mais dígitos repetidos
            resultados.append("Invalido")
            continue
        
        resultados.append("Valido")
    
    return resultados
