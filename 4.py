class StackBase:

    # Construye una pila vacía.
    def __init__(self):
        self.list = []

    # Devuelve un entero, el número de elementos en la pila.
    def size(self):
        return len(self.list)

    # Agrega un elemento al final de la pila.
    def push(self, a):
        return self.list.append(a)

    # Elimina un elemento del final de la pila y lo devuelve.
    def pop(self):
        return self.list.pop()

    # Devuelve un elemento del final de la pila sin eliminarlo.
    def top(self, c):
        return self.list[c]

    # Devuelve True si la pila está vacía, en caso contrario devuelve False.
    def empty(self):
        if len(self.list) == 0:
            return True
        return False

    # Elimina todos los elementos de la pila.
    def clear(self):
        return self.list.clear()

    def __str__(self):
        return str(self.list)


stackbase = StackBase()
stackbase.push(16)
stackbase.push(4)
stackbase.push(1)
stackbase.push(6)
print(stackbase)
print(stackbase.top(1))
print(stackbase.empty())
stackbase.pop()
print(stackbase)
print(stackbase.size())
print(stackbase.clear())
