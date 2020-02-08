import pandas as pd
import numpy as np
import nltk

x_da = pd.read_csv("data/xayah_randomized.csv")
x_da.dropna()

import random

from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()

results = [vader.polarity_scores(text) for text in x_da['Text']]

for i in results:
    print(i['compound'])
    print("\n")
