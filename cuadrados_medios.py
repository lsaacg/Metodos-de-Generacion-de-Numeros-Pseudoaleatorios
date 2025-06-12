print("|ALGORITMO CUADRADOS MEDIOS|")
def cuadrados_medios(semilla, cantidad):
    """
    Genera números pseudoaleatorios usando el método de cuadrados medios.
    
    Args:
        semilla (int): Semilla inicial (valor entero positivo)
        cantidad (int): Cantidad de números aleatorios a generar
        
    Returns:
        list: Lista de números aleatorios entre 0 y 1
    """
    numeros = []
    x = semilla
    digitos = len(str(semilla))
    
    for _ in range(cantidad):
        # Paso 2: Elevar al cuadrado
        cuadrado = x * x
        
        # Paso 3: Extraer dígitos centrales
        str_cuadrado = str(cuadrado).zfill(2 * digitos)
        inicio = (len(str_cuadrado) - digitos) // 2
        x = int(str_cuadrado[inicio:inicio + digitos])
        
        # Paso 4: Convertir a valor entre 0 y 1
        r = x / (10 ** digitos)
        numeros.append(r)
        
    return numeros


if __name__ == "__main__":
    semilla = 4561
    cantidad_numeros = 4
    
    print(f"Generando {cantidad_numeros} números pseudoaleatorios con semilla {semilla}:")
    aleatorios = cuadrados_medios(semilla, cantidad_numeros)
    
    for i, r in enumerate(aleatorios, 1):
        print(f"r{i} = {r:.4f}")