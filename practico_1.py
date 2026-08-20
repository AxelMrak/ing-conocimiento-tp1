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
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
    }
):

    for student_id, student_info in students.items():
        scores = student_info["calificaciones"]
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
def punto_15(
    *values
):
    average = sum(values) / len(values)

    print(f"Promedio: {average}" )
    pass


# 16. Crear perfil de usuario usando **kwargs
def punto_16(**kwargs: dict):
    new_user = {}
    for key, value in kwargs.items():
        new_user[key] = value
    return new_user


# 17. Filtrar empleados según salario
def punto_17(employees: dict, threshold: int):

    matched_employees = {}

    for id, values in employees.items():
        salary_employee = values[2]
        if salary_employee > threshold:
            matched_employees[id] = values

    return matched_employees



# 18. Calcular total y average de ventas diarias
def punto_18(
    sales: list[int | float]
):
    sales_sum = sum(sales)
    sales_qty = len(sales)

    if sales_qty == 0:
        return sales_sum, sales_qty

    average = sales_sum / sales_qty

    return sales_sum, average


# 19. Calcular goles anotados y recibidos
def punto_19(matches: dict[str, tuple[int, int]]):
    total_scored = 0
    total_received = 0

    for _team, match in matches.items():
        goals_scored = match[0]
        goals_received = match[1]

        total_scored += goals_scored
        total_received += goals_received

    return total_scored, total_received

# 20. Configurar aplicación usando **kwargs
def punto_20(
    **kwargs: dict
):
    settings = {
        "modo_oscuro": False,
        "idioma": "es",
        "notificaciones": False
    }

    for key, setting in kwargs.items():
        if settings[key] == setting:
            pass

        settings[key] = setting

    return settings



# 21. Ordenar puntuaciones de mayor a menor
def punto_21(
    scores: list[tuple[str, int]]
):
    sorted_scores = sorted(scores, key=lambda score:score[1], reverse=True)

    return sorted_scores

# 22. Calcular precio total de paquetes turísticos
def punto_22(
    travels: list[tuple[str, int, int]]
):

    formatted_travels = {}

    for (destination, price, duration_days) in travels:
        formatted_travels[destination] = price * duration_days


    return formatted_travels

# 23. Actualizar inventario según ventas
def punto_23(
    inventory: list[int],
    sales: list[int]
):
    for index, sale in enumerate(sales):
        inventory[index] = inventory[index] - sale

    return inventory

# 24. Imprimir eventos usando *args
def punto_24(
    *events: tuple[str]
):
    if len(events) == 0:
        print("No hay eventos disponibles.")

    for key, event in enumerate(events):
        normalized_key = key + 1
        print(f"[{normalized_key}] {event}")

# 25. Calcular balance financiero usando **kwargs
def punto_25(**income: int) -> int:
    return sum(income.values())


# 26. Registrar empleado con parámetros y **kwargs
def punto_26(name: str, age: int, salary: int, **kwargs: object):
    employee = {
        "nombre": name,
        "edad": age,
        "salario": salary,
    }

    for key, value in kwargs.items():
        employee[key] = value

    return employee


# 27. Calcular estadísticas de ventas mensuales
def punto_27(
    monthly_sales: list[int | float]
):
    total_sales = sum(monthly_sales)
    month_count = len(monthly_sales)

    if month_count == 0:
        return {
            "total": total_sales,
            "promedio": 0.0,
            "mes_mayor_venta": None,
        }

    monthly_average = total_sales / month_count
    top_month = monthly_sales.index(max(monthly_sales)) + 1

    return {
        "total": total_sales,
        "promedio": monthly_average,
        "mes_mayor_venta": top_month,
    }


# 28. Obtener libros publicados después del año 2000
def punto_28(
    library: dict[str, dict]
):
    recent_books = []

    for title, details in library.items():
        if details["año"] > 2000:
            recent_books.append(title)

    return recent_books


# 29. Calcular average de notas por estudiante
def punto_29(
    student_grades: list[tuple[str, list[int | float]]]
):
    averages = {}

    for (name, grades) in student_grades:
        average = sum(grades) / len(grades)
        averages[name] = average

    return averages


