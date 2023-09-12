import pandas as pd
import numpy as np

C = pd.read_csv("housing.csv")

X = np.random.permutation(C)
print(X)
