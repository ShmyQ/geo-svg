import svgwrite
import math

iterations = 18
angle = 5
angle_rad = math.radians(angle)
scale = 1 / (math.sin(angle_rad) + math.cos(angle_rad))

dwg = svgwrite.Drawing("images/test.svg", profile="full")

for i in range(iterations):
    rect = dwg.rect((-50, -50), (100, 100), stroke="black")
    rect.fill("blue", opacity=0)
    rect.rotate(angle * i)
    # rect.scale(math.pow(scale,i))
    dwg.add(rect)

dwg.save()
