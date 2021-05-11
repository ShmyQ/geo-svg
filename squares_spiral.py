import svgwrite
import math

iterations = 36
angle = 10
anglerad = math.radians(angle)
scale = 1 / (math.sin(anglerad) + math.cos(anglerad))

dwg = svgwrite.Drawing("images/test.svg", profile="full")

for i in range(iterations):
    rect = dwg.rect((-50, -50), (100, 100), stroke="black", fill="none")
    rect.rotate(angle * i)
    rect.scale(math.pow(scale, i))
    dwg.add(rect)

dwg.save()
