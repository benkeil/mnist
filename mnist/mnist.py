from random import shuffle
import pandas


# mnist class definition
class Mnist(object):

    def __init__(self, path, rows=None):
        self._data = []
        csv = pandas.read_csv(path, nrows=rows, sep=';', header=None)
        for row in csv.values:
            self._data.append(Data(row[0], row[1:]))

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
