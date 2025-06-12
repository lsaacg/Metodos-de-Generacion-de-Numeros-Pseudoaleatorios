print("|ALGORITMO PRODUCTO MEDIO|")

def producto_medio(semilla1, semilla2, cantidad):
    """
    Genera números pseudoaleatorios usando el método de producto medio.
    
    Args:
        semilla1 (int): Primera semilla (X0)
        semilla2 (int): Segunda semilla (X1)
        cantidad (int): Cantidad de números aleatorios a generar
        
    Returns:
        list: Lista de números aleatorios entre 0 y 1
    """
    numeros = []
    xn_2 = semilla1  # Xn-2
    xn_1 = semilla2  # Xn-1
    digitos = max(len(str(semilla1)), len(str(semilla2)))
    
    for _ in range(cantidad):
        # Paso 1: Multiplicar los dos valores anteriores
        producto = xn_2 * xn_1
        
        # Paso 2: Extraer dígitos centrales
        str_producto = str(producto).zfill(2 * digitos)
        inicio = (len(str_producto) - digitos) // 2
        xn = int(str_producto[inicio:inicio + digitos])
        
        # Paso 3: Convertir a valor entre 0 y 1
        r = xn / (10 ** digitos)
        numeros.append(r)
        
        # Actualizar valores para siguiente iteración
        xn_2, xn_1 = xn_1, xn
        
    return numeros


if __name__ == "__main__":
    X0 = 17
    X1 = 23
    cantidad_numeros = 5
    
    print(f"Generando {cantidad_numeros} números pseudoaleatorios con semillas {X0} y {X1}:")
    aleatorios = producto_medio(X0, X1, cantidad_numeros)
    
    # Imprimir tabla similar al ejemplo
    print("\nTabla de resultados:")
    print("Xn-2\tXn-1\tProducto\tr")
    print("-" * 30)
    
    xn_2, xn_1 = X0, X1
    for r in aleatorios:
        producto = xn_2 * xn_1
        print(f"{xn_2}\t{xn_1}\t{producto}\t{r:.2f}")
        xn_2, xn_1 = xn_1, int(r * (10 ** len(str(X0))))