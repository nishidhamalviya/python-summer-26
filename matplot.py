import matplotlib.pyplot as plt
import numpy as np
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [22, 24, 19, 23, 25]
plt.plot(days, temperature, marker='o', linestyle='-', color='blue')
plt.title('Temperature Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
products = ['Laptops', 'Mobiles', 'Tablets']
sales = [150, 300, 100]
plt.bar(products, sales, color='green')
plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.show()

import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 80]
plt.scatter(study_hours, exam_scores, color='red')
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()

import matplotlib.pyplot as plt
ages = [18, 19, 20, 21, 22, 22, 23, 24, 25, 25, 25, 26, 27, 28, 29]
plt.hist(ages, bins=5, color='purple', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

import matplotlib.pyplot as plt
labels = ['Rent', 'Food', 'Transport', 'Savings']
expenses = [500, 300, 100, 100]
plt.pie(expenses, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expenses')
plt.axis('equal') # Ensures pie is a circle
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('3D Surface Plot')
plt.show()