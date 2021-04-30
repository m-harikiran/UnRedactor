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


def testExtractTrain():

    # Location and name of text data file
    file_loc = 'project_docs/package_test/test.txt'

    # Calling the method extractTrain
    train_xy = unredactor.extractTrain(file_loc)

    # Verifying if the return type is list or not
    assert type(train_xy) == list
    # Verifying if the list contains tuples or not
    assert type(train_xy[0]) == tuple
