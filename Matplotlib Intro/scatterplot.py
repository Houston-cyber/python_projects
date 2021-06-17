import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("darkgrid")

N = 50
x1 = np.random.rand(N)
y1 = np.random.rand(N)
s1 = np.random.rand(N) * 300
x2 = np.random.rand(N)
y2 = np.random.rand(N)
s2 = np.random.rand(N) * 300

plt.scatter(x1, y1,s=s10)
plt.scatter(x2, y2,s=s30)
plt.title('Your title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
