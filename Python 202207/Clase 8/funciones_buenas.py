def factorial(n):
    """
    Calcula el factorial de un número.
    Se deben ingresar enteros.
    Levanta errores si es necesario.
    """
    if not isinstance(n, int) and not isinstance(n, float):
        raise TypeError('Solo se aceptan enteros no negativos.')
    if n % 1 != 0 or n < 0:
        raise ValueError('Solo se aceptan enteros no negativos.')
    if n == 0:
        return 1
    n = int(n)
    return n * factorial(n-1)
