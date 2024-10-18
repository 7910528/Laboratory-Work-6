import matplotlib.pyplot
import numpy

x1 = numpy.linspace(0.1, 4, 100) # 0.1 and not 0 to avoid division by zero
x2 = numpy.linspace(1, 7, 100)

y1 = numpy.sin(10*x1) * numpy.sin(3*x1) / (x1**2)
y2 = 5 * numpy.sin(10*x2) * numpy.sin(3*x2) / numpy.sqrt(x2)

# Part a: Plot on one field
matplotlib.pyplot.plot(x1, y1, label='y1 = sin(10x)sin(3x)/x^2', color='blue')
matplotlib.pyplot.plot(x2, y2, label='y2 = 5sin(10x)sin(3x)/x^(1/2)', color='red')

matplotlib.pyplot.title('Functions on one field')
matplotlib.pyplot.xlabel('X-axis')
matplotlib.pyplot.ylabel('Y-axis')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

# Part b: Plot on separate fields using subplot()
matplotlib.pyplot.figure()

matplotlib.pyplot.subplot(2, 1, 1)
matplotlib.pyplot.plot(x1, y1, label='y1 = sin(10x)sin(3x)/x^2', color='blue')
matplotlib.pyplot.title('y1 Function')
matplotlib.pyplot.grid(True)

matplotlib.pyplot.subplot(2, 1, 2)
matplotlib.pyplot.plot(x2, y2, label='y2 = 5sin(10x)sin(3x)/x^(1/2)', color='red')
matplotlib.pyplot.title('y2 Function')
matplotlib.pyplot.grid(True)

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
