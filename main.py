"""Runner de tests local para el práctico.
Ejecuta cada test_punto_N y reporta éxito o fallo.
"""
import tests


def main() -> None:
    for n in range(1, 41):
        print(f"\n----- Punto {n} -----")

        test = getattr(tests, f"test_punto_{n}", None)

        if test is None:
            print("⨯ Test no encontrado.")
            break

        try:
            test()
        except AssertionError as error:
            print(f"⨯ Test fallido: {error}")

            break
        except Exception as error:
            print(f"⨯ Error inesperado: {error}")
            break
        else:
            print("✔︎ Test pasado con éxito")


if __name__ == "__main__":
    main()
