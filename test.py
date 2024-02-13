from scipy.io import loadmat
from util.fdm import fdm
import numpy as np

wave = loadmat('./samples/HR00001.mat')['val'][1];
wave = np.reshape(wave, [1, 5000])
fibf = fdm(wave.T, 500, np.array([0, 500/64, 500/32, 500/16, 500/8, 500/4, 500/2]), plot_subbands=True)
print("Done!")