"""Casos de prueba para los puntos del práctico.
Usa solo la librería estándar.
"""
import io
from contextlib import contextmanager, redirect_stdout
from unittest.mock import patch

import practico_1


@contextmanager
def _ejecutar(func, *args, entrada=None, **kwargs):
    salida = io.StringIO()
    try:
        if entrada is None:
            with redirect_stdout(salida):
                func(*args, **kwargs)
        else:
            with patch("builtins.input", return_value=entrada):
                with redirect_stdout(salida):
                    func(*args, **kwargs)
        yield salida.getvalue()
    except Exception:
        print("--- DEBUG FN ---")
        print(salida.getvalue())
        print("----------------------------")
        raise


def test_punto_1() -> None:
    with _ejecutar(practico_1.punto_1) as salida:
        assert "Mi Primer Código En Python." in salida


def test_punto_2() -> None:
    with _ejecutar(practico_1.punto_2) as salida:
        for letra in "ABCDEFGHI":
            assert letra in salida


def test_punto_3() -> None:
    with _ejecutar(practico_1.punto_3, entrada="  programacion  ") as salida:
        assert "Qué estás estudiando?" in salida
        assert "Estoy estudiando Programacion." in salida


def test_punto_4() -> None:
    with _ejecutar(practico_1.punto_4, entrada="  argentina  ") as salida:
        assert "En qué país vives?" in salida
        assert "Vivo en Argentina." in salida


def test_punto_5() -> None:
    with _ejecutar(practico_1.punto_5) as salida:
        assert "David Bowman" in salida
        assert "51" in salida


def test_punto_6() -> None:
    with _ejecutar(practico_1.punto_6) as salida:
        assert "Julia" in salida
        assert "Roberts" in salida
        assert "Julia Roberts" in salida


def test_punto_7() -> None:
    with _ejecutar(practico_1.punto_7) as salida:
        assert "Ingeniería del Conocimiento" in salida
        assert "materia" in salida


def test_punto_8() -> None:
    with _ejecutar(practico_1.punto_8) as salida:
        assert "35" in salida
        assert "int" in salida


def test_punto_9() -> None:
    with _ejecutar(practico_1.punto_9) as salida:
        assert "Alberto" in salida
        assert "43124" in salida


def test_punto_10() -> None:
    with _ejecutar(practico_1.punto_10) as salida:
        assert "32" in salida


def test_punto_11() -> None:
    with _ejecutar(practico_1.punto_11) as salida:
        assert "11" in salida


def test_punto_12() -> None:
    productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]
    with _ejecutar(practico_1.punto_12, productos) as salida:
        assert "1200" in salida


def test_punto_13() -> None:
    estudiantes = {
        101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
        102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}},
    }
    with _ejecutar(practico_1.punto_13, estudiantes) as salida:
        assert "87.5" in salida
        assert "83.0" in salida


def test_punto_14() -> None:
    temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
    with _ejecutar(practico_1.punto_14, temperaturas) as salida:
        assert "23.07" in salida
        assert "19.5" in salida
        assert "26.5" in salida


def test_punto_15() -> None:
    with _ejecutar(practico_1.punto_15, 85, 90, 78, 92) as salida:
        assert "86.25" in salida

def test_punto_16() -> None:
    datos = {
        "nombre": "Luis",
        "edad": 25,
        "email": "juan@mail.com",
        "ciudad": "Mendoza",
        "n valor": "Camus",
    }
    assert practico_1.punto_16(**datos) == datos
    assert practico_1.punto_16() == {}

def test_punto_17() -> None:
    casos = [
        (
            {
                1: ("Ana", 30, 3000),
                2: ("Luis", 25, 2500),
                3: ("Maria", 35, 4000),
            },
            2500,
            {1: ("Ana", 30, 3000), 3: ("Maria", 35, 4000)},
        ),
        (
            {
                1: ("Ana", 30, 3000),
                2: ("Luis", 25, 2500),
                3: ("Maria", 35, 4000),
            },
            3000,
            {3: ("Maria", 35, 4000)},
        ),
        (
            {},
            2500,
            {},
        ),
        (
            {10: ("Pedro", 40, 1500), 11: ("Sara", 28, 2000)},
            3000,
            {},
        ),
    ]
    for empleados, umbral, esperado in casos:
        assert practico_1.punto_17(empleados, umbral) == esperado

def test_punto_18() -> None:
    casos = [
        (
            [200, 450, 300, 400, 350, 500, 600],
            (2800, 400.0),
        ),
        (
            [100, 200, 150, 300, 250],
            (1000, 200.0),
        ),
        (
            [],
            (0, 0.0),
        ),
    ]

    for ventas, esperado in casos:
        assert practico_1.punto_18(ventas) == esperado

