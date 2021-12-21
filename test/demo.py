from pylayers.antprop.coverage import *

C = Coverage()
C.tx = np.array((30,12))
C.cover()
C.showPower(polarization='o')
