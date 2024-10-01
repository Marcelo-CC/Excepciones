class NumeroNaturalError(Exception):
    """Excepción personalizada para manejar números no naturales."""
    pass

def obtener_numero_natural():
    while True:
        try:
            numero = float(input("Ingrese un número natural: "))
            if numero < 1 or not numero.is_integer():
                raise NumeroNaturalError("El número debe ser un natural (entero y mayor o igual a 1).")
            return int(numero)  # Convertir a entero
        except ValueError:
            print("Debe ser un número válido (int o float).")
        except NumeroNaturalError as e:
            print(e)
        else:
            print("Número ingresado correctamente.")
        finally:
            print("Intentando ingresar un número natural...")

def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
