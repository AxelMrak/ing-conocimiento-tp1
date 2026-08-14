"""Casos de prueba para los puntos del practico."""
import builtins
import io
from contextlib import contextmanager, redirect_stdout

import practico_1


@contextmanager
def _ejecutar(func, entrada=None):
    buffer = io.StringIO()
    original_input = builtins.input
    if entrada is not None:
        builtins.input = lambda *args, **kwargs: entrada
    try:
        with redirect_stdout(buffer):
            func()
        yield buffer.getvalue()
    finally:
        builtins.input = original_input


def test_punto_1() -> int:
    with _ejecutar(practico_1.punto_1) as salida:
        casos = ["Mi Primer Código En Python." in salida]
    return sum(casos)


def test_punto_2() -> int:
    with _ejecutar(practico_1.punto_2) as salida:
        letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        casos = [letra in salida for letra in letras]
    return sum(casos)


def test_punto_3() -> int:
    with _ejecutar(practico_1.punto_3, entrada="  programacion  ") as salida:
        casos = [
            "Qué estás estudiando?" in salida,
            "Estoy estudiando Programacion." in salida,
        ]
    return sum(casos)


def test_punto_4() -> int:
    with _ejecutar(practico_1.punto_4, entrada="  argentina  ") as salida:
        casos = [
            "En qué país vives?" in salida,
            "Vivo en Argentina." in salida,
        ]
    return sum(casos)


def test_punto_5() -> int:
    with _ejecutar(practico_1.punto_5) as salida:
        casos = ["David Bowman" in salida, "51" in salida]
    return sum(casos)


def test_punto_6() -> int:
    with _ejecutar(practico_1.punto_6) as salida:
        casos = [
            "Julia" in salida,
            "Roberts" in salida,
            "Julia Roberts" in salida,
        ]
    return sum(casos)


def test_punto_7() -> int:
    with _ejecutar(practico_1.punto_7) as salida:
        casos = [
            "Ingeniería del Conocimiento" in salida,
            "materia" in salida,
        ]
    return sum(casos)


def test_punto_8() -> int:
    with _ejecutar(practico_1.punto_8) as salida:
        casos = ["35" in salida, "int" in salida]
    return sum(casos)


def test_punto_9() -> int:
    with _ejecutar(practico_1.punto_9) as salida:
        casos = ["Alberto" in salida, "43124" in salida]
    return sum(casos)


def test_punto_10() -> int:
    with _ejecutar(practico_1.punto_10) as salida:
        casos = ["32" in salida]
    return sum(casos)


def test_punto_11() -> int:
    with _ejecutar(practico_1.punto_11) as salida:
        casos = ["11" in salida]
    return sum(casos)

def test_punto_12() -> int:
    with _ejecutar(practico_1.punto_12, entrada=[ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]) as salida:
        casos = ["1200" in salida]
    return sum(casos)

def test_punto_13() -> int:
    with _ejecutar(practico_1.punto_13, entrada={
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}) as salida:
        casos = ["87.5" in salida, "83.0" in salida]
    return sum(casos)

def test_punto_14() -> int:
    with _ejecutar(practico_1.punto_14, entrada=[22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]) as salida:
        casos = ["23.07" in salida, "19.5" in salida, "26.5" in salida]
    return sum(casos)
