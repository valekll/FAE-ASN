import pandas as pd
import numpy as np
import sys

x_da = pd.read_csv("xayah_randomized.csv")
x_da.dropna()

# topic modeling

# tokenize and ngramize (probably) text
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_df=0.8, min_df=2, stop_words="english")
dtm = cv.fit_transform(x_da['Text'].values.astype('U'))

# fit topic model
from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=6, random_state=455337691)
lda.fit(dtm)

# show the top words for the topics
for i,topic in enumerate(lda.components_):
    print(f'Top 10 words for topic #{i}:')
    print([cv.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')

print("done")

# when shown a new text, generate probabilities that it belongs to each topic
print(lda.transform(cv.transform(["The economy is working better than ever"]))[0])

