import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
cancer = datasets.load_breast_cancer()
wine = datasets.load_wine()
boston = datasets.load_boston()
diabetes = datasets.load_diabetes()

# Visualizing structure of dataset in 2D
pca = PCA(n_components=2)
proj = pca.fit_transform(iris.data)
plt.scatter(proj[:, 0], proj[:, 1], c=iris.target, edgecolors='black')
plt.colorbar()
plt.show()
