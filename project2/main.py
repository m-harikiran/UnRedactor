import argparse
import os
import re
from sklearn.feature_extraction import DictVectorizer
from sklearn.neighbors import KNeighborsClassifier

import redactor
import unredactor


def main(input_parameters):

    # Redacting the names present in the input file
    redacted_doc = redactor.redactNames(input_parameters.input)

    # Constructiong the training data set for predicting names from the given training data files
    training_data = unredactor.extractTrain(input_parameters.tdata)

    # Extracting the features of the redacted names from redacted document
    redacted_data = unredactor.extractRedacted(redacted_doc)

    # Using dict vectorizer to vectorize the data present in dictionary
    v = DictVectorizer(sparse=False)

    # Extracting X_train and y_train from training data

    # Extracting features and transforming it
    X_train = v.fit_transform([x for (x, y) in training_data])

    # Extracting target variable (name)
    y_train = [y for (x, y) in training_data]

    # Features of redacted names to be predicted

    X_redacted = v.fit_transform([x for (x, y) in redacted_data])

    # Redacted name for the extracted features
    y_redacted = [y for (x, y) in redacted_data]

    # print(training_data)

    # print(redacted_data)

    # KNN Model

    knnModel = KNeighborsClassifier(
        n_neighbors=5, weights='uniform', algorithm='auto')  # Creating an object for KNN Classifier

    knnModel.fit(X_train, y_train)  # Fitting training data into KNN Model

    # Finding the K Nearest Neighbors for redacted names

    indx_KNN = knnModel.kneighbors(
        X_redacted, n_neighbors=3, return_distance=False)  # Finding the K Nearest Neighbors and returning their indices

    # Predicting the K most likely names and writing it to file with extension .predicted

    # Opening a file in writing mode
    predicted_doc = open(redacted_doc.replace('.redacted', '.predicted'), 'w')

    # Writing the message to file
    predicted_doc.write(
        '*****  Predicting 4 most likely unredacted names for the redacted names present in document  *****\n')

    predicted_doc.close()  # Closing the file

    count = 1
    for x, y in zip(y_redacted, indx_KNN):

        doc = open(redacted_doc.replace('.redacted', '.predicted'),
                   'a')  # Opening the file to append data

        message = '\n{}. The top 4 likely names for {} :: {}, {}, {}, {}\n'.format(
            count, x, y_train[y[0]], y_train[y[1]], y_train[y[2]], y_train[y[3]])

        doc.write(message)

        doc.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--input", type=str, required=True,
                        help="location of the file to be redacted and unredacted")  # Adding optinal argument --inputs

    parser.add_argument("--tdata", type=str, required=True,
                        help="path and pattern to match training files")  # Adding optinal argument --inputs

    # Parsing the arguments to check if the condition if conditions is not met this will throw an error
    args = parser.parse_args()

    main(args)
