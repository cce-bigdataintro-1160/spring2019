from sklearn.datasets import load_breast_cancer
import numpy as np

datas = load_breast_cancer()

new_column = np.array(['target'])
feature_names = datas.feature_names

print(np.append(new_column, feature_names))
