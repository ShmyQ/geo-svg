import svgwrite

dwg = svgwrite.Drawing("images/test2.svg", profile="full")

cx = 0
cy = 0
rad = 10


path = dwg.path(
    d="M 10,0 C 20,-10 , 0,-10 , 0,-20 M -10,0 C -20,-10 , 0,-10 , 0,-20",
    stroke="#000",
    fill="none",
    stroke_width=1,
)
dwg.add(path)

dwg.save()
