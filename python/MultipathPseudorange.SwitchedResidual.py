import numpy as np
from plotRawGPS import plotRawGPS, LOG_WIDTH

data = np.reshape(np.fromfile('/tmp/ceres_sandbox/MultipathPseudorange.SwitchingResidual.log', dtype=np.float64), (-1, LOG_WIDTH))

plotRawGPS(data, "Multipath, Switched")

