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

# This method is used to extract named entity 'PERSON' and build features of identified names


def getTrainFeatures(data):

    # List of tuple containing the dictionary features and it'c corresponding name
    train_data = []

    tokenized_data = nltk.word_tokenize(data)       # Splitting data into words

    # Generationg the parts of speech of each word
    pos_tokenized_data = nltk.pos_tag(tokenized_data)

    # Chunking the tagged words using named entity chunker
    chk_tagged_tokens = nltk.chunk.ne_chunk(pos_tokenized_data)

    for chk in chk_tagged_tokens.subtrees():
        features = {}  # To hold features of each name
        if chk.label().upper() == 'PERSON':  # Extracting the words with tag PERSON
            name = ' '.join([i[0] for i in chk])

            features['name_len_s'] = len(name)  # Length of name with spaces
            # Length of name without spaces
            features['name_len'] = len(name.replace(' ', ''))
            # No. of words in a name
            features['word_cnt'] = len(name.split(' '))
            # No. of white spaces in a name
            features['white_space'] = len(name) - len(name.replace(' ', ''))
            features['w1_len'] = 0  # Length of 1st word
            features['w2_len'] = 0  # Length of 2nd word
            features['w3_len'] = 0  # Length of 3rd word
            features['w4_len'] = 0  # Length of 4th word
            words = name.split(' ')

            for i in range(len(words)):  # Finding the length of words
                if i == 0:
                    features['w1_len'] = len(words[i])
                elif i == 1:
                    features['w2_len'] = len(words[i])
                elif i == 2:
                    features['w3_len'] = len(words[i])
                elif i == 3:
                    features['w4_len'] = len(words[i])

            # Appending tuple of dictionary with features and it's corresponding name to train_data
            train_data.append((features, name))

    return train_data


# This methods the read the redacted data from the given path / file and return's features of redated name for prediction

def extractRedacted(path):

    redacted_data = []          # Data set built from redacted documents for predicting names

    data = open(path).read()        # Reading the redacted data
    # Extracting the features from the redacted data
    redacted_data.extend(getRedactedFeatures(data))

    return redacted_data  # Returning the features of the redacted names

# This method is used to construct the features for the redacted names


def getRedactedFeatures(data):

    redacted_names = []  # list of dictionary of constructed features
    # Using the below regex pattern to identify the redacted names
    pattern = re.compile('\u2588+\s*\u2588*\s*\u2588*\s*\u2588+')

    # Finding all the names with matching pattern
    matched_names = re.findall(pattern, data)

    for names in matched_names:
        features = {}

        # Removing extra spaces present in between words
        name = re.sub('\s+', ' ',  names)

        features['name_len_s'] = len(name)  # Length of name with spaces
        # Length of name without spaces
        features['name_len'] = len(name.replace(' ', ''))
        # No. of words in a name
        features['word_cnt'] = len(name.split(' '))
        # No. of white spaces in a name
        features['white_space'] = len(name) - len(name.replace(' ', ''))
        features['w1_len'] = 0  # Length of 1st word
        features['w2_len'] = 0  # Length of 2nd word
        features['w3_len'] = 0  # Length of 3rd word
        features['w4_len'] = 0  # Length of 4th word
        words = name.split(' ')

        for i in range(len(words)):  # Finding the length of words
            if i == 0:
                features['w1_len'] = len(words[i])
            elif i == 1:
                features['w2_len'] = len(words[i])
            elif i == 2:
                features['w3_len'] = len(words[i])
            elif i == 3:
                features['w4_len'] = len(words[i])

        redacted_names.append(features)
    return redacted_names
