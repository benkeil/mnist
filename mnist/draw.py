from mnist import Mnist
import os
import numpy
import matplotlib.pyplot as plt


def main():
    mnist = Mnist(os.path.join(os.getcwd(), "datasets/train.csv"), max=100)
    for dataset in mnist.random()[:1]:
        # reshape from 1x784 to 28x28 and scale to 0-1
        array = numpy.asfarray(dataset.data).reshape((28, 28)) / 255
        fig, ax = plt.subplots()
        im = ax.imshow(array, cmap=plt.get_cmap('Greys'), interpolation='None')
        fig.colorbar(im)
        ax.set_title(dataset.label)
        plt.show()


if __name__ == '__main__':
    main()
