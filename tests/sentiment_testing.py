import pandas as pd
import numpy as np
import nltk

x_da = pd.read_csv("data/xayah_randomized.csv")
x_da.dropna()

train = pd.read_csv("data/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

import random

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score

vader = SentimentIntensityAnalyzer()
def vader_polarity(text):
    score = vader.polarity_scores(text)
    return 1 if score['pos'] > score['neg'] else 0

results = [vader.polarity_scores(text) for text in x_da['Text']]

for i in results:
    print(i)
    print("\n")
