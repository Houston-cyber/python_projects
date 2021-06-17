import matplotlib.pyplot as plt

plt.style.use('grayscale')
print(plt.style.available)#available styles

x = [1,2,3,4,5]
y = [1,2,4,8,16]

plt.bar(x,y)
plt.title('Your title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
