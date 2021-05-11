import svgwrite
import math

eight_side = 1 + 2 / math.sqrt(2)
six_side = math.sqrt(3)
four_side = 1

angle = 15
iterations = int(360 / angle)
width = 100

length = width * four_side

dwg = svgwrite.Drawing("images/test.svg", profile="full")

for i in range(iterations):
    rect = dwg.rect((-length / 2, -width / 2), (length, width), stroke="black")
    rect.fill(opacity=0)
    rect.rotate(angle * i)
    dwg.add(rect)

dwg.save()
