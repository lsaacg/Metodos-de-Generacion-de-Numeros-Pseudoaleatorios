print("|ALGORITMO CONGRUENCIAL ADITIVO|")

def congruencial_aditivo(semillas, k, m, cantidad):
    """
    Genera números pseudoaleatorios usando el método congruencial aditivo.
    
    Args:
        semillas (list): Lista de semillas iniciales [X0, X1, ..., Xk-1]
        k (int): Número de términos a considerar en la recurrencia
        m (int): Valor del módulo
        cantidad (int): Cantidad de números aleatorios a generar
        
    Returns:
        list: Lista de tuplas con (Xn+1, r) y la lista completa de números aleatorios
    """
    historial = semillas.copy()
    resultados = []
    numeros_aleatorios = []
    
    for n in range(len(semillas), len(semillas) + cantidad):
        # Calcular Xn+1 = (Xn + Xn-k) mod m
        xn = historial[n-1]
        xn_k = historial[n-k]
        xn_mas_1 = (xn + xn_k) % m
        
        # Calcular r = Xn+1 / m
        r = xn_mas_1 / m
        
        # Guardar resultados
        resultados.append((n-k, n-1, xn_k, xn, m, xn_mas_1, r))
        numeros_aleatorios.append(r)
        historial.append(xn_mas_1)
    
    return resultados, numeros_aleatorios


if __name__ == "__main__":
    semillas = [987, 173, 451]  # X0, X1, X2
    k = 2
    m = 1000
    cantidad_numeros = 5
    
    print(f"Generando {cantidad_numeros} números pseudoaleatorios con:")
    print(f"Semillas: {semillas}")
    print(f"k = {k}, m = {m}\n")
    
    resultados, aleatorios = congruencial_aditivo(semillas, k, m, cantidad_numeros)
    
    # Imprimir tabla similar al ejemplo
    print("k\tn\tXn-k\tXn\tM\tXn+1\tr")
    print("-" * 60)
    
    for res in resultados:
        print(f"{k}\t{res[0]}\t{res[2]}\t{res[3]}\t{res[4]}\t{res[5]}\t{res[6]:.3f}")
    
    print("\nNúmeros aleatorios generados:")
    for i, r in enumerate(aleatorios, 1):
        print(f"r{i} = {r:.3f}")