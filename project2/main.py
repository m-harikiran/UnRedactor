import argparse
import os
import re
import redactor
import unredactor


def main(input_parameters):

    # Redacting the names present in the input file
    redacted_doc = redactor.redactNames(input_parameters.input)

    # Constructiong the training data set for predicting names from the given training data files
    training_data = unredactor.extractTrain(input_parameters.tdata)

    # Extracting the features of the redacted names from redacted document
    redacted_data = unredactor.extractRedacted(redacted_doc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--input", type=str, required=True,
                        help="location of the file to be redacted and unredacted")  # Adding optinal argument --inputs

    parser.add_argument("--tdata", type=str, required=True,
                        help="path and pattern to match training files")  # Adding optinal argument --inputs

    # Parsing the arguments to check if the condition if conditions is not met this will throw an error
    args = parser.parse_args()

    main(args)
