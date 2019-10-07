import numpy
import matplotlib.pyplot as plt

x = numpy.random.randn(1000)

values, bins, _ = plt.hist(x, normed=True)
area = sum(numpy.diff(bins)*values)
