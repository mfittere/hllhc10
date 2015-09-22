from pyoptics import *
from matplotlib.pyplot import *

close('all')
optics.open('twiss_lhcb1.tfs').select('S.DS.L8.B1','E.DS.R8.B1').plotbeta()
savefig('twiss_ir8b1.png')
optics.open('twiss_lhcb2.tfs').select('S.DS.L8.B2','E.DS.R8.B2').plotbeta()
savefig('twiss_ir8b2.png')

draw()
show()
