import svgwrite
import math

points = 1000
c = 0.5
angle = 360 / math.pow((1 + math.sqrt(5)) / 2, 2)

dwg = svgwrite.Drawing("images/test.svg", profile="full")


def phyllo_circles():
    for n in range(1, points):
        theta = math.radians(angle) * n
        r = c * n
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        circle = dwg.circle(
            center=(x, y), r=r / math.sqrt(n), stroke="none", fill="black"
        )
        dwg.add(circle)


def px(n):
    return n * math.cos(n * math.radians(angle))


def py(n):
    return n * math.sin(n * math.radians(angle))


def phy_dis(n1, n2):
    return math.sqrt(math.pow(px(n1) - px(n2), 2) + math.pow(py(n1) - py(n2), 2))


def circle_rad(n):
    return (phy_dis(n, n + 13) + phy_dis(n, n + 34) - phy_dis(n, n + 21)) / 2


def phyllo_circles_full():
    for n in range(50, points):
        x = px(n)
        y = py(n)
        # circleRadius = circle_rad(n)
        circleRadius = math.sqrt(n)
        circle = dwg.circle(center=(x, y), r=circleRadius, stroke="black", fill="none")
        dwg.add(circle)


def phyllo_numbered():
    c = 10
    for n in range(points):
        theta = math.radians(angle) * n
        r = c * math.sqrt(n)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        circle = dwg.circle(center=(x, y), r=c / 2, stroke="black", fill="none")
        dwg.add(circle)
        dwg.add(dwg.text(str(n), insert=(x, y)))


def is_perf_square(x):
    rounded = int(math.sqrt(x))
    return rounded * rounded == x


def is_fibo(x):
    return is_perf_square(5 * x * x + 4) or is_perf_square(5 * x * x - 4)


def phyllo_lines():
    for fibo in [21, 34]:
        for i in range(fibo):
            x2 = y2 = None
            for n in range(points):
                if n % fibo == i:
                    theta = math.radians(angle) * n
                    r = c * n
                    x = r * math.cos(theta)
                    y = r * math.sin(theta)
                    if x2 is not None:
                        dwg.add(
                            dwg.line(
                                start=(x2, y2), end=(x, y), stroke="blue", fill="none"
                            )
                        )
                    x2 = x
                    y2 = y


def enclosing_circle():
    # get the max point
    theta = math.radians(angle) * points
    r = c * points + 2 * c * math.sqrt(points)  # add 2x circle radius to get outside
    dwg.add(dwg.circle(center=(0, 0), r=r, stroke="red", fill="none"))


# phyllo_numbered()
# phyllo_circles()
# phyllo_lines()
# enclosing_circle()
phyllo_circles()

dwg.save()
