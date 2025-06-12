print("|ALGORITMO CONGRUENCIAL MULTIPLICATIVO|")

def congruencial_multiplicativo(semilla, k, m, cantidad):
    """
    Genera números pseudoaleatorios usando el método congruencial multiplicativo.
    
    Args:
        semilla (int): Semilla inicial (X0)
        k (int): Constante multiplicativa
        m (int): Valor del módulo
        cantidad (int): Cantidad de números aleatorios a generar
        
    Returns:
        list: Lista de tuplas con (Xn, Xn+1, r) y la lista completa de números aleatorios
    """
    resultados = []
    numeros_aleatorios = []
    xn = semilla
    
    for _ in range(cantidad):
        # Calcular Xn+1 = (k * Xn) mod m
        xn_mas_1 = (k * xn) % m
        
        # Calcular r = Xn+1 / m
        r = xn_mas_1 / m
        
        # Guardar resultados
        resultados.append((xn, xn_mas_1, r))
        numeros_aleatorios.append(r)
        
        # Actualizar Xn para la siguiente iteración
        xn = xn_mas_1
    
    return resultados, numeros_aleatorios


if __name__ == "__main__":
    X0 = 56
    k = 3
    m = 679
    cantidad_numeros = 5
    
    print(f"Generando {cantidad_numeros} números pseudoaleatorios con:")
    print(f"Semilla inicial (X0) = {X0}")
    print(f"Constante multiplicativa (k) = {k}")
    print(f"Módulo (m) = {m}\n")
    
    resultados, aleatorios = congruencial_multiplicativo(X0, k, m, cantidad_numeros)
    
    # Imprimir tabla similar al ejemplo
    print("k\tXn\tXn+1\tr")
    print("-" * 40)
    
    for i, res in enumerate(resultados):
        print(f"{k}\t{res[0]}\t{res[1]}\t{res[2]:.4f}")
    
    print("\nNúmeros aleatorios generados:")
    for i, r in enumerate(aleatorios, 1):
        print(f"r{i} = {r:.4f}")