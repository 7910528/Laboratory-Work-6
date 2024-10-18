import matplotlib.pyplot
import numpy

x = numpy.linspace(-5, 5, 400)

y1 = numpy.abs(x)
y2 = x**3
y3 = (1/3) ** x

matplotlib.pyplot.plot(x, y1, label='y = |x|', color='blue', linestyle='-', marker='o')
matplotlib.pyplot.plot(x, y2, label='y = x^3', color='green', linestyle='--')
matplotlib.pyplot.plot(x, y3, label='y = (1/3)^x', color='red', linestyle='-.')

matplotlib.pyplot.xlabel('X-axis', color='blue', fontsize=12)
matplotlib.pyplot.ylabel('Y-axis', color='blue', fontsize=12)
matplotlib.pyplot.title('Mathematical Functions Graphs', color='red', fontsize=16)
matplotlib.pyplot.legend(loc='lower right')
matplotlib.pyplot.grid(True)

matplotlib.pyplot.savefig('math_functions.png')
matplotlib.pyplot.savefig('math_functions.pdf')

matplotlib.pyplot.show()
