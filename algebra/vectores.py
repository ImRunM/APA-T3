"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Imelda Run Montes Martín

    Pruebas unitarias 
    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * 2
    Vector([2, 4, 6])
    >>> v1 * v2
    Vector([4, 10, 18])
    >>> v1 @ v2
    32
    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v1 // v2
    Vector([1.0, 2.0, 1.0])
    >>> v1 % v2
    Vector([1.0, -1.0, 1.0])

"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    def __mul__(self, other):
            """
            Multiplicación del vector por un escalar o producto de Hadamard con otro vector.
            """

            if isinstance(other, (int, float, complex)):
                return Vector(uno * other for uno in self)
            
            else:
                return Vector(uno * otro for uno, otro in zip(self, other))

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __matmul__(self, other):
        """
        Producto escalar (producto punto) entre dos vectores.
        """
        return sum(uno * otro for uno, otro in zip(self, other))
    
    def __floordiv__(self, other):
        """
        Devuelve la componente tangencial (proyección) de este vector sobre otro vector.
        """
        escalar = (self @ other) / sum(x * x for x in other)
        return Vector(escalar * x for x in other)
    
    def __mod__(self, other):
        """
        Devuelve la componente normal (perpendicular) de este vector respecto a otro vector.
        """
        return self - (self // other)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)