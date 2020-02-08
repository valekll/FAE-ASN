import pandas as pd
import markovify

x_da = pd.read_csv("data/xayah_randomized.csv")
x_da.dropna()

model = markovify.NewlineText(x_da['Text'], state_size = 2)

for i in range(10):
    print(model.make_sentence())
