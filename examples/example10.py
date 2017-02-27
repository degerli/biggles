import biggles
from numpy import log10, logspace, random

biggles.configure('default','fontsize_min',2.5)

x = logspace(log10(0.1), log10(10.0), 10)

model = 1.0/x
yerr = 0.1*model
y = model + yerr*random.normal(size=x.size)


yratio = y/model
yratio_err = yerr/model

a = biggles.FramedArray(
    2,1,
    xlog=True,
    aspect_ratio=1.2,
    xlabel=r'$R [h^{-1} Mpc]$',
)

color='blue'
sym='filled circle'
a.row_fractions=[0.75,0.25]

mcurve = biggles.Curve(x, model)
pts = biggles.Points(x,y, type=sym, color=color)
epts = biggles.SymmetricErrorBarsY(x,y,yerr, color=color)

pts.label='data'
mcurve.label='1/x'

key=biggles.PlotKey(0.9,0.9,[pts,mcurve],halign='right')

a[0,0].add(pts, epts, mcurve, key)
a[0,0].ytitle=r'$\Delta\Sigma  [M_{\odot} pc^{-2}]$'
a[0,0].yrange=[0.05,20.0]
a[0,0].xrange=[0.05,20.0]
a[0,0].ylog=True

a[1,0].add( biggles.Points(x, yratio, type=sym,color=color,size=3) )
a[1,0].add( biggles.SymmetricErrorBarsY(x,yratio,yratio_err, color=color) )
a[1,0].add( biggles.Curve(x, x*0 + 1) )
a[1,0].ytitle=r'$ratio$'
a[1,0].yrange=[0.5,1.5]


a.write("example10.png", dpi=55)
a.write("example10.eps")
a.write("example10.pdf")
a.show()