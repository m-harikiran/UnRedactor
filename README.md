# Uredact Sensitive Information

#### Author: Harikiran Madishetti

---

## About

When confidential data is exchanged with the media, it must go through a redaction procedure. That is to say, all sensitive names, locations, and other sensitive data must be concealed. Documents containing confidential details, such as police reports, court documents, and medical records, are often costly and time-consuming to redact.

This project will learn how to use Sci-Kit Learn, NLTK, and other packages to build a training dataset, train an ML model, and predict redacted data. The dataset created with NLTK can train a Machine Learning model to predict the most likely unredacted words, especially names that the redactor redacted.

Predicting the titles is a difficult challenge. To predict the most reliable and best name, we must practice our ML model with a broad dataset. To create a training dataset for this project, I used the [Large Movie Review Dataset](https://ai.stanford.edu/amaas/data/sentiment/), which includes feedback on most famous movies.

## Packages Required

The below is the list of packages used in this project.

- re
- os
- regex
- argparse
- nltk
- glob
- pytest
- pipenv
- scikit-learn

Libraries such as argparse, re, os, and glob are standard libraries in python3. To install other libraries please use Command `pipenv install -r requirements.txt`

## Directions to Install and Use Pagkage

The below are the insturctions to be followed to download, install and run the package/project.

1. Create a directory and then cd into the directory
   **`mkdir Text_Project2 && cd Test_Project2`**
2. Download the project files from GitHub
   **`git clone https://github.com/Harikiran-Madishetti/cs5293sp21-project2.git`**
3. Cd into project directory **cs5293sp21-project1**
   **`cd cs5293sp21-project2`**
4. Install python package pipenv to create a virtual enviromnent
   **`pip install pipenv`**
5. After successfully installing pipenv create a python3 virtual environment
   **`pipenv install --three`**
6. Install the dependencies listed in **requirements.txt** to start using the package
   **`pipenv install -r requirements.txt`**
7. After installing the dependencies successfully run unit tests
   **`pipenv run pytest`**
8. After running the unit tests successfully start using package (relpace URL with the URL of incidents list) using below command to fetch summary of the incidents by its nature
   **`pipenv run python project2/main.py --tdata "project_docs/train/\*\***/**\*.txt" --input "project_docs/redact/review.txt"`**

## Assumptions

In this project, I use the NLTK package to define people's names and build features from them. I am guessing that the names have a limit of four words for function building. If titles contain more than four words, I am extracting the characteristics of just four words. I also assume the data to be redacted and unredacted is in text file format. If the original text is in a different format, it may produce an error. I am not taking the first and last character indexes of each name into account when we estimate the redacted names. All project-related files are stored in **project docs**, training data that can be used to train the ML model is present in **project docs/train**, and the text file is expected to be redacted, and unredacted must be placed in **project docs/redact**. The text files are censored and saved with the extension **.redacted**. The redacted files are then read, and the top four possible names for redacted names are predicted, with the output saved in the **.predicted** log.
