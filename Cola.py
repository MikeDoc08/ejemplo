from collections import deque

# Cola de números
cola_numeros = deque([1, 2, 3, 4, 5])

# Operaciones de cola (FIFO)
cola_numeros.append(6)   # Agregar al final
cola_numeros.popleft()   # Sacar del principio