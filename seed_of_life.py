import svgwrite
import math

r = 100

dwg = svgwrite.Drawing("images/test.svg", profile="full")

for i in range(6):
    x = r * math.cos(math.pi * 2 * i / 6)
    y = r * math.sin(math.pi * 2 * i / 6)
    print(x, y)
    circle = dwg.circle(center=(x, y), r=r, stroke="black", fill="none")
    dwg.add(circle)

circle = dwg.circle(center=(0, 0), r=r, stroke="black", fill="none")
dwg.add(circle)

dwg.save()
