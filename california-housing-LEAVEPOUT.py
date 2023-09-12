import pandas as pd
from sklearn.model_selection import LeavePOut
import numpy as np

X = pd.read_csv("housing.csv")


selector = LeavePOut(100)
print(selector.get_n_splits(X))

for split in selector.split(X) :
    print(split)
