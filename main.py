"""Banco de pruebas local para el practico.

Importa el modulo `practico_1` y ejecuta cada funcion `punto_N` en orden.
Despues de cada punto corre sus casos de prueba (en `tests`) y muestra
cuantos pasaron. Las funciones son el entregable; este archivo solo
sirve para probarlas localmente.
"""
import practico_1
import tests


def main() -> None:
    for n in range(1, 41):
        funcion = getattr(practico_1, f"punto_{n}", None)
        if funcion is None:
            print(f"\n----- Punto {n}: NO EXISTE -----")
            continue

        print(f"\n----- Punto {n} -----")
        funcion()

        test = getattr(tests, f"test_punto_{n}", None)
        casos_ok = test() if test is not None else 0
        print(f"{casos_ok} caso(s) de test pasados con exito")


if __name__ == "__main__":
    main()
