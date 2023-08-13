## Para ejecutar poner en la consola docstring y doctest
#python -help-all  "c:\Users\juand\PythonProjects\test python\Unitary Tests\main.py"
def suma(x,y):
    



    """    
    Esta función suma dos números.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
        
    Returns:
        int: La suma de a y b.
    """
    """

    Test suma function
    >>> suma(0,1)
    1
    >>> suma(-1,1)
    0
    >>> suma('a','b')
    'ab'
    >>> suma(1.0,'a')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'float' and 'str'
    """
    return x+y

def palindrome(chain:str):
    """"
    Esta función valida sí una cadena de texto es palíndroma
    
    Args:
        chain (str): Primer número.

    Returns:
        bool: Si el texto es palíndromo o no

    
    >>> palindrome("oro")
    True
    >>> palindrome("Ana") #test with Aná
    True
    >>> palindrome("La ruta natural")
    True
    """
    return chain.lower().replace(" ","") == chain[::-1].lower().replace(" ","")
    #return chain.lower() == chain[::-1].lower() # sin tener en cuenta espacios
    #return chain == chain[::-1] #sin tener en cuenta mayúscula

#print(print.__doc__)
print(suma.__doc__)

#def main(): ## es necesario sin librería de VSCode python doctest
    #import doctest## es docstring?
    #doctest.testmod()
    #doctest.testmod(name="palindrome",verbose=True)