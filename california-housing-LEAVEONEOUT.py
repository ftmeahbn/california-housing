import pandas as pd
import numpy as np
from sklearn.model_selection import LeaveOneOut



X = pd.read_csv("housing.csv")


selector = LeaveOneOut()

for split in selector.split(X) :
    print(split)
