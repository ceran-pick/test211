import matplotlib.pyplot as plt

sizes = [25, 30, 15, 10, 20]
labels = ['Раздел 1', 'Раздел 2', 'Раздел 3', 'Раздел 4', 'Раздел 5']


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)


plt.axis('equal') 
plt.show()