def putPixel(x, y):
    pass

# def Bresenham(x0, y0, x1, y1): 
#     dx = x1 - x0
#     dy = y1 - y0

#     if dx != 0:

#         y = y0
#         p = 2*dy - dx

#         for i in range(dx + 1):
#             putPixel(x0 + i, y)

#             if p >= 0:
#                 y += 1
#                 p = p - 2*dx

#             p = p + 2*dy

def BresenhamHorizontal(x0, y0, x1, y1):
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
    if abs(x1 - x0) > abs(y1 - y0):
        BresenhamHorizontal(x0, y0, x1, y1)
    else:
        BresenhamVertical(x0, y0, x1, y1)