# copy, sorted, produtos.sort
# Exercícios

import pprint
from copy import deepcopy

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
new_products = deepcopy(products)
products_sorted_by_name = deepcopy(new_products)
products_sorted_by_cost = deepcopy(new_products)

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

def increase_value(dicts):
    for dict in dicts:
        dict['preco'] = dict['preco'] * 1.1
        return dicts
    
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

def sorted_by_name(list):
    return sorted(list, key=lambda key: key['nome'])

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def sorted_by_cost(list):
    return sorted(list, key=lambda key: key['preco'])

#outputs

pprint.pprint(increase_value(new_products))

print()

pprint.pprint(sorted_by_name(products_sorted_by_name))

print()

pprint.pprint(sorted_by_cost(products_sorted_by_cost))
