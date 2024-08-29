#Ejercicio 1

#Se explica brevemente qué hace cada clase (Paciente, Secretaria, Consultorio).
#Se incluyen comentarios que explican por qué se utilizó una clase en lugar de otros enfoques.
#Se hace referencia a principios de diseño como el Principio de Responsabilidad Única (SRP), que es fundamental en la POO.
#Sección de Ejemplo de Uso:

#Se añade una explicación sobre lo que hace el ejemplo proporcionado y cómo la POO beneficia la estructura del código.

#Ejercicio 2

# Este código ha sido implementado utilizando Programación Orientada a Objetos (POO) 
# debido a la necesidad de modelar entidades con comportamientos y atributos específicos, 
# como lo son los Libros, Usuarios, Préstamos y la Biblioteca en sí.
#
# Se han creado clases para encapsular tanto los datos como el comportamiento relacionado 
# con cada una de estas entidades. Esto facilita la organización del código y permite una 
# mayor flexibilidad y reutilización en futuras modificaciones o ampliaciones del sistema.
#
# La clase `Prestamo` incluye un método `verificar_sancion` que gestiona la lógica de 
# las multas por retraso, lo cual refuerza el principio de responsabilidad única, 
# un concepto clave en la POO. Además, se han utilizado módulos estándar de Python, 
# como `datetime` y `timedelta`, para manejar las fechas de préstamo y devolución de los 
# libros de manera efectiva.
#
# Decidimos utilizar POO para este problema porque nos permite estructurar el código 
# de manera que sea fácil de entender y mantener. En lugar de tener un código monolítico, 
# cada parte de la funcionalidad está distribuida entre diferentes clases, 
# cada una con responsabilidades bien definidas.

#Ejercicio 3

# Este sistema de reservas de hotel ha sido implementado utilizando Programación Orientada a Objetos (POO),
# debido a la necesidad de modelar diversas entidades como habitaciones, servicios extra y reservas.
# 
# Se utilizaron clases para encapsular tanto los datos como el comportamiento relacionado con cada entidad.
# Esto facilita la organización del código, mejorando su legibilidad y escalabilidad.
#
# La clase `Habitacion` encapsula la información relacionada con cada tipo de habitación, 
# mientras que `ServicioExtra` modela los servicios adicionales disponibles. 
# La clase `Hotel` es responsable de gestionar todas las operaciones relacionadas con las reservas, 
# como la creación de reservas, la adición de servicios adicionales y el cálculo del costo total de la reserva.
#
# Las decisiones de diseño se fundamentan en la necesidad de:
# 
# 1. **Modularidad**: Cada clase tiene una responsabilidad específica, lo que permite que el código sea más fácil de mantener y expandir.
# 2. **Encapsulamiento**: Los detalles de la implementación están ocultos dentro de las clases, lo que mejora la seguridad y la integridad de los datos.
# 3. **Reutilización**: Las clases y métodos pueden ser reutilizados o extendidos en el futuro sin necesidad de cambiar la lógica central.
#
# Se han utilizado funcionalidades básicas de Python como listas para manejar colecciones de objetos, 
# así como estructuras de control como `try-except` para la gestión de errores, lo que mejora la robustez del sistema.

#Ejercicio 4

#Se definen las clases Vehiculo y EmpresaRenta con sus respectivos métodos para gestionar los vehículos y las operaciones de renta.
#Constructores y Validación:

#Se valida la entrada de datos en el constructor de Vehiculo y en el método rentar_vehiculo para garantizar que los datos sean correctos y válidos.
#Métodos Especiales:

#El método __str__ proporciona una forma de representar los objetos Vehiculo como cadenas de texto, lo que facilita su impresión.
#Interacción con el Usuario:

#La función menu y el bloque try-except en la función main permiten una interfaz simple para el usuario y manejan posibles errores de entrada.
#Estos elementos hacen que el código sea modular, robusto y fácil de entender y mantener.