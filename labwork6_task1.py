import matplotlib.pyplot

x = [1, 2, 3, 4, 5]
y = [i + 2 for i in x]

matplotlib.pyplot.plot(x, y, label='y = x + 2', color='blue', linestyle='--', marker='o')

matplotlib.pyplot.title('Linear Graph', fontsize=14)
matplotlib.pyplot.xlabel('X-axis', fontsize=12)
matplotlib.pyplot.ylabel('Y-axis', fontsize=12)
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)

matplotlib.pyplot.show()
