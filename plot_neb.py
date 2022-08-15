#!/home/vrahul/anaconda3/bin/python
import numpy as np
import matplotlib.pyplot as plt

eVk=627.51/27.2 # eV_to_kcal 

data = np.loadtxt("energy_data.dat")

x  = data[:, 0]
en = data[:, 1]
#e = min(en)
e = (min(data[0:4, 1]))
en = en - e
#print(e)

plt.scatter(x, en*eVk, color='g', alpha=0.7)
plt.plot(x, en*eVk, color='tab:orange', alpha=1.0, lw=2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

#plt.xticks(np.arange(2.0, 5.0, 0.4))
plt.xticks(np.arange(1, 7.1, 1))
plt.yticks(np.arange(0.0, 48.0, 8.0))

#plt.xlim([2.1, 5.0])
plt.xlim([1, 7])
plt.ylim([-5.3, 48.0])

#plt.legend({"H-ZSM-5"}, fontsize='12')
plt.xlabel('NEB Image', fontsize='18', fontweight='bold')
plt.ylabel(r'$\mathrm {\mathbf{\mathit{E} (kcal \: mol^{-1})}}$', fontsize='18')

plt.grid(color='grey', linestyle='-.', linewidth='1.0')
#plt.title('ZSM-5', fontsize='12', fontweight='bold', color='grey')
plt.savefig('Energy.jpg', bbox_inches='tight', transparent=True, dpi=600)
#plt.savefig('Free_Energy_ZSM.pdf', bbox_inches='tight', transparent=True, dpi=900)
#plt.show()

