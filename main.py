import lightkurve as ik
import matplotlib.pyplot as plt 
import numpy as np 
target = 'RR lyr' 
search = ik.search_lightcurve(target, mission = "TESS") 
print(search) 
lc = search[0].download() 
print(lc) 
ic = lc.remove_nans().normalize()
lc.plot(title = "RR lyr - raw light curve") 
plt.savefig("01_raw__lightcurve.png", dpi = 150 )
plt.show() 
pg = lc.to_periodogram(method = "lombscargle") 
period = pg.period_at_max_power 
print(f"Recovered period : {period:.4f}")
pg.plot(title = "RR Lyr - periodgram") 
plt.savefig("02_periodgram.png", dpi = 150) 
lc.fold(period = period).plot(title = "RR lyr - folded") 
plt.savefig("03_folded.png",dpi = 150)
plt.show()