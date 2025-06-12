print("|ALGORITMO PRODUCTO MEDIO MODIFICADO|")

def producto_medio_modificado(semilla, constante, cantidad):
    """
    Genera números pseudoaleatorios usando el método de producto medio modificado.
    
    Args:
        semilla (int): Semilla inicial (X0)
        constante (int): Constante multiplicativa (K)
        cantidad (int): Cantidad de números aleatorios a generar
        
    Returns:
        list: Lista de números aleatorios entre 0 y 1
    """
    numeros = []
    xn = semilla
    digitos = len(str(semilla))
    
    for _ in range(cantidad):
        # Paso 1: Multiplicar la constante por el valor actual
        producto = constante * xn
        
        # Paso 2: Extraer dígitos centrales
        str_producto = str(producto).zfill(2 * digitos)
        inicio = (len(str_producto) - digitos) // 2
        xn = int(str_producto[inicio:inicio + digitos])
        
        # Paso 3: Convertir a valor entre 0 y 1
        r = xn / (10 ** digitos)
        numeros.append(r)
        
    return numeros


if __name__ == "__main__":
    X0 = 17
    K = 23
    cantidad_numeros = 4
    
    print(f"Generando {cantidad_numeros} números pseudoaleatorios con semilla {X0} y constante {K}:")
    aleatorios = producto_medio_modificado(X0, K, cantidad_numeros)
    
    # Imprimir tabla similar al ejemplo
    print("\nTabla de resultados:")
    print("K\tXn\tProducto\tr")
    print("-" * 30)
    
    xn = X0
    for r in aleatorios:
        producto = K * xn
        print(f"{K}\t{xn}\t{producto}\t{r:.2f}")
        xn = int(r * (10 ** len(str(X0))))