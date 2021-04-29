import os
import nltk
import re
import glob
from nltk.corpus import wordnet


# This method is used to reads train data files and build training dataset for names

def extractTrain(path):

    training_data = []          # Training data set build from all input text files
    # Recursively checks all the files with the matching patterns.
    for file_name in glob.glob(path, recursive=True):
        data = open(file_name).read()
        training_data.extend(getTrainFeatures(data))

    return training_data
