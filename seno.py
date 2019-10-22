import matplotlib.pyplot as plt
import numpy as np


x = np.linspace (0, 2*np.pi, 100) 
cos = np.cos(x) 

plt.plot(x, cos)
plt.savefig('seno.png')