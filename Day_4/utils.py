'''
Created on 06/02/2018

@author: Utilizador
'''


def is_number(valor):
    '''
    param: any value
    return: int if value is integer
    '''
    
    try:
        return int(valor)
    except:
        return None
    
    
def vect_float(valor):
    '''
    param: any value
    return: float
    '''
    
    try:
        return float(valor)
    except:
        return None
    
    
    
def reverse(sequence):
    return sequence[::-1]
    
def complement(sequence):
    sz_return = ''
    for base in sequence:
        if (base == 'A' or base == 'a'): sz_return += 'T'
        elif (base == 'C' or base == 'c'): sz_return += 'G'
        elif (base == 'G' or base == 'g'): sz_return += 'C'
        elif (base == 'T' or base == 't' or base == 'U' or base == 'u'): sz_return += 'A'
        else: sz_return += base
    return sz_return
    