def test_punto_19() -> None:
    casos = [
        (
            {
                "Equipo A": (3, 2),
                "Equipo B": (1, 1),
                "Equipo C": (4, 0)
            },
            (8, 3)
        ),
        (
            {
                "Equipo X": (2, 3),
                "Equipo Y": (0, 1),
                "Equipo Z": (5, 2)
            },
            (7, 6)
        ),
        (
            {
                "Boca Juniors": (3, 1),
                "Independiente": (5, 2),
                "Estudiantes": (1, 3)
            },
            (9, 6)
        ),
        (
            {},
            (0, 0)
        ),
    ]

    for resultados, esperado in casos:
        assert practico_1.punto_19(resultados) == esperado

def test_punto_20() -> None:
    casos = [
        (
            {
                "modo_oscuro": True, "idioma": "es", "notificaciones": False
            },
            {
                "modo_oscuro": True, "idioma": "es", "notificaciones": False
            }
        ),
        (
            {
                "modo_oscuro": False, "idioma": "en", "notificaciones": True
            },
            {
                "modo_oscuro": False, "idioma": "en", "notificaciones": True
            }
        ),
        (
            {},
            {
                "modo_oscuro": False, "idioma": "es", "notificaciones": False
            }
        )
    ]

    for configuraciones, esperado in casos:
        assert practico_1.punto_20(**configuraciones) == esperado

def test_punto_21() -> None:
    casos = [
        (
            [("Ana", 85), ("Luis", 90), ("María", 78)],
            [("Luis", 90), ("Ana", 85), ("María", 78)]
        ),
        (
            [("Pedro", 70), ("Sara", 95), ("Juan", 80)],
            [("Sara", 95), ("Juan", 80), ("Pedro", 70)]
        ),
        (
            [],
            []
        )
    ]

    for estudiantes, esperado in casos:
        assert practico_1.punto_21(estudiantes) == esperado


def test_punto_22() -> None:
    casos = [
        (
            [
                ("Paris", 200, 5),
                ("Roma", 150, 4),
                ("Londres", 180, 3)
            ],
            {
                "Paris": 1000,
                "Roma": 600,
                "Londres": 540
            }
        ),
        (
            [
                ("Madrid", 120, 6),
                ("Berlin", 90, 5),
                ("Lisboa", 80, 4)
            ],
            {
                "Madrid": 720,
                "Berlin": 450,
                "Lisboa": 320
            }
        ),
        (
            [],
            {}
        )
    ]

    for viajes, esperado in casos:
        assert practico_1.punto_22(viajes) == esperado

def test_punto_23() -> None:
    casos = [
        (
           [
                50, 30, 20, 10
            ],
            [
                5, 10, 5, 2
            ],
            [
                45, 20, 15, 8
            ]
        ),
        (
            [
                100, 200, 150
            ],
            [
                20, 50, 30
            ],
            [
                80, 150, 120
            ]
        ),
        (
            [],
            [],
            []
        )
    ]

    for inventario, ventas, esperado in casos:
        assert practico_1.punto_23(inventario, ventas) == esperado

def test_punto_24() -> None:
    with _ejecutar(practico_1.punto_24, "Concierto", "Exposición de arte", "Conferencia") as salida:
        assert "[1] Concierto" in salida
        assert "[2] Exposición de arte" in salida
        assert "[3] Conferencia" in salida

    with _ejecutar(practico_1.punto_24, "Feria", "Festival") as salida:
        assert "[1] Feria" in salida
        assert "[2] Festival" in salida

    with _ejecutar(practico_1.punto_24) as salida:
        assert "No hay eventos disponibles." in salida

def test_punto_25() -> None:
    casos = [
        (
            {
                "sueldo": 2000,
                "renta": -800,
                "transporte": -150,
                "comida": -300,
                "freelance": 500,
            },
            1250,
        ),
        (
            {
                "sueldo": 3000,
                "renta": -1000,
                "transporte": -200,
                "comida": -400,
                "freelance": 800,
            },
            2200,
        ),
        (
            {
                "sueldo": 1500,
                "renta": -600,
                "transporte": -100,
                "comida": -200,
                "freelance": 300,
            },
            900,
        ),
        (
            {},
            0,
        ),
    ]

    for kwargs, esperado in casos:
        assert practico_1.punto_25(**kwargs) == esperado


