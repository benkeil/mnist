import gzip
import os


def main():
    convert('datasets/train-images-idx3-ubyte.gz', 'datasets/train-labels-idx1-ubyte.gz', 'datasets/train.csv')
    convert('datasets/t10k-images-idx3-ubyte.gz', 'datasets/t10k-labels-idx1-ubyte.gz', 'datasets/test.csv')


def convert(image_path, label_path, csv_path):
    image_file = gzip.open(os.path.join(os.getcwd(), image_path), 'rb')
    # skip headers
    image_file.read(16)

    label_file = gzip.open(os.path.join(os.getcwd(), label_path), 'rb')
    # skip headers
    label_file.read(8)

    csv_file = open(os.path.join(os.getcwd(), csv_path), 'x')

    while True:
        label = read_label(label_file)
        if label is None:
            break
        image = read_image(image_file)
        csv_file.write("{};{}\n".format(label, ";".join(str(e) for e in image)))
    pass


def read_label(label_file):
    b = label_file.read(1)
    if len(b) == 0:
        return None
    return ord(b)


def read_image(image_file):
    v = []
    for i in range(28*28):
        b = image_file.read(1)
        v.append(ord(b))
    return v


if __name__ == '__main__':
    main()
