# 1. Imprimir "Mi Primer Código En Python."
def punto_1():
    print("Mi Primer Código En Python.")
    pass


# 2. Imprimir una expresión indicada
def punto_2():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    counter = 0
    for letter in letters:
        counter += 1
        print(letter, end=" ")
        if counter % 3 == 0:
            print("\n")
    pass


# 3. Ingresar e imprimir qué estás estudiando
def punto_3():
    print("Qué estás estudiando?")
    input_text = input()
    formatted_text = input_text.strip().capitalize()
    print(f"Estoy estudiando {formatted_text}.")
    pass


# 4. Ingresar e imprimir el país donde vives
def punto_4():
    print("En qué país vives?")
    input_text = input()
    formatted_text = input_text.strip().title()
    print(f"Vivo en {formatted_text}.")
    pass


# 5. Declarar nombre y edad de David Bowman
def punto_5():
    name = "David Bowman"
    age = 51
    print(f"Nombre: {name}, Edad: {age}")
    pass


# 6. Concatenar nombre, apellido y nombre completo
def punto_6():
    first_name = "Julia"
    last_name = "Roberts"
    full_name = first_name + " " + last_name
    print(f"Nombre: {first_name}, Apellido: {last_name}, Nombre completo: {full_name}")
    pass


# 7. Mostrar la materia concatenada en una frase
def punto_7():
    subject = "Ingeniería del Conocimiento"
    print(f"Estas estudiando la materia: {subject}.")
    pass


# 8. Convertir num1 a int e imprimir su tipo
def punto_8():
    num1 = "35"
    num1_int = int(num1)
    print(f"num1: {num1_int}, Tipo: {type(num1_int)}")
    pass


# 9. Mostrar nombre y número de asociado en una frase
def punto_9():
    name = "Alberto"
    associate_number = 43124
    print(f"Estimado/a {name}, su número de asociado es {associate_number}.")
    pass


# 10. Calcular división al piso de 874 entre 27
def punto_10():
    result = 874 // 27
    print(result)
    pass


# 11. Redondear 10.676767 al entero más próximo
def punto_11():
    number = 10.676767
    rounded_number = round(number)
    print(rounded_number)
    pass


# 12. Obtener el producto más caro del inventario
def punto_12(
    products: list = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]
):
    most_expensive_product = products[0]

    for product in products:
        if product[1] > most_expensive_product[1]:
            most_expensive_product = product
    print(f"Producto más caro: {most_expensive_product[0]}, Precio: {most_expensive_product[1]}")
    pass


# 13. Calcular average de scores de un estudiante
def punto_13(
    students: dict = {
    101: {"nombre": "Ana", "edad": 16, "scores": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "scores": {"matemáticas": 78, "ciencias": 88}}
    }
):

    for student_id, student_info in students.items():
        scores = student_info["scores"]
        average = sum(scores.values()) / len(scores)
        print(f"Estudiante: {student_info['nombre']}, Promedio: {average:.2f}")

    pass


# 14. Calcular media, máxima y mínima de temperaturas
def punto_14(
    temperatures: list = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
):
    average_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    print(f"Temperatura promedio: {average_temp:.2f}, Máxima: {max_temp}, Mínima: {min_temp}")
    pass


# 15. Calcular average usando *args
def punto_15():
    pass


# 16. Crear perfil de usuario usando **kwargs
def punto_16():
    pass


# 17. Filtrar empleados según salario
def punto_17():
    pass


# 18. Calcular total y average de ventas diarias
def punto_18():
    pass


# 19. Calcular goles anotados y recibidos
def punto_19():
    pass


# 20. Configurar aplicación usando **kwargs
def punto_20():
    pass


# 21. Ordenar puntuaciones de mayor a menor
def punto_21():
    pass


# 22. Calcular precio total de paquetes turísticos
def punto_22():
    pass


# 23. Actualizar inventario según ventas
def punto_23():
    pass


# 24. Imprimir eventos usando *args
def punto_24():
    pass


# 25. Calcular balance financiero usando **kwargs
def punto_25():
    pass


# 26. Registrar empleado con parámetros y **kwargs
def punto_26():
    pass


# 27. Calcular estadísticas de ventas mensuales
def punto_27():
    pass


# 28. Obtener libros publicados después del año 2000
def punto_28():
    pass


# 29. Calcular average de notas por estudiante
def punto_29():
    pass


# 30. Configurar perfiles de usuarios usando **kwargs
def punto_30():
    pass


# 31. Crear publicación de red social con etiquetas y opciones
def punto_31():
    pass


# 32. Simular ventas y calcular ingresos totales
def punto_32():
    pass


# 33. Crear una reserva verificando disponibilidad
def punto_33():
    pass


# 34. Calcular frecuencia de respuestas en encuestas
def punto_34():
    pass


# 35. Filtrar rutas según distancias máximas
def punto_35():
    pass


# 36. Actualizar inventario de múltiples tiendas
def punto_36():
    pass


# 37. Analizar tendencias de hashtags
def punto_37():
    pass


# 38. Actualizar suscripciones de usuarios
def punto_38():
    pass


# 39. Simular operaciones del mercado bursátil
def punto_39():
    pass


# 40. Crear ranking de students por average
def punto_40():
    pass
