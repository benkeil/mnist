from random import shuffle
import pandas
import numpy


class Mnist(object):

    def __init__(self, path, max=None):
        self._data = []
        csv = pandas.read_csv(path, nrows=max, sep=';', header=None)
        for row in csv.values:
            list = numpy.asarray(row)
            self._data.append(Data(list[0], list[1:]))

    def __iter__(self):
        return self._data

    def get(self):
        return self._data

    def random(self):
        shuffle(self._data)
        return self._data


class Data(object):

    def __init__(self, label, data):
        self.label = label
        self.data = data

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __repr__(self):
        return str(self.label)
