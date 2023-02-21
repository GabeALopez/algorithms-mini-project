from MiniProject1 import Phone
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
# np.random.seed(1)


# x = np.arange(0.0, 1000.0, 1000.0)
# y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
arry = [Phone] * 100

arry[1].xpos = 500
arry[1].ypos = 500

x = arry[1].xpos
y = arry[1].xpos

size = 100

fig, ax = plt.subplots()
ax.scatter(x, y, size, c="black", alpha=0.5, marker=r'$\cdot$',label="Phone")

plt.xlim([0,1000])
plt.ylim([0,1000])
plt.show()