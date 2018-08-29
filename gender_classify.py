import csv
import nltk

with open('data/names.csv') as f:
    names = [tuple(line) for line in csv.reader(f)]


def get_features(name):
    return {
        'suffix1': name[-1],
        'suffix2': name[-2:],
        'suffix3': name[-3:]
    }


train_names = names[20000:]
test_names = names[:20000]

train_data = [(get_features(n), g) for (n, g) in train_names]
test_data = [(get_features(n), g) for (n, g) in test_names]

clf = nltk.NaiveBayesClassifier.train(train_data)
# print(nltk.classify.accuracy(clf, test_data))


def predict(name):
    return clf.classify(get_features(name))
