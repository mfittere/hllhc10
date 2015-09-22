from pyoptics import *
from matplotlib.pyplot import *

close('all')
optics.open('twiss_ir8b1.tfs').plotbeta()
savefig('twiss_ir8b1.png')
optics.open('twiss_ir8b2.tfs').plotbeta()
savefig('twiss_ir8b2.png')

draw()
show()
