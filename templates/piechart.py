import matplotlib.pyplot as plt


slices = [5, 2, 1, 2]
departments = ['F&B', 'Leisure', 'Essentials', 'Others']
cols = ['r', 'y', 'b', 'g']

plt.pie(slices, labels=departments, colors=cols, startangle=90, shadow=True, autopct='%1.1f%%')
plt.show()
