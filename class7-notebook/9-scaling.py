from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

boston_housing = load_boston()
columns_names = boston_housing.feature_names
y = boston_housing.target
X = boston_housing.data

print('Pre scaling X')
print(X)

scaler = StandardScaler()
scaler.fit(X)
scaled_features = scaler.transform(X)

print('Post scaling X')
print(scaled_features)

X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.35)
