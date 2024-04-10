import numpy as np
import bisect
import matplotlib.pyplot as plt

def BinData(WavelengthLower, WavelengthUpper, WavelengthHR, SpectrumHR):    
    # Find the indices of the wavelength range
    BinnedSpectrum = []
    for Wl, Wu in zip(WavelengthLower, WavelengthUpper):
        indexLower = bisect.bisect_left(WavelengthHR, Wl)
        indexUpper = bisect.bisect_right(WavelengthHR, Wu)
        CurrentBinnedSpectrum = np.mean(SpectrumHR[indexLower:indexUpper])
        BinnedSpectrum.append(CurrentBinnedSpectrum)
    return np.array(BinnedSpectrum)

WarmJupiters = np.loadtxt("data/WarmJupiter_FIT.data", skiprows=1, delimiter=",")
SuperEarth = np.loadtxt("data/SuperEarth_FIT.data", skiprows=1, delimiter=",")
HighResolution_WASP39Data = np.load("data/WASP_39_BestFitModel.npy")
LowResolution_WASP39Data = BinData(WarmJupiters[:,0], WarmJupiters[:,1], HighResolution_WASP39Data[:,0], HighResolution_WASP39Data[:,1])

plt.figure(figsize=(12,8))
plt.subplot(311)
plt.plot(WarmJupiters[:,2], WarmJupiters[:,3], marker='o', color="red", label='Warm Jupiters')
plt.title("Warm Jupiter")
plt.xlabel('Wavelength [Microns]', fontsize=20)
plt.ylabel('Flux [ppm]', fontsize=20)
plt.xlim(0.6, 10.0)
plt.ylim(34500, 36000)
plt.subplot(312)
plt.plot(SuperEarth[:,2], SuperEarth[:,3], marker='o', color="blue", label='Super Earth')
plt.xlabel('Wavelength [Microns]', fontsize=20)
plt.ylabel('Flux [ppm]', fontsize=20)
plt.xlim(0.6, 10.0)
plt.ylim(10000, 12000)
plt.title("Super-Earth")
plt.subplot(313)
plt.plot(WarmJupiters[:,2], LowResolution_WASP39Data, marker='.', color="blue", label='Super Earth')
plt.xlabel('Wavelength [Microns]', fontsize=20)
plt.ylabel('Flux [ppm]', fontsize=20)
plt.xlim(0.6, 10.0)
plt.title("WASP-39b-Best Fit Model based on GRISM-395")
plt.tight_layout()
plt.savefig("DifferentModels.png")
plt.show()