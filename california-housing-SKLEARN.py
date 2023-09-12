import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


X = pd.read_csv("housing.csv")


for i in range(20):
    x_train, x_test = train_test_split(X,
                                        train_size=0.7,
                                        random_state=32)
    print(x_train, x_test)
