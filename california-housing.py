import pandas as pd
import numpy as np
from sklearn.model_selection import KFold



X = pd.read_csv("housing.csv")


selector = KFold(n_splits=10)
print(selector.get_n_splits(X))

for split in selector.split(X) :
    print(split)




    

