import csv
import numpy as np
import emoji
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def read_csv(filename = 'data/dataset_.csv'):
    phrase = []
    label = []

    with open (filename, encoding="Latin-1") as csvDataFile:
        csvReader = csv.reader(csvDataFile, encoding="Latin-1")

        for row in csvReader:
            print(row[0])
            print(row[1])
            phrase.append(row[0])
            label.append(row[1])

    X = np.asarray(phrase)
    Y = np.asarray(label, dtype=int)

    return X, Y

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)]
    return Y

