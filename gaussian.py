import numpy as np
import matplotlib.pyplot as plt


mu = 0       
sigma = 0.1  
x = np.linspace(-1, 1, 1000)

y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)


plt.figure(figsize=(8, 4))
plt.plot(x, y, label=f'μ={mu}, σ={sigma}', color='royalblue', linewidth=2)
plt.title("Gaussian Distribution (Bell Curve)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()