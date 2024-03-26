from math import fabs


def set_pixel(x, y): ...


# Digital Differential Analyzer, 디지털 차분 분석기 알고리즘
def DDA(x0, y0, x_end, y_end):
    # x0 != x_end 또는 y0 != y_end 이라고 가정
    assert x0 != x_end or y0 != y_end

    dx = x_end - x0
    dy = y_end - y0
    x = x0
    y = y0

    if fabs(dx) > fabs(dy):
        steps = fabs(dx)
    else:
        steps = fabs(dy)

    x_increment = dx / steps
    y_increment = dy / steps
    set_pixel(round(x), round(y))

    for _ in range(steps):
        x += x_increment
        y += y_increment
        set_pixel(round(x), round(y))


# Bresenham 선분 알고리즘
def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    diff = dy * 2
    error = 0
    y = y0

    points = []
    for x in range(x0, x1 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))

        error += diff
        if error >= dx:
            y += 1 if y1 > y0 else -1
            error -= dx * 2

    return points


# 선분의 기울기가 0과 1 사이인 경우의 Bresenham 알고리즘
def bresenham_line_with_slope_between_zero_and_one(xl, yl, xr, yr):
    y = yl
    H = yr - yl
    W = xr - xl

    F = 2 * H - W
    for x in range(xl, xr + 1):
        set_pixel(x, y)
        if F < 0:
            F += 2 * H
        else:
            y += 1
            F += 2 * (H - W)


# Bresenham 중간점 원 알고리즘
def bresenham_circle(xc, yc, r):
    def circle_points(xc, yc, x, y):
        set_pixel(xc + x, yc + y)
        set_pixel(xc - x, yc + y)
        set_pixel(xc + x, yc - y)
        set_pixel(xc - x, yc - y)
        set_pixel(xc + y, yc + x)
        set_pixel(xc - y, yc + x)
        set_pixel(xc + y, yc - x)
        set_pixel(xc - y, yc - x)

    # F의 초깃값의 정확한 계산식은 원래 1.25 - r 이며, 이를 1 - r로 근사하여
    # r이 정수인 경우엔 정수 연산만 하게끔 구현함
    F = 1 - r
    x = 0
    y = r

    circle_points(xc, yc, x, y)
    while y >= x:
        if F < 0:
            F += x * 2 + 3
        else:
            F += (x - y) * 2 + 5
            y -= 1

        x += 1
        circle_points(xc, yc, x, y)
