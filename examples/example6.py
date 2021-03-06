#!/usr/bin/env python

import biggles
import numpy
import math

x = numpy.arange(1 * math.pi, 3 * math.pi, math.pi / 30)
c = numpy.cos(x)
s = numpy.sin(x)

p = biggles.FramedPlot()
p.aspect_ratio = 1
p.frame1.draw_grid = 1
p.frame1.tickdir = 1

p.x1.label = "bottom"
p.x1.subticks = 1

p.y1.label = "left"
p.y1.draw_spine = 0

p.x2.label = "top"
p.x2.range = 10, 1000
p.x2.log = 1

p.y2.label = "right"
p.y2.draw_ticks = 0
p.y2.ticklabels = ["-1", "-1/2", "0", "1/2", "1"]

p.add(biggles.Curve(x, c, type='dash'))
p.add(biggles.Curve(x, s))

p.write("example6.png", dpi=55)
p.write("example6.eps")
p.write("example6.pdf")
p.show()
