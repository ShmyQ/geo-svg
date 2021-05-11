import svgwrite
import math

# The scale factor only works with octogons, looks like each scaling factor is unique
# Is there a way to calculate the scaling factor given n?
n = 8
r = 100
layers = 10
angle = 5
anglerad = math.radians(angle)
scale = 1 / ((math.sqrt(2) - 1) * math.sin(anglerad) + math.cos(anglerad))

dwg = svgwrite.Drawing("images/test.svg", profile="full")

for i in range(layers):
    path = dwg.path("m0,0", stroke="black", fill="none")

    # Construct ngon
    for j in range(n):
        x = r * math.cos(math.pi * 2 * j / n)
        y = r * math.sin(math.pi * 2 * j / n)
        print("X: ", x, "Y: ", y, "i: ", i)
        if j == 0:
            path.push("m{},{}".format(x, y))
            x1 = x
            y1 = y
        elif type == "curved":
            path.push_arc(target=(x, y), rotation=-30, r=10)
        else:
            path.push("{},{}".format(x, y))

    # Back to starting point to complete
    if type == "curved":
        path.push_arc(target=(x1, y1), rotation=-30, r=10)
    else:
        path.push("{},{}".format(x1, y1))

    # path.rotate(angle*i)

    # Scale for this iteration
    scaleiter = math.pow(scale, i)
    path.scale(scaleiter)
    # print("Scaleiter: ",scaleiter);

    # Shift back to centered
    shift = r * (1 - scaleiter) / 2
    # print("shift: ", shift)
    path.translate(shift, 0)

    dwg.add(path)

# dwg.add(dwg.path('m0,0 100,0 0,100 -100,0',stroke='black',fill='none'))

dwg.save()
