import nltk
import re
from nltk.corpus import wordnet

# This method reads the file and redacts names in it and writes redacted data to file with extension python3.redacted


def redactNames(path):

    data = open(path).read()  # Reading the file to be redacted

    tokenized_data = nltk.word_tokenize(data)       # Splitting data into words

    # Generationg the parts of speech of each word
    pos_tokenized_data = nltk.pos_tag(tokenized_data)

    # Chunking the tagged words using named entity chunker
    chk_tagged_tokens = nltk.chunk.ne_chunk(pos_tokenized_data)

    for chk in chk_tagged_tokens.subtrees():

        if chk.label().upper() == 'PERSON':  # Extracting the words with tag PERSON

            # Extracting first and last name
            for name in chk:
                # print(name)
                data = re.sub('\\b{}\\b'.format(name[0]),
                              '\u2588'*len(name[0]), data)  # Replacing the names with block character

    # Opening a file with extension .redacted
    redactedDoc = open(path.replace('.txt', '.redacted', 'w'))
    redactedDoc.write(data)  # Writing redacted data to file
