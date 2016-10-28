from collections import Counter
    
def cuenta_elementos_de_lista(lista):
    """
    >>> zero_sum_list([1, 1, 2, 2, 3, 4, 5, 6])
    Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1})
    """
    return Counter(lista)