def test_punto_26() -> None:
    casos = [
        (
            ("Ana", 30, 3000),
            {"direccion": "Calle Falsa 123", "telefono": "123456789"},
            {
                "nombre": "Ana",
                "edad": 30,
                "salario": 3000,
                "direccion": "Calle Falsa 123",
                "telefono": "123456789",
            },
        ),
        (
            ("Luis", 25, 2500),
            {},
            {
                "nombre": "Luis",
                "edad": 25,
                "salario": 2500,
            },
        ),
        (
            ("María", 40, 5000),
            {"ciudad": "Rosario", "activo": True},
            {
                "nombre": "María",
                "edad": 40,
                "salario": 5000,
                "ciudad": "Rosario",
                "activo": True,
            },
        ),
    ]

    for args, kwargs, esperado in casos:
        assert practico_1.punto_26(*args, **kwargs) == esperado


def test_punto_27() -> None:
    casos = [
        (
            [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500],
            {"total": 41900, "promedio": 41900 / 12, "mes_mayor_venta": 12},
        ),
        (
            [100, 200, 150],
            {"total": 450, "promedio": 150.0, "mes_mayor_venta": 2},
        ),
        (
            [],
            {"total": 0, "promedio": 0.0, "mes_mayor_venta": None},
        ),
    ]

    for ventas, esperado in casos:
        assert practico_1.punto_27(ventas) == esperado


def test_punto_28() -> None:
    casos = [
        (
            {
                "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
                "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
                "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"},
            },
            ["El código Da Vinci"],
        ),
        (
            {
                "1984": {"autor": "George Orwell", "año": 1949, "género": "Distopía"},
                "Fahrenheit 451": {"autor": "Ray Bradbury", "año": 1953, "género": "Distopía"},
            },
            [],
        ),
        (
            {},
            [],
        ),
    ]

    for biblioteca, esperado in casos:
        assert practico_1.punto_28(biblioteca) == esperado


def test_punto_29() -> None:
    casos = [
        (
            [
                ("Ana", [85, 90, 78]),
                ("Luis", [88, 92, 80]),
                ("María", [75, 85, 70]),
            ],
            {"Ana": 253 / 3, "Luis": 260 / 3, "María": 230 / 3},
        ),
        (
            [
                ("Pedro", [100, 100, 100]),
                ("Sara", [60, 70, 80]),
            ],
            {"Pedro": 100.0, "Sara": 70.0},
        ),
        (
            [],
            {},
        ),
    ]

    for notas, esperado in casos:
        assert practico_1.punto_29(notas) == esperado


def test_punto_30() -> None:
    casos = [
        (
            ["Ana", "Luis", "María"],
            {"idioma": "es", "modo_oscuro": True, "notificaciones": False},
            {
                "Ana": ["es", True, False],
                "Luis": ["es", True, False],
                "María": ["es", True, False],
            },
        ),
        (
            ["Juan", "Pedro"],
            {"tema": "oscuro", "fuente": "grande"},
            {
                "Juan": ["oscuro", "grande"],
                "Pedro": ["oscuro", "grande"],
            },
        ),
        (
            [],
            {"idioma": "en"},
            {},
        ),
    ]

    for usuarios, kwargs, esperado in casos:
        assert practico_1.punto_30(usuarios, **kwargs) == esperado


def test_punto_31() -> None:
    casos = [
        (
            ("Juan", "Mi primer post!"),
            {"etiquetas": ["#hola", "#primerPost"], "visibilidad": "publica", "likes": 100},
            {
                "usuario": "Juan",
                "texto": "Mi primer post!",
                "etiquetas": ["#hola", "#primerPost"],
                "visibilidad": "publica",
                "likes": 100,
            },
        ),
        (
            ("Ana", "Hola mundo"),
            {},
            {
                "usuario": "Ana",
                "texto": "Hola mundo",
            },
        ),
        (
            ("Luis", "Promoción"),
            {"etiquetas": ["#oferta"], "comentarios": True},
            {
                "usuario": "Luis",
                "texto": "Promoción",
                "etiquetas": ["#oferta"],
                "comentarios": True,
            },
        ),
    ]

    for args, kwargs, esperado in casos:
        assert practico_1.punto_31(*args, **kwargs) == esperado


