import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,4,8,16]

plt.plot(x, y, 'bo-', label='students')
plt.axis([0,10,0,20])
plt.title('Your title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
