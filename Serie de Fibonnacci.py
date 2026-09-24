def generar_fibonacci_hasta(limite):
    """Genera la lista de Fibonacci necesaria para cubrir el valor ingresado."""
    fib = [0, 1, 1]
    while fib[-1] < limite:
        fib.append(fib[-1] + fib[-2])
    return fib


def millas_a_km_fibonacci(millas):
    """Convierte millas a km usando la serie de Fibonacci."""
    fib = generar_fibonacci_hasta(millas * 2)

    # Si el valor exacto está en Fibonacci, tomamos el siguiente
    if millas in fib:
        idx = fib.index(millas)
        return fib[idx + 1]

    # Si no es un número exacto de Fibonacci, lo descomponemos en sumas
    # (Ejemplo: 10 millas = 8 + 2 -> 13 + 3 = 16 km)
    resto = millas
    km_aproximado = 0

    for num in reversed(fib):
        if num > 0 and num <= resto:
            idx = fib.index(num)
            km_aproximado += fib[idx + 1]
            resto -= num
            if resto == 0:
                break

    return km_aproximado


# --- Demostración ---
millas_input = 10
km_fib = millas_a_km_fibonacci(millas_input)
km_real = millas_input * 1.60934

print(f"Millas a convertir: {millas_input}")
print(f"Resultado con Fibonacci: {km_fib} km")
print(f"Resultado exacto real: {km_real:.2f} km")