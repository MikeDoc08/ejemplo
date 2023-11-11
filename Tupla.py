# Tupla de números enteros
tupla_numeros = (1, 2, 3, 4, 5)

# Tupla de cadenas de texto
tupla_nombres = ("Alice", "Bob", "Charlie", "David")

# Son contenedores para el almacenamiento de una colección 
# ordenada de uno o más elementos, accesibles mediante indexación.

# Mutabilidad:

# Listas: Son mutables, lo que significa que puedes cambiar, agregar
# o quitar elementos después de que la lista ha sido creada. Puedes 
# modificar elementos existentes o agregar nuevos elementos utilizando 
# métodos como append(), extend(), insert(), remove(), etc.

# Tuplas: Son inmutables, lo que significa que no puedes cambiar su 
# contenido después de que han sido creadas. Una vez que defines una 
# tupla, no puedes agregar, quitar ni modificar elementos.


# Sintaxis:

# Listas: Se definen mediante corchetes []. Por ejemplo: mi_lista = [1, 2, 3].

# Tuplas: Se definen mediante paréntesis (). Por ejemplo: mi_tupla = (1, 2, 3).


# Uso:

# Listas: Se utilizan cuando necesitas una colección de elementos ordenada y 
# mutable. Pueden ser usadas para almacenar secuencias de elementos que pueden 
# cambiar durante la ejecución del programa.

# Tuplas: Se utilizan cuando necesitas una colección inmutable de elementos. 
# Son eficientes en términos de rendimiento y se utilizan para representar conjuntos 
# de datos que no deben cambiar, como las coordenadas de un punto en un plano.


# Desempaquetado de tuplas:

# Tuplas: Permiten el "desempaquetado", lo que significa asignar los elementos de una 
# tupla a variables individuales en una sola instrucción. Por ejemplo: x, y, z = mi_tupla.

# Rendimiento:

# Tuplas: Generalmente son más eficientes en términos de rendimiento que las listas, 
# debido a su inmutabilidad. En situaciones donde no necesitas cambiar la estructura de 
# datos, usar tuplas puede ser más eficiente.