# 30. Configurar perfiles de usuarios usando **kwargs
def punto_30(
    users: list[str],
    **kwargs: object
):
    settings = list(kwargs.values())

    profiles = {}

    for user in users:
        profiles[user] = list(settings)

    return profiles


# 31. Crear publicación de red social con etiquetas y opciones
def punto_31(user: str, text: str, **kwargs: object):
    post: dict[str, object] = {
        "usuario": user,
        "texto": text,
    }

    for key, value in kwargs.items():
        post[key] = value

    return post


# 32. Simular ventas y calcular ingresos totales
def punto_32(*sales: tuple[str, int, float]):
    total_revenue = 0

    for (product, quantity, unit_price) in sales:
        total_revenue += quantity * unit_price

    return total_revenue


# 33. Crear una reserva verificando disponibilidad
def punto_33(
    reservations: dict[str, list],
    date: str,
    guest: str,
    room: int,
    price: int | float,
):
    if date not in reservations:
        reservations[date] = []

    for (existing_guest, existing_room, existing_price) in reservations[date]:
        if existing_room == room:
            return reservations

    reservations[date].append((guest, room, price))

    return reservations


# 34. Calcular frecuencia de respuestas en encuestas
def punto_34(
    surveys: dict[str, list]
):
    frequencies = {}

    for question, responses in surveys.items():
        question_freq = {}

        for response in responses:
            question_freq[response] = question_freq.get(response, 0) + 1

        frequencies[question] = question_freq

    return frequencies


# 35. Filtrar rutas según distancias máximas
def punto_35(
    routes: list[tuple[str, str, int | float]],
    max_distances: list[int | float],
):
    valid_routes = []

    for index, (origin, destination, distance) in enumerate(routes):
        if distance <= max_distances[index]:
            valid_routes.append((origin, destination, distance))

    return valid_routes


# 36. Actualizar inventario de múltiples tiendas
def punto_36(inventory: dict, store: str, **kwargs: int):
    if store not in inventory:
        inventory[store] = {}

    for product, quantity in kwargs.items():
        inventory[store][product] = inventory[store].get(product, 0) + quantity

    return inventory


# 37. Analizar tendencias de hashtags
def punto_37(
    hashtags: list[str],
    trends: list[tuple[str, int]],
    threshold: int,
):
    trend_freq = {tag: freq for tag, freq in trends}

    mention_counts = {}
    for tag in hashtags:
        mention_counts[tag] = mention_counts.get(tag, 0) + 1

    result = []
    seen = set()

    for tag in hashtags:
        if tag in seen:
            continue

        freq = trend_freq[tag] if tag in trend_freq else mention_counts.get(tag, 0)

        if freq > threshold:
            result.append(tag)
            seen.add(tag)

    return result


# 38. Actualizar suscripciones de usuarios
def punto_38(subscription_history: dict, **kwargs: object):
    user = kwargs["usuario"]
    subscription_type = kwargs["suscripcion"]

    if user not in subscription_history:
        subscription_history[user] = []

    record: dict[str, object] = {"tipo": subscription_type}
    for key, value in kwargs.items():
        if key not in ("usuario", "suscripcion"):
            record[key] = value

    subscription_history[user].append(record)

    return subscription_history


# 39. Simular operaciones del mercado bursátil
def punto_39(
    daily_prices: list[int | float],
    operations: list[tuple[str, int]],
):
    profit = 0

    for (action, day) in operations:
        price = daily_prices[day]

        if action == "compra":
            profit -= price
        elif action == "venta":
            profit += price

    return profit


# 40. Crear ranking de students por average
def punto_40(
    students: dict[int, dict[str, list]]
):
    overall_averages = {}

    for student_id, subjects in students.items():
        all_grades = []

        for grades in subjects.values():
            all_grades.extend(grades)

        overall_averages[student_id] = sum(all_grades) / len(all_grades)

    ranking = sorted(overall_averages.items(), key=lambda item: item[1], reverse=True)

    return ranking
