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
