import os
from project2 import redactor
from project2 import unredactor


# Testing method used to redact names in a document.

def testRedactNames():

    expected = "I couldn't image ██████ ███████ in a serious role, but his performance truly "
    file_loc = 'project_docs/package_test/test.txt'  # Name and path of the test data

    # Redacting the data of the test file
    redacted_doc_loc = redactor.redactNames(file_loc)

    # Reading the data from the redacted document
    redacted_data = open(redacted_doc_loc).read().splitlines()

    # Verifying if the redacted data and expected data is same or not
    assert redacted_data[1] == expected


# Testing method used to construct training datase from the document.


def testExtractTrain():

    # Location and name of text data file
    file_loc = 'project_docs/package_test/test.txt'

    # Calling the method extractTrain
    train_xy = unredactor.extractTrain(file_loc)

    # Verifying if the return type is list or not
    assert type(train_xy) == list
    # Verifying if the list contains tuples or not
    assert type(train_xy[0]) == tuple


# Testing method used to extract and construct features of identified names from dataset

def testGetTrainFeatures():

    expected = [({'name_len': 13,
                  'name_len_s': 14,
                  'w1_len': 6,
                  'w2_len': 7,
                  'w3_len': 0,
                  'w4_len': 0,
                  'white_space': 1,
                  'word_cnt': 2},
                 'Ashton Kutcher')]  # Extected features to be extracted

    # Data to be used for testing
    test_data = "I couldn't image Ashton Kutcher in a serious role, but his performance truly exemplified his character."

    # Calling the method to extract features of names
    extracted_features = unredactor.getTrainFeatures(test_data)

    # Verifying if the return type is list
    assert type(extracted_features) == list
    # Verifying if the returned type contains tuple
    assert type(extracted_features[0]) == tuple
    # Verifying if the tuple returned has dictionary of features
    assert type(extracted_features[0][0]) == dict
    # Verifying it the resulted output and expected output are same or not
    assert extracted_features == expected


# Testing method used to read the redacted document and construct the features for redacted names.


def testExtractRedacted():

    # Location and name of text data file
    file_loc = 'project_docs/package_test/test.redacted'

    # Calling the method extractRedacted
    train_xy = unredactor.extractRedacted(file_loc)

    # Verifying if the return type is list or not
    assert type(train_xy) == list
    # Verifying if the list contains tuples or not
    assert type(train_xy[0]) == tuple


# Testing method used to extract and construct features of identified names from dataset

def testGetRedactedFeatures():

    expected = [({'name_len': 13,
                  'name_len_s': 14,
                  'w1_len': 6,
                  'w2_len': 7,
                  'w3_len': 0,
                  'w4_len': 0,
                  'white_space': 1,
                  'word_cnt': 2},
                 '██████ ███████')]  # Extected features to be extracted

    # Data to be used for testing
    test_data = "I couldn't image ██████ ███████ in a serious role, but his performance truly exemplified his character."

    # Calling the method to extract features of names
    extracted_features = unredactor.getRedactedFeatures(test_data)

    # Verifying if the return type is list
    assert type(extracted_features) == list
    # Verifying if the returned type contains tuple
    assert type(extracted_features[0]) == tuple
    # Verifying if the tuple returned has dictionary of features
    assert type(extracted_features[0][0]) == dict
    # Verifying it the resulted output and expected output are same or not
    assert extracted_features == expected
