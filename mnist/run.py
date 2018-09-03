import matplotlib.pyplot as plt
import numpy
import pandas
import mnist
import os
from nn import NeuralNetwork


def main():
    # number of input, hidden and output nodes
    load_from_file = True
    #load_from_file = False
    input_nodes = 784
    hidden_nodes = 200
    output_nodes = 10

    # learning rate
    learning_rate = 0.1
    epochs = 5
    datasets = 60000

    n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    if not load_from_file:
        train(n, output_nodes, datasets, epochs)
        wih, who = n.get_weights()
        pandas.DataFrame(wih).to_csv(os.path.join(os.getcwd(), 'wih.csv'), sep=';', header=None, index=False)
        pandas.DataFrame(who).to_csv(os.path.join(os.getcwd(), 'who.csv'), sep=';', header=None, index=False)
    else:
        wih = pandas.read_csv(os.path.join(os.getcwd(), 'wih.csv'), sep=';', header=None)
        who = pandas.read_csv(os.path.join(os.getcwd(), 'who.csv'), sep=';', header=None)
        n.weights(wih.values, who.values)
    test(n)
    show(n)


def train(n, output_nodes, datasets, epochs):
    # train the neural network

    # epochs is the number of times the training data set is used for training

    do_print = False

    training_data = mnist.Mnist(os.path.join(os.getcwd(), 'datasets/train.csv'))

    for e in range(epochs):
        print('Start epoch {:>3} of {}'.format(e, epochs))
        # go through all records in the training data set
        count = 0
        for record in training_data.random()[:datasets]:
            if do_print and count % 10 is 0:
                print('data {}'.format(count))
            count += 1
            # scale and shift the inputs
            inputs = (numpy.asfarray(record.data) / 255.0 * 0.99) + 0.01
            # create the target output values (all 0.01, except the desired label which is 0.99)
            targets = numpy.zeros(output_nodes) + 0.01
            # all_values[0] is the target label for this record
            targets[int(record.label)] = 0.99
            n.train(inputs, targets)
            pass
        pass

    # test the neural network


def test(n):
    # scorecard for how well the network performs, initially empty
    scorecard = []

    test_data = mnist.Mnist(os.path.join(os.getcwd(), 'datasets/test.csv')).random()

    # go through all the records in the test data set
    for record in test_data:
        # correct answer is first value
        correct_label = int(record.label)
        # scale and shift the inputs
        inputs = (numpy.asfarray(record.data) / 255.0 * 0.99) + 0.01
        # query the network
        outputs = n.query(inputs)
        # the index of the highest value corresponds to the label
        label = numpy.argmax(outputs)
        # append correct or incorrect to list
        if label == correct_label:
            # network's answer matches correct answer, add 1 to scorecard
            scorecard.append(1)
        else:
            # network's answer doesn't match correct answer, add 0 to scorecard
            scorecard.append(0)
            pass

        pass

    # calculate the performance score, the fraction of correct answers
    scorecard_array = numpy.asarray(scorecard)
    print("performance = ", scorecard_array.sum() / scorecard_array.size)


def show(n):
    test_data = mnist.Mnist(os.path.join(os.getcwd(), 'datasets/test.csv')).random()[:2]
    for dataset in test_data:
        draw(dataset)
        outputs = n.query(dataset.data)
        label = numpy.argmax(outputs)
        print("it is a {}".format(label))
    pass


def draw(dataset):
    array = numpy.asfarray(dataset.data).reshape((28, 28)) / 255
    fig, ax = plt.subplots()
    im = ax.imshow(array, cmap=plt.get_cmap('Greys'), interpolation='None')
    fig.colorbar(im)
    ax.set_title(dataset.label)
    plt.show()

if __name__ == '__main__':
    main()
