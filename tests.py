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

