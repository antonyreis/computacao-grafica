import matplotlib.pyplot as plt

pixels = []

def putPixel(x, y):
    """Função para desenhar um pixel na posição (x, y)"""
    pixels.append((x, y))

def BresenhamHorizontal(x0, y0, x1, y1):
    """Bresenham para linhas mais horizontais"""
    if (x0 > x1): 
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dy < 0 else 1
    dy *= dir

    if dx != 0:
        y = y0
        p = 2*dy - dx

        for i in range(dx + 1):
            putPixel(x0 + i, y)

            if p >= 0:
                y += dir
                p = p - 2*dx

            p = p + 2*dy

def BresenhamVertical(x0, y0, x1, y1):
    """Bresenham para linhas mais verticais"""
    if (y0 > y1): 
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dx < 0 else 1
    dx *= dir

    if dy != 0:
        x = x0
        p = 2*dx - dy

        for i in range(dy + 1):
            putPixel(x, y0 + i)

            if p >= 0:
                x += dir
                p = p - 2*dy

            p = p + 2*dx

def BresenhamConsertado(x0, y0, x1, y1):
    """Função principal que decide qual usar"""
    global pixels
    pixels = []
    
    if abs(x1 - x0) > abs(y1 - y0):
        BresenhamHorizontal(x0, y0, x1, y1)
    else:
        BresenhamVertical(x0, y0, x1, y1)

def mostrar_linha():
    """Mostra a linha desenhada"""
    if not pixels:
        print("Nenhum pixel desenhado!")
        return
    
    x_coords = [p[0] for p in pixels]
    y_coords = [p[1] for p in pixels]
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x_coords, y_coords, c='blue', s=100, marker='s')
    plt.grid(True, alpha=0.3)
    plt.title('Linha desenhada com Bresenham (Grid 30x30)')
    plt.xlim(-1, 31)
    plt.ylim(-1, 31)
    plt.xticks(range(0, 31, 2))
    plt.yticks(range(0, 31, 2))
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    print("=== ALGORITMO DE BRESENHAM (Grid 30x30) ===")
    
    # Pedir coordenadas do primeiro ponto
    x0 = int(input("Digite x0 (0-30): "))
    y0 = int(input("Digite y0 (0-30): "))
    
    # Pedir coordenadas do segundo ponto
    x1 = int(input("Digite x1 (0-30): "))
    y1 = int(input("Digite y1 (0-30): "))
    
    # Desenhar a linha
    BresenhamConsertado(x0, y0, x1, y1)
    
    print(f"\nLinha de ({x0},{y0}) para ({x1},{y1})")
    print(f"Total de pixels: {len(pixels)}")
    print(f"Pixels: {pixels}")
    
    # Mostrar graficamente
    mostrar_linha()