def test_punto_32() -> None:
    casos = [
        (
            (("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0)),
            425.0,
        ),
        (
            (("X", 2, 10.0), ("Y", 3, 5.0)),
            35.0,
        ),
        (
            (),
            0,
        ),
    ]

    for sales, esperado in casos:
        assert practico_1.punto_32(*sales) == esperado


def test_punto_33() -> None:
    casos = [
        (
            {
                "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
                "2024-08-16": [("Luis", 101, 150)],
            },
            "2024-08-15", "Pedro", 103, 200,
            {
                "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180), ("Pedro", 103, 200)],
                "2024-08-16": [("Luis", 101, 150)],
            },
        ),
        (
            {
                "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
                "2024-08-16": [("Luis", 101, 150)],
            },
            "2024-08-15", "Pedro", 101, 200,
            {
                "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
                "2024-08-16": [("Luis", 101, 150)],
            },
        ),
    ]

    for reservations, date, guest, room, price, esperado in casos:
        assert practico_1.punto_33(reservations, date, guest, room, price) == esperado


def test_punto_34() -> None:
    casos = [
        (
            {
                "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
                "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0],
            },
            {
                "¿Cómo califica el servicio?": {5: 3, 4: 2, 3: 1},
                "¿Recomendaría nuestro producto?": {1: 4, 0: 2},
            },
        ),
        (
            {"Pregunta": [1, 1, 1]},
            {"Pregunta": {1: 3}},
        ),
        (
            {},
            {},
        ),
    ]

    for surveys, esperado in casos:
        assert practico_1.punto_34(surveys) == esperado


def test_punto_35() -> None:
    casos = [
        (
            [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)],
            [600, 400, 500],
            [("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)],
        ),
        (
            [("A", "B", 100)],
            [50],
            [],
        ),
        (
            [("A", "B", 100)],
            [200],
            [("A", "B", 100)],
        ),
    ]

    for routes, max_distances, esperado in casos:
        assert practico_1.punto_35(routes, max_distances) == esperado


def test_punto_36() -> None:
    casos = [
        (
            {"Tienda A": {"producto_1": 50, "producto_2": 30}, "Tienda B": {"producto_1": 20, "producto_2": 40}},
            "Tienda A",
            {"producto_1": 10, "producto_2": -5},
            {"Tienda A": {"producto_1": 60, "producto_2": 25}, "Tienda B": {"producto_1": 20, "producto_2": 40}},
        ),
        (
            {"Tienda A": {"producto_1": 50, "producto_2": 30}, "Tienda B": {"producto_1": 20, "producto_2": 40}},
            "Tienda C",
            {"producto_1": 5},
            {"Tienda A": {"producto_1": 50, "producto_2": 30}, "Tienda B": {"producto_1": 20, "producto_2": 40}, "Tienda C": {"producto_1": 5}},
        ),
    ]

    for inventory, store, kwargs, esperado in casos:
        assert practico_1.punto_36(inventory, store, **kwargs) == esperado


def test_punto_37() -> None:
    casos = [
        (
            ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"],
            [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)],
            50,
            ["#verano", "#moda", "#tecnologia"],
        ),
        (
            ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"],
            [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)],
            100,
            ["#verano", "#tecnologia"],
        ),
        (
            ["#a", "#a", "#b"],
            [("#a", 10), ("#b", 3)],
            5,
            ["#a"],
        ),
    ]

    for hashtags, trends, threshold, esperado in casos:
        assert practico_1.punto_37(hashtags, trends, threshold) == esperado


def test_punto_38() -> None:
    casos = [
        (
            {"Jose": ["mensual", "anual"], "Ana": ["mensual"]},
            {"usuario": "Luis", "suscripcion": "mensual", "auto_renovacion": True},
            {"Jose": ["mensual", "anual"], "Ana": ["mensual"], "Luis": [{"tipo": "mensual", "auto_renovacion": True}]},
        ),
        (
            {"Jose": ["mensual"]},
            {"usuario": "Jose", "suscripcion": "anual"},
            {"Jose": ["mensual", {"tipo": "anual"}]},
        ),
    ]

    for history, kwargs, esperado in casos:
        assert practico_1.punto_38(history, **kwargs) == esperado


def test_punto_39() -> None:
    casos = [
        (
            [100, 105, 102, 110, 108],
            [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)],
            16,
        ),
        (
            [50, 60, 55],
            [("compra", 0), ("venta", 2)],
            5,
        ),
        (
            [10, 20],
            [],
            0,
        ),
    ]

    for prices, operations, esperado in casos:
        assert practico_1.punto_39(prices, operations) == esperado


def test_punto_40() -> None:
    casos = [
        (
            {
                101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
                102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
                103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]},
            },
            [(103, 528 / 6), (101, 506 / 6), (102, 504 / 6)],
        ),
    ]

    for students, esperado in casos:
        assert practico_1.punto_40(students) == esperado
