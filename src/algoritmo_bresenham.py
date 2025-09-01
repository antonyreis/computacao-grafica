def putPixel(x, y):
    """Função para desenhar um pixel na posição (x, y)"""
    pass

# ALGORITMO ORIGINAL DE BRESENHAM (COMENTADO)
# Este algoritmo original só funciona para o primeiro octante (0° a 45°)
# onde dx > 0, dy > 0 e dx >= dy
# def Bresenham(x0, y0, x1, y1): 
#     dx = x1 - x0
#     dy = y1 - y0
#
#     if dx != 0:
#
#         y = y0
#         p = 2*dy - dx  # Parâmetro de decisão inicial
#
#         for i in range(dx + 1):
#             putPixel(x0 + i, y)
#
#             if p >= 0:
#                 y += 1      # Move para cima
#                 p = p - 2*dx
#
#             p = p + 2*dy

def BresenhamHorizontal(x0, y0, x1, y1):
    """
    BRESENHAM HORIZONTAL - Para linhas mais horizontais que verticais
    Usado quando |dx| > |dy| (octantes 1, 2, 7, 8)
    Itera sobre X e calcula Y correspondente
    """
    
    # VALIDAÇÃO 1: Garantir que sempre caminhamos da esquerda para direita
    # Se x0 > x1, trocar os pontos para normalizar a direção
    if (x0 > x1): 
        x0, x1 = x1, x0  # Troca coordenadas X
        y0, y1 = y1, y0  # Troca coordenadas Y correspondentes

    # Calcular deltas após possível troca de pontos
    dx = x1 - x0  # Delta X (sempre positivo após a troca)
    dy = y1 - y0  # Delta Y (pode ser positivo ou negativo)

    # VALIDAÇÃO 2: Determinar direção vertical
    # dir = -1 para linhas que descem (dy < 0)
    # dir = +1 para linhas que sobem (dy >= 0)
    dir = -1 if dy < 0 else 1
    dy *= dir  # Tornar dy sempre positivo para os cálculos

    # Verificar se há movimento horizontal (evitar divisão por zero)
    if dx != 0:
        y = y0  # Posição Y atual
        p = 2*dy - dx  # Parâmetro de decisão inicial de Bresenham

        # LOOP PRINCIPAL: Iterar sobre todos os pontos X
        for i in range(dx + 1):
            putPixel(x0 + i, y)  # Desenhar pixel na posição atual

            # DECISÃO DE BRESENHAM: Deve incrementar Y?
            if p >= 0:
                y += dir    # Mover Y na direção correta (subir ou descer)
                p = p - 2*dx  # Ajustar parâmetro de decisão

            p = p + 2*dy  # Atualizar parâmetro para próxima iteração

def BresenhamVertical(x0, y0, x1, y1):
    """
    BRESENHAM VERTICAL - Para linhas mais verticais que horizontais
    Usado quando |dy| > |dx| (octantes 3, 4, 5, 6)
    Itera sobre Y e calcula X correspondente
    """
    
    # VALIDAÇÃO 1: Garantir que sempre caminhamos de baixo para cima
    # Se y0 > y1, trocar os pontos para normalizar a direção
    if (y0 > y1): 
        x0, x1 = x1, x0  # Troca coordenadas X correspondentes
        y0, y1 = y1, y0  # Troca coordenadas Y

    # Calcular deltas após possível troca de pontos
    dx = x1 - x0  # Delta X (pode ser positivo ou negativo)
    dy = y1 - y0  # Delta Y (sempre positivo após a troca)

    # VALIDAÇÃO 2: Determinar direção horizontal
    # dir = -1 para linhas que vão para esquerda (dx < 0)
    # dir = +1 para linhas que vão para direita (dx >= 0)
    dir = -1 if dx < 0 else 1
    dx *= dir  # Tornar dx sempre positivo para os cálculos

    # Verificar se há movimento vertical (evitar divisão por zero)
    if dy != 0:
        x = x0  # Posição X atual
        p = 2*dx - dy  # Parâmetro de decisão inicial de Bresenham

        # LOOP PRINCIPAL: Iterar sobre todos os pontos Y
        for i in range(dy + 1):
            putPixel(x, y0 + i)  # Desenhar pixel na posição atual

            # DECISÃO DE BRESENHAM: Deve incrementar X?
            if p >= 0:
                x += dir    # Mover X na direção correta (esquerda ou direita)
                p = p - 2*dy  # Ajustar parâmetro de decisão

            p = p + 2*dx  # Atualizar parâmetro para próxima iteração

def BresenhamConsertado(x0, y0, x1, y1):
    """
    FUNÇÃO PRINCIPAL - Decide qual algoritmo usar baseado na inclinação da linha
    
    CONCEITO DOS OCTANTES:
    O plano cartesiano é dividido em 8 octantes baseados na inclinação da linha:
    - Octantes 1,2,7,8: |dx| > |dy| → Linha mais horizontal → Usar BresenhamHorizontal
    - Octantes 3,4,5,6: |dy| > |dx| → Linha mais vertical → Usar BresenhamVertical
    
    Esta divisão garante que sempre iteramos sobre a coordenada com maior variação,
    minimizando erros de aproximação e garantindo que todos os pixels sejam desenhados.
    """
    
    # DECISÃO PRINCIPAL: Comparar magnitudes dos deltas
    if abs(x1 - x0) > abs(y1 - y0):
        # Linha é mais horizontal que vertical
        # Usar algoritmo que itera sobre X
        BresenhamHorizontal(x0, y0, x1, y1)
    else:
        # Linha é mais vertical que horizontal (ou diagonal 45°)
        # Usar algoritmo que itera sobre Y
        BresenhamVertical(x0, y0, x1, y1)

"""
RESUMO DA SOLUÇÃO:

O algoritmo original de Bresenham só funcionava para o primeiro octante porque:
1. Assumia dx > 0 (movimento sempre para direita)
2. Assumia dy > 0 (movimento sempre para cima)  
3. Assumia dx >= dy (linha mais horizontal que vertical)

Para corrigir isso e cobrir todos os 8 octantes, foram feitas as seguintes adaptações:

1. NORMALIZAÇÃO DE DIREÇÃO:
   - BresenhamHorizontal: Garante x0 <= x1 trocando pontos se necessário
   - BresenhamVertical: Garante y0 <= y1 trocando pontos se necessário

2. TRATAMENTO DE SINAIS:
   - Usa variável 'dir' para controlar direção de incremento
   - Torna deltas sempre positivos para cálculos, mas incrementa na direção correta

3. SELEÇÃO DE ALGORITMO:
   - Compara |dx| vs |dy| para escolher qual coordenada iterar
   - Garante que sempre iteramos sobre a coordenada com maior variação

4. REUTILIZAÇÃO DA LÓGICA ORIGINAL:
   - Mantém o mesmo parâmetro de decisão (p) do algoritmo original
   - Apenas adapta para diferentes direções e orientações

Resultado: Algoritmo funciona perfeitamente em todos os 8 octantes mantendo
a eficiência e precisão do algoritmo original de Bresenham.
"""